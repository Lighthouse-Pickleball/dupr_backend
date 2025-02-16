# PlayerSignUpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | 
**ambassador_code** | **str** |  | [optional] 
**birthdate** | **date** |  | 
**client_key** | **str** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**doubles_rating** | **float** |  | [optional] 
**email** | **str** |  | 
**enable_newsletter** | **bool** |  | 
**first_name** | **str** |  | 
**full_name** | **str** |  | 
**gender** | **str** |  | 
**hand** | **str** |  | 
**identifier** | **str** | An unique identifier of this user from your platform | [optional] 
**iso_code** | **str** |  | [optional] 
**last_name** | **str** |  | 
**media_id** | **int** |  | [optional] 
**password** | **str** |  | 
**phone** | **str** |  | [optional] 
**singles_rating** | **float** |  | [optional] 
**user_id** | **int** |  | [optional] 
**username** | **str** |  | [optional] 

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


