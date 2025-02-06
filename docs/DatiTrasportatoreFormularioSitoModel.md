# DatiTrasportatoreFormularioSitoModel

Dati trasportatore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero di iscrizione al RENTRI | 
**tipo_trasporto** | [**TipoTrasporto**](TipoTrasporto.md) |  | 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasportatore_formulario_sito_model import DatiTrasportatoreFormularioSitoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportatoreFormularioSitoModel from a JSON string
dati_trasportatore_formulario_sito_model_instance = DatiTrasportatoreFormularioSitoModel.from_json(json)
# print the JSON string representation of the object
print DatiTrasportatoreFormularioSitoModel.to_json()

# convert the object into a dict
dati_trasportatore_formulario_sito_model_dict = dati_trasportatore_formulario_sito_model_instance.to_dict()
# create an instance of DatiTrasportatoreFormularioSitoModel from a dict
dati_trasportatore_formulario_sito_model_from_dict = DatiTrasportatoreFormularioSitoModel.from_dict(dati_trasportatore_formulario_sito_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


