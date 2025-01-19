# DatiTrasbordoTotaleModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore** | [**DatiPartenzaModelTrasportatoriInner**](DatiPartenzaModelTrasportatoriInner.md) |  | 
**presa_in_carico** | [**DatiTrasportoTerrestreModel1**](DatiTrasportoTerrestreModel1.md) |  | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_totale_model import DatiTrasbordoTotaleModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoTotaleModel from a JSON string
dati_trasbordo_totale_model_instance = DatiTrasbordoTotaleModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoTotaleModel.to_json())

# convert the object into a dict
dati_trasbordo_totale_model_dict = dati_trasbordo_totale_model_instance.to_dict()
# create an instance of DatiTrasbordoTotaleModel from a dict
dati_trasbordo_totale_model_from_dict = DatiTrasbordoTotaleModel.from_dict(dati_trasbordo_totale_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


