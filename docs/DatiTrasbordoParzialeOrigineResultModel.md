# DatiTrasbordoParzialeOrigineResultModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir_origine** | **str** |  | [optional] 
**produttore_originario** | [**DatiProduttoreOriginarioModel**](DatiProduttoreOriginarioModel.md) |  | [optional] 
**causale** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasbordo_parziale_origine_result_model import DatiTrasbordoParzialeOrigineResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasbordoParzialeOrigineResultModel from a JSON string
dati_trasbordo_parziale_origine_result_model_instance = DatiTrasbordoParzialeOrigineResultModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasbordoParzialeOrigineResultModel.to_json())

# convert the object into a dict
dati_trasbordo_parziale_origine_result_model_dict = dati_trasbordo_parziale_origine_result_model_instance.to_dict()
# create an instance of DatiTrasbordoParzialeOrigineResultModel from a dict
dati_trasbordo_parziale_origine_result_model_from_dict = DatiTrasbordoParzialeOrigineResultModel.from_dict(dati_trasbordo_parziale_origine_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


