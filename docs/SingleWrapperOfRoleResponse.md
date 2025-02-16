# SingleWrapperOfRoleResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**RoleResponse**](RoleResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_role_response import SingleWrapperOfRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfRoleResponse from a JSON string
single_wrapper_of_role_response_instance = SingleWrapperOfRoleResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfRoleResponse.to_json()

# convert the object into a dict
single_wrapper_of_role_response_dict = single_wrapper_of_role_response_instance.to_dict()
# create an instance of SingleWrapperOfRoleResponse from a dict
single_wrapper_of_role_response_form_dict = single_wrapper_of_role_response.from_dict(single_wrapper_of_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


