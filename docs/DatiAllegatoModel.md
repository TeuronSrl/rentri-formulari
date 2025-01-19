# DatiAllegatoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** |  | 
**nome_file** | **str** |  | 
**contenuto** | **bytearray** |  | 
**identificativo_soggetto** | **str** |  | 
**descrizione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_allegato_model import DatiAllegatoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAllegatoModel from a JSON string
dati_allegato_model_instance = DatiAllegatoModel.from_json(json)
# print the JSON string representation of the object
print(DatiAllegatoModel.to_json())

# convert the object into a dict
dati_allegato_model_dict = dati_allegato_model_instance.to_dict()
# create an instance of DatiAllegatoModel from a dict
dati_allegato_model_from_dict = DatiAllegatoModel.from_dict(dati_allegato_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


