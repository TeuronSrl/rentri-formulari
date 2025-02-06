# NuovoFormularioModel

Formulario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero iscrizione unità locale di riferimento a cui il formulario verrà associato.  L&#39;unità locale deve appartenere al produttore o al primo trasportatore. | 
**dati_partenza** | [**DatiPartenzaModel**](DatiPartenzaModel.md) | Dati iniziali del formulario | 
**dati_trasporto_partenza** | [**NuovoFormularioModelDatiTrasportoPartenza**](NuovoFormularioModelDatiTrasportoPartenza.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.nuovo_formulario_model import NuovoFormularioModel

# TODO update the JSON string below
json = "{}"
# create an instance of NuovoFormularioModel from a JSON string
nuovo_formulario_model_instance = NuovoFormularioModel.from_json(json)
# print the JSON string representation of the object
print NuovoFormularioModel.to_json()

# convert the object into a dict
nuovo_formulario_model_dict = nuovo_formulario_model_instance.to_dict()
# create an instance of NuovoFormularioModel from a dict
nuovo_formulario_model_from_dict = NuovoFormularioModel.from_dict(nuovo_formulario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


