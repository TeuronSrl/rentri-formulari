# DatiDestinatarioFormularioModel3

Dati destinatario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**denominazione** | **str** | Denominazione del soggetto | 
**codice_fiscale** | **str** | Codice fiscale del soggetto. In base alla nazione (\&quot;nazione_id\&quot;) verranno effettuate le seguenti validazioni: - IT: validazioni formale per codice fiscale personale (16 caratteri) o formato partita IVA (11 cifre decimali) - UE: da 5 a 20 caratteri con successiva validazione formale specifica per il paese UE - Extra UE: da 5 a 20 caratteri | 
**nazione_id** | **str** | Codice ISO 3166-1 alpha-2 della nazione, in caso di \&quot;IT\&quot; è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/nazioni&lt;/i&gt; | [optional] 
**indirizzo** | [**IndirizzoModel**](IndirizzoModel.md) | Indirizzo | 
**autorizzazione** | [**AutorizzazioneModel**](AutorizzazioneModel.md) | Autorizzazione.  Il valore è sempre necessario tranne quando l&#39;unità locale del destinatario coincide con quella del produttore ed il rifiuto è stato prodotto fuori dall&#39;unità locale. | [optional] 
**attivita** | [**OperazioniRecuperoSmaltimento**](OperazioniRecuperoSmaltimento.md) | Attività di recupero o smaltimento a destinazione.  Il valore è sempre necessario tranne quando l&#39;unità locale del destinatario coincide con quella del produttore ed il rifiuto è stato prodotto fuori dall&#39;unità locale.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;R1&lt;/i&gt; - Utilizzazione principale come combustibile o come altro mezzo per produrre energia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R2&lt;/i&gt; - Rigenerazione/recupero di solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R3&lt;/i&gt; - Riciclo/recupero delle sostanze organiche non utilizzate come solventi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R4&lt;/i&gt; - Riciclo/recupero dei metalli e dei composti metallici&lt;/li&gt;&lt;li&gt;&lt;i&gt;R5&lt;/i&gt; - Riciclo/recupero di altre sostanze inorganiche&lt;/li&gt;&lt;li&gt;&lt;i&gt;R6&lt;/i&gt; - Rigenerazione degli acidi o delle basi&lt;/li&gt;&lt;li&gt;&lt;i&gt;R7&lt;/i&gt; - Recupero dei prodotti che servono a captare gli inquinanti&lt;/li&gt;&lt;li&gt;&lt;i&gt;R8&lt;/i&gt; - Recupero dei prodotti provenienti dai catalizzatori&lt;/li&gt;&lt;li&gt;&lt;i&gt;R9&lt;/i&gt; - Rigenerazione o altri reimpieghi degli oli&lt;/li&gt;&lt;li&gt;&lt;i&gt;R10&lt;/i&gt; - Spandimento sul suolo a beneficio dell&#39;agricoltura o dell&#39;ecologia&lt;/li&gt;&lt;li&gt;&lt;i&gt;R11&lt;/i&gt; - Utilizzazione di rifiuti ottenuti da una delle operazioni indicate da R1 a R10&lt;/li&gt;&lt;li&gt;&lt;i&gt;R12&lt;/i&gt; - Scambio di rifiuti per sottoporli a una delle operazioni indicate da R1 a R11&lt;/li&gt;&lt;li&gt;&lt;i&gt;R13&lt;/i&gt; - Messa in riserva di rifiuti per sottoporli a una delle operazioni indicate nei punti da R1 a R12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D1&lt;/i&gt; - Deposito sul o nel suolo&lt;/li&gt;&lt;li&gt;&lt;i&gt;D2&lt;/i&gt; - Trattamento in ambiente terrestre&lt;/li&gt;&lt;li&gt;&lt;i&gt;D3&lt;/i&gt; - Iniezioni in profondità&lt;/li&gt;&lt;li&gt;&lt;i&gt;D4&lt;/i&gt; - Lagunaggio&lt;/li&gt;&lt;li&gt;&lt;i&gt;D5&lt;/i&gt; - Messa in discarica specialmente allestita&lt;/li&gt;&lt;li&gt;&lt;i&gt;D6&lt;/i&gt; - Scarico dei rifiuti solidi nell&#39;ambiente idrico eccetto l&#39;immersione&lt;/li&gt;&lt;li&gt;&lt;i&gt;D7&lt;/i&gt; - Immersione, compreso il seppellimento nel sottosuolo marino&lt;/li&gt;&lt;li&gt;&lt;i&gt;D8&lt;/i&gt; - Trattamento biologico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D9&lt;/i&gt; - Trattamento fisico-chimico non specificato altrove nel presente allegato&lt;/li&gt;&lt;li&gt;&lt;i&gt;D10&lt;/i&gt; - Incenerimento a terra&lt;/li&gt;&lt;li&gt;&lt;i&gt;D11&lt;/i&gt; - Incenerimento in mare&lt;/li&gt;&lt;li&gt;&lt;i&gt;D12&lt;/i&gt; - Deposito permanente&lt;/li&gt;&lt;li&gt;&lt;i&gt;D13&lt;/i&gt; - Raggruppamento preliminare prima di una delle operazioni di cui ai punti da D1 a D12&lt;/li&gt;&lt;li&gt;&lt;i&gt;D14&lt;/i&gt; - Ricondizionamento preliminare prima di una delle operazioni di cui ai punti da D1 a D13&lt;/li&gt;&lt;li&gt;&lt;i&gt;D15&lt;/i&gt; - Deposito preliminare prima di una delle operazioni di cui ai punti da D1 a D14&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**numero_iscrizione_albo** | **str** | Iscrizione Albo | [optional] 

## Example

```python
from rentri_formulari.models.dati_destinatario_formulario_model3 import DatiDestinatarioFormularioModel3

# TODO update the JSON string below
json = "{}"
# create an instance of DatiDestinatarioFormularioModel3 from a JSON string
dati_destinatario_formulario_model3_instance = DatiDestinatarioFormularioModel3.from_json(json)
# print the JSON string representation of the object
print DatiDestinatarioFormularioModel3.to_json()

# convert the object into a dict
dati_destinatario_formulario_model3_dict = dati_destinatario_formulario_model3_instance.to_dict()
# create an instance of DatiDestinatarioFormularioModel3 from a dict
dati_destinatario_formulario_model3_from_dict = DatiDestinatarioFormularioModel3.from_dict(dati_destinatario_formulario_model3_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


