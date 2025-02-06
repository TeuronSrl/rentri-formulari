# DatiTrasportoTrasmissioneBaseModel1


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treno** | **str** |  | 
**tratta** | **str** |  | [optional] 
**rid** | **bool** |  | [optional] 
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi | 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** |  | [optional] 
**targa_rimorchio** | **str** |  | [optional] 
**percorso** | **str** |  | [optional] 
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_trasmissione_base_model1 import DatiTrasportoTrasmissioneBaseModel1

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoTrasmissioneBaseModel1 from a JSON string
dati_trasporto_trasmissione_base_model1_instance = DatiTrasportoTrasmissioneBaseModel1.from_json(json)
# print the JSON string representation of the object
print DatiTrasportoTrasmissioneBaseModel1.to_json()

# convert the object into a dict
dati_trasporto_trasmissione_base_model1_dict = dati_trasporto_trasmissione_base_model1_instance.to_dict()
# create an instance of DatiTrasportoTrasmissioneBaseModel1 from a dict
dati_trasporto_trasmissione_base_model1_from_dict = DatiTrasportoTrasmissioneBaseModel1.from_dict(dati_trasporto_trasmissione_base_model1_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


