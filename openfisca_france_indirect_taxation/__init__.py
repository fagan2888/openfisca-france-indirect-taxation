# -*- coding: utf-8 -*-


# OpenFisca -- A versatile microsimulation software
# By: OpenFisca Team <contact@openfisca.fr>
#
# Copyright (C) 2011, 2012, 2013, 2014 OpenFisca Team
# https://github.com/openfisca
#
# This file is part of OpenFisca.
#
# OpenFisca is free software; you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# OpenFisca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import os

from openfisca_core.taxbenefitsystems import XmlBasedTaxBenefitSystem

from .entities import entity_class_by_symbol
from .scenarios import Scenario
from . import param
from .param import preprocessing


# TaxBenefitSystems

def init_country():
    class TaxBenefitSystem(XmlBasedTaxBenefitSystem):
        entity_class_by_key_plural = {
            entity_class.key_plural: entity_class
            for entity_class in entity_class_by_symbol.itervalues()
            }
        legislation_xml_file_path = os.path.join(
            os.path.dirname(os.path.abspath(param.__file__)),
            'parameters.xml'
            )
        preprocess_legislation = staticmethod(preprocessing.preprocess_legislation)

        def prefill_cache(self):
            # Define categorie_fiscale_* and poste_coicp_* variables
            from .model.consommation import categories_fiscales
            categories_fiscales.preload_categories_fiscales_data_frame()
            from .model.consommation import postes_coicop
            postes_coicop.preload_postes_coicop_data_frame()
            # Reindex columns since preload functions generate new columns.
            self.index_columns()

    # Define class attributes after class declaration to avoid "name is not defined" exceptions.
    TaxBenefitSystem.Scenario = Scenario

    from .model import model  # noqa analysis:ignore

    return TaxBenefitSystem


def init_tax_benefit_system():
    """
    Helper function which suits most of the time.

    Use `init_country` if you need to get the `TaxBenefitSystem` class.
    """
    TaxBenefitSystem = init_country()
    tax_benefit_system = TaxBenefitSystem()
    return tax_benefit_system
