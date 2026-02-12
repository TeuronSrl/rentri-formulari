# DatiTrasmissioneFormularioModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dati_partenza** | [**DatiTrasmissionePartenzaModel**](DatiTrasmissionePartenzaModel.md) |  | 
**dati_trasporto** | [**List[DatiTrasportoTrasmissioneBaseModel1]**](DatiTrasportoTrasmissioneBaseModel1.md) |  | [optional] 
**dati_accettazione** | [**DatiAccettazioneModel**](DatiAccettazioneModel.md) | Dati accettazione | [optional] 
**dati_annotazioni** | [**List[DatiAnnotazioneModel]**](DatiAnnotazioneModel.md) |  | [optional] 
**dati_trasbordo_totale** | [**DatiTrasbordoTotaleTrasmissioneModel**](DatiTrasbordoTotaleTrasmissioneModel.md) |  | [optional] 
**dati_trasbordi_parziali** | [**List[DatiTrasbordoParzialeTrasmissioneModel]**](DatiTrasbordoParzialeTrasmissioneModel.md) |  | [optional] 
**dati_soste_tecniche** | [**List[DatiSostaTecnicaTrasmissioneModel]**](DatiSostaTecnicaTrasmissioneModel.md) |  | [optional] 
**dati_destinazioni_successive** | [**List[DatiDestinazioniSuccessiveTrasmissioniModel]**](DatiDestinazioniSuccessiveTrasmissioniModel.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasmissione_formulario_model import DatiTrasmissioneFormularioModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasmissioneFormularioModel from a JSON string
dati_trasmissione_formulario_model_instance = DatiTrasmissioneFormularioModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasmissioneFormularioModel.to_json())

# convert the object into a dict
dati_trasmissione_formulario_model_dict = dati_trasmissione_formulario_model_instance.to_dict()
# create an instance of DatiTrasmissioneFormularioModel from a dict
dati_trasmissione_formulario_model_from_dict = DatiTrasmissioneFormularioModel.from_dict(dati_trasmissione_formulario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


