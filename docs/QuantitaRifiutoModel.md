# QuantitaRifiutoModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quantita** | [**QuantitaModel**](QuantitaModel.md) | Quantità | 
**verificato_in_partenza** | **bool** | Verificato in partenza | [optional] 
**numero_colli** | **str** | Numero di colli.  Specificare un valore in caso non si imposti \&quot;rinfusa\&quot; a &lt;i&gt;true&lt;/i&gt; | [optional] 
**rinfusa** | **bool** | Rinfusa.  Se valorizzato a &lt;i&gt;true&lt;/i&gt; indica che il rifiuto non è partizionato in colli. | [optional] 

## Example

```python
from rentri_formulari.models.quantita_rifiuto_model import QuantitaRifiutoModel

# TODO update the JSON string below
json = "{}"
# create an instance of QuantitaRifiutoModel from a JSON string
quantita_rifiuto_model_instance = QuantitaRifiutoModel.from_json(json)
# print the JSON string representation of the object
print QuantitaRifiutoModel.to_json()

# convert the object into a dict
quantita_rifiuto_model_dict = quantita_rifiuto_model_instance.to_dict()
# create an instance of QuantitaRifiutoModel from a dict
quantita_rifiuto_model_from_dict = QuantitaRifiutoModel.from_dict(quantita_rifiuto_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


