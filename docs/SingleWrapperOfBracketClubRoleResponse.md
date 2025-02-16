# SingleWrapperOfBracketClubRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**BracketClubRoleResponse**](BracketClubRoleResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_bracket_club_role_response import SingleWrapperOfBracketClubRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfBracketClubRoleResponse from a JSON string
single_wrapper_of_bracket_club_role_response_instance = SingleWrapperOfBracketClubRoleResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfBracketClubRoleResponse.to_json())

# convert the object into a dict
single_wrapper_of_bracket_club_role_response_dict = single_wrapper_of_bracket_club_role_response_instance.to_dict()
# create an instance of SingleWrapperOfBracketClubRoleResponse from a dict
single_wrapper_of_bracket_club_role_response_from_dict = SingleWrapperOfBracketClubRoleResponse.from_dict(single_wrapper_of_bracket_club_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


