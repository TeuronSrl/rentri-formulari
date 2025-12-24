# NumeroFirTrasportoPostRequest

Dati del trasporto base

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
**nave** | **str** |  | 
**imdg** | **bool** |  | [optional] 
**treno** | **str** |  | 
**rid** | **bool** |  | [optional] 
**tratta** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.numero_fir_trasporto_post_request import NumeroFirTrasportoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of NumeroFirTrasportoPostRequest from a JSON string
numero_fir_trasporto_post_request_instance = NumeroFirTrasportoPostRequest.from_json(json)
# print the JSON string representation of the object
print(NumeroFirTrasportoPostRequest.to_json())

# convert the object into a dict
numero_fir_trasporto_post_request_dict = numero_fir_trasporto_post_request_instance.to_dict()
# create an instance of NumeroFirTrasportoPostRequest from a dict
numero_fir_trasporto_post_request_from_dict = NumeroFirTrasportoPostRequest.from_dict(numero_fir_trasporto_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


