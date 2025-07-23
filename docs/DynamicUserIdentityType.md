# DynamicUserIdentityType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input** | **str** |  | [optional] 
**type** | **str** |  | 

## Example

```python
from dupr_backend.models.dynamic_user_identity_type import DynamicUserIdentityType

# TODO update the JSON string below
json = "{}"
# create an instance of DynamicUserIdentityType from a JSON string
dynamic_user_identity_type_instance = DynamicUserIdentityType.from_json(json)
# print the JSON string representation of the object
print(DynamicUserIdentityType.to_json())

# convert the object into a dict
dynamic_user_identity_type_dict = dynamic_user_identity_type_instance.to_dict()
# create an instance of DynamicUserIdentityType from a dict
dynamic_user_identity_type_from_dict = DynamicUserIdentityType.from_dict(dynamic_user_identity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


