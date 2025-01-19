# DatiTrasportoTerrestreTrasmissioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** |  | [optional] 
**targa_rimorchio** | **str** |  | [optional] 
**percorso** | **str** |  | [optional] 
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi | 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_terrestre_trasmissione_model import DatiTrasportoTerrestreTrasmissioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoTerrestreTrasmissioneModel from a JSON string
dati_trasporto_terrestre_trasmissione_model_instance = DatiTrasportoTerrestreTrasmissioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoTerrestreTrasmissioneModel.to_json())

# convert the object into a dict
dati_trasporto_terrestre_trasmissione_model_dict = dati_trasporto_terrestre_trasmissione_model_instance.to_dict()
# create an instance of DatiTrasportoTerrestreTrasmissioneModel from a dict
dati_trasporto_terrestre_trasmissione_model_from_dict = DatiTrasportoTerrestreTrasmissioneModel.from_dict(dati_trasporto_terrestre_trasmissione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


