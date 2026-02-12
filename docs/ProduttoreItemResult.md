# ProduttoreItemResult

Dati anagrafici riassuntivi riferiti ad un produttore

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
from rentri_formulari.models.produttore_item_result import ProduttoreItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of ProduttoreItemResult from a JSON string
produttore_item_result_instance = ProduttoreItemResult.from_json(json)
# print the JSON string representation of the object
print ProduttoreItemResult.to_json()

# convert the object into a dict
produttore_item_result_dict = produttore_item_result_instance.to_dict()
# create an instance of ProduttoreItemResult from a dict
produttore_item_result_from_dict = ProduttoreItemResult.from_dict(produttore_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


