# DatiTrasbordoParzialeOrigineModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir_origine** | **str** | Numero FIR del formulario che ha subito il trasbordo parziale da cui prende origine il nuovo formulario | 
**produttore_originario** | [**DatiProduttoreOriginarioModel**](DatiProduttoreOriginarioModel.md) | Dati del produttore del rifiuto originario come compariva nel formulario di origine | 
**causale** | **str** | Causale del trasbordo parziale | 

## Example

```python
from rentri_formulari.models.dati_trasbordo_parziale_origine_model import DatiTrasbordoParzialeOrigineModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoParzialeOrigineModel from a JSON string
dati_trasbordo_parziale_origine_model_instance = DatiTrasbordoParzialeOrigineModel.from_json(json)
# print the JSON string representation of the object
print DatiTrasbordoParzialeOrigineModel.to_json()

# convert the object into a dict
dati_trasbordo_parziale_origine_model_dict = dati_trasbordo_parziale_origine_model_instance.to_dict()
# create an instance of DatiTrasbordoParzialeOrigineModel from a dict
dati_trasbordo_parziale_origine_model_from_dict = DatiTrasbordoParzialeOrigineModel.from_dict(dati_trasbordo_parziale_origine_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


