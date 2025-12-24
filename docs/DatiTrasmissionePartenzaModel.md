# DatiTrasmissionePartenzaModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** |  | 
**produttore** | [**DatiProduttoreTrasmissioneModel**](DatiProduttoreTrasmissioneModel.md) |  | [optional] 
**trasbordo_parziale_origine** | [**DatiTrasbordoParzialeOrigineModel**](DatiTrasbordoParzialeOrigineModel.md) |  | [optional] 
**destinatario** | [**DatiDestinatarioTrasmissioneModel**](DatiDestinatarioTrasmissioneModel.md) |  | 
**trasportatori** | [**List[DatiTrasportatoreTrasmissioneModel]**](DatiTrasportatoreTrasmissioneModel.md) |  | 
**data_emissione** | **datetime** |  | 
**intermediari** | [**List[DatiIntermediariFormularioModel]**](DatiIntermediariFormularioModel.md) | Intermediari | [optional] 
**rifiuto** | [**DatiRifiutoModel**](DatiRifiutoModel.md) | Caratteristiche del rifiuto | 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_trasmissione_partenza_model import DatiTrasmissionePartenzaModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiTrasmissionePartenzaModel from a JSON string
dati_trasmissione_partenza_model_instance = DatiTrasmissionePartenzaModel.from_json(json)
# print the JSON string representation of the object
print(DatiTrasmissionePartenzaModel.to_json())

# convert the object into a dict
dati_trasmissione_partenza_model_dict = dati_trasmissione_partenza_model_instance.to_dict()
# create an instance of DatiTrasmissionePartenzaModel from a dict
dati_trasmissione_partenza_model_from_dict = DatiTrasmissionePartenzaModel.from_dict(dati_trasmissione_partenza_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


