# AnnouncementHistoryRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**league_id** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 

## Example

```python
from dupr_backend.models.announcement_history_request import AnnouncementHistoryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementHistoryRequest from a JSON string
announcement_history_request_instance = AnnouncementHistoryRequest.from_json(json)
# print the JSON string representation of the object
print AnnouncementHistoryRequest.to_json()

# convert the object into a dict
announcement_history_request_dict = announcement_history_request_instance.to_dict()
# create an instance of AnnouncementHistoryRequest from a dict
announcement_history_request_form_dict = announcement_history_request.from_dict(announcement_history_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


