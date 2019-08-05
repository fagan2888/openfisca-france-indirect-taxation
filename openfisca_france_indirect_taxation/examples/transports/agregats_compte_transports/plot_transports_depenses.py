# -*- coding: utf-8 -*-

# Ce script réalise des graphiques à partir des données des comptes des transports, i.e. nos agrégats de référence
# pour les transports : dépenses totales des ménages en carburants, et part de ces dépenses dans leur consommation

# Import de fonctions spécifiques à Openfisca indirect taxation et de bases de données des Comptes des Transports
from ipp_macro_series_parser.agregats_transports.transports_cleaner import a3_a
from openfisca_france_indirect_taxation.examples.utils_example import graph_builder_carburants, \
    graph_builder_carburants_no_color

# Sélection des variables utilisées dans les graphiques
a3_a['to_be_used'] = 0
a3_a.loc[a3_a['index'] == '0722 Carburants et lubrifiants (1)', 'to_be_used'] = 1
a3_a.loc[a3_a['index'] == '0722 Carburants et lubrifiants (1)', 'index'] = 'Dépenses carburants et lubrifiants'

a3_a.loc[a3_a['index'] == '07 Transport', 'to_be_used'] = 1
a3_a.loc[a3_a['index'] == '07 Transport', 'index'] = 'Dépenses totales en transports'

a3_a.loc[a3_a['index'] == 'Ensemble des dépenses de consommation des ménages ', 'to_be_used'] = 1

depenses_menages_transports = a3_a[a3_a['to_be_used'] == 1]
depenses_menages_transports = depenses_menages_transports.drop(['to_be_used'] + ['categorie'], axis = 1)
depenses_menages_transports = depenses_menages_transports.set_index(['index'])
depenses_menages_transports = depenses_menages_transports.transpose()

# Calcul des parts des transports et des carburants dans les dépenses totales des ménages
depenses_menages_transports['part carburants dépenses totales'] = (
    depenses_menages_transports['Dépenses carburants et lubrifiants']
    / depenses_menages_transports['Ensemble des dépenses de consommation des ménages ']
    )
depenses_menages_transports['part transports dépenses totales'] = (
    depenses_menages_transports['Dépenses totales en transports']
    / depenses_menages_transports['Ensemble des dépenses de consommation des ménages ']
    )

# Réalisation des graphiques
log.info('Evolution des dépenses des ménages en carburants')
graph_builder_carburants_no_color(depenses_menages_transports['Dépenses carburants et lubrifiants'],
    'depenses menages carburants', 0.9, 0.20)

log.info('Evolution de la part des carburants et des transports dans les dépenses totales des ménages')
graph_builder_carburants(
    depenses_menages_transports[['part transports dépenses totales'] + ['part carburants dépenses totales']],
    'part transports depenses menages', 1, 0.65, 'midnightblue', 'turquoise', 'blue', None)
