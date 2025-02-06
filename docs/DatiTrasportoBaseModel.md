# DatiTrasportoBaseModel

Dati del trasporto base

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_base_model import DatiTrasportoBaseModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoBaseModel from a JSON string
dati_trasporto_base_model_instance = DatiTrasportoBaseModel.from_json(json)
# print the JSON string representation of the object
print DatiTrasportoBaseModel.to_json()

# convert the object into a dict
dati_trasporto_base_model_dict = dati_trasporto_base_model_instance.to_dict()
# create an instance of DatiTrasportoBaseModel from a dict
dati_trasporto_base_model_from_dict = DatiTrasportoBaseModel.from_dict(dati_trasporto_base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


