# coding: utf-8

"""
    formulari

    Servizio Formulari RENTRI

    The version of the OpenAPI document: 1.0.20250114-507
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from rentri_formulari.models.dati_trasportatore_formulario_result_model import DatiTrasportatoreFormularioResultModel

class TestDatiTrasportatoreFormularioResultModel(unittest.TestCase):
    """DatiTrasportatoreFormularioResultModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasportatoreFormularioResultModel:
        """Test DatiTrasportatoreFormularioResultModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasportatoreFormularioResultModel`
        """
        model = DatiTrasportatoreFormularioResultModel()
        if include_optional:
            return DatiTrasportatoreFormularioResultModel(
                trasportatore_id = 56,
                denominazione = '0',
                codice_fiscale = '01234',
                nazione_id = '',
                tipo_trasporto = 'Terrestre',
                numero_iscrizione_albo = 'AE/807288'
            )
        else:
            return DatiTrasportatoreFormularioResultModel(
                denominazione = '0',
                codice_fiscale = '01234',
                tipo_trasporto = 'Terrestre',
        )
        """

    def testDatiTrasportatoreFormularioResultModel(self):
        """Test DatiTrasportatoreFormularioResultModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
