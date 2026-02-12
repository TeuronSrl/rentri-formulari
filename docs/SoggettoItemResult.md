# SoggettoItemResult

Dati anagrafici riassuntivi riferiti ad un soggetto

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.soggetto_item_result import SoggettoItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of SoggettoItemResult from a JSON string
soggetto_item_result_instance = SoggettoItemResult.from_json(json)
# print the JSON string representation of the object
print SoggettoItemResult.to_json()

# convert the object into a dict
soggetto_item_result_dict = soggetto_item_result_instance.to_dict()
# create an instance of SoggettoItemResult from a dict
soggetto_item_result_from_dict = SoggettoItemResult.from_dict(soggetto_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


