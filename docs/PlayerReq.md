# PlayerReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**birthdate** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**display_username** | **bool** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**doubles** | **float** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**doubles_reliability** | **float** |  | [optional] 
**doubles_verified** | **float** |  | [optional] 
**email** | **str** |  | 
**enable_privacy** | **bool** |  | [optional] 
**first_name** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**iso_alpha2_code** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**latitude** | **float** |  | [optional] 
**location** | **str** |  | [optional] 
**longitude** | **float** |  | [optional] 
**lucra_connected** | **bool** |  | [optional] 
**phone** | **str** |  | [optional] 
**provisional_doubles_rating** | **float** |  | [optional] 
**provisional_singles_rating** | **float** |  | [optional] 
**referral_code** | **str** |  | [optional] 
**registered** | **bool** |  | [optional] 
**registration_type** | **str** |  | [optional] 
**reliability_score** | **int** |  | [optional] 
**short_address** | **str** |  | [optional] 
**singles** | **float** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**singles_reliability** | **float** |  | [optional] 
**singles_verified** | **float** |  | [optional] 
**sponsor** | [**SponsorReq**](SponsorReq.md) |  | [optional] 
**status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified_email** | **bool** |  | [optional] 
**verified_phone** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.player_req import PlayerReq

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerReq from a JSON string
player_req_instance = PlayerReq.from_json(json)
# print the JSON string representation of the object
print(PlayerReq.to_json())

# convert the object into a dict
player_req_dict = player_req_instance.to_dict()
# create an instance of PlayerReq from a dict
player_req_from_dict = PlayerReq.from_dict(player_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


