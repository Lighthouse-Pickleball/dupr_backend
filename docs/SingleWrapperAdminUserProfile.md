# SingleWrapperAdminUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**AdminUserProfile**](AdminUserProfile.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_admin_user_profile import SingleWrapperAdminUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperAdminUserProfile from a JSON string
single_wrapper_admin_user_profile_instance = SingleWrapperAdminUserProfile.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperAdminUserProfile.to_json())

# convert the object into a dict
single_wrapper_admin_user_profile_dict = single_wrapper_admin_user_profile_instance.to_dict()
# create an instance of SingleWrapperAdminUserProfile from a dict
single_wrapper_admin_user_profile_from_dict = SingleWrapperAdminUserProfile.from_dict(single_wrapper_admin_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


