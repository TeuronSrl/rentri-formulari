# DatiSostaTecnicaTrasmissioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi | 
**luogo_stazionamento** | **str** |  | 
**data_ora_sospensione** | **datetime** | Formato ISO 8601 UTC | 
**data_ora_ripresa** | **datetime** | Formato ISO 8601 UTC | 

## Example

```python
from rentri_formulari.models.dati_sosta_tecnica_trasmissione_model import DatiSostaTecnicaTrasmissioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiSostaTecnicaTrasmissioneModel from a JSON string
dati_sosta_tecnica_trasmissione_model_instance = DatiSostaTecnicaTrasmissioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiSostaTecnicaTrasmissioneModel.to_json())

# convert the object into a dict
dati_sosta_tecnica_trasmissione_model_dict = dati_sosta_tecnica_trasmissione_model_instance.to_dict()
# create an instance of DatiSostaTecnicaTrasmissioneModel from a dict
dati_sosta_tecnica_trasmissione_model_from_dict = DatiSostaTecnicaTrasmissioneModel.from_dict(dati_sosta_tecnica_trasmissione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


