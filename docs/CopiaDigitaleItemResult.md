# CopiaDigitaleItemResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Codice univoco associato alla restituzione della copia digitale | [optional] 
**numero_fir** | **str** | Numero FIR | [optional] 
**data_emissione** | **datetime** | Data di emissione indicata nel FIR digitale | [optional] 
**data_caricamento** | **datetime** | Data di caricamento | [optional] 
**tipo_accettazione** | [**TipiAccettazione**](TipiAccettazione.md) | Tipo di accettazione del destinatario&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;A&lt;/i&gt; - Accettato per intero&lt;/li&gt;&lt;li&gt;&lt;i&gt;P&lt;/i&gt; - Accettato parzialmente&lt;/li&gt;&lt;li&gt;&lt;i&gt;R&lt;/i&gt; - Respinto&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**is_confermata** | **bool** | Indica se per la copia digitale è già stata confermata la presa visione | [optional] 
**note** | **str** | Eventuali note aggiunte dal destinatario in fase di caricamento | [optional] 
**produttore** | [**CopiaDigitaleRuoloItemResult**](CopiaDigitaleRuoloItemResult.md) | Dati del produttore indicati nel FIR digitale | [optional] 
**trasportatori** | [**List[CopiaDigitaleRuoloItemResult]**](CopiaDigitaleRuoloItemResult.md) | Dati dei trasportatori indicati nel FIR digitale | [optional] 
**intermediari** | [**List[CopiaDigitaleRuoloItemResult]**](CopiaDigitaleRuoloItemResult.md) | Dati degli intermediari indicati nel FIR digitale | [optional] 

## Example

```python
from rentri_formulari.models.copia_digitale_item_result import CopiaDigitaleItemResult

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaDigitaleItemResult from a JSON string
copia_digitale_item_result_instance = CopiaDigitaleItemResult.from_json(json)
# print the JSON string representation of the object
print(CopiaDigitaleItemResult.to_json())

# convert the object into a dict
copia_digitale_item_result_dict = copia_digitale_item_result_instance.to_dict()
# create an instance of CopiaDigitaleItemResult from a dict
copia_digitale_item_result_from_dict = CopiaDigitaleItemResult.from_dict(copia_digitale_item_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


