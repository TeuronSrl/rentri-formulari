# DatiProduttoreFormularioBaseModel

Dati produttore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**luogo_produzione** | [**IndirizzoModel**](IndirizzoModel.md) | Luogo di produzione se diverso da indirizzo | [optional] 
**autorizzazione** | [**AutorizzazioneModel**](AutorizzazioneModel.md) | Autorizzazione | [optional] 
**detentore** | **bool** | Specifica se il dato del produttore è riferito al detentore del rifiuto | [optional] 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_produttore_formulario_base_model import DatiProduttoreFormularioBaseModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiProduttoreFormularioBaseModel from a JSON string
dati_produttore_formulario_base_model_instance = DatiProduttoreFormularioBaseModel.from_json(json)
# print the JSON string representation of the object
print(DatiProduttoreFormularioBaseModel.to_json())

# convert the object into a dict
dati_produttore_formulario_base_model_dict = dati_produttore_formulario_base_model_instance.to_dict()
# create an instance of DatiProduttoreFormularioBaseModel from a dict
dati_produttore_formulario_base_model_from_dict = DatiProduttoreFormularioBaseModel.from_dict(dati_produttore_formulario_base_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


