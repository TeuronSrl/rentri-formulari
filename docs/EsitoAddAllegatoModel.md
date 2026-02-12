# EsitoAddAllegatoModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allegato_id** | **int** | Identificativo interno al FIR digitale associato all&#39;allegato | [optional] 

## Example

```python
from rentri_formulari.models.esito_add_allegato_model import EsitoAddAllegatoModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoAddAllegatoModel from a JSON string
esito_add_allegato_model_instance = EsitoAddAllegatoModel.from_json(json)
# print the JSON string representation of the object
print EsitoAddAllegatoModel.to_json()

# convert the object into a dict
esito_add_allegato_model_dict = esito_add_allegato_model_instance.to_dict()
# create an instance of EsitoAddAllegatoModel from a dict
esito_add_allegato_model_from_dict = EsitoAddAllegatoModel.from_dict(esito_add_allegato_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


