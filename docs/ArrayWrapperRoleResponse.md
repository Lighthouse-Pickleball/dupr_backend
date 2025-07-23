# ArrayWrapperRoleResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[RoleResponse]**](RoleResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_role_response import ArrayWrapperRoleResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperRoleResponse from a JSON string
array_wrapper_role_response_instance = ArrayWrapperRoleResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperRoleResponse.to_json())

# convert the object into a dict
array_wrapper_role_response_dict = array_wrapper_role_response_instance.to_dict()
# create an instance of ArrayWrapperRoleResponse from a dict
array_wrapper_role_response_from_dict = ArrayWrapperRoleResponse.from_dict(array_wrapper_role_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


