# AnalisiClassificazioneModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tipo** | [**TipoAnalisiClassificazione**](TipoAnalisiClassificazione.md) | &lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Analisi&lt;/i&gt; - Analisi/rapporto di prova&lt;/li&gt;&lt;li&gt;&lt;i&gt;Classificazione&lt;/i&gt; - Classificazione&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | 
**numero** | **str** |  | 
**data** | **datetime** |  | [optional] 

## Example

```python
from rentri_formulari.models.analisi_classificazione_model import AnalisiClassificazioneModel

# TODO update the JSON string below
json = "{}"
# create an instance of AnalisiClassificazioneModel from a JSON string
analisi_classificazione_model_instance = AnalisiClassificazioneModel.from_json(json)
# print the JSON string representation of the object
print(AnalisiClassificazioneModel.to_json())

# convert the object into a dict
analisi_classificazione_model_dict = analisi_classificazione_model_instance.to_dict()
# create an instance of AnalisiClassificazioneModel from a dict
analisi_classificazione_model_from_dict = AnalisiClassificazioneModel.from_dict(analisi_classificazione_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


