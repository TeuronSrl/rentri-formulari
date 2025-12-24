# IntermediarioItemResult

Dati anagrafici riassuntivi riferiti ad un intermediario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | [optional] 
**denominazione** | **str** |  | [optional] 
**codice_fiscale** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.intermediario_item_result import IntermediarioItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediarioItemResult from a JSON string
intermediario_item_result_instance = IntermediarioItemResult.from_json(json)
# print the JSON string representation of the object
print(IntermediarioItemResult.to_json())

# convert the object into a dict
intermediario_item_result_dict = intermediario_item_result_instance.to_dict()
# create an instance of IntermediarioItemResult from a dict
intermediario_item_result_from_dict = IntermediarioItemResult.from_dict(intermediario_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


