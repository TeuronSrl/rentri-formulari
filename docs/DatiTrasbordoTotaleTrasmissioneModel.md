# DatiTrasbordoTotaleTrasmissioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi a cui è riferito il trasbordo | 
**id_trasportatore_trasbordo** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi a cui è riferito il trasbordo       ⚠️ Deprecato: utilizzare \&quot;trasportatore_id\&quot; | [optional] 
**trasportatore** | [**DatiTrasportatoreTrasmissioneModel**](DatiTrasportatoreTrasmissioneModel.md) |  | 
**presa_in_carico** | [**DatiTrasportoTrasmissioneBaseModel1**](DatiTrasportoTrasmissioneBaseModel1.md) |  | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_totale_trasmissione_model import DatiTrasbordoTotaleTrasmissioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoTotaleTrasmissioneModel from a JSON string
dati_trasbordo_totale_trasmissione_model_instance = DatiTrasbordoTotaleTrasmissioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoTotaleTrasmissioneModel.to_json())

# convert the object into a dict
dati_trasbordo_totale_trasmissione_model_dict = dati_trasbordo_totale_trasmissione_model_instance.to_dict()
# create an instance of DatiTrasbordoTotaleTrasmissioneModel from a dict
dati_trasbordo_totale_trasmissione_model_from_dict = DatiTrasbordoTotaleTrasmissioneModel.from_dict(dati_trasbordo_totale_trasmissione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


