# -*- coding: utf-8 -*-

from __future__ import division

import logging
import numpy as np
import os
import pandas as pd
import pkg_resources

from openfisca_core import reforms
from openfisca_core.columns import FloatCol
from openfisca_core.formulas import dated_function

from openfisca_france_indirect_taxation.model.base import get_legislation_data_frames, Menages

from openfisca_france_indirect_taxation.model.consommation.postes_coicop import generate_postes_agreges_variables
from openfisca_france_indirect_taxation.model.consommation.categories_fiscales import generate_variables
from openfisca_france_indirect_taxation.build_survey_data.calibration_aliss import (
    add_poste_coicop,
    build_clean_aliss_data_frame,
    )


log = logging.getLogger(__name__)


aliss_assets_reform_directory = os.path.join(
    pkg_resources.get_distribution('openfisca_france_indirect_taxation').location,
    'openfisca_france_indirect_taxation',
    'reforms',
    'aliss_assets',
    )


def build_aliss_reform(rebuild = False):
    aliss_reform_path = os.path.join(aliss_assets_reform_directory, 'aliss_reform.csv')
    if os.path.exists(aliss_reform_path) and rebuild is False:
        aliss_reform = pd.read_csv(aliss_reform_path)
        return aliss_reform

    aliss_reform_data = pd.read_csv(os.path.join(aliss_assets_reform_directory, 'aliss_reform_unprocessed_data.csv'))
    aliss_uncomplete = build_clean_aliss_data_frame()
    aliss = add_poste_coicop(aliss_uncomplete)
    aliss_extract = aliss[['nomf', 'nomc', 'poste_bdf']].copy()
    aliss_extract.drop_duplicates(inplace = True)
    legislation_directory = os.path.join(
        pkg_resources.get_distribution('openfisca_france_indirect_taxation').location,
        'openfisca_france_indirect_taxation',
        'assets',
        'legislation',
        )
    codes_coicop_data_frame = pd.read_csv(
        os.path.join(legislation_directory, 'coicop_legislation.csv'),
        )
    legislation = codes_coicop_data_frame[['code_bdf', 'categorie_fiscale']].copy()
    legislation.rename(columns = {'code_bdf': 'poste_bdf'}, inplace = True)
    aliss_legislation = aliss_extract.merge(legislation)
    aliss_legislation.rename(columns = {'poste_bdf': 'code_bdf'}, inplace = True)
    aliss_reform = aliss_legislation.merge(aliss_reform_data)

    # Dealing with mismatch in reforms
    reforms = ['sante', 'environnement', 'tva_sociale', 'mixte']
    for reform in reforms:
        labels = [removed_reform for removed_reform in reforms if removed_reform != reform]
        mismatch = aliss_reform.drop(
            labels,
            axis = 1,
            ).groupby(['code_bdf']).filter(
                lambda x: x[reform].nunique() > 1,
                ).sort_values('code_bdf')

        mismatch.nomc = mismatch.nomc.str.decode('latin-1').str.encode('utf-8')
        mismatch.to_csv(
            os.path.join(aliss_assets_reform_directory, '{}_reform_mismatch.csv'.format(reform)),
            index = False,
            )

    if rebuild:
        aliss_reform.to_csv(aliss_reform_path, index = False)

    return aliss_reform


def build_reform_environnement(tax_benefit_system):
    key = 'aliss_environnement'
    name = u"Réforme Aliss-Environnement de l'imposition indirecte des biens alimentaires"
    return build_custom_aliss_reform(tax_benefit_system, key = key, name = name)


def build_reform_mixte(tax_benefit_system):
    key = 'aliss_mixte'
    name = u"Réforme Aliss-Mixte-Environnement-Sante de l'imposition indirecte des biens alimentaires"
    return build_custom_aliss_reform(tax_benefit_system, key = key, name = name)


def build_reform_sante(tax_benefit_system):
    key = 'aliss_sante'
    name = u"Réforme Aliss-Santé de l'imposition indirecte des biens alimentaires"
    return build_custom_aliss_reform(tax_benefit_system, key = key, name = name)


def build_reform_tva_sociale(tax_benefit_system):
    key = 'aliss_tva_sociale'
    name = u"Réforme Aliss-TVA sociale de l'imposition indirecte des biens alimentaires"
    return build_custom_aliss_reform(tax_benefit_system, key = key, name = name)


