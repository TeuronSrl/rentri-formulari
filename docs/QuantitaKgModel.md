# QuantitaKgModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valore** | **float** | Quantità (parte intera: 10, parte decimale: 4) compresa tra 0.0000 e 9999999999.9999. | 

## Example

```python
from rentri_formulari.models.quantita_kg_model import QuantitaKgModel

# TODO update the JSON string below
json = "{}"
# create an instance of QuantitaKgModel from a JSON string
quantita_kg_model_instance = QuantitaKgModel.from_json(json)
# print the JSON string representation of the object
print(QuantitaKgModel.to_json())

# convert the object into a dict
quantita_kg_model_dict = quantita_kg_model_instance.to_dict()
# create an instance of QuantitaKgModel from a dict
quantita_kg_model_from_dict = QuantitaKgModel.from_dict(quantita_kg_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


