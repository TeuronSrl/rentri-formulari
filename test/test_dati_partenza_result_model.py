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

from rentri_formulari.models.dati_partenza_result_model import DatiPartenzaResultModel

class TestDatiPartenzaResultModel(unittest.TestCase):
    """DatiPartenzaResultModel unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DatiPartenzaResultModel:
        """Test DatiPartenzaResultModel
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DatiPartenzaResultModel`
        """
        model = DatiPartenzaResultModel()
        if include_optional:
            return DatiPartenzaResultModel(
                produttore = rentri_formulari.models.dati_produttore_formulario_model.DatiProduttoreFormularioModel(
                    denominazione = '0', 
                    codice_fiscale = '01234', 
                    nazione_id = '', 
                    indirizzo = null, ),
                destinatario = None,
                trasportatori = [
                    rentri_formulari.models.dati_trasportatore_formulario_result_model.DatiTrasportatoreFormularioResultModel(
                        trasportatore_id = 56, )
                    ],
                intermediari = [
                    rentri_formulari.models.dati_intermediari_formulario_model.DatiIntermediariFormularioModel(
                        denominazione = '0', 
                        codice_fiscale = '01234', 
                        nazione_id = '', 
                        numero_iscrizione_albo = 'AE/807288', )
                    ],
                rifiuto = rentri_formulari.models.dati_rifiuto_model.DatiRifiutoModel(
                    codice_eer = '0', 
                    descrizione = '', 
                    provenienza = null, 
                    caratteristiche_chimico_fisiche = '', 
                    caratteristiche_pericolo = [
                        'HP01'
                        ], 
                    stato_fisico = null, 
                    quantita = null, 
                    verificato_in_partenza = True, 
                    trasporto_adr = True, 
                    dati_adr = null, 
                    analisi_classificazione = null, 
                    numero_colli = '', 
                    rinfusa = True, ),
                trasbordo_parziale_origine = rentri_formulari.models.dati_trasbordo_parziale_origine_result_model.DatiTrasbordoParzialeOrigineResultModel(
                    numero_fir_origine = '', 
                    produttore_originario = null, 
                    causale = '', ),
                dati_firma_produttore = rentri_formulari.models.dati_firma_result.DatiFirmaResult(
                    denominazione_firmatario = '', 
                    identificativo_firmatario = '', 
                    data_firma = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    identificativo_utente = '', 
                    credentials_id = '', ),
                numero_fir = 'WPQZYQ ) ._),,#_**&,\"%\"* - *- !\'# 1757701929816286488291663/.$\'\"&(_#+% #\"&%-/*- )!./ !),+#/)B',
                annotazioni = ''
            )
        else:
            return DatiPartenzaResultModel(
        )
        """

    def testDatiPartenzaResultModel(self):
        """Test DatiPartenzaResultModel"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
