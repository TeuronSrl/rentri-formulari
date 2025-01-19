# ValidaXfirModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xfir** | **bytearray** | Contenuto del file xFIR | 

## Example

```python
from rentri_formulari.models.valida_xfir_model import ValidaXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of ValidaXfirModel from a JSON string
valida_xfir_model_instance = ValidaXfirModel.from_json(json)
# print the JSON string representation of the object
print(ValidaXfirModel.to_json())

# convert the object into a dict
valida_xfir_model_dict = valida_xfir_model_instance.to_dict()
# create an instance of ValidaXfirModel from a dict
valida_xfir_model_from_dict = ValidaXfirModel.from_dict(valida_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


