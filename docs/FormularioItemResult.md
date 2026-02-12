# FormularioItemResult

Contiene le informazioni principali riguardanti un FIR digitale in area virtuale di interscambio,  utilizzato dagli endpoint che restituiscono elencazioni di FIR

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** | Numero FIR | [optional] 
**data_emissione** | **datetime** | Data emissione | [optional] 
**num_iscr_sito** | **str** | Numero iscrizione dell&#39;unità locale in cui è stato creato FIR | [optional] 
**identificativo_soggetto** | **str** |  | [optional] 
**data_creazione** | **datetime** | Data creazione | [optional] 
**codice_eer** | **str** | Codice EER del rifiuto indicato nel FIR | [optional] 
**quantita** | **float** | Quantità del rifiuto | [optional] 
**unita_misura** | [**UnitaMisura**](UnitaMisura.md) | Unità di misura della quantità del rifiuto&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;kg&lt;/i&gt; - Chilogrammi&lt;/li&gt;&lt;li&gt;&lt;i&gt;l&lt;/i&gt; - Litri&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**stato_fisico** | [**StatiFisici**](StatiFisici.md) | Stato fisico del rifiuto&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;SP&lt;/i&gt; - In polvere o pulverulento&lt;/li&gt;&lt;li&gt;&lt;i&gt;S&lt;/i&gt; - Solido&lt;/li&gt;&lt;li&gt;&lt;i&gt;FP&lt;/i&gt; - Fangoso&lt;/li&gt;&lt;li&gt;&lt;i&gt;L&lt;/i&gt; - Liquido&lt;/li&gt;&lt;li&gt;&lt;i&gt;VS&lt;/i&gt; - Vischioso sciropposo&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**caratteristiche_pericolo** | **str** | Eventuali caratteristiche di pericolo del rifiuto, quando pericoloso | [optional] 
**descrizione_rifiuto** | **str** | Eventuale descrizione del rifiuto | [optional] 
**produttore** | [**ProduttoreItemResult**](ProduttoreItemResult.md) | Dati anagrafici del produttore/detentore indicato nel formulario | [optional] 
**trasbordo_parziale_origine** | [**TrasbordoParzialeOrigineResult**](TrasbordoParzialeOrigineResult.md) | Informazioni su FIR e produttore originario, in caso di FIR creato a seguito di trasbordo parziale | [optional] 
**destinatari** | [**List[DestinatarioItemResult]**](DestinatarioItemResult.md) | Dati anagrafici dei destinatari indicati nel formulario | [optional] 
**trasportatori** | [**List[TrasportatoreItemResult]**](TrasportatoreItemResult.md) | Dati anagrafici dei trasportatori indicati nel formulario | [optional] 
**intermediari** | [**List[IntermediarioItemResult]**](IntermediarioItemResult.md) | Dati anagrafici degli intermediari indicati nel formulario | [optional] 
**stato** | [**StatoFormulario**](StatoFormulario.md) | Stato del formulario&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantita&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoQuantitaTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati sulla quantità del rifiuto e dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoIniziale&lt;/i&gt; - Il formulario necessita dei dati del trasporto iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttoreTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del produttore e del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreIniziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore iniziale&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaProduttore&lt;/i&gt; - Il formulario necessita della firma del produttore&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoTrasportoSuccessivo&lt;/i&gt; - Il formulario è in carico ad un traportatore e necessita dell&#39;inserimento dei dati del trasporto successivo;             il trasportatore che ha in carico il rifiuto può inserire informazioni aggiuntive (annotazioni, trasbordo parziale, sosta tecnica, trasbordo totale, allegati)             che dovranno essere successivamente firmate&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasportatoreSuccessivo&lt;/i&gt; - Il formulario necessita della firma del trasportatore successivo al primo che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnotazione&lt;/i&gt; - Il formulario necessita della firma dell&#39;annotazione da parte del soggetto che l&#39;ha inserita&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoParziale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che effettua il trasbordo parziale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaTrasbordoTotale&lt;/i&gt; - Il formulario necessita della firma del trasportatore che prende in carico il rifiuto con l&#39;operazione di trasbordo totale del rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaSostaTecnica&lt;/i&gt; - Il formulario necessita della firma del trasportatore che ha in carico il rifiuto e ha inserito i dati della sosta tecnica&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAllegato&lt;/i&gt; - Il formulario necessita della firma del soggetto che ha aggiunto i dati relativi all&#39;allegato al formulario digitale. ATTENZIONE!: questo valore è DEPRECATO: lo stato non è più utilizzato, per gli allegati aggiunti via API non è più prevista la firma&lt;/li&gt;&lt;li&gt;&lt;i&gt;InserimentoAccettazione&lt;/i&gt; - Il formulario è in carico all&#39;ultimo trasportatore ed è in attesa dell&#39;inserimento dei dati di accettazione da parte del destinatario verso cui è destinato il rifiuto             (a meno di ulteriori informazioni aggiuntive che l&#39;ultimo trasportatore può inserire prima della consegna al destinatario)&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazione&lt;/i&gt; - Il formulario necessita della firma del destinatario indicato nei dati di partenza&lt;/li&gt;&lt;li&gt;&lt;i&gt;Accettato&lt;/i&gt; - Il formulario è stato accettato dal destinatario ed ha concluso il suo ciclo di vita&lt;/li&gt;&lt;li&gt;&lt;i&gt;RespintoAccettatoParzialmente&lt;/i&gt; - Il formulario è stato respinto o accettato parzialmente, il trasportatore che ha in carico il rifiuto può inserire (in accordo con il produttore) i dati             di un nuovo destinatario&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaDestinatarioSuccessivo&lt;/i&gt; - Il formulario è in attesa della firma dei dati del nuovo destinatario inseriti da parte del trasportatore che ha in carico il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAccettazioneSuccessiva&lt;/i&gt; - Il formulario necessita della firma del destinatario successivo a quello indicato nei dati di partenza che ha rifiutato totalmente o parzialmente il rifiuto&lt;/li&gt;&lt;li&gt;&lt;i&gt;FirmaAnnullamento&lt;/i&gt; - Il formulario necessita della firma dei dati di annullamento inseriti dal soggetto titolare della vidimazione del numero FIR&lt;/li&gt;&lt;li&gt;&lt;i&gt;Annullato&lt;/i&gt; - Il formulario risulta essere stato annullato&lt;/li&gt;&lt;li&gt;&lt;i&gt;Indeterminato&lt;/i&gt; - Il formulario è in uno stato non determinato per incoerenza dei dati contenuti&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**is_upload** | **bool** | Indica se il formulario è stato prodotto e/o modificato al di fuori dell&#39;area virtuale di interscambio | [optional] 
**versione** | **int** | Numero incrementale della versione del formulario presente in Area virtuale di interscambio | [optional] 

## Example

```python
from rentri_formulari.models.formulario_item_result import FormularioItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of FormularioItemResult from a JSON string
formulario_item_result_instance = FormularioItemResult.from_json(json)
# print the JSON string representation of the object
print FormularioItemResult.to_json()

# convert the object into a dict
formulario_item_result_dict = formulario_item_result_instance.to_dict()
# create an instance of FormularioItemResult from a dict
formulario_item_result_from_dict = FormularioItemResult.from_dict(formulario_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


