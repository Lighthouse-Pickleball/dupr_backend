# UnclaimedPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age** | **int** |  | [optional] 
**claimed** | **bool** |  | 
**fullname** | **str** |  | 
**gender** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**ratings** | [**RatingsUnclaimedPlayerResponse**](RatingsUnclaimedPlayerResponse.md) |  | 
**referral_code** | **str** |  | [optional] 
**short_address** | **str** |  | [optional] 
**sponsor** | [**SponsorLogoResponse**](SponsorLogoResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.unclaimed_player_response import UnclaimedPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UnclaimedPlayerResponse from a JSON string
unclaimed_player_response_instance = UnclaimedPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(UnclaimedPlayerResponse.to_json())

# convert the object into a dict
unclaimed_player_response_dict = unclaimed_player_response_instance.to_dict()
# create an instance of UnclaimedPlayerResponse from a dict
unclaimed_player_response_from_dict = UnclaimedPlayerResponse.from_dict(unclaimed_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


