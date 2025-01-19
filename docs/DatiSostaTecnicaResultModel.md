# DatiSostaTecnicaResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ora_trasbordo** | **datetime** | Formato ISO 8601 UTC | [optional] 
**trasportatore_id** | **int** |  | [optional] 
**dati_firma** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**luogo_stazionamento** | **str** |  | 
**data_ora_sospensione** | **datetime** | Formato ISO 8601 UTC | 
**data_ora_ripresa** | **datetime** | Formato ISO 8601 UTC | 

## Example

```python
from rentri_formulari.models.dati_sosta_tecnica_result_model import DatiSostaTecnicaResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiSostaTecnicaResultModel from a JSON string
dati_sosta_tecnica_result_model_instance = DatiSostaTecnicaResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiSostaTecnicaResultModel.to_json())

# convert the object into a dict
dati_sosta_tecnica_result_model_dict = dati_sosta_tecnica_result_model_instance.to_dict()
# create an instance of DatiSostaTecnicaResultModel from a dict
dati_sosta_tecnica_result_model_from_dict = DatiSostaTecnicaResultModel.from_dict(dati_sosta_tecnica_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


