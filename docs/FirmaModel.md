# FirmaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificato** | **str** | Certificato in base64 | 
**token** | **str** | Stringa in base64 contenente il token restituito dalla chiamata con cui si è ottenuto l&#39;hash che si è firmato. Deve essere restituita assieme alla firma nella procedura di acquisizione | 
**firma** | **bytearray** | Stringa in base64 contenente l&#39;array di byte che costituisce la firma dell&#39;hash | 
**identificativo_utente** | **str** | Identificativo dell&#39;utente, contestuale all&#39;ambiente di utilizzo del chiamante, al quale far risalire l&#39;operazione di firma | [optional] 

## Example

```python
from rentri_formulari.models.firma_model import FirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of FirmaModel from a JSON string
firma_model_instance = FirmaModel.from_json(json)
# print the JSON string representation of the object
print(FirmaModel.to_json())

# convert the object into a dict
firma_model_dict = firma_model_instance.to_dict()
# create an instance of FirmaModel from a dict
firma_model_from_dict = FirmaModel.from_dict(firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


