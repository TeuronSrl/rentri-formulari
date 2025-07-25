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

from rentri_formulari.models.dati_trasporto_terrestre_model import DatiTrasportoTerrestreModel

class TestDatiTrasportoTerrestreModel(unittest.TestCase):
    """DatiTrasportoTerrestreModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasportoTerrestreModel:
        """Test DatiTrasportoTerrestreModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasportoTerrestreModel`
        """
        model = DatiTrasportoTerrestreModel()
        if include_optional:
            return DatiTrasportoTerrestreModel(
                conducente = rentri_formulari.models.conducente_model.ConducenteModel(
                    nome = '0', 
                    cognome = '0', ),
                targa_automezzo = '',
                targa_rimorchio = '',
                percorso = '',
                data_ora_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                annotazioni = ''
            )
        else:
            return DatiTrasportoTerrestreModel(
                conducente = rentri_formulari.models.conducente_model.ConducenteModel(
                    nome = '0', 
                    cognome = '0', ),
                data_ora_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDatiTrasportoTerrestreModel(self):
        """Test DatiTrasportoTerrestreModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
