# TrasmissioneDatiItemResult

Oggetto che contiene gli estremi di una trasmissione dati di FIR digitale

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Numero identificativo univoco della trasmissione dati | [optional] 
**sito_oggetto_trasmissione** | [**TrasmissioneDatiSitoResult**](TrasmissioneDatiSitoResult.md) | Unità locale a cui si riferisce la trasmissione dei dati | [optional] 
**sito_trasportatore_per_conto_produttore** | [**TrasmissioneDatiSitoResult**](TrasmissioneDatiSitoResult.md) | Eventuale unità locale del trasportatore che ha provveduto a trasmettere i dati per conto del produttore | [optional] 
**numero_fir** | **str** | Numero FIR del formulario trasmesso | [optional] 
**user_name** | **str** | Identificazione dell&#39;utente o soggetto che ha eseguito la trasmissione | [optional] 
**data_trasmissione** | **datetime** | Data in cui è stata effettuata la trasmissione (Formato ISO 8601 UTC) | [optional] 
**data_emissione** | **datetime** | Data emissione del formulario trasmesso (Formato ISO 8601 UTC) | [optional] 
**codice_eer** | **str** | Codice EER del rifiuto oggetto del formulario trasmesso | [optional] 
**rifiuto_quantita** | **float** | Quantità del rifiuto indicata dal produttore nel formulario trasmesso | [optional] 
**rifiuto_unita_misura** | [**UnitaMisura**](UnitaMisura.md) | Unità di misura della quantità del rifiuto indicata dal produttore nel formulario trasmesso&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;kg&lt;/i&gt; - Chilogrammi&lt;/li&gt;&lt;li&gt;&lt;i&gt;l&lt;/i&gt; - Litri&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**tipo** | [**TipoTrasmissione**](TipoTrasmissione.md) | Modalità con cui è avvenuta la trasmissione dei dati | [optional] 
**stato** | [**StatiTrasmissioneDati**](StatiTrasmissioneDati.md) | Stato della trasmissione | [optional] 

## Example

```python
from rentri_formulari.models.trasmissione_dati_item_result import TrasmissioneDatiItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasmissioneDatiItemResult from a JSON string
trasmissione_dati_item_result_instance = TrasmissioneDatiItemResult.from_json(json)
# print the JSON string representation of the object
print TrasmissioneDatiItemResult.to_json()

# convert the object into a dict
trasmissione_dati_item_result_dict = trasmissione_dati_item_result_instance.to_dict()
# create an instance of TrasmissioneDatiItemResult from a dict
trasmissione_dati_item_result_from_dict = TrasmissioneDatiItemResult.from_dict(trasmissione_dati_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


