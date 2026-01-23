# DatiTrasbordoTotaleResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore** | [**DatiTrasportatoreFormularioResultModel**](DatiTrasportatoreFormularioResultModel.md) | Dati del nuovo trasportatore | [optional] 
**presa_in_carico** | [**DatiTrasportoTerrestreResultModel**](DatiTrasportoTerrestreResultModel.md) | Dati relativi alla firma sui dati di trasporto | [optional] 
**trasportatore_id** | **int** | Riferimento al trasportatore che ha effettuato il trasbordo totale nel contesto del FIR | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasbordo_totale_result_model import DatiTrasbordoTotaleResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoTotaleResultModel from a JSON string
dati_trasbordo_totale_result_model_instance = DatiTrasbordoTotaleResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoTotaleResultModel.to_json())

# convert the object into a dict
dati_trasbordo_totale_result_model_dict = dati_trasbordo_totale_result_model_instance.to_dict()
# create an instance of DatiTrasbordoTotaleResultModel from a dict
dati_trasbordo_totale_result_model_from_dict = DatiTrasbordoTotaleResultModel.from_dict(dati_trasbordo_totale_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


