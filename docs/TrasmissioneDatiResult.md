# TrasmissioneDatiResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**numero_fir** | **str** |  | [optional] 
**user_name** | **str** |  | [optional] 
**data_trasmissione** | **datetime** | Formato ISO 8601 UTC | [optional] 
**data_emissione** | **datetime** | Formato ISO 8601 UTC | [optional] 
**tipo** | [**TipoTrasmissione**](TipoTrasmissione.md) |  | [optional] 
**stato** | [**StatiTrasmissioneDati**](StatiTrasmissioneDati.md) |  | [optional] 
**formulario** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.trasmissione_dati_result import TrasmissioneDatiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasmissioneDatiResult from a JSON string
trasmissione_dati_result_instance = TrasmissioneDatiResult.from_json(json)
# print the JSON string representation of the object
print TrasmissioneDatiResult.to_json()

# convert the object into a dict
trasmissione_dati_result_dict = trasmissione_dati_result_instance.to_dict()
# create an instance of TrasmissioneDatiResult from a dict
trasmissione_dati_result_from_dict = TrasmissioneDatiResult.from_dict(trasmissione_dati_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


