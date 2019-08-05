# -*- coding: utf-8 -*-


from openfisca_france_indirect_taxation.examples.utils_example import graph_builder_bar, \
    save_dataframe_to_graph
from openfisca_france_indirect_taxation.surveys import SurveyScenario
from openfisca_france_indirect_taxation.almost_ideal_demand_system.aids_estimation_from_stata import get_elasticities
from openfisca_france_indirect_taxation.examples.calage_bdf_cn_energy import get_inflators_by_year_energy

# Simulate contribution to fuel tax reform by categories
inflators_by_year = get_inflators_by_year_energy(rebuild = False)
year = 2014
data_year = 2011
elasticities = get_elasticities(data_year)
inflation_kwargs = dict(inflator_by_variable = inflators_by_year[year])
del inflation_kwargs['inflator_by_variable']['somme_coicop12']

for reforme in ['cce_2016_in_2014']:
    simulated_variables = [
        'total_taxes_energies'
        ]

survey_scenario = SurveyScenario.create(
    elasticities = elasticities,
    inflation_kwargs = inflation_kwargs,
    reform = reforme,
    year = year,
    data_year = data_year
    )


x = survey_scenario.compute_pivot_table(
    values = ['emissions_CO2_gaz'], columns = ['{}'.format('niveau_vie_decile')]
    )
y = survey_scenario.compute_pivot_table(
    values = ['emissions_CO2_gaz'], columns = ['{}'.format('niveau_vie_decile')],
    use_baseline =True,
    )

x == y

df_by_entity = survey_scenario.create_data_frame_by_entity(simulated_variables, period = year)
df_by_entity_bis = survey_scenario.create_data_frame_by_entity(simulated_variables, use_baseline =True, period = year)

menages = df_by_entity['menage']
menages_bis = df_by_entity_bis['menage']

unite_conso = (menages['ocde10'] * menages['pondmen']).sum()
contribution = (menages['difference_contribution_energie_{}'.format(reforme)] * menages['pondmen']).sum()
contribution_unite_conso = contribution / unite_conso

# for category in ['niveau_vie_decile', 'age_group_pr', 'strate']:
menages['Cost_after_green_cheques'] = (
    ((contribution_unite_conso) * menages['ocde10'] - menages['difference_contribution_energie_{}'.format(reforme)])
    )

log.info(reforme)
for i in range(1, 11):
    menages_decile = menages.loc[menages['niveau_vie_decile'] == i]
    len_decile = float(len(menages_decile))

    menages_decile_loosers = menages_decile.query('Cost_after_green_cheques < 0')
    len_loosers = float(len(menages_decile_loosers))
    share = len_loosers / len_decile

    mean_loosers = menages_decile_loosers['Cost_after_green_cheques'].mean()
    mean_loosers_income = menages_decile_loosers['rev_disp_loyerimput'].mean()

    log.info(i, share * 100, mean_loosers, mean_loosers_income)
