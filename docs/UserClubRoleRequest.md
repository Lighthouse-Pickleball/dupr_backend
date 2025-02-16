# UserClubRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.user_club_role_request import UserClubRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserClubRoleRequest from a JSON string
user_club_role_request_instance = UserClubRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UserClubRoleRequest.to_json())

# convert the object into a dict
user_club_role_request_dict = user_club_role_request_instance.to_dict()
# create an instance of UserClubRoleRequest from a dict
user_club_role_request_from_dict = UserClubRoleRequest.from_dict(user_club_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


