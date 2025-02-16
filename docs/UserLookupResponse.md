# UserLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**birthdate** | **date** |  | [optional] 
**created** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**external_id** | **str** |  | [optional] 
**full_name** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**is_valid_email** | **bool** |  | [optional] 
**is_valid_phone** | **bool** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**registered** | **bool** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**role** | [**RoleResponse**](RoleResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.user_lookup_response import UserLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserLookupResponse from a JSON string
user_lookup_response_instance = UserLookupResponse.from_json(json)
# print the JSON string representation of the object
print(UserLookupResponse.to_json())

# convert the object into a dict
user_lookup_response_dict = user_lookup_response_instance.to_dict()
# create an instance of UserLookupResponse from a dict
user_lookup_response_from_dict = UserLookupResponse.from_dict(user_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


