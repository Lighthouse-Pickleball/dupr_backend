# SingleWrapperPageClubMemberResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageClubMemberResponse**](PageClubMemberResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_club_member_response import SingleWrapperPageClubMemberResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageClubMemberResponse from a JSON string
single_wrapper_page_club_member_response_instance = SingleWrapperPageClubMemberResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageClubMemberResponse.to_json())

# convert the object into a dict
single_wrapper_page_club_member_response_dict = single_wrapper_page_club_member_response_instance.to_dict()
# create an instance of SingleWrapperPageClubMemberResponse from a dict
single_wrapper_page_club_member_response_from_dict = SingleWrapperPageClubMemberResponse.from_dict(single_wrapper_page_club_member_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


