# ProprietaDatiNotificaPushCaricaCopiaDigitaleModel

Proprietà specifiche della notifica per il caricamento della copia digitale

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Identificativo della copia digitale caricata | [optional] 
**numero_fir** | **str** | Numero FIR | [optional] 
**data_evento** | **datetime** | Data di caricamento della copia digitale | [optional] 
**tipo_accettazione** | [**TipiAccettazione**](TipiAccettazione.md) | Tipo di accettazione indicato nel formulario digitale | [optional] 
**destinatario** | [**IAnagrafica**](IAnagrafica.md) | Destinatario indicato nel formulario digitale | [optional] 

## Example

```python
from rentri_formulari.models.proprieta_dati_notifica_push_carica_copia_digitale_model import ProprietaDatiNotificaPushCaricaCopiaDigitaleModel

# TODO update the JSON string below
json = "{}"
# create an instance of ProprietaDatiNotificaPushCaricaCopiaDigitaleModel from a JSON string
proprieta_dati_notifica_push_carica_copia_digitale_model_instance = ProprietaDatiNotificaPushCaricaCopiaDigitaleModel.from_json(json)
# print the JSON string representation of the object
print(ProprietaDatiNotificaPushCaricaCopiaDigitaleModel.to_json())

# convert the object into a dict
proprieta_dati_notifica_push_carica_copia_digitale_model_dict = proprieta_dati_notifica_push_carica_copia_digitale_model_instance.to_dict()
# create an instance of ProprietaDatiNotificaPushCaricaCopiaDigitaleModel from a dict
proprieta_dati_notifica_push_carica_copia_digitale_model_from_dict = ProprietaDatiNotificaPushCaricaCopiaDigitaleModel.from_dict(proprieta_dati_notifica_push_carica_copia_digitale_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