def build_custom_aliss_reform(tax_benefit_system = None, key = None, name = None, missmatch_rates = "weighted"):
    assert missmatch_rates in ["higher", "weighted"]  # "lower"]
    assert key is not None
    assert tax_benefit_system is not None
    taux_by_categorie_fiscale = None
    Reform = reforms.make_reform(
        key = key,
        name = name,
        reference = tax_benefit_system,
        )
    reform_key = key[6:]
    aliss_reform = build_aliss_reform()
    categories_fiscales_reform = aliss_reform[[reform_key, 'code_bdf']].drop_duplicates().copy()
    reform_mismatch = categories_fiscales_reform.groupby(['code_bdf']).filter(
        lambda x: x[reform_key].nunique() > 1).copy().sort_values('code_bdf')

    if not reform_mismatch.empty:
        if missmatch_rates == "weighted":
            categories_fiscales_reform, taux_by_categorie_fiscale = build_updated_categorie_fiscale(
                reform_key, categories_fiscales_reform)

        elif missmatch_rates == "higher":
            categories_fiscales_reform[reform_key] = categories_fiscales_reform[reform_key].astype(
                'category',
                categories = ['tva_taux_reduit', 'tva_taux_intermediaire', 'tva_taux_plein'],
                ordered = True,
                )
            # Keeping higher rate
            categories_fiscales_reform = categories_fiscales_reform.sort_values(
                ['code_bdf', reform_key]
                ).drop_duplicates(
                    subset = 'code_bdf', keep = 'last'
                    )
            assert not categories_fiscales_reform.code_bdf.duplicated().any()
            categories_fiscales_reform[reform_key] = categories_fiscales_reform[reform_key].astype(str)

    categories_fiscales_reform.rename(columns=({reform_key: 'categorie_fiscale'}), inplace = True)
    year = 2014
    categories_fiscales_data_frame, _ = get_legislation_data_frames()
    categories_fiscales = categories_fiscales_data_frame.query('start <= @year & @year <= stop').copy()

    assert not categories_fiscales.empty
    assert not categories_fiscales.code_bdf.duplicated().any()

    categories_fiscales_reform = categories_fiscales_reform.loc[
        categories_fiscales_reform.code_bdf.str[:3] == 'c01'].copy()

    assert not (categories_fiscales_reform.code_bdf == 'c02131').any()

    codes_bdf_by_reform_categorie_fiscale = dict(
        (
            categorie_fiscale,
            categories_fiscales_reform.query('categorie_fiscale == @categorie_fiscale')['code_bdf'].unique().tolist()
            )
        for categorie_fiscale in categories_fiscales_reform.categorie_fiscale.unique()
        )

    for categorie_fiscale, codes_bdf in codes_bdf_by_reform_categorie_fiscale.iteritems():
        categories_fiscales.loc[
            categories_fiscales.code_bdf.isin(codes_bdf), 'categorie_fiscale'] = categorie_fiscale

    assert not categories_fiscales.code_bdf.duplicated().any(), "there are {} duplicated entries".format(
        categories_fiscales.code_bdf.duplicated().sum())

    generate_variables(
        categories_fiscales = categories_fiscales,
        Reform = Reform,
        tax_benefit_system = tax_benefit_system,
        )  # Dépenses hors taxes
    generate_postes_agreges_variables(
        categories_fiscales = categories_fiscales,
        Reform = Reform,
        taux_by_categorie_fiscale = taux_by_categorie_fiscale,
        tax_benefit_system = tax_benefit_system,
        )  # Dépenses taxes comprises des postes agrégés
    taux_by_categorie_fiscale = taux_by_categorie_fiscale if taux_by_categorie_fiscale is not None else dict()
    generate_additional_tva_variables(
        Reform = Reform,
        taux_by_categorie_fiscale = taux_by_categorie_fiscale,
        tax_benefit_system = tax_benefit_system,
        )

    reform = Reform()
    return reform


