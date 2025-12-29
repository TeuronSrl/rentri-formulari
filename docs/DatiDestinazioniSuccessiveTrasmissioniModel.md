# DatiDestinazioniSuccessiveTrasmissioniModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destinatario** | [**DatiDestinatarioFormularioModel**](DatiDestinatarioFormularioModel.md) | Dati destinatario | [optional] 
**accettazione** | [**DatiAccettazioneModel**](DatiAccettazioneModel.md) | Dati accettazione | [optional] 

## Example

```python
from rentri_formulari.models.dati_destinazioni_successive_trasmissioni_model import DatiDestinazioniSuccessiveTrasmissioniModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiDestinazioniSuccessiveTrasmissioniModel from a JSON string
dati_destinazioni_successive_trasmissioni_model_instance = DatiDestinazioniSuccessiveTrasmissioniModel.from_json(json)
# print the JSON string representation of the object
print(DatiDestinazioniSuccessiveTrasmissioniModel.to_json())

# convert the object into a dict
dati_destinazioni_successive_trasmissioni_model_dict = dati_destinazioni_successive_trasmissioni_model_instance.to_dict()
# create an instance of DatiDestinazioniSuccessiveTrasmissioniModel from a dict
dati_destinazioni_successive_trasmissioni_model_from_dict = DatiDestinazioniSuccessiveTrasmissioniModel.from_dict(dati_destinazioni_successive_trasmissioni_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


