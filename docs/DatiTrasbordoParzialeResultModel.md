# DatiTrasbordoParzialeResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trasportatore** | [**DatiTrasportatoreModel**](DatiTrasportatoreModel.md) | Dati del trasportatore che prende parzialmente in carico il rifiuto | [optional] 
**trasportatore_id** | **int** | Riferimento al trasportatore che ha effettuato il trasbordo parziale nel contesto del FIR | [optional] 
**dati_firma** | [**DatiFirmaResult**](DatiFirmaResult.md) | Dati di firma del trasportatore che registra il trasbordo parziale | [optional] 
**numero_fir** | **str** | Numero FIR del formulario in cui viene trasbordato parzialmente il rifiuto | 
**quantita_residua** | [**QuantitaModel**](QuantitaModel.md) | Quantità residua del rifiuto nel formulario di origine | 
**causale** | **str** | Causale del trasbordo parziale | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_parziale_result_model import DatiTrasbordoParzialeResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoParzialeResultModel from a JSON string
dati_trasbordo_parziale_result_model_instance = DatiTrasbordoParzialeResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoParzialeResultModel.to_json())

# convert the object into a dict
dati_trasbordo_parziale_result_model_dict = dati_trasbordo_parziale_result_model_instance.to_dict()
# create an instance of DatiTrasbordoParzialeResultModel from a dict
dati_trasbordo_parziale_result_model_from_dict = DatiTrasbordoParzialeResultModel.from_dict(dati_trasbordo_parziale_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


