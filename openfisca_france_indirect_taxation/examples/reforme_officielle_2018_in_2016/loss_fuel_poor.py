# -*- coding: utf-8 -*-

# This script computes the share of households that financial lose from the reform,
# after transfers. This share is given by category (in particular by income deciles).
# Losses are computed on the basis of total financial gains and losses : a person
# loses from the reform if the transfer is lower than the additional spending induced
# by the reform.


from __future__ import division

import pandas as pd

from openfisca_france_indirect_taxation.surveys import SurveyScenario
from openfisca_france_indirect_taxation.examples.utils_example import graph_builder_bar, save_dataframe_to_graph
from openfisca_france_indirect_taxation.almost_ideal_demand_system.aids_estimation_from_stata import get_elasticities

from openfisca_france_indirect_taxation.examples.calage_bdf_cn_energy import get_inflators_by_year_energy


year = 2016
data_year = 2011
inflators_by_year = get_inflators_by_year_energy(rebuild = False)
inflation_kwargs = dict(inflator_by_variable = inflators_by_year[year])
elasticities = get_elasticities(data_year)

reforme = 'officielle_2018_in_2016'

survey_scenario = SurveyScenario.create(
    elasticities = elasticities,
    inflation_kwargs = inflation_kwargs,
    reform_key = reforme,
    year = year,
    data_year = data_year
    )

simulated_variables = [
    'revenu_reforme_officielle_2018_in_2016',
    'pertes_financieres_avant_redistribution_officielle_2018_in_2016',
    'cheques_energie_ruraux_officielle_2018_in_2016',
    'cheques_energie_officielle_2018_in_2016',
    'cheques_energie_by_energy_officielle_2018_in_2016',
    'cheques_energie_ruraux_by_energy_officielle_2018_in_2016',
    'reste_transferts_neutre_officielle_2018_in_2016',
    'niveau_vie_decile',
    'pondmen',
    'precarite_energetique_rev_disponible',
    'precarite_transports_rev_disponible',
    ]


def distribution_pertes_precaires(df_precaires):
    quantiles = [0.1, 0.25, 0.5, 0.75, 0.9]
    df_to_plot = pd.DataFrame(index = quantiles, columns = ['transfert_net_cheque_officiel'])
    for i in quantiles:
        df_to_plot['transfert_net_cheque_officiel'][i] = \
            df_precaires['transfert_net_cheque_officiel'].quantile(i)
    
    graph_builder_bar(df_to_plot, False)
    #save_dataframe_to_graph(df_to_plot, 'Monetary/losses_among_fuel_poors.csv')
    
    return df_to_plot


df_reforme = survey_scenario.create_data_frame_by_entity(simulated_variables, period = year)['menage']

df_reforme[u'transfert_net_cheque_officiel'] = (
    df_reforme['cheques_energie_ruraux_by_energy_officielle_2018_in_2016']
    + df_reforme['reste_transferts_neutre_officielle_2018_in_2016']
    - df_reforme['revenu_reforme_officielle_2018_in_2016'] 
    )
df_reforme['perdant_fiscal_cheque_officiel'] = 1 * (df_reforme['transfert_net_cheque_officiel'] < 0)

df_reforme['precarite_jointe'] = (
    1 * ((df_reforme['precarite_energetique_rev_disponible'] + df_reforme['precarite_transports_rev_disponible']) > 0)
    )

df_precaires_joint = df_reforme.query('precarite_jointe == 1')
df_precaires_transports = df_reforme.query('precarite_transports_rev_disponible == 1')
df_precaires_logement = df_reforme.query('precarite_energetique_rev_disponible == 1')

df_to_plot = distribution_pertes_precaires(df_precaires_joint)
#df_to_plot = distribution_pertes_precaires(df_precaires_transports)
#df_to_plot = distribution_pertes_precaires(df_precaires_logement)
