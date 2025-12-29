# DatiTrasportoTerrestreModel

Dati del trasporto terrestre

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** | Targa automezzo.  Il dato è necessario se non si indica una targa per il rimorchio | [optional] 
**targa_rimorchio** | **str** | Targa rimorchio | [optional] 
**percorso** | **str** | Percorso (se diverso dal più breve) | [optional] 
**presa_in_carico_rimorchio_precedente** | **bool** | Significativo solo per i trasporti successivi al primo | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasporto_terrestre_model import DatiTrasportoTerrestreModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportoTerrestreModel from a JSON string
dati_trasporto_terrestre_model_instance = DatiTrasportoTerrestreModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportoTerrestreModel.to_json())

# convert the object into a dict
dati_trasporto_terrestre_model_dict = dati_trasporto_terrestre_model_instance.to_dict()
# create an instance of DatiTrasportoTerrestreModel from a dict
dati_trasporto_terrestre_model_from_dict = DatiTrasportoTerrestreModel.from_dict(dati_trasporto_terrestre_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


