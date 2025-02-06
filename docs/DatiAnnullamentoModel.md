# DatiAnnullamentoModel

Dati richiesti per l'annullamento di un FIR

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**note** | **str** | Note di annullamento | 
**codice_fiscale_soggetto** | **str** | Codice fiscale del soggetto. | 

## Example

```python
from rentri_formulari.models.dati_annullamento_model import DatiAnnullamentoModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiAnnullamentoModel from a JSON string
dati_annullamento_model_instance = DatiAnnullamentoModel.from_json(json)
# print the JSON string representation of the object
print DatiAnnullamentoModel.to_json()

# convert the object into a dict
dati_annullamento_model_dict = dati_annullamento_model_instance.to_dict()
# create an instance of DatiAnnullamentoModel from a dict
dati_annullamento_model_from_dict = DatiAnnullamentoModel.from_dict(dati_annullamento_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


