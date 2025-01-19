# DatiTrasportoTerrestreResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_trasporto** | [**TipoTrasporto**](TipoTrasporto.md) |  | [optional] 
**dati_firma_trasportatore** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**trasportatore_id** | **int** |  | [optional] 
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** | TargaAutomezzo | [optional] 
**targa_rimorchio** | **str** | TargaRimorchio | [optional] 
**percorso** | **str** | Percorso (se diverso dal più breve) | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_terrestre_result_model import DatiTrasportoTerrestreResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoTerrestreResultModel from a JSON string
dati_trasporto_terrestre_result_model_instance = DatiTrasportoTerrestreResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoTerrestreResultModel.to_json())

# convert the object into a dict
dati_trasporto_terrestre_result_model_dict = dati_trasporto_terrestre_result_model_instance.to_dict()
# create an instance of DatiTrasportoTerrestreResultModel from a dict
dati_trasporto_terrestre_result_model_from_dict = DatiTrasportoTerrestreResultModel.from_dict(dati_trasporto_terrestre_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


