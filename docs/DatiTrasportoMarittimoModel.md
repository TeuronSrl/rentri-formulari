# DatiTrasportoMarittimoModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_marittimo_model import DatiTrasportoMarittimoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoMarittimoModel from a JSON string
dati_trasporto_marittimo_model_instance = DatiTrasportoMarittimoModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoMarittimoModel.to_json())

# convert the object into a dict
dati_trasporto_marittimo_model_dict = dati_trasporto_marittimo_model_instance.to_dict()
# create an instance of DatiTrasportoMarittimoModel from a dict
dati_trasporto_marittimo_model_from_dict = DatiTrasportoMarittimoModel.from_dict(dati_trasporto_marittimo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


