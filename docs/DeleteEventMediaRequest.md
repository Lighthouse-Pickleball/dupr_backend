# DeleteEventMediaRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **int** |  | 
**liability_waiver_id** | **int** |  | [optional] 
**media_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.delete_event_media_request import DeleteEventMediaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteEventMediaRequest from a JSON string
delete_event_media_request_instance = DeleteEventMediaRequest.from_json(json)
# print the JSON string representation of the object
print DeleteEventMediaRequest.to_json()

# convert the object into a dict
delete_event_media_request_dict = delete_event_media_request_instance.to_dict()
# create an instance of DeleteEventMediaRequest from a dict
delete_event_media_request_form_dict = delete_event_media_request.from_dict(delete_event_media_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


