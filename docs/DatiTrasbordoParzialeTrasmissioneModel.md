# DatiTrasbordoParzialeTrasmissioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore_id** | **int** | Id del trasportatore definito all&#39;interno dei dati che vengono trasmessi | 
**trasportatore** | [**DatiTrasportatoreTrasbordoModel**](DatiTrasportatoreTrasbordoModel.md) | Dati trasportatore per il trasbordo parziale | 
**numero_fir** | **str** | Numero FIR del formulario in cui viene trasbordato parzialmente il rifiuto | 
**quantita_residua** | [**QuantitaModel**](QuantitaModel.md) | Quantità residua del rifiuto nel formulario di origine | 
**causale** | **str** | Causale del trasbordo parziale | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_parziale_trasmissione_model import DatiTrasbordoParzialeTrasmissioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoParzialeTrasmissioneModel from a JSON string
dati_trasbordo_parziale_trasmissione_model_instance = DatiTrasbordoParzialeTrasmissioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoParzialeTrasmissioneModel.to_json())

# convert the object into a dict
dati_trasbordo_parziale_trasmissione_model_dict = dati_trasbordo_parziale_trasmissione_model_instance.to_dict()
# create an instance of DatiTrasbordoParzialeTrasmissioneModel from a dict
dati_trasbordo_parziale_trasmissione_model_from_dict = DatiTrasbordoParzialeTrasmissioneModel.from_dict(dati_trasbordo_parziale_trasmissione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