def build_budget_shares(rebuild = False):
    budget_shares_csv_path = os.path.join(aliss_assets_reform_directory, 'budget-shares.csv')
    if not rebuild and os.path.exists(budget_shares_csv_path):
        return pd.read_csv(budget_shares_csv_path)

    aliss = build_clean_aliss_data_frame()
    aliss = add_poste_coicop(aliss)
    kept_variables = ['dt_k', 'nomf', 'nomc', 'poste_coicop', 'tpoids']
    aliss = aliss[kept_variables].copy()
    aliss_expenditures = aliss.groupby(
        ['poste_coicop', 'nomc', 'nomf']).apply(
            lambda df: (df.tpoids * df.dt_k).sum()
            ).reset_index()
    aliss_expenditures.rename(columns = {0: "expenditures"}, inplace = True)

    aliss_expenditures['budget_share'] = aliss_expenditures.groupby(
        ['poste_coicop'])['expenditures'].transform(
            lambda x: x / x.sum()
            )
    budget_shares = aliss_expenditures.query('budget_share < 1').copy()
    budget_shares.to_csv(budget_shares_csv_path)

    return budget_shares


def build_legislation_including_f_nomencalture():
    aliss_uncomplete = build_clean_aliss_data_frame()
    aliss = add_poste_coicop(aliss_uncomplete)
    aliss_extract = aliss[['nomf', 'nomk', 'poste_bdf', 'poste_coicop']].copy()
    aliss_extract.drop_duplicates(inplace = True)

    legislation_directory = os.path.join(
        pkg_resources.get_distribution('openfisca_france_indirect_taxation').location,
        'openfisca_france_indirect_taxation',
        'assets',
        'legislation',
        )
    codes_coicop_data_frame = pd.read_csv(
        os.path.join(legislation_directory, 'coicop_legislation.csv'),
        )
    legislation = codes_coicop_data_frame[['code_bdf', 'categorie_fiscale']].copy()
    legislation.rename(columns = {'code_bdf': 'poste_bdf'}, inplace = True)
    return aliss_extract.merge(legislation)


def build_updated_categorie_fiscale(reform_key, categories_fiscales_reform):
    mismatch = pd.read_csv(os.path.join(
        aliss_assets_reform_directory,
        '{}_reform_mismatch.csv'.format(reform_key)
        ))
    mismatch['nomc_shrinked'] = mismatch.nomc.str[:4].copy()
    mismatch.drop('nomc', axis = 1, inplace = True)
    budget_shares = build_budget_shares()
    budget_shares['nomc_shrinked'] = budget_shares.nomc.str[:4].copy()

    taux_by_categorie_fiscale = {
        'tva_taux_super_reduit': .021,
        'tva_taux_reduit': .055,
        'tva_taux_intermediaire': .1,
        'tva_taux_plein': .2,
        }

    weighted_categories_fiscales = mismatch.merge(budget_shares)
    weighted_categories_fiscales['reform_rate'] = weighted_categories_fiscales[reform_key].map(
        taux_by_categorie_fiscale)

    def weighted_mean(x):
        return np.average(x, weights = weighted_categories_fiscales.loc[x.index, "budget_share"])

    reform_rate = weighted_categories_fiscales.groupby(['code_bdf', 'poste_coicop'])['reform_rate'].agg(
        weighted_mean).reset_index()

    weighted_categories_fiscales = weighted_categories_fiscales.drop('reform_rate', axis = 1).merge(reform_rate)
    weighted_categories_fiscales[reform_key] = "tva_taux_" + weighted_categories_fiscales.poste_coicop.str[6:]

    # Updating taux_by_categorie_fiscale
    taux_by_categorie_fiscale_update = weighted_categories_fiscales[
        [reform_key, 'reform_rate']
        ].set_index(reform_key).to_dict()['reform_rate']
    taux_by_categorie_fiscale.update(taux_by_categorie_fiscale_update)

    # Updating categories_fiscales_reform
    weighted_categories_fiscales = weighted_categories_fiscales[
        ['code_bdf', reform_key, 'reform_rate']
        ].drop_duplicates()

    duplicated_code_bdf = categories_fiscales_reform.code_bdf.loc[
        categories_fiscales_reform.code_bdf.duplicated(keep = False)
        ].unique()

    # We check that the duplicated code_bdf corresponds to the mismatched ones ...
    assert set(duplicated_code_bdf) == set(weighted_categories_fiscales.code_bdf.unique())
    # ... so we can remove them ...
    categories_fiscales_reform.drop_duplicates(subset = 'code_bdf', keep = False, inplace = True)
    assert not categories_fiscales_reform.code_bdf.duplicated().any()
    # ... to replace them by the ad hoc categories fiscales
    categories_fiscales_reform.set_index('code_bdf', inplace = True)
    categories_fiscales_reform = categories_fiscales_reform.combine_first(
        weighted_categories_fiscales[[reform_key, 'code_bdf']].set_index('code_bdf')
        )
    categories_fiscales_reform.reset_index(inplace = True)
    log.info(u'The tva categries for reform_key {} are:\n{}'.format(reform_key, sorted(taux_by_categorie_fiscale)))
    return categories_fiscales_reform, taux_by_categorie_fiscale


