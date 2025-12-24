# StatusResponse

Risposta di stato dell'API

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**StatusResponseEnum**](StatusResponseEnum.md) | Stato dell&#39;API&lt;p&gt;Valori ammessi:&lt;ul style&#x3D;\&quot;margin:0\&quot;&gt;&lt;li&gt;&lt;i&gt;Ok&lt;/i&gt; - API regolarmente funzionante&lt;/li&gt;&lt;li&gt;&lt;i&gt;Warning&lt;/i&gt; - API funzionante, ma con probabili disservizi come indicato nei warning&lt;/li&gt;&lt;/ul&gt;&lt;/p&gt; | [optional] 
**warnings** | **List[str]** | Eventuali messaggi di warning relativi allo stato dell&#39;API | [optional] 

## Example

```python
from rentri_formulari.models.status_response import StatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StatusResponse from a JSON string
status_response_instance = StatusResponse.from_json(json)
# print the JSON string representation of the object
print(StatusResponse.to_json())

# convert the object into a dict
status_response_dict = status_response_instance.to_dict()
# create an instance of StatusResponse from a dict
status_response_from_dict = StatusResponse.from_dict(status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


