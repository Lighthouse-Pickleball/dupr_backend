# BracketClubRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | 
**is_club_member** | **bool** |  | 
**role_name** | **str** |  | 

## Example

```python
from dupr_backend.models.bracket_club_role_response import BracketClubRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BracketClubRoleResponse from a JSON string
bracket_club_role_response_instance = BracketClubRoleResponse.from_json(json)
# print the JSON string representation of the object
print(BracketClubRoleResponse.to_json())

# convert the object into a dict
bracket_club_role_response_dict = bracket_club_role_response_instance.to_dict()
# create an instance of BracketClubRoleResponse from a dict
bracket_club_role_response_from_dict = BracketClubRoleResponse.from_dict(bracket_club_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


