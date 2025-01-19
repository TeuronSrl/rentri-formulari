# DatiTrasportoFerroviarioResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_trasporto** | [**TipoTrasporto**](TipoTrasporto.md) |  | [optional] 
**dati_firma_trasportatore** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**trasportatore_id** | **int** |  | [optional] 
**treno** | **str** |  | 
**rid** | **bool** |  | [optional] 
**tratta** | **str** |  | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_ferroviario_result_model import DatiTrasportoFerroviarioResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoFerroviarioResultModel from a JSON string
dati_trasporto_ferroviario_result_model_instance = DatiTrasportoFerroviarioResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoFerroviarioResultModel.to_json())

# convert the object into a dict
dati_trasporto_ferroviario_result_model_dict = dati_trasporto_ferroviario_result_model_instance.to_dict()
# create an instance of DatiTrasportoFerroviarioResultModel from a dict
dati_trasporto_ferroviario_result_model_from_dict = DatiTrasportoFerroviarioResultModel.from_dict(dati_trasporto_ferroviario_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


