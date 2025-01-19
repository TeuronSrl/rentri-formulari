# DatiTrasbordoParzialeModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** |  | 
**trasportatore** | [**DatiTrasportatoreTrasbordoModel**](DatiTrasportatoreTrasbordoModel.md) | Dati trasportatore per il trasbordo parziale | 
**quantita_residua** | [**QuantitaModel**](QuantitaModel.md) |  | 
**causale** | **str** |  | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_parziale_model import DatiTrasbordoParzialeModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoParzialeModel from a JSON string
dati_trasbordo_parziale_model_instance = DatiTrasbordoParzialeModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoParzialeModel.to_json())

# convert the object into a dict
dati_trasbordo_parziale_model_dict = dati_trasbordo_parziale_model_instance.to_dict()
# create an instance of DatiTrasbordoParzialeModel from a dict
dati_trasbordo_parziale_model_from_dict = DatiTrasbordoParzialeModel.from_dict(dati_trasbordo_parziale_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


