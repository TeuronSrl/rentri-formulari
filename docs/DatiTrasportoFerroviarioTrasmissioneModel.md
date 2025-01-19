# DatiTrasportoFerroviarioTrasmissioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treno** | **str** |  | 
**tratta** | **str** |  | [optional] 
**rid** | **bool** |  | [optional] 
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi | 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_ferroviario_trasmissione_model import DatiTrasportoFerroviarioTrasmissioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoFerroviarioTrasmissioneModel from a JSON string
dati_trasporto_ferroviario_trasmissione_model_instance = DatiTrasportoFerroviarioTrasmissioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoFerroviarioTrasmissioneModel.to_json())

# convert the object into a dict
dati_trasporto_ferroviario_trasmissione_model_dict = dati_trasporto_ferroviario_trasmissione_model_instance.to_dict()
# create an instance of DatiTrasportoFerroviarioTrasmissioneModel from a dict
dati_trasporto_ferroviario_trasmissione_model_from_dict = DatiTrasportoFerroviarioTrasmissioneModel.from_dict(dati_trasporto_ferroviario_trasmissione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


