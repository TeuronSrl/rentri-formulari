# EsitoFormularioModelEsito

Esito

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** | Numero FIR | [optional] 
**hash_algorithm** | **str** | Sigla dell&#39;algoritmo di hashing con cui è stato calcolato il codice hash | [optional] 
**digest_to_sign** | **str** | Valore del codice hash su cui calcolare la firma crittografica | [optional] 
**token** | **str** | Struttura dati \&quot;opaca\&quot;, richiesta come input nell&#39;endpoint di acquisizione della firma crittografica,  utilizzata dal backend per collegare le due operazioni | [optional] 
**versione** | **int** | Versione di modifica del formulario su cui è stato calcolato il codice hash da firmare. Se diverso dal valore di cui si è presa visione è consigliabile che il flusso di chiamata preveda un nuovo caricamento dei dati su cui si va ad apporre la firma da esporre al soggetto firmatario. | [optional] 
**allegato_id** | **int** | Identificativo interno al FIR digitale associato all&#39;allegato | [optional] 
**result** | [**ValidazioneXfirResult**](ValidazioneXfirResult.md) |  | [optional] 
**identificativo** | **str** |  | [optional] 
**formulario** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md) |  | [optional] 

## Example

```python
from rentri_formulari.models.esito_formulario_model_esito import EsitoFormularioModelEsito

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoFormularioModelEsito from a JSON string
esito_formulario_model_esito_instance = EsitoFormularioModelEsito.from_json(json)
# print the JSON string representation of the object
print(EsitoFormularioModelEsito.to_json())

# convert the object into a dict
esito_formulario_model_esito_dict = esito_formulario_model_esito_instance.to_dict()
# create an instance of EsitoFormularioModelEsito from a dict
esito_formulario_model_esito_from_dict = EsitoFormularioModelEsito.from_dict(esito_formulario_model_esito_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


