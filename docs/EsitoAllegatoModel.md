# EsitoAllegatoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoAddAllegatoModel**](EsitoAddAllegatoModel.md) | Esito | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_allegato_model import EsitoAllegatoModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoAllegatoModel from a JSON string
esito_allegato_model_instance = EsitoAllegatoModel.from_json(json)
# print the JSON string representation of the object
print(EsitoAllegatoModel.to_json())

# convert the object into a dict
esito_allegato_model_dict = esito_allegato_model_instance.to_dict()
# create an instance of EsitoAllegatoModel from a dict
esito_allegato_model_from_dict = EsitoAllegatoModel.from_dict(esito_allegato_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


