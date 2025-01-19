# DatiPartenzaModelProduttore

Produttore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** | Denominazione del soggetto | 
**codice_fiscale** | **str** | Codice fiscale del soggetto. In base alla nazione (\&quot;nazione_id\&quot;) verranno effettuate le seguenti validazioni: - IT: validazioni formale per codice fiscale personale (16 caratteri) o formato partita IVA (11 cifre decimali) - UE: da 5 a 20 caratteri con successiva validazione formale specifica per il paese UE - Extra UE: da 5 a 20 caratteri | 
**nazione_id** | **str** | Codice ISO 3166-1 alpha-2 della nazione, in caso di \&quot;IT\&quot; è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/nazioni&lt;/i&gt; | [optional] 
**indirizzo** | [**IndirizzoModel**](IndirizzoModel.md) | Indirizzo | 
**luogo_produzione** | [**IndirizzoModel**](IndirizzoModel.md) | Luogo di produzione se diverso da indirizzo | [optional] 
**autorizzazione** | [**AutorizzazioneModel**](AutorizzazioneModel.md) | Autorizzazione | [optional] 
**detentore** | **bool** | Specifica se il dato del produttore è riferito al detentore del rifiuto | [optional] 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 
**num_iscr_sito** | **str** | Numero di iscrizione al RENTRI | 

## Example

```python
from rentri_formulari.models.dati_partenza_model_produttore import DatiPartenzaModelProduttore

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPartenzaModelProduttore from a JSON string
dati_partenza_model_produttore_instance = DatiPartenzaModelProduttore.from_json(json)
# print the JSON string representation of the object
print(DatiPartenzaModelProduttore.to_json())

# convert the object into a dict
dati_partenza_model_produttore_dict = dati_partenza_model_produttore_instance.to_dict()
# create an instance of DatiPartenzaModelProduttore from a dict
dati_partenza_model_produttore_from_dict = DatiPartenzaModelProduttore.from_dict(dati_partenza_model_produttore_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


