# EsitoUploadXfirResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**esito** | [**EsitoUploadXfirModel**](EsitoUploadXfirModel.md) | Esito | [optional] 
**tipo** | **str** | Tipo di esito | [optional] 
**transazione_id** | **str** | Identificativo della transazione asincrona | [optional] 
**validazione** | [**List[EsitoMessaggioModel]**](EsitoMessaggioModel.md) | Messaggi di validazione | [optional] 
**errore** | **bool** |  | [optional] 
**tempo_elaborazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_upload_xfir_result_model import EsitoUploadXfirResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoUploadXfirResultModel from a JSON string
esito_upload_xfir_result_model_instance = EsitoUploadXfirResultModel.from_json(json)
# print the JSON string representation of the object
print(EsitoUploadXfirResultModel.to_json())

# convert the object into a dict
esito_upload_xfir_result_model_dict = esito_upload_xfir_result_model_instance.to_dict()
# create an instance of EsitoUploadXfirResultModel from a dict
esito_upload_xfir_result_model_from_dict = EsitoUploadXfirResultModel.from_dict(esito_upload_xfir_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


