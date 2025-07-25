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

from rentri_formulari.models.trasbordo_parziale_origine_result import TrasbordoParzialeOrigineResult

class TestTrasbordoParzialeOrigineResult(unittest.TestCase):
    """TrasbordoParzialeOrigineResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TrasbordoParzialeOrigineResult:
        """Test TrasbordoParzialeOrigineResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TrasbordoParzialeOrigineResult`
        """
        model = TrasbordoParzialeOrigineResult()
        if include_optional:
            return TrasbordoParzialeOrigineResult(
                numero_fir_origine = '',
                produttore_origine = rentri_formulari.models.soggetto_item_result.SoggettoItemResult(
                    denominazione = '', 
                    codice_fiscale = '', )
            )
        else:
            return TrasbordoParzialeOrigineResult(
        )
        """

    def testTrasbordoParzialeOrigineResult(self):
        """Test TrasbordoParzialeOrigineResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
