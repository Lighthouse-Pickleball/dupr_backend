# SingleWrapperOfPageOfClubResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfClubResponse**](PageOfClubResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_club_response import SingleWrapperOfPageOfClubResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfClubResponse from a JSON string
single_wrapper_of_page_of_club_response_instance = SingleWrapperOfPageOfClubResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfClubResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_club_response_dict = single_wrapper_of_page_of_club_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfClubResponse from a dict
single_wrapper_of_page_of_club_response_from_dict = SingleWrapperOfPageOfClubResponse.from_dict(single_wrapper_of_page_of_club_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


