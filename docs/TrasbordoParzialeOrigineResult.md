# TrasbordoParzialeOrigineResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir_origine** | **str** |  | [optional] 
**produttore_origine** | [**SoggettoItemResult**](SoggettoItemResult.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.trasbordo_parziale_origine_result import TrasbordoParzialeOrigineResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasbordoParzialeOrigineResult from a JSON string
trasbordo_parziale_origine_result_instance = TrasbordoParzialeOrigineResult.from_json(json)
# print the JSON string representation of the object
print(TrasbordoParzialeOrigineResult.to_json())

# convert the object into a dict
trasbordo_parziale_origine_result_dict = trasbordo_parziale_origine_result_instance.to_dict()
# create an instance of TrasbordoParzialeOrigineResult from a dict
trasbordo_parziale_origine_result_from_dict = TrasbordoParzialeOrigineResult.from_dict(trasbordo_parziale_origine_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


