# DatiTrasportoTrasmissioneBaseModel2


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
**presa_in_carico_rimorchio_precedente** | **bool** | Significativo solo per i trasporti successivi al primo | [optional] 
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_trasmissione_base_model2 import DatiTrasportoTrasmissioneBaseModel2

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoTrasmissioneBaseModel2 from a JSON string
dati_trasporto_trasmissione_base_model2_instance = DatiTrasportoTrasmissioneBaseModel2.from_json(json)
# print the JSON string representation of the object
print DatiTrasportoTrasmissioneBaseModel2.to_json()

# convert the object into a dict
dati_trasporto_trasmissione_base_model2_dict = dati_trasporto_trasmissione_base_model2_instance.to_dict()
# create an instance of DatiTrasportoTrasmissioneBaseModel2 from a dict
dati_trasporto_trasmissione_base_model2_from_dict = DatiTrasportoTrasmissioneBaseModel2.from_dict(dati_trasporto_trasmissione_base_model2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


