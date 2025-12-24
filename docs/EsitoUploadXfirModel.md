# EsitoUploadXfirModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ValidazioneXfirResult**](ValidazioneXfirResult.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_upload_xfir_model import EsitoUploadXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoUploadXfirModel from a JSON string
esito_upload_xfir_model_instance = EsitoUploadXfirModel.from_json(json)
# print the JSON string representation of the object
print(EsitoUploadXfirModel.to_json())

# convert the object into a dict
esito_upload_xfir_model_dict = esito_upload_xfir_model_instance.to_dict()
# create an instance of EsitoUploadXfirModel from a dict
esito_upload_xfir_model_from_dict = EsitoUploadXfirModel.from_dict(esito_upload_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


