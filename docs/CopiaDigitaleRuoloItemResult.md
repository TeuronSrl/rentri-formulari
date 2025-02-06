# CopiaDigitaleRuoloItemResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**denominazione** | **str** |  | [optional] 
**num_iscr_sito** | **str** |  | [optional] 
**nome_sito** | **str** |  | [optional] 
**data_conferma** | **datetime** |  | [optional] 

## Example

```python
from rentri_formulari.models.copia_digitale_ruolo_item_result import CopiaDigitaleRuoloItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleRuoloItemResult from a JSON string
copia_digitale_ruolo_item_result_instance = CopiaDigitaleRuoloItemResult.from_json(json)
# print the JSON string representation of the object
print CopiaDigitaleRuoloItemResult.to_json()

# convert the object into a dict
copia_digitale_ruolo_item_result_dict = copia_digitale_ruolo_item_result_instance.to_dict()
# create an instance of CopiaDigitaleRuoloItemResult from a dict
copia_digitale_ruolo_item_result_from_dict = CopiaDigitaleRuoloItemResult.from_dict(copia_digitale_ruolo_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


