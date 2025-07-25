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

from rentri_formulari.models.esito_copia_digitale_model import EsitoCopiaDigitaleModel

class TestEsitoCopiaDigitaleModel(unittest.TestCase):
    """EsitoCopiaDigitaleModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EsitoCopiaDigitaleModel:
        """Test EsitoCopiaDigitaleModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EsitoCopiaDigitaleModel`
        """
        model = EsitoCopiaDigitaleModel()
        if include_optional:
            return EsitoCopiaDigitaleModel(
                esito = rentri_formulari.models.esito_carica_copia_digitale_model.EsitoCaricaCopiaDigitaleModel(
                    identificativo = '', ),
                transazione_id = '',
                validazione = [
                    rentri_formulari.models.esito_messaggio_model.EsitoMessaggioModel(
                        indice = 56, 
                        campo = '', 
                        tipo = null, 
                        codice_messaggio = '', 
                        parametri = [
                            null
                            ], )
                    ],
                errore = True,
                tempo_elaborazione = ''
            )
        else:
            return EsitoCopiaDigitaleModel(
        )
        """

    def testEsitoCopiaDigitaleModel(self):
        """Test EsitoCopiaDigitaleModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
