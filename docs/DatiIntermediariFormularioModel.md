# DatiIntermediariFormularioModel

Dati intermediario

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** | Denominazione del soggetto | 
**codice_fiscale** | **str** | Codice fiscale del soggetto. In base alla nazione (\&quot;nazione_id\&quot;) verranno effettuate le seguenti validazioni: - IT: validazioni formale per codice fiscale personale (16 caratteri) o formato partita IVA (11 cifre decimali) - UE: da 5 a 20 caratteri con successiva validazione formale specifica per il paese UE - Extra UE: da 5 a 20 caratteri | 
**nazione_id** | **str** | Codice ISO 3166-1 alpha-2 della nazione, in caso di \&quot;IT\&quot; è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/nazioni&lt;/i&gt; | [optional] 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_intermediari_formulario_model import DatiIntermediariFormularioModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiIntermediariFormularioModel from a JSON string
dati_intermediari_formulario_model_instance = DatiIntermediariFormularioModel.from_json(json)
# print the JSON string representation of the object
print(DatiIntermediariFormularioModel.to_json())

# convert the object into a dict
dati_intermediari_formulario_model_dict = dati_intermediari_formulario_model_instance.to_dict()
# create an instance of DatiIntermediariFormularioModel from a dict
dati_intermediari_formulario_model_from_dict = DatiIntermediariFormularioModel.from_dict(dati_intermediari_formulario_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


