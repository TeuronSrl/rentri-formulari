# EsitoDatiPerFirmaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoGetHashPerFirmaModel**](EsitoGetHashPerFirmaModel.md) | Esito | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_dati_per_firma_model import EsitoDatiPerFirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoDatiPerFirmaModel from a JSON string
esito_dati_per_firma_model_instance = EsitoDatiPerFirmaModel.from_json(json)
# print the JSON string representation of the object
print(EsitoDatiPerFirmaModel.to_json())

# convert the object into a dict
esito_dati_per_firma_model_dict = esito_dati_per_firma_model_instance.to_dict()
# create an instance of EsitoDatiPerFirmaModel from a dict
esito_dati_per_firma_model_from_dict = EsitoDatiPerFirmaModel.from_dict(esito_dati_per_firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


