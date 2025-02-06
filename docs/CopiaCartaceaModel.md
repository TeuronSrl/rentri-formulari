# CopiaCartaceaModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_content** | **bytearray** | Contenuto del file che rappresenta la copia cartacea del formulario codificato in base64 | 
**nome_file** | **str** | Nome del file | 
**mime** | **str** | Tipo MIME del file da caricare | 
**numero_fir** | **str** | Numero del FIR cartaceo, rilasciato al momento della vidimazione | 
**data_emissione** | **datetime** | Data emissione del formulario cartaceo (formato ISO 8601 UTC) È necessario specificare una data antecedente o uguale alla data corrente | 
**produttore** | [**CopiaCartaceaSoggettoInfo**](CopiaCartaceaSoggettoInfo.md) | Dati del produttore a cui si rende disponibile la copia cartacea | 
**trasportatori** | [**List[CopiaCartaceaSoggettoInfo]**](CopiaCartaceaSoggettoInfo.md) |  | [optional] 
**intermediari** | [**List[CopiaCartaceaSoggettoInfo]**](CopiaCartaceaSoggettoInfo.md) |  | [optional] 
**note** | **str** | Eventuali note riguardanti la copia cartacea | [optional] 

## Example

```python
from rentri_formulari.models.copia_cartacea_model import CopiaCartaceaModel

# TODO update the JSON string below
json = "{}"
# create an instance of CopiaCartaceaModel from a JSON string
copia_cartacea_model_instance = CopiaCartaceaModel.from_json(json)
# print the JSON string representation of the object
print CopiaCartaceaModel.to_json()

# convert the object into a dict
copia_cartacea_model_dict = copia_cartacea_model_instance.to_dict()
# create an instance of CopiaCartaceaModel from a dict
copia_cartacea_model_from_dict = CopiaCartaceaModel.from_dict(copia_cartacea_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


