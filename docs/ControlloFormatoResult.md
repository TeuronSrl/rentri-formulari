# ControlloFormatoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice** | **str** |  | [optional] 
**esito** | [**EsitoValidazione**](EsitoValidazione.md) |  | [optional] 
**controllo** | **str** |  | [optional] 
**dettaglio** | **str** |  | [optional] 
**nome_file** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.controllo_formato_result import ControlloFormatoResult

# TODO update the JSON string below
json = "{}"
# create an instance of ControlloFormatoResult from a JSON string
controllo_formato_result_instance = ControlloFormatoResult.from_json(json)
# print the JSON string representation of the object
print(ControlloFormatoResult.to_json())

# convert the object into a dict
controllo_formato_result_dict = controllo_formato_result_instance.to_dict()
# create an instance of ControlloFormatoResult from a dict
controllo_formato_result_from_dict = ControlloFormatoResult.from_dict(controllo_formato_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


