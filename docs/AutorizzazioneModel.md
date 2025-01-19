# AutorizzazioneModel

Autorizzazione

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero** | **str** | Numero di autorizzazione | [optional] 
**tipo** | [**TipiAutorizzazione**](TipiAutorizzazione.md) | Tipo autorizzazione&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;RecSmalArt208&lt;/i&gt; - Autorizzazione unica per i nuovi impianti di recupero/smaltimento - art. 208 decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RecSmalImpMobiliArt208&lt;/i&gt; - Autorizzazione all&#39;esercizio di operazioni di recupero e/o smaltimento dei rifiuti con impianti mobili - art.208, comma 15 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RicercaSperimentazione&lt;/i&gt; - Autorizzazione alla realizzazione di impianti di ricerca e sperimentazione - art. 211 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;AIA&lt;/i&gt; - Autorizzazione Integrata Ambientale - artt. 29-ter e 213 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;RecProcSemplificata&lt;/i&gt; - Operazioni di recupero mediante Comunicazione in \&quot;Procedura Semplificata\&quot; - artt.214 e 216 del decreto legislativo 3 aprile 2006, n. 152e autorizzazione unica ambientale (AUA) - Decreto Presidente Repubblica n. 59 del 13 marzo 2013.&lt;/li&gt;&lt;li&gt;&lt;i&gt;OpBonifica&lt;/i&gt; - Provvedimenti che autorizzano le operazioni di bonifica, ai sensi del comma 7 dell’art. 242 del decreto legislativo 3 aprile 2006, n. 152.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Straordinario&lt;/i&gt; - Autorizzazioni “straordinarie” art. 191 del decreto legislativo 3 aprile 2006, n. 152 (attività svolte in regime di ordinanza contingibile e urgente)&lt;/li&gt;&lt;li&gt;&lt;i&gt;ComTrattamentoAcqueReflue&lt;/i&gt; - Comunicazione al trattamento di rifiuti e materiali in impianti di trattamento di acque reflue urbane - art. 110 c.3 del D.Lgs. 152/2006&lt;/li&gt;&lt;li&gt;&lt;i&gt;AutTrattamentoAcqueReflue&lt;/i&gt; - Autorizzazione  al trattamento di rifiuti liquidi in impianti di trattamento di acque reflue urbane - artt. 110 c.2 con provvedimento secondo artt. 208 oppure 29-ter e 213 del D.Lgs. 152/2006&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 

## Example

```python
from rentri_formulari.models.autorizzazione_model import AutorizzazioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of AutorizzazioneModel from a JSON string
autorizzazione_model_instance = AutorizzazioneModel.from_json(json)
# print the JSON string representation of the object
print(AutorizzazioneModel.to_json())

# convert the object into a dict
autorizzazione_model_dict = autorizzazione_model_instance.to_dict()
# create an instance of AutorizzazioneModel from a dict
autorizzazione_model_from_dict = AutorizzazioneModel.from_dict(autorizzazione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


