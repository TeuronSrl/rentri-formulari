# DatiFirmaResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione_firmatario** | **str** | Nome intestatario certificato di firma | [optional] 
**identificativo_firmatario** | **str** | Codice fiscale estratto dal certificato di firma | [optional] 
**data_firma** | **datetime** | Data della firma | [optional] 
**identificativo_utente** | **str** | Utente a cui è da attribuire l&#39;operazione di firma | [optional] 
**credentials_id** | **str** | Identificativo delle credenziali che hanno autorizzato la firma | [optional] 
**nome_certificato_ca** | **str** | Distinguished Name (DN) della CA che ha rilasciato il certificato di firma | [optional] 

## Example

```python
from rentri_formulari.models.dati_firma_result import DatiFirmaResult

# TODO update the JSON string below
json = "{}"
# create an instance of DatiFirmaResult from a JSON string
dati_firma_result_instance = DatiFirmaResult.from_json(json)
# print the JSON string representation of the object
print DatiFirmaResult.to_json()

# convert the object into a dict
dati_firma_result_dict = dati_firma_result_instance.to_dict()
# create an instance of DatiFirmaResult from a dict
dati_firma_result_from_dict = DatiFirmaResult.from_dict(dati_firma_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


