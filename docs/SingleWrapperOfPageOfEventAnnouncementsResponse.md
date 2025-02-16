# SingleWrapperOfPageOfEventAnnouncementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfEventAnnouncementsResponse**](PageOfEventAnnouncementsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_event_announcements_response import SingleWrapperOfPageOfEventAnnouncementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfEventAnnouncementsResponse from a JSON string
single_wrapper_of_page_of_event_announcements_response_instance = SingleWrapperOfPageOfEventAnnouncementsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfEventAnnouncementsResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_event_announcements_response_dict = single_wrapper_of_page_of_event_announcements_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfEventAnnouncementsResponse from a dict
single_wrapper_of_page_of_event_announcements_response_from_dict = SingleWrapperOfPageOfEventAnnouncementsResponse.from_dict(single_wrapper_of_page_of_event_announcements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


