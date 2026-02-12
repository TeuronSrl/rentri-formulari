# ValidazioneXfirResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**formulario** | [**DettaglioFormulario**](DettaglioFormulario.md) |  | [optional] 
**formulario_presente_in_rentri** | **bool** | Indica se un formulario con lo stesso Numero FIR è presente nell&#39;area virtuale di interscambio RENTRI | [optional] 
**formulario_aggiornato_in_rentri** | **bool** | Se il formulario è già presente nell&#39;area di interscambio RENTRI, quando valorizzato a true indica che lo stato di avanzamento del file validato è lo stesso della versione presente in RENTRI | [optional] 
**formato** | [**List[ControlloFormatoResult]**](ControlloFormatoResult.md) | Lista dei controlli effettuati riguardanti il formato del file validato | [optional] 
**var_schema** | [**List[ControlloSchemaResult]**](ControlloSchemaResult.md) | Lista dei controlli effettuati riguardanti lo schema dei file XML, e l&#39;integrità referenziale dei dati presenti | [optional] 
**firme** | [**List[ControlloFirmeResult]**](ControlloFirmeResult.md) | Lista dei controlli effettuati riguardanti le firme digitali presenti nel file | [optional] 
**vidimazione** | [**List[ControlloVidimazioneResult]**](ControlloVidimazioneResult.md) | Lista dei controlli sul file di vidimazione del FIR e sul suo stato | [optional] 
**valido** | **bool** | Dato riassuntivo sulla presenza di controlli che segnalano errori bloccanti | [optional] 

## Example

```python
from rentri_formulari.models.validazione_xfir_result import ValidazioneXfirResult

# TODO update the JSON string below
json = "{}"
# create an instance of ValidazioneXfirResult from a JSON string
validazione_xfir_result_instance = ValidazioneXfirResult.from_json(json)
# print the JSON string representation of the object
print ValidazioneXfirResult.to_json()

# convert the object into a dict
validazione_xfir_result_dict = validazione_xfir_result_instance.to_dict()
# create an instance of ValidazioneXfirResult from a dict
validazione_xfir_result_from_dict = ValidazioneXfirResult.from_dict(validazione_xfir_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


