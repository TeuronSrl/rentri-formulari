# CopiaCartaceaSoggettoInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**nazione_id** | **str** | Codice ISO 3166-1 alpha-2 della nazione, in caso di \&quot;IT\&quot; è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/nazioni&lt;/i&gt;  &lt;i&gt;Questo campo viene utilizzato esclusivamente per validare i dati di input in base alla nazione di appartenenza (non viene memorizzato e quindi restituito in output).&lt;/i&gt; | [optional] 
**identificativo** | **str** | Codice fiscale del soggetto ⚠️ Deprecato: utilizzare \&quot;codice_fiscale\&quot; | [optional] 
**codice_fiscale** | **str** | Codice fiscale del soggetto.  In base alla nazione (\&quot;nazione_id\&quot;) verranno effettuate le seguenti validazioni: - IT: validazioni formale per codice fiscale personale (16 caratteri) o formato partita IVA (11 cifre decimali) - UE: da 5 a 20 caratteri con successiva validazione formale specifica per il paese UE - Extra UE: da 5 a 20 caratteri | 
**denominazione** | **str** | Denominazione del soggetto | 
**num_iscr_sito** | **str** | Numero iscrizione unità locale.  Il parametro è opzionale e deve essere fornito al trasportatore dal soggetto. | [optional] 

## Example

```python
from rentri_formulari.models.copia_cartacea_soggetto_info import CopiaCartaceaSoggettoInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaCartaceaSoggettoInfo from a JSON string
copia_cartacea_soggetto_info_instance = CopiaCartaceaSoggettoInfo.from_json(json)
# print the JSON string representation of the object
print(CopiaCartaceaSoggettoInfo.to_json())

# convert the object into a dict
copia_cartacea_soggetto_info_dict = copia_cartacea_soggetto_info_instance.to_dict()
# create an instance of CopiaCartaceaSoggettoInfo from a dict
copia_cartacea_soggetto_info_from_dict = CopiaCartaceaSoggettoInfo.from_dict(copia_cartacea_soggetto_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


