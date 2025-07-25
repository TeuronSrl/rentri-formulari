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

from rentri_formulari.models.dati_accettazione_model import DatiAccettazioneModel

class TestDatiAccettazioneModel(unittest.TestCase):
    """DatiAccettazioneModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiAccettazioneModel:
        """Test DatiAccettazioneModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiAccettazioneModel`
        """
        model = DatiAccettazioneModel()
        if include_optional:
            return DatiAccettazioneModel(
                tipo_accettazione = 'A',
                quantita_accettata = rentri_formulari.models.quantita_kg_model.QuantitaKgModel(
                    valore = 1.337, ),
                causale_respingimento = 'NC',
                motivo_respingimento = '',
                data_ora_arrivo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                attesa_verifica_analitica = True
            )
        else:
            return DatiAccettazioneModel(
                tipo_accettazione = 'A',
                data_ora_arrivo = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
        )
        """

    def testDatiAccettazioneModel(self):
        """Test DatiAccettazioneModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
