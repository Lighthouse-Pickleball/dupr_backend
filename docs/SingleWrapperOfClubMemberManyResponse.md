# SingleWrapperOfClubMemberManyResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**ClubMemberManyResponse**](ClubMemberManyResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_club_member_many_response import SingleWrapperOfClubMemberManyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfClubMemberManyResponse from a JSON string
single_wrapper_of_club_member_many_response_instance = SingleWrapperOfClubMemberManyResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfClubMemberManyResponse.to_json()

# convert the object into a dict
single_wrapper_of_club_member_many_response_dict = single_wrapper_of_club_member_many_response_instance.to_dict()
# create an instance of SingleWrapperOfClubMemberManyResponse from a dict
single_wrapper_of_club_member_many_response_form_dict = single_wrapper_of_club_member_many_response.from_dict(single_wrapper_of_club_member_many_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


