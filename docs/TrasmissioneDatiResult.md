# TrasmissioneDatiResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identificativo** | **str** | Numero identificativo univoco della trasmissione dati | [optional] 
**sito_oggetto_trasmissione** | [**TrasmissioneDatiSitoResult**](TrasmissioneDatiSitoResult.md) | Unità locale a cui si riferisce la trasmissione dei dati | [optional] 
**sito_trasportatore_per_conto_produttore** | [**TrasmissioneDatiSitoResult**](TrasmissioneDatiSitoResult.md) | Eventuale unità locale del trasportatore che ha provveduto ad trasmettere i dati per conto del produttore | [optional] 
**numero_fir** | **str** | Numero FIR del formulario trasmesso | [optional] 
**user_name** | **str** | Identificazione dell&#39;utente o soggetto che ha eseguito la trasmissione | [optional] 
**data_trasmissione** | **datetime** | Data in cui è stata effettuata la trasmissione (Formato ISO 8601 UTC) | [optional] 
**data_emissione** | **datetime** | Data emissione del formulario trasmesso (Formato ISO 8601 UTC) | [optional] 
**tipo** | [**TipoTrasmissione**](TipoTrasmissione.md) | Modalità con cui è avvenuta la trasmissione dei dati | [optional] 
**stato** | [**StatiTrasmissioneDati**](StatiTrasmissioneDati.md) | Stato della trasmissione | [optional] 
**formulario** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md) | Dati del formulario inviati con la trasmissione | [optional] 

## Example

```python
from rentri_formulari.models.trasmissione_dati_result import TrasmissioneDatiResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasmissioneDatiResult from a JSON string
trasmissione_dati_result_instance = TrasmissioneDatiResult.from_json(json)
# print the JSON string representation of the object
print(TrasmissioneDatiResult.to_json())

# convert the object into a dict
trasmissione_dati_result_dict = trasmissione_dati_result_instance.to_dict()
# create an instance of TrasmissioneDatiResult from a dict
trasmissione_dati_result_from_dict = TrasmissioneDatiResult.from_dict(trasmissione_dati_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


