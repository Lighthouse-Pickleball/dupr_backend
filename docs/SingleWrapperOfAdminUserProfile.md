# SingleWrapperOfAdminUserProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**AdminUserProfile**](AdminUserProfile.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_admin_user_profile import SingleWrapperOfAdminUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfAdminUserProfile from a JSON string
single_wrapper_of_admin_user_profile_instance = SingleWrapperOfAdminUserProfile.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfAdminUserProfile.to_json()

# convert the object into a dict
single_wrapper_of_admin_user_profile_dict = single_wrapper_of_admin_user_profile_instance.to_dict()
# create an instance of SingleWrapperOfAdminUserProfile from a dict
single_wrapper_of_admin_user_profile_form_dict = single_wrapper_of_admin_user_profile.from_dict(single_wrapper_of_admin_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


