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

from rentri_formulari.models.citta_estera_model import CittaEsteraModel

class TestCittaEsteraModel(unittest.TestCase):
    """CittaEsteraModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CittaEsteraModel:
        """Test CittaEsteraModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CittaEsteraModel`
        """
        model = CittaEsteraModel()
        if include_optional:
            return CittaEsteraModel(
                nazione_id = ERROR_TO_EXAMPLE_VALUE,
                nome_citta = '0'
            )
        else:
            return CittaEsteraModel(
                nazione_id = ERROR_TO_EXAMPLE_VALUE,
                nome_citta = '0',
        )
        """

    def testCittaEsteraModel(self):
        """Test CittaEsteraModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
