# DettaglioFormularioDatiTrasportoInner

Dati del trasporto base

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo_trasporto** | [**TipoTrasporto**](TipoTrasporto.md) |  | [optional] 
**dati_firma_trasportatore** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**trasportatore_id** | **int** | Riferimento al trasportatore nel contesto del FIR a cui sono da attribuire i dati di trasporto | [optional] 
**conducente** | [**ConducenteModel**](ConducenteModel.md) | Conducente | 
**targa_automezzo** | **str** | Targa automezzo.  Il dato è necessario se non si indica una targa per il rimorchio | [optional] 
**targa_rimorchio** | **str** | Targa rimorchio | [optional] 
**percorso** | **str** | Percorso (se diverso dal più breve) | [optional] 
**presa_in_carico_rimorchio_precedente** | **bool** | Significativo solo per i trasporti successivi al primo | [optional] 
**data_ora_inizio_trasporto** | **datetime** | Data e ora inizio trasporto (formato ISO 8601 UTC) | 
**annotazioni** | **str** | Annotazioni | [optional] 
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 
**treno** | **str** |  | 
**rid** | **bool** |  | [optional] 
**tratta** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dettaglio_formulario_dati_trasporto_inner import DettaglioFormularioDatiTrasportoInner

# TODO update the JSON string below
json = "{}"
# create an instance of DettaglioFormularioDatiTrasportoInner from a JSON string
dettaglio_formulario_dati_trasporto_inner_instance = DettaglioFormularioDatiTrasportoInner.from_json(json)
# print the JSON string representation of the object
print(DettaglioFormularioDatiTrasportoInner.to_json())

# convert the object into a dict
dettaglio_formulario_dati_trasporto_inner_dict = dettaglio_formulario_dati_trasporto_inner_instance.to_dict()
# create an instance of DettaglioFormularioDatiTrasportoInner from a dict
dettaglio_formulario_dati_trasporto_inner_from_dict = DettaglioFormularioDatiTrasportoInner.from_dict(dettaglio_formulario_dati_trasporto_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


