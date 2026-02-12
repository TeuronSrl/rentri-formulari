# ControlloFirmeResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_firma** | **datetime** | Data dichiarata nella firma digitale | [optional] 
**riferimenti** | **List[str]** | Riferimenti ai file coperti dalla firma | [optional] 
**codice** | **str** | Codice identificativo del controllo | [optional] 
**esito** | [**EsitoValidazione**](EsitoValidazione.md) | Esito del controllo | [optional] 
**dettaglio** | **str** | Eventuali dati di dettaglio considerati nel controllo | [optional] 
**nome_file** | **str** | Nome del file oggetto del controllo | [optional] 

## Example

```python
from rentri_formulari.models.controllo_firme_result import ControlloFirmeResult

# TODO update the JSON string below
json = "{}"
# create an instance of ControlloFirmeResult from a JSON string
controllo_firme_result_instance = ControlloFirmeResult.from_json(json)
# print the JSON string representation of the object
print ControlloFirmeResult.to_json()

# convert the object into a dict
controllo_firme_result_dict = controllo_firme_result_instance.to_dict()
# create an instance of ControlloFirmeResult from a dict
controllo_firme_result_from_dict = ControlloFirmeResult.from_dict(controllo_firme_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


