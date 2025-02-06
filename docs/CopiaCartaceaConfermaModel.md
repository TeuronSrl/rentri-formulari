# CopiaCartaceaConfermaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Identificativo univoco della copia del FIR cartaceo | 
**num_iscr_sito** | **str** | Eventuale Numero iscrizione unità locale al quale associare la conferma della copia del FIR cartaceo | [optional] 
**ruolo** | [**RuoloConfermaCopiaCartacea**](RuoloConfermaCopiaCartacea.md) | Ruolo all&#39;interno del FIR del soggetto per cui si effettua l&#39;operazione di conferma di presa visione. | [optional] 
**respingi** | **bool** | Effettua l&#39;operazione di annullamento di una precedente conferma | [optional] 

## Example

```python
from rentri_formulari.models.copia_cartacea_conferma_model import CopiaCartaceaConfermaModel

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaCartaceaConfermaModel from a JSON string
copia_cartacea_conferma_model_instance = CopiaCartaceaConfermaModel.from_json(json)
# print the JSON string representation of the object
print CopiaCartaceaConfermaModel.to_json()

# convert the object into a dict
copia_cartacea_conferma_model_dict = copia_cartacea_conferma_model_instance.to_dict()
# create an instance of CopiaCartaceaConfermaModel from a dict
copia_cartacea_conferma_model_from_dict = CopiaCartaceaConfermaModel.from_dict(copia_cartacea_conferma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


