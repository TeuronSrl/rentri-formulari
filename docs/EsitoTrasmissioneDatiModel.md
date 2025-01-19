# EsitoTrasmissioneDatiModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoFormularioModelEsito**](EsitoFormularioModelEsito.md) |  | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] [readonly] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_trasmissione_dati_model import EsitoTrasmissioneDatiModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoTrasmissioneDatiModel from a JSON string
esito_trasmissione_dati_model_instance = EsitoTrasmissioneDatiModel.from_json(json)
# print the JSON string representation of the object
print(EsitoTrasmissioneDatiModel.to_json())

# convert the object into a dict
esito_trasmissione_dati_model_dict = esito_trasmissione_dati_model_instance.to_dict()
# create an instance of EsitoTrasmissioneDatiModel from a dict
esito_trasmissione_dati_model_from_dict = EsitoTrasmissioneDatiModel.from_dict(esito_trasmissione_dati_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


