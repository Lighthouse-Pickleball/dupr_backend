# SingleWrapperOpenPlayEventWaitlist


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**OpenPlayEventWaitlist**](OpenPlayEventWaitlist.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_open_play_event_waitlist import SingleWrapperOpenPlayEventWaitlist

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOpenPlayEventWaitlist from a JSON string
single_wrapper_open_play_event_waitlist_instance = SingleWrapperOpenPlayEventWaitlist.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOpenPlayEventWaitlist.to_json())

# convert the object into a dict
single_wrapper_open_play_event_waitlist_dict = single_wrapper_open_play_event_waitlist_instance.to_dict()
# create an instance of SingleWrapperOpenPlayEventWaitlist from a dict
single_wrapper_open_play_event_waitlist_from_dict = SingleWrapperOpenPlayEventWaitlist.from_dict(single_wrapper_open_play_event_waitlist_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


