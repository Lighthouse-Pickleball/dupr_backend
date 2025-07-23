# PlayerProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**iso_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**gender** | **str** |  | 
**birthdate** | **date** |  | 
**hand** | **str** |  | 
**default_rating** | **str** |  | 
**address_id** | **int** |  | 
**media_id** | **int** |  | [optional] 
**paddle_brand** | **str** |  | [optional] 
**shoe_brand** | **str** |  | [optional] 
**apparel_brand** | **str** |  | [optional] 
**preferred_ball** | **str** |  | [optional] 
**preferred_side** | **str** |  | [optional] 
**place_id** | **str** |  | [optional] 
**is_valid_phone** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.player_profile_request import PlayerProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerProfileRequest from a JSON string
player_profile_request_instance = PlayerProfileRequest.from_json(json)
# print the JSON string representation of the object
print(PlayerProfileRequest.to_json())

# convert the object into a dict
player_profile_request_dict = player_profile_request_instance.to_dict()
# create an instance of PlayerProfileRequest from a dict
player_profile_request_from_dict = PlayerProfileRequest.from_dict(player_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


