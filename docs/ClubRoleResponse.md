# ClubRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role_id** | **int** |  | 
**role** | **str** |  | 

## Example

```python
from dupr_backend.models.club_role_response import ClubRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRoleResponse from a JSON string
club_role_response_instance = ClubRoleResponse.from_json(json)
# print the JSON string representation of the object
print(ClubRoleResponse.to_json())

# convert the object into a dict
club_role_response_dict = club_role_response_instance.to_dict()
# create an instance of ClubRoleResponse from a dict
club_role_response_from_dict = ClubRoleResponse.from_dict(club_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


