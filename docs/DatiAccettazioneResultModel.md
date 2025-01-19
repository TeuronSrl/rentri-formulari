# DatiAccettazioneResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_firma** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**tipo_accettazione** | [**TipiAccettazione**](TipiAccettazione.md) | Tipo accettazione&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;A&lt;/i&gt; - Accettato per intero&lt;/li&gt;&lt;li&gt;&lt;i&gt;P&lt;/i&gt; - Accettato parzialmente&lt;/li&gt;&lt;li&gt;&lt;i&gt;R&lt;/i&gt; - Respinto&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
**quantita_accettata** | [**QuantitaKgModel**](QuantitaKgModel.md) | Quantita accettata | [optional] 
**causale_respingimento** | [**CausaliRespingimento**](CausaliRespingimento.md) | Causale di respingimento&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;NC&lt;/i&gt; - Non Conformità, a titolo esemplificativo e non esaustivo, si riporta: rifiuti diverso da quello descritto dal formulario o da quanto dichiarato ai fini della pratica di conferimento all&#39;impianto, rifiuto confezionato in modo non conforme da quanto previsto per la specifica destinazione o dalle norme applicabili, di stato fisico diverso da quello previsto)&lt;/li&gt;&lt;li&gt;&lt;i&gt;IR&lt;/i&gt; - Irricevibile, (a titolo esemplificativo e non esaustivo, si riporta: rifiuto non previsto dall&#39;autorizzazione / iscrizione dell&#39;impianto di destino, mancanza dei requisiti per l&#39;ammissibilità all&#39;impianto quali caratterizzazione di base, analisi di classificazione o di ammissibilità…)&lt;/li&gt;&lt;li&gt;&lt;i&gt;A&lt;/i&gt; - Indicare motivazione. A titolo esemplificativo e non esaustivo, si riporta: esaurimento volumetria disponibile per conferimento rifiuto, chiusura impianto per manutenzione straordinaria, ecc.&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**motivo_respingimento** | **str** | Motivo di respingimento per causale A | [optional] 
**data_ora_arrivo** | **datetime** | Data ora arrivo (formato ISO 8601 UTC) | 
**attesa_verifica_analitica** | **bool** | Da valorizzare a true se il destinatario sottopone il rifiuto ad analisi | [optional] 

## Example

```python
from rentri_formulari.models.dati_accettazione_result_model import DatiAccettazioneResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAccettazioneResultModel from a JSON string
dati_accettazione_result_model_instance = DatiAccettazioneResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiAccettazioneResultModel.to_json())

# convert the object into a dict
dati_accettazione_result_model_dict = dati_accettazione_result_model_instance.to_dict()
# create an instance of DatiAccettazioneResultModel from a dict
dati_accettazione_result_model_from_dict = DatiAccettazioneResultModel.from_dict(dati_accettazione_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


