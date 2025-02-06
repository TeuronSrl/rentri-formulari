# ValidazioneXfirResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formulario** | [**DettaglioFormulario**](DettaglioFormulario.md) |  | [optional] 
**numero_fir** | **str** |  | [optional] [readonly] 
**formulario_presente_in_rentri** | **bool** |  | [optional] 
**formulario_aggiornato_in_rentri** | **bool** |  | [optional] 
**formato** | [**List[ControlloFormatoResult]**](ControlloFormatoResult.md) |  | [optional] 
**var_schema** | [**List[ControlloSchemaResult]**](ControlloSchemaResult.md) |  | [optional] 
**firme** | [**List[ControlloFirmeResult]**](ControlloFirmeResult.md) |  | [optional] 
**vidimazione** | [**List[ControlloVidimazioneResult]**](ControlloVidimazioneResult.md) |  | [optional] 
**codice_fiscale_soggetto** | **str** |  | [optional] [readonly] 
**valido** | **bool** |  | [optional] [readonly] 

## Example

```python
from rentri_formulari.models.validazione_xfir_result import ValidazioneXfirResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidazioneXfirResult from a JSON string
validazione_xfir_result_instance = ValidazioneXfirResult.from_json(json)
# print the JSON string representation of the object
print ValidazioneXfirResult.to_json()

# convert the object into a dict
validazione_xfir_result_dict = validazione_xfir_result_instance.to_dict()
# create an instance of ValidazioneXfirResult from a dict
validazione_xfir_result_from_dict = ValidazioneXfirResult.from_dict(validazione_xfir_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


