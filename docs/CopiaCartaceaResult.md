# CopiaCartaceaResult

Dati della copia del FIR cartaceo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Identificativo univco della copia del FIR cartaceo caricata | [optional] 
**numero_fir** | **str** | Numero del FIR cartaceo | [optional] 
**data_emissione** | **datetime** | Data emissione del FIR cartaceo (formato ISO 8601 UTC) | [optional] 
**num_iscr_sito** | **str** | Numero iscrizione unità locale dell&#39;operatore che ha effettuato il caricamento | [optional] 
**produttore** | [**CopiaCartaceaRuoloResult**](CopiaCartaceaRuoloResult.md) | Dati del produttore a cui si rende disponibile la copia del FIR cartaceo | [optional] 
**trasportatori** | [**List[CopiaCartaceaRuoloResult]**](CopiaCartaceaRuoloResult.md) | Dati dei trasportatori ai quali si rende disponibile la copia del FIR cartaceo | [optional] 
**intermediari** | [**List[CopiaCartaceaRuoloResult]**](CopiaCartaceaRuoloResult.md) | Dati degli intermediari ai quali si rende disponibile la copia del FIR cartaceo | [optional] 
**note** | **str** | Eventuali note riguardanti la copia del FIR cartaceo | [optional] 
**data_caricamento** | **datetime** | Data di caricamento della copia del FIR cartaceo (formato ISO 8601 UTC) | [optional] 
**codice_fiscale_caricamento** | **str** | Codice fiscale del soggetto che ha effettuato il caricamento | [optional] 
**denominazione_caricamento** | **str** | Denominazione del soggetto che ha effettuato il caricamento | [optional] 
**emesso_da_identificativo** | **str** | Codice fiscale del soggetto intestatario del numero FIR | [optional] 
**emesso_da_denominazione** | **str** | Denominazione del soggetto intestatario del numero FIR | [optional] 

## Example

```python
from rentri_formulari.models.copia_cartacea_result import CopiaCartaceaResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaCartaceaResult from a JSON string
copia_cartacea_result_instance = CopiaCartaceaResult.from_json(json)
# print the JSON string representation of the object
print CopiaCartaceaResult.to_json()

# convert the object into a dict
copia_cartacea_result_dict = copia_cartacea_result_instance.to_dict()
# create an instance of CopiaCartaceaResult from a dict
copia_cartacea_result_from_dict = CopiaCartaceaResult.from_dict(copia_cartacea_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


