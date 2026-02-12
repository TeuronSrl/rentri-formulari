# IAnagrafica


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** | Denominazione del soggetto | [optional] 
**codice_fiscale** | **str** | Codice fiscale del soggetto | [optional] 

## Example

```python
from rentri_formulari.models.i_anagrafica import IAnagrafica

# TODO update the JSON string below
json = "{}"
# create an instance of IAnagrafica from a JSON string
i_anagrafica_instance = IAnagrafica.from_json(json)
# print the JSON string representation of the object
print IAnagrafica.to_json()

# convert the object into a dict
i_anagrafica_dict = i_anagrafica_instance.to_dict()
# create an instance of IAnagrafica from a dict
i_anagrafica_from_dict = IAnagrafica.from_dict(i_anagrafica_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


