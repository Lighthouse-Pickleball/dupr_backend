# PlayerSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**iso_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**password** | **str** |  | 
**ambassador_code** | **str** |  | [optional] 
**media_id** | **int** |  | [optional] 
**gender** | **str** |  | 
**birthdate** | **date** |  | 
**address_id** | **int** |  | 
**hand** | **str** |  | 
**singles_rating** | **float** |  | [optional] 
**doubles_rating** | **float** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**enable_newsletter** | **bool** |  | 
**username** | **str** |  | [optional] 
**user_id** | **int** |  | [optional] 
**client_key** | **str** |  | [optional] 
**identifier** | **str** | An unique identifier of this user from your platform | [optional] 
**marketing_opt_in** | **bool** |  | [optional] 
**terms_of_service** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.player_sign_up_request import PlayerSignUpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerSignUpRequest from a JSON string
player_sign_up_request_instance = PlayerSignUpRequest.from_json(json)
# print the JSON string representation of the object
print(PlayerSignUpRequest.to_json())

# convert the object into a dict
player_sign_up_request_dict = player_sign_up_request_instance.to_dict()
# create an instance of PlayerSignUpRequest from a dict
player_sign_up_request_from_dict = PlayerSignUpRequest.from_dict(player_sign_up_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


