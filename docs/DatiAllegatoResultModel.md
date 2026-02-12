# DatiAllegatoResultModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allegato_id** | **int** | Identificatore dell&#39;allegato nel contesto del FIR | [optional] 
**content_type** | **str** | Tipo del documento Valori ammessi: “application/pdf” | 
**nome_file** | **str** | Nome del file | 
**identificativo_soggetto** | **str** | Codice fiscale del soggetto, tra quelli indicati nel formulario, a cui è da riferirsi l&#39;allegato | 
**descrizione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_allegato_result_model import DatiAllegatoResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAllegatoResultModel from a JSON string
dati_allegato_result_model_instance = DatiAllegatoResultModel.from_json(json)
# print the JSON string representation of the object
print DatiAllegatoResultModel.to_json()

# convert the object into a dict
dati_allegato_result_model_dict = dati_allegato_result_model_instance.to_dict()
# create an instance of DatiAllegatoResultModel from a dict
dati_allegato_result_model_from_dict = DatiAllegatoResultModel.from_dict(dati_allegato_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


