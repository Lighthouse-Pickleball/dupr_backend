# Player


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**full_name** | **str** |  | 
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | 
**email** | **str** |  | 
**verified_email** | **bool** |  | 
**iso_alpha2_code** | **str** |  | [optional] 
**phone** | **str** |  | [optional] 
**verified_phone** | **bool** |  | 
**short_address** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**gender** | **str** |  | [optional] 
**birthdate** | **date** |  | [optional] 
**age** | **int** |  | [optional] 
**hand** | **str** |  | [optional] 
**reliability_score** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**singles** | **float** |  | [optional] 
**singles_verified** | **float** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**doubles** | **float** |  | [optional] 
**doubles_verified** | **float** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**registration_type** | **str** |  | [optional] 
**registered** | **bool** |  | 
**referral_code** | **str** |  | [optional] 
**sponsor** | [**Sponsor**](Sponsor.md) |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**enable_privacy** | **bool** |  | 
**status** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**singles_reliability** | **float** |  | [optional] 
**doubles_reliability** | **float** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 
**provisional_doubles_rating** | **float** |  | [optional] 
**location** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.player import Player

# TODO update the JSON string below
json = "{}"
# create an instance of Player from a JSON string
player_instance = Player.from_json(json)
# print the JSON string representation of the object
print(Player.to_json())

# convert the object into a dict
player_dict = player_instance.to_dict()
# create an instance of Player from a dict
player_from_dict = Player.from_dict(player_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


