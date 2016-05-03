# -*- coding: utf-8 -*-

from __future__ import division

from openfisca_core import reforms


def build_reform(tax_benefit_system):
    Reform = reforms.make_reform(
        key = 'taxe_carbone',
        name = u"Réforme de l'imposition indirecte des énergies selon leur contenu carbone",
        reference = tax_benefit_system,
        )

    reform = Reform()
    reform.modify_legislation_json(modifier_function = modify_legislation_json)
    return reform

# Réforme selon le prix du carbone : prix fixé à 50 euros par tonne de CO2. En utilisant nos données
# d'équivalence entre consommation et émission, on met en place les montants de taxe suivants :


def modify_legislation_json(reference_legislation_json_copy):
    reform_legislation_subtree = {
        "@type": "Node",
        "description": "taxe_carbone",
        "children": {
            "electricite": {
                "@type": "Parameter",
                "description": u"Surcroît de prix de l'électricité (en euros par kWh)",
                "format": 'float',
                "unit": 'currency',
                "values": [{'start': u'2010-01-01', 'stop': '2014-12-31', 'value': 0.0045}],
                },
            "essence": {
                "@type": "Parameter",
                "description": u"Surcroît de prix de l'essence (en euros par hectolitres)",
                "format": "float",
                "unit": 'currency',
                "values": [{'start': u'2010-01-01', 'stop': '2014-12-31', 'value': 12.1 - 1.694}],
                },
            "diesel": {
                "@type": "Parameter",
                "description": u"Surcroît de prix du diesel (en euros par hectolitres)",
                "format": 'float',
                "unit": 'currency',
                "values": [{'start': u'2010-01-01', 'stop': '2014-12-31', 'value': 13.3 - 1.862}],
                },
            "fioul_domestique": {
                "@type": "Parameter",
                "description": u"Surcroît de prix du diesel (en euros par litre)",
                "format": 'float',
                "unit": 'currency',
                "values": [{'start': u'2010-01-01', 'stop': '2014-12-31', 'value': 0.155 - 0.0217}],
                },
            "gaz": {
                "@type": "Parameter",
                "description": u"Surcroît de prix du gaz (en euros par kWh)",
                "format": 'float',
                "unit": 'currency',
                "values": [{'start': u'2010-01-01', 'stop': '2014-12-31', 'value': 0.012 - 0.00168}],
                },
            "abaissement_tva_taux_plein": {
                "@type": "Parameter",
                "description": u"Baisse de la TVA à taux plein pour obtenir un budget constant",
                "format": 'float',
                "values": [{'start': u'2010-01-01', 'stop': '2017-12-31', 'value': 0.03}],
                },
            "abaissement_tva_taux_plein_bis": {
                "@type": "Parameter",
                "description": u"Baisse de la TVA à taux plein pour obtenir un budget constant",
                "format": 'float',
                "values": [{'start': u'2010-01-01', 'stop': '2017-12-31', 'value': 0.022}],
                },
            "abaissement_tva_taux_reduit": {
                "@type": "Parameter",
                "description": u"Baisse de la TVA à taux plein pour obtenir un budget constant",
                "format": 'float',
                "values": [{'start': u'2010-01-01', 'stop': '2017-12-31', 'value': 0.015}],
                },
            "abaissement_tva_taux_super_reduit": {
                "@type": "Parameter",
                "description": u"Baisse de la TVA à taux plein pour obtenir un budget constant",
                "format": 'float',
                "values": [{'start': u'2010-01-01', 'stop': '2017-12-31', 'value': 0.015}],
                },
            },
        }

    reference_legislation_json_copy['children']['taxe_carbone'] = reform_legislation_subtree
    return reference_legislation_json_copy