def depenses_new_tva_function_creator(categorie_fiscale = None, taux = None):
    assert categorie_fiscale is not None
    assert taux is not None

    @dated_function(start = None, stop = None)
    def func(self, simulation, period, categorie_fiscale = categorie_fiscale, taux = taux):
        return period, (
            simulation.calculate('depenses_ht_poste_{}'.format(categorie_fiscale[9:]), period) * (1 + taux)
            )

    func.__name__ = "function"
    return func


def new_tva_function_creator(categorie_fiscale = None, taux = None):
    assert categorie_fiscale is not None
    assert taux is not None

    @dated_function(start = None, stop = None)
    def func(self, simulation, period, categorie_fiscale = categorie_fiscale, taux = taux):
        return period, (
            simulation.calculate('depenses_ht_poste_{}'.format(categorie_fiscale[9:]), period) * taux
            )

    func.__name__ = "function"
    return func


def new_tva_total_function_creator(categories_fiscales):
    @dated_function(start = None, stop = None)
    def func(self, simulation, period):
        return period, sum(
            simulation.calculate(categorie_fiscale, period) for categorie_fiscale in categories_fiscales
            )

    func.__name__ = "function"
    return func


def generate_additional_tva_variables(Reform = None, taux_by_categorie_fiscale = None, tax_benefit_system = None):
    for categorie_fiscale, taux in taux_by_categorie_fiscale.iteritems():
        depenses_new_tva_func = depenses_new_tva_function_creator(categorie_fiscale = categorie_fiscale, taux = taux)
        new_tva_func = new_tva_function_creator(categorie_fiscale = categorie_fiscale, taux = taux)
        if not categorie_fiscale.startswith('tva'):
            continue
        # Trick to create a class with a dynamic name.
        try:
            definitions_by_name = dict(
                column = FloatCol,
                entity_class = Menages,
                label = u"Dépenses taxes comprises: {0}".format(categorie_fiscale),
                function = depenses_new_tva_func,
                )
            depenses_class_name = u'depenses_{}'.format(categorie_fiscale)
            type(depenses_class_name.encode('utf-8'), (Reform.DatedVariable,), definitions_by_name)
            del definitions_by_name

            definitions_by_name = dict(
                column = FloatCol,
                entity_class = Menages,
                label = u"Montant de la TVA acquitée à {0}".format(categorie_fiscale),
                function = new_tva_func,
                )
            tva_class_name = u'{}'.format(categorie_fiscale)
            type(tva_class_name.encode('utf-8'), (Reform.DatedVariable,), definitions_by_name)
            del definitions_by_name
            log.info(u'{} Created new fiscal category {}'.format(Reform.name, categorie_fiscale))

        except AssertionError as e:
            log.info(e)
            log.info(u'{} Fiscal category {} is not new : passing'.format(Reform.name, categorie_fiscale))
            pass

    # tva_total variable creation
    categories_fiscales = [
        categorie_fiscale
        for categorie_fiscale in taux_by_categorie_fiscale.keys()
        if categorie_fiscale.startswith('tva_taux_')
        ]
    new_tva_total_func = new_tva_total_function_creator(categories_fiscales)
    definitions_by_name = dict(
        reference = tax_benefit_system.column_by_name[u'tva_total'.encode('utf-8')],
        function = new_tva_total_func,
        )
    type(u'tva_total'.encode('utf-8'), (Reform.Variable,), definitions_by_name)
    del definitions_by_name


if __name__ == '__main__':
    pass
#    from openfisca_france_indirect_taxation.tests import base
#    year = 2014
#    data_year = 2011
#    reform_key = 'aliss_sante'
#    tax_benefit_system = base.tax_benefit_system
#    reform = build_reform_mixte(tax_benefit_system)