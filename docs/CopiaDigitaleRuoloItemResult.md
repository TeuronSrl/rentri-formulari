# CopiaDigitaleRuoloItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Identificativo del soggetto | [optional] 
**denominazione** | **str** | Denominazione del soggetto | [optional] 
**num_iscr_sito** | **str** | Eventuale numero di iscrizione dell&#39;unità locale indicata per il soggetto | [optional] 
**nome_sito** | **str** | Eventuale nome del comune dell&#39;unità locale indicata per il soggetto | [optional] 
**data_conferma** | **datetime** | Data dell&#39;avvenuta presa visione da parte del soggetto | [optional] 

## Example

```python
from rentri_formulari.models.copia_digitale_ruolo_item_result import CopiaDigitaleRuoloItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleRuoloItemResult from a JSON string
copia_digitale_ruolo_item_result_instance = CopiaDigitaleRuoloItemResult.from_json(json)
# print the JSON string representation of the object
print(CopiaDigitaleRuoloItemResult.to_json())

# convert the object into a dict
copia_digitale_ruolo_item_result_dict = copia_digitale_ruolo_item_result_instance.to_dict()
# create an instance of CopiaDigitaleRuoloItemResult from a dict
copia_digitale_ruolo_item_result_from_dict = CopiaDigitaleRuoloItemResult.from_dict(copia_digitale_ruolo_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


