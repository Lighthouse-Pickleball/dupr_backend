# SingleWrapperBracketClubRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**BracketClubRoleResponse**](BracketClubRoleResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_bracket_club_role_response import SingleWrapperBracketClubRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperBracketClubRoleResponse from a JSON string
single_wrapper_bracket_club_role_response_instance = SingleWrapperBracketClubRoleResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperBracketClubRoleResponse.to_json())

# convert the object into a dict
single_wrapper_bracket_club_role_response_dict = single_wrapper_bracket_club_role_response_instance.to_dict()
# create an instance of SingleWrapperBracketClubRoleResponse from a dict
single_wrapper_bracket_club_role_response_from_dict = SingleWrapperBracketClubRoleResponse.from_dict(single_wrapper_bracket_club_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


