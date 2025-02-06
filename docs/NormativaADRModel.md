# NormativaADRModel

Normativa ADR

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_onu** | **str** | Numero ONU | [optional] 
**classe** | **str** |  | [optional] 
**note** | **str** | Note ADR | [optional] 

## Example

```python
from rentri_formulari.models.normativa_adr_model import NormativaADRModel

# TODO update the JSON string below
json = "{}"
# create an instance of NormativaADRModel from a JSON string
normativa_adr_model_instance = NormativaADRModel.from_json(json)
# print the JSON string representation of the object
print NormativaADRModel.to_json()

# convert the object into a dict
normativa_adr_model_dict = normativa_adr_model_instance.to_dict()
# create an instance of NormativaADRModel from a dict
normativa_adr_model_from_dict = NormativaADRModel.from_dict(normativa_adr_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


