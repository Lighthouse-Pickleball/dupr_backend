# PageEventAnnouncementsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[EventAnnouncementsResponse]**](EventAnnouncementsResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**empty** | **bool** | Are results empty | 
**has_previous** | **bool** | Is there any previous page | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_event_announcements_response import PageEventAnnouncementsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageEventAnnouncementsResponse from a JSON string
page_event_announcements_response_instance = PageEventAnnouncementsResponse.from_json(json)
# print the JSON string representation of the object
print(PageEventAnnouncementsResponse.to_json())

# convert the object into a dict
page_event_announcements_response_dict = page_event_announcements_response_instance.to_dict()
# create an instance of PageEventAnnouncementsResponse from a dict
page_event_announcements_response_from_dict = PageEventAnnouncementsResponse.from_dict(page_event_announcements_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


