# UploadXfirModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero iscrizione dell&#39;unità locale | 
**xfir** | **bytearray** | Contenuto del file xFIR | 

## Example

```python
from rentri_formulari.models.upload_xfir_model import UploadXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of UploadXfirModel from a JSON string
upload_xfir_model_instance = UploadXfirModel.from_json(json)
# print the JSON string representation of the object
print UploadXfirModel.to_json()

# convert the object into a dict
upload_xfir_model_dict = upload_xfir_model_instance.to_dict()
# create an instance of UploadXfirModel from a dict
upload_xfir_model_from_dict = UploadXfirModel.from_dict(upload_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


