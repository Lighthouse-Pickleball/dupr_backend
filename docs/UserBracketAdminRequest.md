# UserBracketAdminRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**user_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.user_bracket_admin_request import UserBracketAdminRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserBracketAdminRequest from a JSON string
user_bracket_admin_request_instance = UserBracketAdminRequest.from_json(json)
# print the JSON string representation of the object
print UserBracketAdminRequest.to_json()

# convert the object into a dict
user_bracket_admin_request_dict = user_bracket_admin_request_instance.to_dict()
# create an instance of UserBracketAdminRequest from a dict
user_bracket_admin_request_form_dict = user_bracket_admin_request.from_dict(user_bracket_admin_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


