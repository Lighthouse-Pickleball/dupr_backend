# UserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**full_name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**is_valid_phone** | **bool** |  | [optional] 
**email** | **str** |  | 
**is_valid_email** | **bool** |  | [optional] 
**image_url** | **str** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**role** | [**RoleResponse**](RoleResponse.md) |  | [optional] 
**stats** | [**PlayerRatingResponse**](PlayerRatingResponse.md) |  | [optional] 
**addresses** | [**List[AddressResponse]**](AddressResponse.md) |  | [optional] 
**active** | **bool** |  | 
**user_preferences** | [**UserPreferencesResponse**](UserPreferencesResponse.md) |  | [optional] 
**paddle_brand** | **str** |  | [optional] 
**shoe_brand** | **str** |  | [optional] 
**apparel_brand** | **str** |  | [optional] 
**preferred_ball** | **str** |  | [optional] 
**preferred_side** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**valid_email** | **bool** |  | [optional] 
**valid_phone** | **bool** |  | [optional] 

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


