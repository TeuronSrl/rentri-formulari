# DatiAnnotazioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annotazione** | **str** |  | 
**identificativo_soggetto** | **str** | Il codice fiscale del soggetto per cui viene richiesta l&#39;aggiunta dell&#39;annotazione al formulario.  Deve coincidere con quello di uno dei soggetti coinvolti nel formulario. L&#39;identità con cui viene eseguita l&#39;operazione deve avere visibilità su (o coincidere con) questo soggetto. | 

## Example

```python
from rentri_formulari.models.dati_annotazione_model import DatiAnnotazioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnnotazioneModel from a JSON string
dati_annotazione_model_instance = DatiAnnotazioneModel.from_json(json)
# print the JSON string representation of the object
print(DatiAnnotazioneModel.to_json())

# convert the object into a dict
dati_annotazione_model_dict = dati_annotazione_model_instance.to_dict()
# create an instance of DatiAnnotazioneModel from a dict
dati_annotazione_model_from_dict = DatiAnnotazioneModel.from_dict(dati_annotazione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


