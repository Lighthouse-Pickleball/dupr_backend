# OpenPlayEventWaitlist


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event_id** | **int** |  | 
**message** | **str** |  | [optional] 
**waitlist_position** | **int** |  | 

## Example

```python
from dupr_backend.models.open_play_event_waitlist import OpenPlayEventWaitlist

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayEventWaitlist from a JSON string
open_play_event_waitlist_instance = OpenPlayEventWaitlist.from_json(json)
# print the JSON string representation of the object
print OpenPlayEventWaitlist.to_json()

# convert the object into a dict
open_play_event_waitlist_dict = open_play_event_waitlist_instance.to_dict()
# create an instance of OpenPlayEventWaitlist from a dict
open_play_event_waitlist_form_dict = open_play_event_waitlist.from_dict(open_play_event_waitlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


