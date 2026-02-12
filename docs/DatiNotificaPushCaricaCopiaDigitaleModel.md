# DatiNotificaPushCaricaCopiaDigitaleModel

Dati della notifica push per il caricamento della copia digitale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proprieta** | [**ProprietaDatiNotificaPushCaricaCopiaDigitaleModel**](ProprietaDatiNotificaPushCaricaCopiaDigitaleModel.md) | Proprietà specifiche della notifica | [optional] 
**tipo** | **str** | Tipo di notifica | [optional] 

## Example

```python
from rentri_formulari.models.dati_notifica_push_carica_copia_digitale_model import DatiNotificaPushCaricaCopiaDigitaleModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiNotificaPushCaricaCopiaDigitaleModel from a JSON string
dati_notifica_push_carica_copia_digitale_model_instance = DatiNotificaPushCaricaCopiaDigitaleModel.from_json(json)
# print the JSON string representation of the object
print DatiNotificaPushCaricaCopiaDigitaleModel.to_json()

# convert the object into a dict
dati_notifica_push_carica_copia_digitale_model_dict = dati_notifica_push_carica_copia_digitale_model_instance.to_dict()
# create an instance of DatiNotificaPushCaricaCopiaDigitaleModel from a dict
dati_notifica_push_carica_copia_digitale_model_from_dict = DatiNotificaPushCaricaCopiaDigitaleModel.from_dict(dati_notifica_push_carica_copia_digitale_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


