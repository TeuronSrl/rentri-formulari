# EsitoFormularioModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoFormularioModelEsito**](EsitoFormularioModelEsito.md) |  | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_formulario_model import EsitoFormularioModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoFormularioModel from a JSON string
esito_formulario_model_instance = EsitoFormularioModel.from_json(json)
# print the JSON string representation of the object
print EsitoFormularioModel.to_json()

# convert the object into a dict
esito_formulario_model_dict = esito_formulario_model_instance.to_dict()
# create an instance of EsitoFormularioModel from a dict
esito_formulario_model_from_dict = EsitoFormularioModel.from_dict(esito_formulario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


