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

from rentri_formulari.models.normativa_adr_model import NormativaADRModel

class TestNormativaADRModel(unittest.TestCase):
    """NormativaADRModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NormativaADRModel:
        """Test NormativaADRModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NormativaADRModel`
        """
        model = NormativaADRModel()
        if include_optional:
            return NormativaADRModel(
                numero_onu = '',
                classe = '',
                note = ''
            )
        else:
            return NormativaADRModel(
        )
        """

    def testNormativaADRModel(self):
        """Test NormativaADRModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
