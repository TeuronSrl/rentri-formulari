# DatiDestinazioniSuccessiveResultMdodel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinatario** | [**DatiDestinatarioSuccessivoResultModel**](DatiDestinatarioSuccessivoResultModel.md) | Dati del nuovo destinatario | [optional] 
**accettazione** | [**DatiAccettazioneResultModel**](DatiAccettazioneResultModel.md) | Dati di accettazione del rifiuto del nuovo destinatario | [optional] 

## Example

```python
from rentri_formulari.models.dati_destinazioni_successive_result_mdodel import DatiDestinazioniSuccessiveResultMdodel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiDestinazioniSuccessiveResultMdodel from a JSON string
dati_destinazioni_successive_result_mdodel_instance = DatiDestinazioniSuccessiveResultMdodel.from_json(json)
# print the JSON string representation of the object
print(DatiDestinazioniSuccessiveResultMdodel.to_json())

# convert the object into a dict
dati_destinazioni_successive_result_mdodel_dict = dati_destinazioni_successive_result_mdodel_instance.to_dict()
# create an instance of DatiDestinazioniSuccessiveResultMdodel from a dict
dati_destinazioni_successive_result_mdodel_from_dict = DatiDestinazioniSuccessiveResultMdodel.from_dict(dati_destinazioni_successive_result_mdodel_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


