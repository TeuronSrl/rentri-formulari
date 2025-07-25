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

from rentri_formulari.models.dati_trasportatore_formulario_model import DatiTrasportatoreFormularioModel

class TestDatiTrasportatoreFormularioModel(unittest.TestCase):
    """DatiTrasportatoreFormularioModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasportatoreFormularioModel:
        """Test DatiTrasportatoreFormularioModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasportatoreFormularioModel`
        """
        model = DatiTrasportatoreFormularioModel()
        if include_optional:
            return DatiTrasportatoreFormularioModel(
                denominazione = '0',
                codice_fiscale = '01234',
                nazione_id = '',
                tipo_trasporto = 'Terrestre',
                numero_iscrizione_albo = 'AE/807288'
            )
        else:
            return DatiTrasportatoreFormularioModel(
                denominazione = '0',
                codice_fiscale = '01234',
                tipo_trasporto = 'Terrestre',
        )
        """

    def testDatiTrasportatoreFormularioModel(self):
        """Test DatiTrasportatoreFormularioModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
