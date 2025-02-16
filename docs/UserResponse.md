# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **bool** |  | 
**addresses** | [**List[AddressResponse]**](AddressResponse.md) |  | [optional] 
**apparel_brand** | **str** |  | [optional] 
**birthdate** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**email** | **str** |  | 
**first_name** | **str** |  | 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | 
**image_url** | **str** |  | [optional] 
**is_valid_email** | **bool** |  | [optional] 
**is_valid_phone** | **bool** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**last_name** | **str** |  | 
**lucra_connected** | **bool** |  | [optional] 
**paddle_brand** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**preferred_ball** | **str** |  | [optional] 
**preferred_side** | **str** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**role** | [**RoleResponse**](RoleResponse.md) |  | [optional] 
**shoe_brand** | **str** |  | [optional] 
**stats** | [**PlayerRatingResponse**](PlayerRatingResponse.md) |  | [optional] 
**user_preferences** | [**UserPreferencesResponse**](UserPreferencesResponse.md) |  | [optional] 
**username** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.user_response import UserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserResponse from a JSON string
user_response_instance = UserResponse.from_json(json)
# print the JSON string representation of the object
print(UserResponse.to_json())

# convert the object into a dict
user_response_dict = user_response_instance.to_dict()
# create an instance of UserResponse from a dict
user_response_from_dict = UserResponse.from_dict(user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


