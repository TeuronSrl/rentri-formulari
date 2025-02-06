# EsitoCopiaCartaceaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoCaricaCopiaCartaceaModel**](EsitoCaricaCopiaCartaceaModel.md) | Esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] [readonly] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_copia_cartacea_model import EsitoCopiaCartaceaModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoCopiaCartaceaModel from a JSON string
esito_copia_cartacea_model_instance = EsitoCopiaCartaceaModel.from_json(json)
# print the JSON string representation of the object
print EsitoCopiaCartaceaModel.to_json()

# convert the object into a dict
esito_copia_cartacea_model_dict = esito_copia_cartacea_model_instance.to_dict()
# create an instance of EsitoCopiaCartaceaModel from a dict
esito_copia_cartacea_model_from_dict = EsitoCopiaCartaceaModel.from_dict(esito_copia_cartacea_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


