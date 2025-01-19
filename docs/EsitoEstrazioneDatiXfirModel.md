# EsitoEstrazioneDatiXfirModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoEstraiDatiXfirModel**](EsitoEstraiDatiXfirModel.md) | Esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] [readonly] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_estrazione_dati_xfir_model import EsitoEstrazioneDatiXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoEstrazioneDatiXfirModel from a JSON string
esito_estrazione_dati_xfir_model_instance = EsitoEstrazioneDatiXfirModel.from_json(json)
# print the JSON string representation of the object
print(EsitoEstrazioneDatiXfirModel.to_json())

# convert the object into a dict
esito_estrazione_dati_xfir_model_dict = esito_estrazione_dati_xfir_model_instance.to_dict()
# create an instance of EsitoEstrazioneDatiXfirModel from a dict
esito_estrazione_dati_xfir_model_from_dict = EsitoEstrazioneDatiXfirModel.from_dict(esito_estrazione_dati_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


