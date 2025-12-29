# NoteAnnullamentoModel

Dati richiesti per l'aggiunta delle note di annullamento di un FIR

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note di annullamento | 

## Example

```python
from rentri_formulari.models.note_annullamento_model import NoteAnnullamentoModel

# TODO update the JSON string below
json = "{}"
# create an instance of NoteAnnullamentoModel from a JSON string
note_annullamento_model_instance = NoteAnnullamentoModel.from_json(json)
# print the JSON string representation of the object
print(NoteAnnullamentoModel.to_json())

# convert the object into a dict
note_annullamento_model_dict = note_annullamento_model_instance.to_dict()
# create an instance of NoteAnnullamentoModel from a dict
note_annullamento_model_from_dict = NoteAnnullamentoModel.from_dict(note_annullamento_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


