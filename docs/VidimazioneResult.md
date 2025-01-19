# VidimazioneResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**codice_fiscale** | **str** |  | [optional] 
**denominazione** | **str** |  | [optional] 

## Example

```python
from rentri_formulari.models.vidimazione_result import VidimazioneResult

# TODO update the JSON string below
json = "{}"
# create an instance of VidimazioneResult from a JSON string
vidimazione_result_instance = VidimazioneResult.from_json(json)
# print the JSON string representation of the object
print(VidimazioneResult.to_json())

# convert the object into a dict
vidimazione_result_dict = vidimazione_result_instance.to_dict()
# create an instance of VidimazioneResult from a dict
vidimazione_result_from_dict = VidimazioneResult.from_dict(vidimazione_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


