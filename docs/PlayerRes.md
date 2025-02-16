# PlayerRes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**birthdate** | **str** |  | [optional] 
**created** | **str** |  | [optional] 
**default_rating** | **str** |  | [optional] 
**display_username** | **bool** |  | 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**doubles** | **float** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**doubles_reliability** | **float** |  | [optional] 
**doubles_verified** | **float** |  | [optional] 
**email** | **str** |  | 
**enable_privacy** | **bool** |  | 
**first_name** | **str** |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**full_name** | **str** |  | 
**gender** | **str** |  | [optional] 
**hand** | **str** |  | [optional] 
**id** | **int** |  | 
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
**registered** | **bool** |  | 
**registration_type** | **str** |  | [optional] 
**reliability_score** | **int** |  | [optional] 
**short_address** | **str** |  | [optional] 
**singles** | **float** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**singles_reliability** | **float** |  | [optional] 
**singles_verified** | **float** |  | [optional] 
**sponsor** | [**SponsorRes**](SponsorRes.md) |  | [optional] 
**status** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**verified_email** | **bool** |  | 
**verified_phone** | **bool** |  | 

## Example

```python
from dupr_backend.models.player_res import PlayerRes

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRes from a JSON string
player_res_instance = PlayerRes.from_json(json)
# print the JSON string representation of the object
print PlayerRes.to_json()

# convert the object into a dict
player_res_dict = player_res_instance.to_dict()
# create an instance of PlayerRes from a dict
player_res_form_dict = player_res.from_dict(player_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


