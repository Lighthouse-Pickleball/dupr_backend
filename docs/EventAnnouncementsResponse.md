# EventAnnouncementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_id** | **int** |  | 
**league_id** | **int** |  | 
**bracket_id** | **int** |  | 
**title** | **str** |  | 
**description** | [**ContentResponse**](ContentResponse.md) |  | [optional] 
**status** | **str** |  | 
**email_sent** | **int** |  | 
**email_failed** | **int** |  | 
**push_sent** | **int** |  | 
**push_failed** | **int** |  | 
**sms_sent** | **int** |  | 
**sms_failed** | **int** |  | 
**created** | **str** |  | 
**registered_members** | **int** |  | [optional] 
**notification_count** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.event_announcements_response import EventAnnouncementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EventAnnouncementsResponse from a JSON string
event_announcements_response_instance = EventAnnouncementsResponse.from_json(json)
# print the JSON string representation of the object
print(EventAnnouncementsResponse.to_json())

# convert the object into a dict
event_announcements_response_dict = event_announcements_response_instance.to_dict()
# create an instance of EventAnnouncementsResponse from a dict
event_announcements_response_from_dict = EventAnnouncementsResponse.from_dict(event_announcements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


