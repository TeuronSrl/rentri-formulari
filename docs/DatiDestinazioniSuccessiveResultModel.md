# DatiDestinazioniSuccessiveResultModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinatario** | [**DatiDestinatarioSuccessivoResultModel**](DatiDestinatarioSuccessivoResultModel.md) | Dati del nuovo destinatario | [optional] 
**accettazione** | [**DatiAccettazioneResultModel**](DatiAccettazioneResultModel.md) | Dati di accettazione del rifiuto del nuovo destinatario | [optional] 

## Example

```python
from rentri_formulari.models.dati_destinazioni_successive_result_model import DatiDestinazioniSuccessiveResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiDestinazioniSuccessiveResultModel from a JSON string
dati_destinazioni_successive_result_model_instance = DatiDestinazioniSuccessiveResultModel.from_json(json)
# print the JSON string representation of the object
print DatiDestinazioniSuccessiveResultModel.to_json()

# convert the object into a dict
dati_destinazioni_successive_result_model_dict = dati_destinazioni_successive_result_model_instance.to_dict()
# create an instance of DatiDestinazioniSuccessiveResultModel from a dict
dati_destinazioni_successive_result_model_from_dict = DatiDestinazioniSuccessiveResultModel.from_dict(dati_destinazioni_successive_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


