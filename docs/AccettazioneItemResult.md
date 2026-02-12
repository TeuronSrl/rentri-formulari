# AccettazioneItemResult

Dati di accettazione del rifiuto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_accettazione** | [**TipiAccettazione**](TipiAccettazione.md) | Tipo accettazione&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;A&lt;/i&gt; - Accettato per intero&lt;/li&gt;&lt;li&gt;&lt;i&gt;P&lt;/i&gt; - Accettato parzialmente&lt;/li&gt;&lt;li&gt;&lt;i&gt;R&lt;/i&gt; - Respinto&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**quantita_accettata** | **float** | Quantità accettata in kg | [optional] 
**data_ora_arrivo** | **datetime** | Data ora arrivo (formato ISO 8601 UTC) | [optional] 

## Example

```python
from rentri_formulari.models.accettazione_item_result import AccettazioneItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of AccettazioneItemResult from a JSON string
accettazione_item_result_instance = AccettazioneItemResult.from_json(json)
# print the JSON string representation of the object
print AccettazioneItemResult.to_json()

# convert the object into a dict
accettazione_item_result_dict = accettazione_item_result_instance.to_dict()
# create an instance of AccettazioneItemResult from a dict
accettazione_item_result_from_dict = AccettazioneItemResult.from_dict(accettazione_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


