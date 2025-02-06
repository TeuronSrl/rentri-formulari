# ConducenteModel

Conducente

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nome** | **str** | Nome | 
**cognome** | **str** | Cognome | 

## Example

```python
from rentri_formulari.models.conducente_model import ConducenteModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConducenteModel from a JSON string
conducente_model_instance = ConducenteModel.from_json(json)
# print the JSON string representation of the object
print ConducenteModel.to_json()

# convert the object into a dict
conducente_model_dict = conducente_model_instance.to_dict()
# create an instance of ConducenteModel from a dict
conducente_model_from_dict = ConducenteModel.from_dict(conducente_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


