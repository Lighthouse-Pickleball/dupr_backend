# AnnouncementsNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_id** | **int** |  | 
**league_id** | **int** |  | 
**bracket_id** | **int** |  | [optional] 
**user_id** | **int** |  | 
**email_sent** | **bool** |  | 
**push_sent** | **bool** |  | 
**sms_sent** | **bool** |  | 

## Example

```python
from dupr_backend.models.announcements_notifications import AnnouncementsNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementsNotifications from a JSON string
announcements_notifications_instance = AnnouncementsNotifications.from_json(json)
# print the JSON string representation of the object
print(AnnouncementsNotifications.to_json())

# convert the object into a dict
announcements_notifications_dict = announcements_notifications_instance.to_dict()
# create an instance of AnnouncementsNotifications from a dict
announcements_notifications_from_dict = AnnouncementsNotifications.from_dict(announcements_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


