# DatiProduttoreFormularioSitoModel

Dati produttore

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero di iscrizione al RENTRI | 
**luogo_produzione** | [**IndirizzoModel**](IndirizzoModel.md) | Luogo di produzione se diverso da indirizzo | [optional] 
**autorizzazione** | [**AutorizzazioneModel**](AutorizzazioneModel.md) | Autorizzazione | [optional] 
**detentore** | **bool** | Specifica se il dato del produttore è riferito al detentore del rifiuto | [optional] 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_produttore_formulario_sito_model import DatiProduttoreFormularioSitoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiProduttoreFormularioSitoModel from a JSON string
dati_produttore_formulario_sito_model_instance = DatiProduttoreFormularioSitoModel.from_json(json)
# print the JSON string representation of the object
print DatiProduttoreFormularioSitoModel.to_json()

# convert the object into a dict
dati_produttore_formulario_sito_model_dict = dati_produttore_formulario_sito_model_instance.to_dict()
# create an instance of DatiProduttoreFormularioSitoModel from a dict
dati_produttore_formulario_sito_model_from_dict = DatiProduttoreFormularioSitoModel.from_dict(dati_produttore_formulario_sito_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


