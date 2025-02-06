# CopiaDigitaleItemResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** |  | [optional] 
**numero_fir** | **str** |  | [optional] 
**data_emissione** | **datetime** |  | [optional] 
**data_caricamento** | **datetime** |  | [optional] 
**is_confermata** | **bool** |  | [optional] 
**note** | **str** |  | [optional] 
**produttore** | [**CopiaDigitaleRuoloItemResult**](CopiaDigitaleRuoloItemResult.md) |  | [optional] 
**trasportatori** | [**List[CopiaDigitaleRuoloItemResult]**](CopiaDigitaleRuoloItemResult.md) |  | [optional] 
**intermediari** | [**List[CopiaDigitaleRuoloItemResult]**](CopiaDigitaleRuoloItemResult.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.copia_digitale_item_result import CopiaDigitaleItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleItemResult from a JSON string
copia_digitale_item_result_instance = CopiaDigitaleItemResult.from_json(json)
# print the JSON string representation of the object
print CopiaDigitaleItemResult.to_json()

# convert the object into a dict
copia_digitale_item_result_dict = copia_digitale_item_result_instance.to_dict()
# create an instance of CopiaDigitaleItemResult from a dict
copia_digitale_item_result_from_dict = CopiaDigitaleItemResult.from_dict(copia_digitale_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


