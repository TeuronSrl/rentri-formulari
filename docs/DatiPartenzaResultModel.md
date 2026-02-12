# DatiPartenzaResultModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_emissione** | **datetime** | Data di emissione del formulario | [optional] 
**produttore** | [**DatiProduttoreFormularioResultModel**](DatiProduttoreFormularioResultModel.md) | Dati del produttore | [optional] 
**destinatario** | [**DatiDestinatarioFormularioResultModel**](DatiDestinatarioFormularioResultModel.md) | Dati del destinatario | [optional] 
**trasportatori** | [**List[DatiTrasportatoreFormularioResultModel]**](DatiTrasportatoreFormularioResultModel.md) | Dati dei trasportatori | [optional] 
**intermediari** | [**List[DatiIntermediariFormularioModel]**](DatiIntermediariFormularioModel.md) | Dati degli intermediari | [optional] 
**rifiuto** | [**DatiRifiutoModel**](DatiRifiutoModel.md) | Dati del rifiuto | [optional] 
**trasbordo_parziale_origine** | [**DatiTrasbordoParzialeOrigineResultModel**](DatiTrasbordoParzialeOrigineResultModel.md) | Dati del produttore originario indicato nel caso di creazione del formulario a seguito di un trasbordo parziale | [optional] 
**dati_firma_produttore** | [**DatiFirmaResult**](DatiFirmaResult.md) | Dati relativi alla firma del produttore | [optional] 
**numero_fir** | **str** | Numero di vidimazione da attribuire al nuovo FIR digitale. Qualora non venga specificato, il sistema ne assegnerà uno automaticamente. | [optional] 
**annotazioni** | **str** | Annotazioni | [optional] 

## Example

```python
from rentri_formulari.models.dati_partenza_result_model import DatiPartenzaResultModel

# TODO update the JSON string below
json = "{}"
# create an instance of DatiPartenzaResultModel from a JSON string
dati_partenza_result_model_instance = DatiPartenzaResultModel.from_json(json)
# print the JSON string representation of the object
print DatiPartenzaResultModel.to_json()

# convert the object into a dict
dati_partenza_result_model_dict = dati_partenza_result_model_instance.to_dict()
# create an instance of DatiPartenzaResultModel from a dict
dati_partenza_result_model_from_dict = DatiPartenzaResultModel.from_dict(dati_partenza_result_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


