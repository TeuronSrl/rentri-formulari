# QuantitaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**valore** | **float** | Quantità (parte intera: 10, parte decimale: 4) compresa tra 0.0000 e 9999999999.9999. | 
**unita_misura** | [**UnitaMisura**](UnitaMisura.md) | Unità di misura della quantità  Vedi API di codifica: &lt;i&gt;GET /codifiche/v1.0/unita-misura&lt;/i&gt;&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;kg&lt;/i&gt; - Chilogrammi&lt;/li&gt;&lt;li&gt;&lt;i&gt;l&lt;/i&gt; - Litri&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 

## Example

```python
from rentri_formulari.models.quantita_model import QuantitaModel

# TODO update the JSON string below
json = "{}"
# create an instance of QuantitaModel from a JSON string
quantita_model_instance = QuantitaModel.from_json(json)
# print the JSON string representation of the object
print QuantitaModel.to_json()

# convert the object into a dict
quantita_model_dict = quantita_model_instance.to_dict()
# create an instance of QuantitaModel from a dict
quantita_model_from_dict = QuantitaModel.from_dict(quantita_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


