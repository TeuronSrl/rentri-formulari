# AzioniResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**versione** | **int** |  | [optional] 
**stato** | [**StatoFormulario**](StatoFormulario.md) | Stati del FIR digitale&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantita&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantitaTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto e dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttoreTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del produttore e del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttore&lt;/i&gt; - Il formulario necessita della firma del produttore&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoSuccessivo&lt;/i&gt; - Il formulario è in carico ad un traportatore e necessita dell&#39;inserimento dei dati del trasporto successivo;             il trasportatore che ha in carico il rifiuto può inserire informazioni aggiuntive (annotazioni, trasbordo parziale, sosta tecnica, trasbordo totale, allegati)             che dovranno essere successivamente firmate&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreSuccessivo&lt;/i&gt; - Il formulario necessita della firma del trasportatore successivo al primo che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnotazione&lt;/i&gt; - Il formulario necessita della firma dell&#39;annotazione da parte del soggetto che l&#39;ha inserita&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoParziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che effettua il trasbordo parziale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoTotale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che prende in carico il rifiuto con l&#39;operazione di trasbordo totale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaSostaTecnica&lt;/i&gt; - Il formulario necessita della firma del trasportatore che ha in carico il rifiuto e ha inserito i dati della sosta tecnica&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAllegato&lt;/i&gt; - Il formulario necessita della firma del soggetto che ha aggiunto i dati relativi all&#39;allegato al formulario digitale&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoAccettazione&lt;/i&gt; - Il formulario è in carico all&#39;ultimo trasportatore ed è in attesa dell&#39;inserimento dei dati di accettazione da parte del destinatario verso cui è destinato il rifiuto             (a meno di ulteriori informazioni aggiuntive che l&#39;ultimo trasportatore può inserire prima della consegna al destinatario)&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazione&lt;/i&gt; - Il formulario necessita della firma del destinatario indicato nei dati di partenza&lt;/li&gt;&lt;li&gt;&lt;i&gt;Accettato&lt;/i&gt; - Il formulario è stato accettato dal destinatario ed ha concluso il suo ciclo di vita&lt;/li&gt;&lt;li&gt;&lt;i&gt;RespintoParzialmenteRespinto&lt;/i&gt; - Il formulario è stato respinto o parzialmente respinto, il trasportatore che ha in carico il rifiuto può inserire (in accordo con il produttore) i dati              di un nuovo destinatario&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaDestinatarioSuccessivo&lt;/i&gt; - Il formulario è in attesa della firma dei dati del nuovo destinatario inseriti da parte del trasportatore che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazioneSuccessiva&lt;/i&gt; - Il formulario necessita della firma del destinatario successivo a quello indicato nei dati di partenza che ha rifiutato totalmente o parzialmente il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnullamento&lt;/i&gt; - Il formulario necessita della firma dei dati di annullamento inseriti dal soggetto titolare della vidimazione del numero FIR&lt;/li&gt;&lt;li&gt;&lt;i&gt;Annullato&lt;/i&gt; - Il formulario risulta essere stato annullato&lt;/li&gt;&lt;li&gt;&lt;i&gt;Indeterminato&lt;/i&gt; - Il formulario è in uno stato non determinato per incoerenza dei dati contenuti&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**azioni** | [**List[Operazione]**](Operazione.md) | Elenco delle operazioni e specifici soggetti abilitati ad eseguirle effettuabili sul formulario in funzione dello stato in cui si trova | [optional] 

## Example

```python
from rentri_formulari.models.azioni_result import AzioniResult

# TODO update the JSON string below
json = "{}"
# create an instance of AzioniResult from a JSON string
azioni_result_instance = AzioniResult.from_json(json)
# print the JSON string representation of the object
print(AzioniResult.to_json())

# convert the object into a dict
azioni_result_dict = azioni_result_instance.to_dict()
# create an instance of AzioniResult from a dict
azioni_result_from_dict = AzioniResult.from_dict(azioni_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


