# PlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**full_name** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**username** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**short_address** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**longitude** | **float** |  | [optional] 
**gender** | **str** |  | [optional] 
**age** | **int** |  | [optional] 
**hand** | **str** |  | [optional] 
**image_url** | **str** |  | [optional] 
**ratings** | [**PlayerRatingResponse**](PlayerRatingResponse.md) | Ratings data | [optional] 
**invited** | **bool** |  | [optional] 
**distance** | **str** |  | [optional] 
**enable_privacy** | **bool** |  | 
**distance_in_miles** | **float** |  | [optional] 
**is_logged_in_user** | **bool** |  | [optional] 
**partner_status** | **str** |  | [optional] 
**team_status** | **str** |  | [optional] 
**is_player1** | **bool** |  | 
**registration_details** | [**RegistrationResponse**](RegistrationResponse.md) |  | 
**phone** | **str** |  | [optional] 
**email** | **str** |  | 
**verified_email** | **bool** |  | [optional] 
**registration_type** | **str** |  | 
**registered** | **bool** |  | 
**dupr_id** | **str** |  | 
**show_rating_banner** | **bool** |  | 
**status** | **str** |  | [optional] 
**sponsor** | [**SponsorLogoResponse**](SponsorLogoResponse.md) |  | [optional] 
**substitution_details** | [**List[PlayerResponse]**](PlayerResponse.md) |  | [optional] 
**is_substitute** | **bool** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**substitute** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.player_response import PlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerResponse from a JSON string
player_response_instance = PlayerResponse.from_json(json)
# print the JSON string representation of the object
print(PlayerResponse.to_json())

# convert the object into a dict
player_response_dict = player_response_instance.to_dict()
# create an instance of PlayerResponse from a dict
player_response_from_dict = PlayerResponse.from_dict(player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


