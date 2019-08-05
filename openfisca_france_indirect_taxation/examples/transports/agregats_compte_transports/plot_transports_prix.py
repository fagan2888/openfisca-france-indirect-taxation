# -*- coding: utf-8 -*-

# Import de modules spécifiques à Openfisca, et import des données de prix des carburants
from ipp_macro_series_parser.agregats_transports.parser_cleaner_prix_carburants import prix_mensuel_carburants_90_15
from openfisca_france_indirect_taxation.examples.utils_example import graph_builder_carburants

# Utilisation de la date comme index
prix_mensuel_carburants_90_15[['annee'] + ['mois']] = prix_mensuel_carburants_90_15[['annee'] + ['mois']].astype(str)
prix_mensuel_carburants_90_15['date'] = \
    prix_mensuel_carburants_90_15['annee'] + '_' + prix_mensuel_carburants_90_15['mois']
prix_mensuel_carburants_90_15 = prix_mensuel_carburants_90_15.set_index('date')

# Calcul des taux de taxation implicite sur les carburants, incluant la TICPE et la TVA
prix_mensuel_carburants_90_15['taux_implicite_diesel_ticpe'] = (
    (prix_mensuel_carburants_90_15['diesel_ttc'] - prix_mensuel_carburants_90_15['diesel_ht'])
    / prix_mensuel_carburants_90_15['diesel_ht']
    )
prix_mensuel_carburants_90_15['taux_implicite_ticpe_super_95'] = (
    (prix_mensuel_carburants_90_15['super_95_ttc'] - prix_mensuel_carburants_90_15['super_95_ht'])
    / prix_mensuel_carburants_90_15['super_95_ht']
    )

# Changement des noms des variables pour être plus explicites
prix_mensuel_carburants_90_15.rename(columns = {'diesel_ht': 'prix diesel ht', 'diesel_ttc': 'prix diesel ttc',
    'super_95_ht': 'prix SP95 ht', 'super_95_ttc': 'prix SP95 ttc',
    'taux_implicite_diesel_ticpe': 'taux implicite diesel', 'taux_implicite_ticpe_super_95': 'taux implicite super 95'},
    inplace = True)

# Réalisation des graphiques
log.info('Evolution du prix des carburants entre 1990 et 2015')
graph_builder_carburants(
    prix_mensuel_carburants_90_15[['prix SP95 ttc'] + ['prix diesel ttc'] + ['prix SP95 ht'] + ['prix diesel ht']],
    'prix carburants', 0.39, 1.025, 'darkgreen', 'darkred', 'lawngreen', 'orangered')

log.info('Evolution du taux implicite de taxation (incluant la TVA) des carburants entre 1990 et 2015')
graph_builder_carburants(
    prix_mensuel_carburants_90_15[['taux implicite diesel'] + ['taux implicite super 95']],
    'taux implicite ticpe', 1, 1, 'darkred', 'darkgreen', None, None)
