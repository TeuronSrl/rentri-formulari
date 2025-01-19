# EstraiDatiXfirModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**xfir** | **bytearray** | Contenuto del file xFIR | 

## Example

```python
from rentri_formulari.models.estrai_dati_xfir_model import EstraiDatiXfirModel

# TODO update the JSON string below
json = "{}"
# create an instance of EstraiDatiXfirModel from a JSON string
estrai_dati_xfir_model_instance = EstraiDatiXfirModel.from_json(json)
# print the JSON string representation of the object
print(EstraiDatiXfirModel.to_json())

# convert the object into a dict
estrai_dati_xfir_model_dict = estrai_dati_xfir_model_instance.to_dict()
# create an instance of EstraiDatiXfirModel from a dict
estrai_dati_xfir_model_from_dict = EstraiDatiXfirModel.from_dict(estrai_dati_xfir_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


