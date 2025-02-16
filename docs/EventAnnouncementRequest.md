# EventAnnouncementRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_id** | **int** |  | 
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**description** | [**AnnouncementContent**](AnnouncementContent.md) |  | 
**league_id** | **int** |  | 
**title** | **str** |  | 

## Example

```python
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventAnnouncementRequest from a JSON string
event_announcement_request_instance = EventAnnouncementRequest.from_json(json)
# print the JSON string representation of the object
print EventAnnouncementRequest.to_json()

# convert the object into a dict
event_announcement_request_dict = event_announcement_request_instance.to_dict()
# create an instance of EventAnnouncementRequest from a dict
event_announcement_request_form_dict = event_announcement_request.from_dict(event_announcement_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


