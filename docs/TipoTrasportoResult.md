# TipoTrasportoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_trasporto** | [**TipoTrasporto**](TipoTrasporto.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.tipo_trasporto_result import TipoTrasportoResult

# TODO update the JSON string below
json = "{}"
# create an instance of TipoTrasportoResult from a JSON string
tipo_trasporto_result_instance = TipoTrasportoResult.from_json(json)
# print the JSON string representation of the object
print(TipoTrasportoResult.to_json())

# convert the object into a dict
tipo_trasporto_result_dict = tipo_trasporto_result_instance.to_dict()
# create an instance of TipoTrasportoResult from a dict
tipo_trasporto_result_from_dict = TipoTrasportoResult.from_dict(tipo_trasporto_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


