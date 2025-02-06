# ControlloFirmeResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_firma** | **datetime** |  | [optional] 
**riferimenti** | **List[str]** |  | [optional] 
**codice** | **str** |  | [optional] 
**esito** | [**EsitoValidazione**](EsitoValidazione.md) |  | [optional] 
**controllo** | **str** |  | [optional] 
**dettaglio** | **str** |  | [optional] 
**nome_file** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.controllo_firme_result import ControlloFirmeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ControlloFirmeResult from a JSON string
controllo_firme_result_instance = ControlloFirmeResult.from_json(json)
# print the JSON string representation of the object
print ControlloFirmeResult.to_json()

# convert the object into a dict
controllo_firme_result_dict = controllo_firme_result_instance.to_dict()
# create an instance of ControlloFirmeResult from a dict
controllo_firme_result_from_dict = ControlloFirmeResult.from_dict(controllo_firme_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


