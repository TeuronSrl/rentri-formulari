# TrasmissioneDatiSitoResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_iscr_sito** | **str** | Numero iscrizione dell&#39;unità locale | [optional] 
**codice_fiscale** | **str** | Identificativo del soggetto | [optional] 
**denominazione** | **str** | Denominazione del soggettto | [optional] 
**comune_id** | **str** | Codice ISTAT comune dell&#39;unità locale del soggetto | [optional] 
**indirizzo** | **str** | Indirizzo dell&#39;unità locale del soggetto | [optional] 
**civico** | **str** | Numero civico dell&#39;unità locale del soggetto | [optional] 

## Example

```python
from rentri_formulari.models.trasmissione_dati_sito_result import TrasmissioneDatiSitoResult

# TODO update the JSON string below
json = "{}"
# create an instance of TrasmissioneDatiSitoResult from a JSON string
trasmissione_dati_sito_result_instance = TrasmissioneDatiSitoResult.from_json(json)
# print the JSON string representation of the object
print(TrasmissioneDatiSitoResult.to_json())

# convert the object into a dict
trasmissione_dati_sito_result_dict = trasmissione_dati_sito_result_instance.to_dict()
# create an instance of TrasmissioneDatiSitoResult from a dict
trasmissione_dati_sito_result_from_dict = TrasmissioneDatiSitoResult.from_dict(trasmissione_dati_sito_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


