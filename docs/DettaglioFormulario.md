# DettaglioFormulario


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stato_formulario** | [**StatoFormulario**](StatoFormulario.md) | Stato del formulario&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantita&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantitaTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto e dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttoreTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del produttore e del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttore&lt;/i&gt; - Il formulario necessita della firma del produttore&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoSuccessivo&lt;/i&gt; - Il formulario è in carico ad un traportatore e necessita dell&#39;inserimento dei dati del trasporto successivo;             il trasportatore che ha in carico il rifiuto può inserire informazioni aggiuntive (annotazioni, trasbordo parziale, sosta tecnica, trasbordo totale, allegati)             che dovranno essere successivamente firmate&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreSuccessivo&lt;/i&gt; - Il formulario necessita della firma del trasportatore successivo al primo che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnotazione&lt;/i&gt; - Il formulario necessita della firma dell&#39;annotazione da parte del soggetto che l&#39;ha inserita&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoParziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che effettua il trasbordo parziale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoTotale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che prende in carico il rifiuto con l&#39;operazione di trasbordo totale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaSostaTecnica&lt;/i&gt; - Il formulario necessita della firma del trasportatore che ha in carico il rifiuto e ha inserito i dati della sosta tecnica&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAllegato&lt;/i&gt; - Il formulario necessita della firma del soggetto che ha aggiunto i dati relativi all&#39;allegato al formulario digitale. ATTENZIONE!: questo valore è DEPRECATO: lo stato non è più utilizzato, per gli allegati aggiunti via API non è più prevista la firma&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoAccettazione&lt;/i&gt; - Il formulario è in carico all&#39;ultimo trasportatore ed è in attesa dell&#39;inserimento dei dati di accettazione da parte del destinatario verso cui è destinato il rifiuto             (a meno di ulteriori informazioni aggiuntive che l&#39;ultimo trasportatore può inserire prima della consegna al destinatario)&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazione&lt;/i&gt; - Il formulario necessita della firma del destinatario indicato nei dati di partenza&lt;/li&gt;&lt;li&gt;&lt;i&gt;Accettato&lt;/i&gt; - Il formulario è stato accettato dal destinatario ed ha concluso il suo ciclo di vita&lt;/li&gt;&lt;li&gt;&lt;i&gt;RespintoAccettatoParzialmente&lt;/i&gt; - Il formulario è stato respinto o accettato parzialmente, il trasportatore che ha in carico il rifiuto può inserire (in accordo con il produttore) i dati             di un nuovo destinatario&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaDestinatarioSuccessivo&lt;/i&gt; - Il formulario è in attesa della firma dei dati del nuovo destinatario inseriti da parte del trasportatore che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazioneSuccessiva&lt;/i&gt; - Il formulario necessita della firma del destinatario successivo a quello indicato nei dati di partenza che ha rifiutato totalmente o parzialmente il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnullamento&lt;/i&gt; - Il formulario necessita della firma dei dati di annullamento inseriti dal soggetto titolare della vidimazione del numero FIR&lt;/li&gt;&lt;li&gt;&lt;i&gt;Annullato&lt;/i&gt; - Il formulario risulta essere stato annullato&lt;/li&gt;&lt;li&gt;&lt;i&gt;Indeterminato&lt;/i&gt; - Il formulario è in uno stato non determinato per incoerenza dei dati contenuti&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**versione** | **int** | Numero incrementale della versione del formulario presente in Area virtuale di interscambio. Ad ogni modifica dei dati del formulario che avviene attraverso le API di compilazione il numero di versione viene incrementato di una unità | [optional] 
**dati_vidimazione** | [**VidimazioneResult**](VidimazioneResult.md) | Soggetto che ha provveduto alla vidimazione del numero FIR | [optional] 
**data_creazione** | **datetime** | Timestamp di creazione del FIR | [optional] 
**provenienza_upload** | **bool** | Quando le informazioni di dettaglio si riferiscono ad un FIR presente nell&#39;area virtuale di interscambio, indica se il formulario è stato prodotto e/o modificato al di fuori delle API di compilazione | [optional] 
**num_iscr_sito** | **str** | Numero iscrizione dell&#39;unità locale nel contesto della quale è stato creato il FIR | [optional] 
**dati_partenza** | [**DatiPartenzaResultModel**](DatiPartenzaResultModel.md) | Dati di partenza del formulario | [optional] 
**dati_trasporto** | [**List[DettaglioFormularioDatiTrasportoInner]**](DettaglioFormularioDatiTrasportoInner.md) | Dati di trasporto per ciascun trasportatore indicato nei dati di partenza | [optional] 
**dati_accettazione** | [**DatiAccettazioneResultModel**](DatiAccettazioneResultModel.md) | Dati di accettazione inseriti dal destinatario indicato nei dati di partenza | [optional] 
**dati_annotazioni** | [**List[DatiAnnotazioneResultModel]**](DatiAnnotazioneResultModel.md) | Dati relativi alle annotazioni aggiuntive | [optional] 
**dati_allegati** | [**List[DatiAllegatoResultModel]**](DatiAllegatoResultModel.md) | Dati relativi agli allegati inseriti via API | [optional] 
**dati_annullamento** | [**DatiAnnullamentoResultModel**](DatiAnnullamentoResultModel.md) | Dati relativi all&#39;eventuale annullamento | [optional] 
**dati_trasbordo_totale** | [**DatiTrasbordoTotaleResultModel**](DatiTrasbordoTotaleResultModel.md) | Dati relativa all&#39;eventuale trasbordo totale del rifiuto | [optional] 
**dati_trasbordi_parziali** | [**List[DatiTrasbordoParzialeResultModel]**](DatiTrasbordoParzialeResultModel.md) | Dati relativi agli eventuali trasbordi parziali del rifiuto | [optional] 
**dati_soste_tecniche** | [**List[DatiSostaTecnicaResultModel]**](DatiSostaTecnicaResultModel.md) | Dati relativi alle eventuali soste tecniche effettuate nel trasporto | [optional] 
**dati_destinazioni_successive** | [**List[DatiDestinazioniSuccessiveResultModel]**](DatiDestinazioniSuccessiveResultModel.md) | Dati relativi alle eventuali destinazioni successive inserite per il rifiuto a seguito di respingimenti | [optional] 

## Example

```python
from rentri_formulari.models.dettaglio_formulario import DettaglioFormulario

# TODO update the JSON string below
json = "{}"
# create an instance of DettaglioFormulario from a JSON string
dettaglio_formulario_instance = DettaglioFormulario.from_json(json)
# print the JSON string representation of the object
print DettaglioFormulario.to_json()

# convert the object into a dict
dettaglio_formulario_dict = dettaglio_formulario_instance.to_dict()
# create an instance of DettaglioFormulario from a dict
dettaglio_formulario_from_dict = DettaglioFormulario.from_dict(dettaglio_formulario_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


