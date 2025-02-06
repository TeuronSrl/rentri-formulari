# DatiFirmaResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione_firmatario** | **str** |  | [optional] 
**identificativo_firmatario** | **str** |  | [optional] 
**data_firma** | **datetime** |  | [optional] 
**identificativo_utente** | **str** |  | [optional] 
**credentials_id** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_firma_result import DatiFirmaResult

# TODO update the JSON string below
json = "{}"
# create an instance of DatiFirmaResult from a JSON string
dati_firma_result_instance = DatiFirmaResult.from_json(json)
# print the JSON string representation of the object
print DatiFirmaResult.to_json()

# convert the object into a dict
dati_firma_result_dict = dati_firma_result_instance.to_dict()
# create an instance of DatiFirmaResult from a dict
dati_firma_result_from_dict = DatiFirmaResult.from_dict(dati_firma_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


