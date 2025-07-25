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

from rentri_formulari.models.dati_trasbordo_parziale_result_model import DatiTrasbordoParzialeResultModel

class TestDatiTrasbordoParzialeResultModel(unittest.TestCase):
    """DatiTrasbordoParzialeResultModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiTrasbordoParzialeResultModel:
        """Test DatiTrasbordoParzialeResultModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiTrasbordoParzialeResultModel`
        """
        model = DatiTrasbordoParzialeResultModel()
        if include_optional:
            return DatiTrasbordoParzialeResultModel(
                trasportatore = rentri_formulari.models.dati_trasportatore_model.DatiTrasportatoreModel(
                    denominazione = '0', 
                    codice_fiscale = '01234', 
                    nazione_id = '', 
                    numero_iscrizione_albo = 'AE/807288', ),
                data_ora_trasbordo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                trasportatore_id = 56,
                dati_firma = rentri_formulari.models.dati_firma_result.DatiFirmaResult(
                    denominazione_firmatario = '', 
                    identificativo_firmatario = '', 
                    data_firma = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identificativo_utente = '', 
                    credentials_id = '', ),
                numero_fir = '0',
                quantita_residua = rentri_formulari.models.quantita_model.QuantitaModel(
                    valore = 1.337, 
                    unita_misura = null, ),
                causale = '0'
            )
        else:
            return DatiTrasbordoParzialeResultModel(
                trasportatore = rentri_formulari.models.dati_trasportatore_model.DatiTrasportatoreModel(
                    denominazione = '0', 
                    codice_fiscale = '01234', 
                    nazione_id = '', 
                    numero_iscrizione_albo = 'AE/807288', ),
                numero_fir = '0',
                quantita_residua = rentri_formulari.models.quantita_model.QuantitaModel(
                    valore = 1.337, 
                    unita_misura = null, ),
                causale = '0',
        )
        """

    def testDatiTrasbordoParzialeResultModel(self):
        """Test DatiTrasbordoParzialeResultModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
