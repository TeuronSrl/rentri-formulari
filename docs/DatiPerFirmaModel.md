# DatiPerFirmaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificato** | **str** | Certificato in base64 | 

## Example

```python
from rentri_formulari.models.dati_per_firma_model import DatiPerFirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPerFirmaModel from a JSON string
dati_per_firma_model_instance = DatiPerFirmaModel.from_json(json)
# print the JSON string representation of the object
print(DatiPerFirmaModel.to_json())

# convert the object into a dict
dati_per_firma_model_dict = dati_per_firma_model_instance.to_dict()
# create an instance of DatiPerFirmaModel from a dict
dati_per_firma_model_from_dict = DatiPerFirmaModel.from_dict(dati_per_firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


