# TrasportatoreItemResult

Dati anagrafici riassuntivi riferiti ad un trasportatore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | [optional] 
**is_trasbordo_totale** | **bool** |  | [optional] 
**denominazione** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.trasportatore_item_result import TrasportatoreItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasportatoreItemResult from a JSON string
trasportatore_item_result_instance = TrasportatoreItemResult.from_json(json)
# print the JSON string representation of the object
print(TrasportatoreItemResult.to_json())

# convert the object into a dict
trasportatore_item_result_dict = trasportatore_item_result_instance.to_dict()
# create an instance of TrasportatoreItemResult from a dict
trasportatore_item_result_from_dict = TrasportatoreItemResult.from_dict(trasportatore_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


