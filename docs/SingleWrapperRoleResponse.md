# SingleWrapperRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**RoleResponse**](RoleResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_role_response import SingleWrapperRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperRoleResponse from a JSON string
single_wrapper_role_response_instance = SingleWrapperRoleResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperRoleResponse.to_json())

# convert the object into a dict
single_wrapper_role_response_dict = single_wrapper_role_response_instance.to_dict()
# create an instance of SingleWrapperRoleResponse from a dict
single_wrapper_role_response_from_dict = SingleWrapperRoleResponse.from_dict(single_wrapper_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


