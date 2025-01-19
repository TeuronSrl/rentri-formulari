# CopiaCartaceaRuoloResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** | Codice fiscale del soggetto a cui viene resa disponibile la copia del FIR cartaceo | [optional] 
**denominazione** | **str** | Denominazione del soggetto a cui viene resa disponibile la copia del FIR cartaceo | [optional] 
**num_iscr_sito** | **str** | Numero iscrizione unità locale del soggetto a cui viene resa disponibile la copia del FIR cartaceo | [optional] 
**data_conferma** | **datetime** | Data dell&#39;eventuale avvenuta conferma da parte del soggetto (formato ISO 8601 UTC) | [optional] 

## Example

```python
from rentri_formulari.models.copia_cartacea_ruolo_result import CopiaCartaceaRuoloResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaCartaceaRuoloResult from a JSON string
copia_cartacea_ruolo_result_instance = CopiaCartaceaRuoloResult.from_json(json)
# print the JSON string representation of the object
print(CopiaCartaceaRuoloResult.to_json())

# convert the object into a dict
copia_cartacea_ruolo_result_dict = copia_cartacea_ruolo_result_instance.to_dict()
# create an instance of CopiaCartaceaRuoloResult from a dict
copia_cartacea_ruolo_result_from_dict = CopiaCartaceaRuoloResult.from_dict(copia_cartacea_ruolo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


