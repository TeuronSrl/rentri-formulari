# DatiTrasportoFerroviarioModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**treno** | **str** |  | 
**rid** | **bool** |  | [optional] 
**tratta** | **str** |  | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_ferroviario_model import DatiTrasportoFerroviarioModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoFerroviarioModel from a JSON string
dati_trasporto_ferroviario_model_instance = DatiTrasportoFerroviarioModel.from_json(json)
# print the JSON string representation of the object
print DatiTrasportoFerroviarioModel.to_json()

# convert the object into a dict
dati_trasporto_ferroviario_model_dict = dati_trasporto_ferroviario_model_instance.to_dict()
# create an instance of DatiTrasportoFerroviarioModel from a dict
dati_trasporto_ferroviario_model_from_dict = DatiTrasportoFerroviarioModel.from_dict(dati_trasporto_ferroviario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


