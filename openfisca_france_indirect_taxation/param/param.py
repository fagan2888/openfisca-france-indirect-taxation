# -*- coding: utf-8 -*-


legislation_json = {
    "start": '2000-01-01',
    # "stop": u'2014-12-31',
    "@type": "Node",
    "children": {
        "imposition_indirecte": {

            "description": "Impôts et taxes indirectes",
            "children": {
                "tva": {

                    "description": "Taxe sur la valeur ajoutée",
                    "children": {
                        "taux_plein": {
                                        "description": "Taux plein",
                            "format": "float",
                            "values": [
                                {'start': '2014-01-01', 'value': .2},
                                {'start': '2000-04-01', 'value': .196},
                                {'start': '1995-08-01', 'value': .206},
                                {'start': '1993-01-01', 'value': .186},
                                ],
                            },
                        "taux_intermediaire": {
                                        "description": "Taux intermédiaire",
                            "format": "float",
                            "values": [
                                {'start': '2014-01-01', 'value': .1},
                                {'start': '2012-01-01', 'value': .07},
                                {'start': '1995-01-01', 'value': 0},
                                ],
                            },
                        "taux_reduit": {
                                        "description": "Taux réduit",
                            "format": "float",
                            "values": [
                                {'start': '2000-01-01', 'value': .055}
                                ],
                            },
                        "taux_super_reduit": {
                                        "description": "Taux super réduit",
                            "format": "float",
                            "values": [
                                {'start': '1995-01-01', 'value': .021}
                                ],
                            },
                        },
                    },
                "taux_assurances": {

                    "description": "Différentes taxes sur les assurances",
                    "children": {
                        "taux_assur_transport": {
                                        "description": "Le taux d'assurance sur les transports",
                            "format": "float",
                            "values": [
                                {'start': '2014-01-01', 'value': 0.342},
                                {'start': '2013-01-01', 'value': 0.342},
                                {'start': '2012-01-01', 'value': 0.342},
                                {'start': '2011-01-01', 'value': 0.342},
                                {'start': '2010-01-01', 'value': 0.342},
                                {'start': '2009-01-01', 'value': 0.336},
                                {'start': '2008-01-01', 'value': 0.336},
                                {'start': '2007-01-01', 'value': 0.331},
                                {'start': '2006-01-01', 'value': 0.331},
                                {'start': '2005-01-01', 'value': 0.331},
                                {'start': '2004-01-01', 'value': 0.33},
                                {'start': '2003-01-01', 'value': 0.33},
                                {'start': '2002-01-01', 'value': 0.33},
                                {'start': '1995-01-01', 'value': 0.18},
                                ],
                            },
                        "taux_assurances_sante": {
                                        "description": "Le taux d'assurance sante",
                            "format": "float",
                            "values": [
                                {'start': '2014-01-01', 'value': 0.1327},
                                {'start': '2013-01-01', 'value': 0.1327},
                                {'start': '2012-01-01', 'value': 0.1327},
                                {'start': '2011-01-01', 'value': 0.094},
                                {'start': '2010-01-01', 'value': 0.059},
                                {'start': '2009-01-01', 'value': 0.059},
                                {'start': '2008-01-01', 'value': 0.035},
                                {'start': '2007-01-01', 'value': 0.045},
                                {'start': '2006-01-01', 'value': 0.055},
                                {'start': '2005-01-01', 'value': 0.0575},
                                {'start': '2004-01-01', 'value': 0.0675},
                                {'start': '2003-01-01', 'value': 0.0775},
                                {'start': '2002-01-01', 'value': 0.0875},
                                {'start': '2001-01-01', 'value': 0.0875},
                                {'start': '2000-01-01', 'value': 0.0875},
                                {'start': '1995-01-01', 'value': 0.07},
                                ],
                            },
                        "taux_assurances_autres": {
                                        "description": "Le taux d'assurance sur autres",
                            "format": "float",
                            "values": [
                                {'start': '2014-01-01', 'value': 0.09},
                                {'start': '2013-01-01', 'value': 0.09},
                                {'start': '2012-01-01', 'value': 0.09},
                                {'start': '2011-01-01', 'value': 0.09},
                                {'start': '2010-01-01', 'value': 0.09},
                                {'start': '2009-01-01', 'value': 0.09},
                                {'start': '2008-01-01', 'value': 0.09},
                                {'start': '2007-01-01', 'value': 0.09},
                                {'start': '2006-01-01', 'value': 0.09},
                                {'start': '2005-01-01', 'value': 0.09},
                                {'start': '2004-01-01', 'value': 0.09},
                                {'start': '2003-01-01', 'value': 0.09},
                                {'start': '2002-01-01', 'value': 0.09},
                                {'start': '2001-01-01', 'value': 0.09},
                                {'start': '2000-01-01', 'value': 0.09},
                                {'start': '1995-01-01', 'value': 0.09},
                                ],
                            },
                        },
                    },
                "prix_carburants": {

                    "description": "prix des carburants en euros par hectolitre",
                    "children": {
                        "prix_ttc_gazole": {
                                        "description": "prix ttc gazole",
                            "format": "float",
                            "values": [
                                # TODO: Doit-on déplacer les prix dans un autre arbre ?
                                {'start': '2014-01-01', 'value': 128.56},
                                {'start': '2013-01-01', 'value': 135.02},
                                {'start': '2012-01-01', 'value': 139.58},
                                {'start': '2011-01-01', 'value': 133.42},
                                {'start': '2010-01-01', 'value': 114.6749057},
                                {'start': '2009-01-01', 'value': 100.235},
                                {'start': '2008-01-01', 'value': 126.7092308},
                                {'start': '2007-01-01', 'value': 109.4932692},
                                {'start': '2006-01-01', 'value': 107.7509615},
                                {'start': '2005-01-01', 'value': 102.6803846},
                                {'start': '2004-01-01', 'value': 88.4709434},
                                {'start': '2003-01-01', 'value': 79.34711538},
                                {'start': '2002-01-01', 'value': 77.24235269},
                                {'start': '2001-01-01', 'value': 79.60183423},
                                {'start': '2000-01-01', 'value': 84.68271802},
                                {'start': '1999-01-01', 'value': 68.9985},
                                {'start': '1998-01-01', 'value': 64.239},
                                {'start': '1997-01-01', 'value': 67.64},
                                {'start': '1996-01-01', 'value': 65.33},
                                {'start': '1995-01-01', 'value': 58.69},
                                ],
                            },
                        "prix_ttc_super95": {
                                        "description": "Prix ttc super95 ",
                            "format": "float",
                            "values": [
                                {'start': '2012-01-01', 'value': 156.58},
                                {'start': '2011-01-01', 'value': 149.94},
                                {'start': '2010-01-01', 'value': 134.6401887},
                                {'start': '2009-01-01', 'value': 120.9205769},
                                {'start': '2008-01-01', 'value': 135.3755769},
                                {'start': '2007-01-01', 'value': 127.6451923},
                                {'start': '2006-01-01', 'value': 123.6817308},
                                {'start': '2005-01-01', 'value': 116.5913462},
                                {'start': '2004-01-01', 'value': 106.0273585},
                                {'start': '2003-01-01', 'value': 101.6317308},
                                {'start': '2002-01-01', 'value': 101.4594819},
                                {'start': '2001-01-01', 'value': 103.2881858},
                                {'start': '2000-01-01', 'value': 109.1731165},
                                {'start': '1999-01-01', 'value': 95.5},
                                {'start': '1998-01-01', 'value': 91.8586},
                                {'start': '1997-01-01', 'value': 94.1098},
                                {'start': '1996-01-01', 'value': 90.91},
                                {'start': '1995-01-01', 'value': 85.7},
                                ],
                            },
                        #                        Bien changer les prix et appliquer ceux de l'E10
                        #                            "prix_ttc_superE10": {
                        #                                    #                            "description": u"Prix ttc super95 ",
                        #                            "format": "float",
                        #                            "values": [
                        #                                {'start': u'1995-01-01', 'value': 85.7},
                        #                                {'start': u'1996-01-01', 'value': 90.91},
                        #                                {'start': u'1997-01-01', 'value': 94.1098},
                        #                                {'start': u'1998-01-01', 'value': 91.8586},
                        #                                {'start': u'1999-01-01', 'value': 95.5},
                        #                                {'start': u'2000-01-01', 'value': 109.1731165},
                        #                                {'start': u'2001-01-01', 'value': 103.2881858},
                        #                                {'start': u'2002-01-01', 'value': 101.4594819},
                        #                                {'start': u'2003-01-01', 'value': 101.6317308},
                        #                                {'start': u'2004-01-01', 'value': 106.0273585},
                        #                                {'start': u'2005-01-01', 'value': 116.5913462},
                        #                                {'start': u'2006-01-01', 'value': 123.6817308},
                        #                                {'start': u'2007-01-01', 'value': 127.6451923},
                        #                                {'start': u'2008-01-01', 'value': 135.3755769},
                        #                                {'start': u'2009-01-01', 'value': 120.9205769},
                        #                                {'start': u'2010-01-01', 'value': 134.6401887},
                        #                                {'start': u'2011-01-01', 'value': 149.94},
                        #                                # TODO: {'start': u'2012-01-01', 'value': },
                        #                                ],
                        #                            },
                        "prix_ttc_super98": {
                                        "description": "prix ttc super98",
                            "format": "float",
                            "values": [
                                {'start': '2011-01-01', 'value': 153.75},
                                {'start': '2010-01-01', 'value': 138.214717},
                                {'start': '2009-01-01', 'value': 124.3081974},
                                {'start': '2008-01-01', 'value': 139.2867308},
                                {'start': '2007-01-01', 'value': 130.8551923},
                                {'start': '2006-01-01', 'value': 127.4303846},
                                {'start': '2005-01-01', 'value': 120.5273077},
                                {'start': '2004-01-01', 'value': 108.2684906},
                                {'start': '2003-01-01', 'value': 103.655},
                                {'start': '2002-01-01', 'value': 103.6501704},
                                {'start': '2001-01-01', 'value': 105.7028769},
                                {'start': '2000-01-01', 'value': 110.9293672},
                                {'start': '1999-01-01', 'value': 96.36062},
                                {'start': '1998-01-01', 'value': 92.3176},
                                {'start': '1997-01-01', 'value': 95.034},
                                {'start': '1996-01-01', 'value': 91.71},
                                {'start': '1995-01-01', 'value': 86.31},
                                ],
                            },
                        },
                    },
                "ticpe": {

                    "description": "ticpe sur les différents produits énergetiques",
                    "children": {
                        "ticpe_supercarburants": {
                                        "description": "ticpe sur super95 super98 et superE10, incluant majorations des régions",
                            "format": "float",
                            "values": [
                                {'start': '2016-01-01', 'value': 64.85},
                                {'start': '2015-01-01', 'value': 63.14},
                                {'start': '2014-01-01', 'value': 61.42},
                                {'start': '2013-01-01', 'value': 61.42},
                                {'start': '2012-01-01', 'value': 61.42},
                                {'start': '2011-01-01', 'value': 61.42},
                                {'start': '2010-01-01', 'value': 60.69},
                                {'start': '2009-01-01', 'value': 60.69},
                                {'start': '2008-01-01', 'value': 60.69},
                                {'start': '2007-01-01', 'value': 60.69},
                                {'start': '2006-01-01', 'value': 58.92},
                                {'start': '2005-01-01', 'value': 58.92},
                                {'start': '2004-01-01', 'value': 58.92},
                                {'start': '2003-01-01', 'value': 58.92},
                                {'start': '2002-01-01', 'value': 58.63},
                                {'start': '2001-01-01', 'value': 58.63},
                                {'start': '1995-01-01', 'value': 58.63},
                                ],
                            },
                        "ticpe_gazole": {
                                        "description": "ticpe sur diesel, incluant majorations des régions ",
                            "format": "float",
                            "values": [
                                {'start': '2016-01-01', 'value': 50.16},
                                {'start': '2015-01-01', 'value': 48.17},
                                {'start': '2011-01-01', 'value': 44.19},
                                {'start': '2007-01-01', 'value': 42.84},
                                {'start': '2004-01-01', 'value': 41.69},
                                {'start': '2003-01-01', 'value': 39.19},
                                {'start': '1995-01-01', 'value': 38.9},
                                ],
                            },
                        },
                    },





                "alcool_conso_et_vin": {

                    "description": "alcools",
                    "children": {
                        "vin": {

                            "description": "Pour calculer le taux de taxation implicite sur le vin",
                            "children": {
                                "droit_cn_vin": {
                                                        "description": "Masse droit vin, vin mousseux, cidres et poirés selon comptabilité nationale",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 122},
                                        {'start': '2012-01-01', 'value': 120},
                                        {'start': '2011-01-01', 'value': 118},
                                        {'start': '2010-01-01', 'value': 119},
                                        {'start': '2009-01-01', 'value': 117},
                                        {'start': '2008-01-01', 'value': 114},
                                        {'start': '2007-01-01', 'value': 117},
                                        {'start': '2006-01-01', 'value': 119},
                                        {'start': '2005-01-01', 'value': 117},
                                        {'start': '2004-01-01', 'value': 125},
                                        {'start': '2003-01-01', 'value': 127},
                                        {'start': '2002-01-01', 'value': 127},
                                        {'start': '2001-01-01', 'value': 127},
                                        {'start': '2000-01-01', 'value': 127},
                                        {'start': '1999-01-01', 'value': 133},
                                        {'start': '1998-01-01', 'value': 132},
                                        {'start': '1997-01-01', 'value': 129},
                                        {'start': '1996-01-01', 'value': 130},
                                        {'start': '1995-01-01', 'value': 129},
                                        ],
                                    },
                                "masse_conso_cn_vin": {
                                                        "description": "Masse consommation vin, vin mousseux, cidres et poirés selon comptabilité nationale",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 11515},
                                        {'start': '2012-01-01', 'value': 11407},
                                        {'start': '2011-01-01', 'value': 11387},
                                        {'start': '2010-01-01', 'value': 11002},
                                        {'start': '2009-01-01', 'value': 10728},
                                        {'start': '2008-01-01', 'value': 10461},
                                        {'start': '2007-01-01', 'value': 10345},
                                        {'start': '2006-01-01', 'value': 10002},
                                        {'start': '2005-01-01', 'value': 9933},
                                        {'start': '2004-01-01', 'value': 9985},
                                        {'start': '2003-01-01', 'value': 9695},
                                        {'start': '2002-01-01', 'value': 9476},
                                        {'start': '2001-01-01', 'value': 9168},
                                        {'start': '2000-01-01', 'value': 8854},
                                        {'start': '1999-01-01', 'value': 8451},
                                        {'start': '1998-01-01', 'value': 8025},
                                        {'start': '1997-01-01', 'value': 7636},
                                        {'start': '1996-01-01', 'value': 7419},
                                        {'start': '1995-01-01', 'value': 7191},
                                        ],
                                    },
                                },
                            },
                        "biere": {

                            "description": "Pour calculer le taux de taxation implicite sur la bière",
                            "children": {
                                "droit_cn_biere": {
                                                        "description": "Masse droit biere selon comptabilité nationale",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 897},
                                        {'start': '2012-01-01', 'value': 783},
                                        {'start': '2011-01-01', 'value': 393},
                                        {'start': '2010-01-01', 'value': 375},
                                        {'start': '2009-01-01', 'value': 376},
                                        {'start': '2008-01-01', 'value': 375},
                                        {'start': '2007-01-01', 'value': 382},
                                        {'start': '2006-01-01', 'value': 396},
                                        {'start': '2005-01-01', 'value': 364},
                                        {'start': '2004-01-01', 'value': 378},
                                        {'start': '2003-01-01', 'value': 370},
                                        {'start': '2002-01-01', 'value': 361},
                                        {'start': '2001-01-01', 'value': 364},
                                        {'start': '2000-01-01', 'value': 359},
                                        {'start': '1999-01-01', 'value': 380},
                                        {'start': '1998-01-01', 'value': 365},
                                        {'start': '1997-01-01', 'value': 364},
                                        {'start': '1996-01-01', 'value': 366},
                                        {'start': '1995-01-01', 'value': 361},
                                        ],
                                    },
                                "masse_conso_cn_biere": {
                                                        "description": "Masse consommation biere selon comptabilité nationale",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 3321},
                                        {'start': '2012-01-01', 'value': 2868},
                                        {'start': '2011-01-01', 'value': 2769},
                                        {'start': '2010-01-01', 'value': 2461},
                                        {'start': '2009-01-01', 'value': 2375},
                                        {'start': '2008-01-01', 'value': 2287},
                                        {'start': '2007-01-01', 'value': 2458},
                                        {'start': '2006-01-01', 'value': 2486},
                                        {'start': '2005-01-01', 'value': 2466},
                                        {'start': '2004-01-01', 'value': 2484},
                                        {'start': '2003-01-01', 'value': 2554},
                                        {'start': '2002-01-01', 'value': 2405},
                                        {'start': '2001-01-01', 'value': 2327},
                                        {'start': '2000-01-01', 'value': 2290},
                                        {'start': '1999-01-01', 'value': 2334},
                                        {'start': '1998-01-01', 'value': 2291},
                                        {'start': '1997-01-01', 'value': 2186},
                                        {'start': '1996-01-01', 'value': 2144},
                                        {'start': '1995-01-01', 'value': 2111},
                                        ],
                                    },
                                },
                            },
                        "alcools_forts": {

                            "description": "Pour calculer le taux de taxation implicite sur alcools forts",
                            "children": {
                                "droit_cn_alcools": {
                                                        "description": "Masse droit alcool selon comptabilité nationale sans droits sur les produits intermediaires et cotisation spéciale alcool fort",
                                    "format": "float",
                                    "values": [
                                        {'start': '2012-01-01', 'value': 2225},
                                        {'start': '2011-01-01', 'value': 2150},
                                        {'start': '2010-01-01', 'value': 2111},
                                        {'start': '2009-01-01', 'value': 2031},
                                        {'start': '2008-01-01', 'value': 2005},
                                        {'start': '2007-01-01', 'value': 1990},
                                        {'start': '2006-01-01', 'value': 1954},
                                        {'start': '2005-01-01', 'value': 1842},
                                        {'start': '2004-01-01', 'value': 1908},
                                        {'start': '2003-01-01', 'value': 1891},
                                        {'start': '2002-01-01', 'value': 1932},
                                        {'start': '2001-01-01', 'value': 1957},
                                        {'start': '2000-01-01', 'value': 1872},
                                        # TODO: Problème pour les alcools forts chiffres différents entre les deux bases excel !
                                        ],
                                    },
                                "droit_cn_alcools_total": {
                                                        "description": "Masse droit alcool selon comptabilité nationale avec les differents droits",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 3022},
                                        {'start': '2012-01-01', 'value': 2718},
                                        {'start': '2011-01-01', 'value': 3078},
                                        {'start': '2010-01-01', 'value': 2734},
                                        {'start': '2009-01-01', 'value': 2629},
                                        {'start': '2008-01-01', 'value': 2528},
                                        {'start': '2007-01-01', 'value': 2516},
                                        {'start': '2006-01-01', 'value': 2477},
                                        {'start': '2005-01-01', 'value': 2352},
                                        {'start': '2004-01-01', 'value': 2409},
                                        {'start': '2003-01-01', 'value': 2453},
                                        {'start': '2002-01-01', 'value': 2503},
                                        {'start': '2001-01-01', 'value': 2514},
                                        {'start': '2000-01-01', 'value': 2416},
                                        {'start': '1999-01-01', 'value': 2385},
                                        {'start': '1998-01-01', 'value': 2369},
                                        {'start': '1997-01-01', 'value': 2366},
                                        {'start': '1996-01-01', 'value': 2350},
                                        {'start': '1995-01-01', 'value': 2337},
                                        ],
                                    },
                                "masse_conso_cn_alcools": {
                                                        "description": "Masse consommation alcool selon comptabilité nationale",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 7022},
                                        {'start': '2012-01-01', 'value': 6996},
                                        {'start': '2011-01-01', 'value': 6680},
                                        {'start': '2010-01-01', 'value': 6618},
                                        {'start': '2009-01-01', 'value': 6342},
                                        {'start': '2008-01-01', 'value': 6147},
                                        {'start': '2007-01-01', 'value': 6142},
                                        {'start': '2006-01-01', 'value': 6106},
                                        {'start': '2005-01-01', 'value': 5960},
                                        {'start': '2004-01-01', 'value': 5967},
                                        {'start': '2003-01-01', 'value': 5895},
                                        {'start': '2002-01-01', 'value': 5932},
                                        {'start': '2001-01-01', 'value': 5721},
                                        {'start': '2000-01-01', 'value': 5558},
                                        {'start': '1999-01-01', 'value': 5234},
                                        {'start': '1998-01-01', 'value': 5123},
                                        {'start': '1997-01-01', 'value': 5065},
                                        {'start': '1996-01-01', 'value': 5075},
                                        {'start': '1995-01-01', 'value': 4893},
                                        ],
                                    },
                                },
                            },
                        },
                    },
                "tabac": {

                    "description": "tabac",
                    "children": {
                        "cigarettes": {

                            "description": "Pour calculer le taux de taxation implicite sur les cigarettes",
                            "children": {
                                "taux_normal_cigarette": {
                                                        "description": "Taux normal cigarette",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-07-01', 'value': 0.647},
                                        {'start': '2011-01-01', 'value': 0.6425},
                                        {'start': '2004-05-01', 'value': 0.64},
                                        {'start': '2003-09-01', 'value': 0.62},
                                        {'start': '2000-04-01', 'value': 0.5899},
                                        {'start': '1995-08-01', 'value': 0.583},
                                        {'start': '1993-05-24', 'value': 0.587},
                                        ],
                                    },
                                "taux_specifique_cigarette": {
                                                        "description": "Taux specifique cigarette",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-07-01', 'value': 0.15},
                                        {'start': '2013-01-01', 'value': 0.125},
                                        {'start': '2012-01-01', 'value': 0.12},
                                        {'start': '2011-01-01', 'value': 0.09},
                                        {'start': '2004-01-05', 'value': 0.075},
                                        {'start': '1995-01-01', 'value': 0.05},
                                        ],
                                    },
                                },
                            },
                        "tabac_a_rouler": {

                            "description": "Pour calculer le taux de taxation implicite sur le tabac à rouler",
                            "children": {
                                "taux_normal_tabac_a_rouler": {
                                                        "description": "Taux normal tabac à rouler",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-07-01', 'value': 0.62},
                                        {'start': '2013-01-01', 'value': 0.6},
                                        {'start': '2004-01-05', 'value': 0.5857},
                                        {'start': '2000-04-01', 'value': 0.5169},
                                        {'start': '1995-08-01', 'value': 0.51},
                                        {'start': '1993-05-24', 'value': 0.514},
                                        ],
                                    },
                                "taux_specifique_tabac_a_rouler": {
                                                        "description": "Taux specifique tabac à rouler",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-12-01', 'value': 0.3},
                                        {'start': '1995-01-01', 'value': 0},
                                        ],
                                    },
                                },
                            },
                        "cigares": {

                            "description": "Pour calculer le taux de taxation implicite sur les cigares",
                            "children": {
                                "taux_normal_cigare": {
                                                        "description": "Taux normaux de taxation cigares",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 0.28},
                                        {'start': '2012-08-17', 'value': 0.2757},
                                        {'start': '2012-03-15', 'value': 0.2716},
                                        {'start': '2004-01-05', 'value': 0.2757},
                                        {'start': '2001-12-31', 'value': 0.2},
                                        {'start': '2001-01-08', 'value': 0.25},
                                        {'start': '2000-04-01', 'value': 0.2955},
                                        {'start': '1995-08-01', 'value': 0.2886},
                                        {'start': '1993-05-24', 'value': 0.2926},
                                        ]
                                    },
                                "taux_specifique_cigare": {
                                                        "description": "Taux spécifique de taxation cigares",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 0.05},
                                        {'start': '1995-01-01', 'value': 0},
                                        ]
                                    },
                                }
                            },
                        },
                    },
                "contribution_solidarite_avion": {

                    "description": "Taxe sur les billets d'avions",
                    "children": {
                        "Taxe sur les billets d'avions": {

                            "description": "Pour calculer le taux de taxation implicite sur les billets d'avions",
                            "children": {
                                "consommation_billets_d_avions": {
                                                        "description": "Consommation billets d'avions",
                                    "format": "float",
                                    "values": [
                                        {'start': '2013-01-01', 'value': 9605},
                                        {'start': '2012-01-01', 'value': 9490},
                                        {'start': '2011-01-01', 'value': 9130},
                                        {'start': '2010-01-01', 'value': 8618},
                                        {'start': '2009-01-01', 'value': 8734},
                                        {'start': '2008-01-01', 'value': 8609},
                                        {'start': '2007-01-01', 'value': 7853},
                                        {'start': '2006-01-01', 'value': 7355},
                                        {'start': '2005-01-01', 'value': 6658},
                                        {'start': '2004-01-01', 'value': 6122},
                                        {'start': '2003-01-01', 'value': 5543},
                                        {'start': '2000-01-01', 'value': 5024},
                                        {'start': '2002-01-01', 'value': 5422},
                                        {'start': '2001-01-01', 'value': 5187},
                                        ]
                                    },
                                "recette_de_la_contribution_sur_billets_d_avions": {
                                                        "description": "Revenu de la contribution",
                                    "format": "float",
                                    "values": [
                                        {'start': '2011-01-01', 'value': 175},
                                        {'start': '2010-01-01', 'value': 163},
                                        {'start': '2009-01-01', 'value': 162},
                                        {'start': '2008-01-01', 'value': 173},
                                        {'start': '2007-01-01', 'value': 164},
                                        {'start': '2006-01-01', 'value': 45},
                                        {'start': '1995-01-01', 'value': 0},
                                        ]
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
