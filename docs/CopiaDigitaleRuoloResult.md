# CopiaDigitaleRuoloResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** | Codice fiscale del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 
**denominazione** | **str** | Denominazione del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 
**num_iscr_sito** | **str** | Numero iscrizione unità locale del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 
**num_iscr_sito_conferma** | **str** | Numero iscrizione unità locale del soggetto che ha confermato la presa visione della copia del FIR digitale | [optional] 
**data_conferma** | **datetime** | Data dell&#39;eventuale avvenuta conferma di presa visione da parte del soggetto (formato ISO 8601 UTC) | [optional] 
**via** | **str** | Via del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 
**civico** | **str** | Civico del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 
**comune_id** | **str** | Codice ISTAT del comune del soggetto a cui viene resa disponibile la copia del FIR digitale | [optional] 

## Example

```python
from rentri_formulari.models.copia_digitale_ruolo_result import CopiaDigitaleRuoloResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleRuoloResult from a JSON string
copia_digitale_ruolo_result_instance = CopiaDigitaleRuoloResult.from_json(json)
# print the JSON string representation of the object
print(CopiaDigitaleRuoloResult.to_json())

# convert the object into a dict
copia_digitale_ruolo_result_dict = copia_digitale_ruolo_result_instance.to_dict()
# create an instance of CopiaDigitaleRuoloResult from a dict
copia_digitale_ruolo_result_from_dict = CopiaDigitaleRuoloResult.from_dict(copia_digitale_ruolo_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


