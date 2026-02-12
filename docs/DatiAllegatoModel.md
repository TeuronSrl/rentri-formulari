# DatiAllegatoModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_type** | **str** | Tipo del documento Valori ammessi: “application/pdf” | 
**nome_file** | **str** | Nome del file | 
**contenuto** | **bytearray** | Contenuto del file. Il contenuto non deve suepere 1 MB di dimensione. La dimensione massima dell&#39;xFIR risultante non dovrà superare i 3 MB a seguito dell&#39;aggiunta dell&#39;allegato. | 
**identificativo_soggetto** | **str** | Codice fiscale del soggetto, tra quelli indicati nel formulario, a cui è da riferirsi l&#39;allegato | 
**descrizione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_allegato_model import DatiAllegatoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAllegatoModel from a JSON string
dati_allegato_model_instance = DatiAllegatoModel.from_json(json)
# print the JSON string representation of the object
print DatiAllegatoModel.to_json()

# convert the object into a dict
dati_allegato_model_dict = dati_allegato_model_instance.to_dict()
# create an instance of DatiAllegatoModel from a dict
dati_allegato_model_from_dict = DatiAllegatoModel.from_dict(dati_allegato_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


