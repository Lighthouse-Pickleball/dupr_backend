# AdminUserProfile


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **int** |  | 
**dupr_id** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**full_name** | **str** |  | 
**email** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**iso_code** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.admin_user_profile import AdminUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserProfile from a JSON string
admin_user_profile_instance = AdminUserProfile.from_json(json)
# print the JSON string representation of the object
print(AdminUserProfile.to_json())

# convert the object into a dict
admin_user_profile_dict = admin_user_profile_instance.to_dict()
# create an instance of AdminUserProfile from a dict
admin_user_profile_from_dict = AdminUserProfile.from_dict(admin_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


