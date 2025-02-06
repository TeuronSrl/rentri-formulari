# EsitoGetHashPerFirmaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_algorithm** | **str** |  | [optional] 
**digest_to_sign** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_get_hash_per_firma_model import EsitoGetHashPerFirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoGetHashPerFirmaModel from a JSON string
esito_get_hash_per_firma_model_instance = EsitoGetHashPerFirmaModel.from_json(json)
# print the JSON string representation of the object
print EsitoGetHashPerFirmaModel.to_json()

# convert the object into a dict
esito_get_hash_per_firma_model_dict = esito_get_hash_per_firma_model_instance.to_dict()
# create an instance of EsitoGetHashPerFirmaModel from a dict
esito_get_hash_per_firma_model_from_dict = EsitoGetHashPerFirmaModel.from_dict(esito_get_hash_per_firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


