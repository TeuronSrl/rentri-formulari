# CopiaDigitaleModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** |  | 
**note** | **str** |  | [optional] 
**xfir** | **bytearray** | Contenuto del file xFIR | 

## Example

```python
from rentri_formulari.models.copia_digitale_model import CopiaDigitaleModel

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleModel from a JSON string
copia_digitale_model_instance = CopiaDigitaleModel.from_json(json)
# print the JSON string representation of the object
print CopiaDigitaleModel.to_json()

# convert the object into a dict
copia_digitale_model_dict = copia_digitale_model_instance.to_dict()
# create an instance of CopiaDigitaleModel from a dict
copia_digitale_model_from_dict = CopiaDigitaleModel.from_dict(copia_digitale_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


