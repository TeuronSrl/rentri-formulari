# EsitoGetHashPerFirmaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_algorithm** | **str** | Sigla dell&#39;algoritmo di hashing con cui è stato calcolato il codice hash | [optional] 
**digest_to_sign** | **str** | Valore del codice hash su cui calcolare la firma crittografica | [optional] 
**token** | **str** | Struttura dati \&quot;opaca\&quot;, richiesta come input nell&#39;endpoint di acquisizione della firma crittografica,  utilizzata dal backend per collegare le due operazioni | [optional] 
**versione** | **int** | Versione di modifica del formulario su cui è stato calcolato il codice hash da firmare. Se diverso dal valore di cui si è presa visione è consigliabile che il flusso di chiamata preveda un nuovo caricamento dei dati su cui si va ad apporre la firma da esporre al soggetto firmatario. | [optional] 

## Example

```python
from rentri_formulari.models.esito_get_hash_per_firma_model import EsitoGetHashPerFirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of EsitoGetHashPerFirmaModel from a JSON string
esito_get_hash_per_firma_model_instance = EsitoGetHashPerFirmaModel.from_json(json)
# print the JSON string representation of the object
print EsitoGetHashPerFirmaModel.to_json()

# convert the object into a dict
esito_get_hash_per_firma_model_dict = esito_get_hash_per_firma_model_instance.to_dict()
# create an instance of EsitoGetHashPerFirmaModel from a dict
esito_get_hash_per_firma_model_from_dict = EsitoGetHashPerFirmaModel.from_dict(esito_get_hash_per_firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


