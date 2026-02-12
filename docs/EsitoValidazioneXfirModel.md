# EsitoValidazioneXfirModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoValidaXfirModel**](EsitoValidaXfirModel.md) | Esito | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_validazione_xfir_model import EsitoValidazioneXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoValidazioneXfirModel from a JSON string
esito_validazione_xfir_model_instance = EsitoValidazioneXfirModel.from_json(json)
# print the JSON string representation of the object
print EsitoValidazioneXfirModel.to_json()

# convert the object into a dict
esito_validazione_xfir_model_dict = esito_validazione_xfir_model_instance.to_dict()
# create an instance of EsitoValidazioneXfirModel from a dict
esito_validazione_xfir_model_from_dict = EsitoValidazioneXfirModel.from_dict(esito_validazione_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


