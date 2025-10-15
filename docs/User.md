# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**full_name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**email** | **str** |  | 
**is_valid_email** | **bool** |  | [optional] 
**secret** | **str** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**is_valid_phone** | **bool** |  | [optional] 
**nickname** | **str** |  | [optional] 
**display_username** | **bool** |  | 
**media_id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**hand** | **str** |  | [optional] 
**role** | [**Role**](Role.md) |  | [optional] 
**customer_key** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**external_id** | **str** |  | [optional] 
**restricted** | **bool** |  | [optional] 
**reliability_score** | **int** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**is_enabled** | **bool** |  | 
**password** | **str** |  | 
**authorities** | [**List[GrantedAuthority]**](GrantedAuthority.md) |  | 
**is_account_non_expired** | **bool** |  | 
**is_account_non_locked** | **bool** |  | 
**is_credentials_non_expired** | **bool** |  | 
**username** | **str** |  | 
**is_admin** | **bool** |  | 
**valid_email** | **bool** |  | [optional] 
**valid_phone** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


