# DatiRifiutoModel

Identificazione del rifiuto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_eer** | **str** | Codice EER | 
**descrizione** | **str** | Descrizione del rifiuto, richiesta se il Codice EER specificato è di tipo .99 | [optional] 
**provenienza** | [**ProvenienzaRifiuto**](ProvenienzaRifiuto.md) | Provenienza&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;U&lt;/i&gt; - Urbano&lt;/li&gt;&lt;li&gt;&lt;i&gt;S&lt;/i&gt; - Speciale&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
**caratteristiche_chimico_fisiche** | **str** | Caratteristiche chimico fisiche del rifiuto | [optional] 
**caratteristiche_pericolo** | [**List[CaratteristichePericolo]**](CaratteristichePericolo.md) | Classificazione di pericolo (HP), richiesta se e solo se il Codice EER si riferisce ad un rifiuto pericoloso&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;HP01&lt;/i&gt; - Esplosivo&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP02&lt;/i&gt; - Comburente&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP03&lt;/i&gt; - Infiammabile&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP04&lt;/i&gt; - Irritante - Irritazione cutanea e lesioni oculari&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP05&lt;/i&gt; - Tossicità specifica per organi bersaglio (STOT)/Tossicità in caso di respirazione&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP06&lt;/i&gt; - Tossicità acuta&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP07&lt;/i&gt; - Cancerogeno&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP08&lt;/i&gt; - Corrosivo&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP09&lt;/i&gt; - Infettivo&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP10&lt;/i&gt; - Tossico per la riproduzione&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP11&lt;/i&gt; - Mutageno&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP12&lt;/i&gt; - Liberazione di gas a tossicità acuta&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP13&lt;/i&gt; - Sensibilizzante&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP14&lt;/i&gt; - Ecotossico&lt;/li&gt;&lt;li&gt;&lt;i&gt;HP15&lt;/i&gt; - Rifiuto che non possiede direttamente una delle caratteristiche di pericolo già menzionate, ma può manifestarla successivamente&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**stato_fisico** | [**StatiFisici**](StatiFisici.md) | Stato fisico&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;SP&lt;/i&gt; - In polvere o pulverulento&lt;/li&gt;&lt;li&gt;&lt;i&gt;S&lt;/i&gt; - Solido&lt;/li&gt;&lt;li&gt;&lt;i&gt;FP&lt;/i&gt; - Fangoso&lt;/li&gt;&lt;li&gt;&lt;i&gt;L&lt;/i&gt; - Liquido&lt;/li&gt;&lt;li&gt;&lt;i&gt;VS&lt;/i&gt; - Vischioso sciropposo&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
**quantita** | [**QuantitaModel**](QuantitaModel.md) | Quantità | [optional] 
**verificato_in_partenza** | **bool** | Verificato in partenza | [optional] 
**trasporto_adr** | **bool** | Trasporto ADR | [optional] 
**dati_adr** | [**NormativaADRModel**](NormativaADRModel.md) | Dati ADR.  Il dato non deve essere indicato se la proprietà \&quot;trasporto_adr\&quot; è diversa da true. | [optional] 
**analisi_classificazione** | [**AnalisiClassificazioneModel**](AnalisiClassificazioneModel.md) | Analisi/Classificazione | [optional] 
**numero_colli** | **str** | Numero di colli.  Specificare un valore in caso non si imposti \&quot;rinfusa\&quot; a &lt;i&gt;true&lt;/i&gt; | [optional] 
**rinfusa** | **bool** | Rinfusa.  Se valorizzato a &lt;i&gt;true&lt;/i&gt; indica che il rifiuto non è partizionato in colli. | [optional] 

## Example

```python
from rentri_formulari.models.dati_rifiuto_model import DatiRifiutoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiRifiutoModel from a JSON string
dati_rifiuto_model_instance = DatiRifiutoModel.from_json(json)
# print the JSON string representation of the object
print(DatiRifiutoModel.to_json())

# convert the object into a dict
dati_rifiuto_model_dict = dati_rifiuto_model_instance.to_dict()
# create an instance of DatiRifiutoModel from a dict
dati_rifiuto_model_from_dict = DatiRifiutoModel.from_dict(dati_rifiuto_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


