# DatiPartenzaModel

Dati di partenza del formulario

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**numero_fir** | **str** | Numero di vidimazione da attribuire al nuovo FIR digitale. Qualora non venga specificato, il sistema ne assegnerà uno automaticamente. | [optional] 
**produttore** | [**DatiPartenzaModelProduttore**](DatiPartenzaModelProduttore.md) |  | [optional] 
**destinatario** | [**DatiPartenzaModelDestinatario**](DatiPartenzaModelDestinatario.md) |  | 
**trasportatori** | [**List[DatiPartenzaModelTrasportatoriInner]**](DatiPartenzaModelTrasportatoriInner.md) | Trasportatori | 
**intermediari** | [**List[DatiIntermediariFormularioModel]**](DatiIntermediariFormularioModel.md) | Intermediari | [optional] 
**rifiuto** | [**DatiRifiutoModel**](DatiRifiutoModel.md) | Caratteristiche del rifiuto | 
**trasbordo_parziale_origine** | [**DatiTrasbordoParzialeOrigineModel**](DatiTrasbordoParzialeOrigineModel.md) | Dati relativi al trasbordo parziale da cui prende origine il formulario. Il dato deve essere valorizzato solo se il formulario prende origine da un trasbordo parziale. Se il dato viene valorizzato, la proprietà \&quot;produttore\&quot; non deve essere valorizzata. | [optional] 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_partenza_model import DatiPartenzaModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPartenzaModel from a JSON string
dati_partenza_model_instance = DatiPartenzaModel.from_json(json)
# print the JSON string representation of the object
print DatiPartenzaModel.to_json()

# convert the object into a dict
dati_partenza_model_dict = dati_partenza_model_instance.to_dict()
# create an instance of DatiPartenzaModel from a dict
dati_partenza_model_from_dict = DatiPartenzaModel.from_dict(dati_partenza_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


