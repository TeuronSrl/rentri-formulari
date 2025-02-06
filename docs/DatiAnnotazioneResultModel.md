# DatiAnnotazioneResultModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_firma** | [**DatiFirmaResult**](DatiFirmaResult.md) |  | [optional] 
**annotazione** | **str** |  | 
**identificativo_soggetto** | **str** | Il codice fiscale del soggetto per cui viene richiesta l&#39;aggiunta dell&#39;annotazione al formulario.  Deve coincidere con quello di uno dei soggetti coinvolti nel formulario. L&#39;identità con cui viene eseguita l&#39;operazione deve avere visibilità su (o coincidere con) questo soggetto. | 

## Example

```python
from rentri_formulari.models.dati_annotazione_result_model import DatiAnnotazioneResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnnotazioneResultModel from a JSON string
dati_annotazione_result_model_instance = DatiAnnotazioneResultModel.from_json(json)
# print the JSON string representation of the object
print DatiAnnotazioneResultModel.to_json()

# convert the object into a dict
dati_annotazione_result_model_dict = dati_annotazione_result_model_instance.to_dict()
# create an instance of DatiAnnotazioneResultModel from a dict
dati_annotazione_result_model_from_dict = DatiAnnotazioneResultModel.from_dict(dati_annotazione_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


