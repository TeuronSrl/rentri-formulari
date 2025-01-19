# UnitaLocaleItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | [optional] 
**denominazione** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 
**indirizzo** | **str** |  | [optional] 
**civico** | **str** |  | [optional] 
**comune_id** | **str** |  | [optional] 
**nazione_id** | **str** |  | [optional] 
**citta_estera** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.unita_locale_item_result import UnitaLocaleItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of UnitaLocaleItemResult from a JSON string
unita_locale_item_result_instance = UnitaLocaleItemResult.from_json(json)
# print the JSON string representation of the object
print(UnitaLocaleItemResult.to_json())

# convert the object into a dict
unita_locale_item_result_dict = unita_locale_item_result_instance.to_dict()
# create an instance of UnitaLocaleItemResult from a dict
unita_locale_item_result_from_dict = UnitaLocaleItemResult.from_dict(unita_locale_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


