# EsitoCreaFormularioModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoNuovoFormularioModel**](EsitoNuovoFormularioModel.md) | Esito | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_crea_formulario_model import EsitoCreaFormularioModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoCreaFormularioModel from a JSON string
esito_crea_formulario_model_instance = EsitoCreaFormularioModel.from_json(json)
# print the JSON string representation of the object
print EsitoCreaFormularioModel.to_json()

# convert the object into a dict
esito_crea_formulario_model_dict = esito_crea_formulario_model_instance.to_dict()
# create an instance of EsitoCreaFormularioModel from a dict
esito_crea_formulario_model_from_dict = EsitoCreaFormularioModel.from_dict(esito_crea_formulario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


