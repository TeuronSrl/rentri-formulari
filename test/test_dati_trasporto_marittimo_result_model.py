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

from rentri_formulari.models.dati_trasporto_marittimo_result_model import DatiTrasportoMarittimoResultModel

class TestDatiTrasportoMarittimoResultModel(unittest.TestCase):
    """DatiTrasportoMarittimoResultModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasportoMarittimoResultModel:
        """Test DatiTrasportoMarittimoResultModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasportoMarittimoResultModel`
        """
        model = DatiTrasportoMarittimoResultModel()
        if include_optional:
            return DatiTrasportoMarittimoResultModel(
                tipo_trasporto = 'Terrestre',
                dati_firma_trasportatore = rentri_formulari.models.dati_firma_result.DatiFirmaResult(
                    denominazione_firmatario = '', 
                    identificativo_firmatario = '', 
                    data_firma = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identificativo_utente = '', 
                    credentials_id = '', ),
                trasportatore_id = 56,
                nave = '0',
                imdg = True,
                data_ora_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                annotazioni = ''
            )
        else:
            return DatiTrasportoMarittimoResultModel(
                nave = '0',
                data_ora_inizio_trasporto = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDatiTrasportoMarittimoResultModel(self):
        """Test DatiTrasportoMarittimoResultModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
