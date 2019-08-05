# -*- coding: utf-8 -*-


from openfisca_france_indirect_taxation.examples.utils_example import graph_builder_line_percent, \
    save_dataframe_to_graph, dataframe_by_group
from openfisca_france_indirect_taxation.surveys import SurveyScenario
from openfisca_france_indirect_taxation.almost_ideal_demand_system.aids_estimation_from_stata import get_elasticities
from openfisca_france_indirect_taxation.examples.calage_bdf_cn_energy import get_inflators_by_year_energy

#
inflators_by_year = get_inflators_by_year_energy(rebuild = False)
year = 2014
data_year = 2011
elasticities = get_elasticities(data_year)
inflation_kwargs = dict(inflator_by_variable = inflators_by_year[year])

simulated_variables = ['depenses_energies_totales', 'depenses_energies_logement', 'depenses_essence_corrigees', 'depenses_diesel_corrigees',
                       'depenses_carburants_corrigees', 'depenses_electricite', 'depenses_gaz_ville', 'depenses_combustibles_liquides',
                       'depenses_combustibles_solides', 'poste_04_5_4_1_1', 'rev_disp_loyerimput']

survey_scenario = SurveyScenario.create(
    elasticities = elasticities,
    inflation_kwargs = inflation_kwargs,
    year = year,
    data_year = data_year
    )

for category in ['niveau_vie_decile', 'age_group_pr', 'strate']:
    df = dataframe_by_group(survey_scenario, category, simulated_variables, use_baseline =True)

    df.rename(columns = {'rev_disp_loyerimput': 'disposable income'},
        inplace = True)
    for resource in ['disposable income']:
        df['Energy share in {}'.format(resource)] = df['depenses_energies_totales'] / df[resource]
        df['Housing energy share in {}'.format(resource)] = df['depenses_energies_logement'] / df[resource]
        df['Transport energy share in {}'.format(resource)] = df['depenses_carburants_corrigees'] / df[resource]
        df['Diesel share in {}'.format(resource)] = df['depenses_diesel_corrigees'] / df[resource]
        df['Gasoline share in {}'.format(resource)] = df['depenses_essence_corrigees'] / df[resource]
        df['Electricity share in {}'.format(resource)] = df['depenses_electricite'] / df[resource]
        df['Natural gas share in {}'.format(resource)] = df['depenses_gaz_ville'] / df[resource]
        df['Domestic fuel share in {}'.format(resource)] = df['depenses_combustibles_liquides'] / df[resource]
        df['Solid fuels share in {}'.format(resource)] = df['depenses_combustibles_solides'] / df[resource]

        # Réalisation de graphiques
        log.info(('Percentage of energy expenditure in {}').format(resource))
        graph_builder_line_percent(
            df[['Energy share in {}'.format(resource),
            'Housing energy share in {}'.format(resource),
            'Transport energy share in {}'.format(resource)]]
            )
        graph_builder_line_percent(
            df[['Diesel share in {}'.format(resource),
            'Gasoline share in {}'.format(resource)]]
            )
        graph_builder_line_percent(
            df[['Electricity share in {}'.format(resource),
            'Natural gas share in {}'.format(resource),
            'Domestic fuel share in {}'.format(resource),
            'Solid fuels share in {}'.format(resource)]]
            )

        # save_dataframe_to_graph(df,
        #    'Expenditures/share_energy_expenditures_in_{0}_by_{1}.csv'.format(resource.replace(' ', '_'), category))
