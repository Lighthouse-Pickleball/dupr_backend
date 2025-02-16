# SingleWrapperOfPageOfClubMemberResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfClubMemberResponse**](PageOfClubMemberResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_club_member_response import SingleWrapperOfPageOfClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfClubMemberResponse from a JSON string
single_wrapper_of_page_of_club_member_response_instance = SingleWrapperOfPageOfClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfPageOfClubMemberResponse.to_json()

# convert the object into a dict
single_wrapper_of_page_of_club_member_response_dict = single_wrapper_of_page_of_club_member_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfClubMemberResponse from a dict
single_wrapper_of_page_of_club_member_response_form_dict = single_wrapper_of_page_of_club_member_response.from_dict(single_wrapper_of_page_of_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


