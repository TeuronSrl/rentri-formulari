# NuovoFormularioModelDatiTrasportoPartenza

Dati del trasporto iniziale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** | TargaAutomezzo | [optional] 
**targa_rimorchio** | **str** | TargaRimorchio | [optional] 
**percorso** | **str** | Percorso (se diverso dal più breve) | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 
**treno** | **str** |  | 
**rid** | **bool** |  | [optional] 
**tratta** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.nuovo_formulario_model_dati_trasporto_partenza import NuovoFormularioModelDatiTrasportoPartenza

# TODO update the JSON string below
json = "{}"
# create an instance of NuovoFormularioModelDatiTrasportoPartenza from a JSON string
nuovo_formulario_model_dati_trasporto_partenza_instance = NuovoFormularioModelDatiTrasportoPartenza.from_json(json)
# print the JSON string representation of the object
print NuovoFormularioModelDatiTrasportoPartenza.to_json()

# convert the object into a dict
nuovo_formulario_model_dati_trasporto_partenza_dict = nuovo_formulario_model_dati_trasporto_partenza_instance.to_dict()
# create an instance of NuovoFormularioModelDatiTrasportoPartenza from a dict
nuovo_formulario_model_dati_trasporto_partenza_from_dict = NuovoFormularioModelDatiTrasportoPartenza.from_dict(nuovo_formulario_model_dati_trasporto_partenza_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


