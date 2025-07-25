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

from rentri_formulari.models.esito_estrazione_dati_xfir_model import EsitoEstrazioneDatiXfirModel

class TestEsitoEstrazioneDatiXfirModel(unittest.TestCase):
    """EsitoEstrazioneDatiXfirModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EsitoEstrazioneDatiXfirModel:
        """Test EsitoEstrazioneDatiXfirModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EsitoEstrazioneDatiXfirModel`
        """
        model = EsitoEstrazioneDatiXfirModel()
        if include_optional:
            return EsitoEstrazioneDatiXfirModel(
                esito = rentri_formulari.models.esito_estrai_dati_xfir_model.EsitoEstraiDatiXfirModel(
                    formulario = null, ),
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
            return EsitoEstrazioneDatiXfirModel(
        )
        """

    def testEsitoEstrazioneDatiXfirModel(self):
        """Test EsitoEstrazioneDatiXfirModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
