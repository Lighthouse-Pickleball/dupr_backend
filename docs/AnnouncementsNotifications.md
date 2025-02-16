# AnnouncementsNotifications


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**announcement_id** | **int** |  | [optional] 
**bracket_id** | **int** |  | [optional] 
**email_sent** | **bool** |  | [optional] 
**league_id** | **int** |  | [optional] 
**push_sent** | **bool** |  | [optional] 
**sms_sent** | **bool** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.announcements_notifications import AnnouncementsNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementsNotifications from a JSON string
announcements_notifications_instance = AnnouncementsNotifications.from_json(json)
# print the JSON string representation of the object
print AnnouncementsNotifications.to_json()

# convert the object into a dict
announcements_notifications_dict = announcements_notifications_instance.to_dict()
# create an instance of AnnouncementsNotifications from a dict
announcements_notifications_form_dict = announcements_notifications.from_dict(announcements_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


