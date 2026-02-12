# DatiPerFirmaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**certificato** | **str** | Certificato in base64 | 
**tipo_firma** | [**TipoFirma**](TipoFirma.md) | Indica i dati del formulario che si intendono firmare. Il dato è richiesto solo quando non può essere dedotto dal contesto, in particolare quando il formulario è nello stato di attesa delle firme sia del  produttore che del trasportatore, ed il chiamante ha visibilità su entrambi i soggetti. In tutti gli altri casi il valore eventualmente specificato viene ignorato.&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Produttore&lt;/i&gt; - Da indicare quando il produttore intende firmare il formulario alla partenza.&lt;/li&gt;&lt;li&gt;&lt;i&gt;Trasportatore&lt;/i&gt; - Da indicare quando il trasportatore intende firmare il formulario alla partenza.&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 

## Example

```python
from rentri_formulari.models.dati_per_firma_model import DatiPerFirmaModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPerFirmaModel from a JSON string
dati_per_firma_model_instance = DatiPerFirmaModel.from_json(json)
# print the JSON string representation of the object
print DatiPerFirmaModel.to_json()

# convert the object into a dict
dati_per_firma_model_dict = dati_per_firma_model_instance.to_dict()
# create an instance of DatiPerFirmaModel from a dict
dati_per_firma_model_from_dict = DatiPerFirmaModel.from_dict(dati_per_firma_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


