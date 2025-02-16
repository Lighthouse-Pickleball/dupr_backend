# AdminUserProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**full_name** | **str** |  | 
**iso_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.admin_user_profile import AdminUserProfile

# TODO update the JSON string below
json = "{}"
# create an instance of AdminUserProfile from a JSON string
admin_user_profile_instance = AdminUserProfile.from_json(json)
# print the JSON string representation of the object
print AdminUserProfile.to_json()

# convert the object into a dict
admin_user_profile_dict = admin_user_profile_instance.to_dict()
# create an instance of AdminUserProfile from a dict
admin_user_profile_form_dict = admin_user_profile.from_dict(admin_user_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


