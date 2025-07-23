# UserBracketAdminRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | [optional] 
**email** | **str** |  | [optional] 
**dupr_id** | **str** |  | [optional] 
**offset** | **int** |  | 
**limit** | **int** |  | 

## Example

```python
from dupr_backend.models.user_bracket_admin_request import UserBracketAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserBracketAdminRequest from a JSON string
user_bracket_admin_request_instance = UserBracketAdminRequest.from_json(json)
# print the JSON string representation of the object
print(UserBracketAdminRequest.to_json())

# convert the object into a dict
user_bracket_admin_request_dict = user_bracket_admin_request_instance.to_dict()
# create an instance of UserBracketAdminRequest from a dict
user_bracket_admin_request_from_dict = UserBracketAdminRequest.from_dict(user_bracket_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


