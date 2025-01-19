# EsitoFormularioModelEsito

Esito

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** |  | [optional] 
**hash_algorithm** | **str** |  | [optional] 
**digest_to_sign** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**result** | [**ValidazioneXfirResult**](ValidazioneXfirResult.md) |  | [optional] 
**identificativo** | **str** |  | [optional] 
**formulario** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_formulario_model_esito import EsitoFormularioModelEsito

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoFormularioModelEsito from a JSON string
esito_formulario_model_esito_instance = EsitoFormularioModelEsito.from_json(json)
# print the JSON string representation of the object
print(EsitoFormularioModelEsito.to_json())

# convert the object into a dict
esito_formulario_model_esito_dict = esito_formulario_model_esito_instance.to_dict()
# create an instance of EsitoFormularioModelEsito from a dict
esito_formulario_model_esito_from_dict = EsitoFormularioModelEsito.from_dict(esito_formulario_model_esito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


