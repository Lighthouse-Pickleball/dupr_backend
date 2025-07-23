# SingleWrapperPageEventAnnouncementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageEventAnnouncementsResponse**](PageEventAnnouncementsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_event_announcements_response import SingleWrapperPageEventAnnouncementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageEventAnnouncementsResponse from a JSON string
single_wrapper_page_event_announcements_response_instance = SingleWrapperPageEventAnnouncementsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageEventAnnouncementsResponse.to_json())

# convert the object into a dict
single_wrapper_page_event_announcements_response_dict = single_wrapper_page_event_announcements_response_instance.to_dict()
# create an instance of SingleWrapperPageEventAnnouncementsResponse from a dict
single_wrapper_page_event_announcements_response_from_dict = SingleWrapperPageEventAnnouncementsResponse.from_dict(single_wrapper_page_event_announcements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


