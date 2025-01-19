# TrasmissioneDatiItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**numero_fir** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**data_trasmissione** | **datetime** | Formato ISO 8601 UTC | [optional] 
**data_emissione** | **datetime** | Formato ISO 8601 UTC | [optional] 
**codice_eer** | **str** |  | [optional] 
**rifiuto_quantita** | **float** |  | [optional] 
**rifiuto_unita_misura** | [**UnitaMisura**](UnitaMisura.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;kg&lt;/i&gt; - Chilogrammi&lt;/li&gt;&lt;li&gt;&lt;i&gt;l&lt;/i&gt; - Litri&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**tipo** | [**TipoTrasmissione**](TipoTrasmissione.md) |  | [optional] 
**stato** | [**StatiTrasmissioneDati**](StatiTrasmissioneDati.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.trasmissione_dati_item_result import TrasmissioneDatiItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasmissioneDatiItemResult from a JSON string
trasmissione_dati_item_result_instance = TrasmissioneDatiItemResult.from_json(json)
# print the JSON string representation of the object
print(TrasmissioneDatiItemResult.to_json())

# convert the object into a dict
trasmissione_dati_item_result_dict = trasmissione_dati_item_result_instance.to_dict()
# create an instance of TrasmissioneDatiItemResult from a dict
trasmissione_dati_item_result_from_dict = TrasmissioneDatiItemResult.from_dict(trasmissione_dati_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


