# DatiTrasportatoreTrasbordoModel

Dati trasportatore per il trasbordo parziale

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nazione_id** | **str** | Codice ISO 3166-1 alpha-2 della nazione, in caso di \&quot;IT\&quot; è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/nazioni&lt;/i&gt; | [optional] 
**denominazione** | **str** | Denominazione del soggetto | 
**codice_fiscale** | **str** | Codice fiscale del soggetto. In base alla nazione (\&quot;nazione_id\&quot;) verranno effettuate le seguenti validazioni: - IT: validazioni formale per codice fiscale personale (16 caratteri) o formato partita IVA (11 cifre decimali) - UE: da 5 a 20 caratteri con successiva validazione formale specifica per il paese UE - Extra UE: da 5 a 20 caratteri | 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasportatore_trasbordo_model import DatiTrasportatoreTrasbordoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasportatoreTrasbordoModel from a JSON string
dati_trasportatore_trasbordo_model_instance = DatiTrasportatoreTrasbordoModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasportatoreTrasbordoModel.to_json())

# convert the object into a dict
dati_trasportatore_trasbordo_model_dict = dati_trasportatore_trasbordo_model_instance.to_dict()
# create an instance of DatiTrasportatoreTrasbordoModel from a dict
dati_trasportatore_trasbordo_model_from_dict = DatiTrasportatoreTrasbordoModel.from_dict(dati_trasportatore_trasbordo_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


