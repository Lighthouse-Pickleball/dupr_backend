# RatingsUnclaimedPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | **str** |  | [optional] 
**doubles_provisional** | **bool** |  | [optional] 
**doubles_verified** | **str** |  | [optional] 
**singles** | **str** |  | [optional] 
**singles_provisional** | **bool** |  | [optional] 
**singles_verified** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.ratings_unclaimed_player_response import RatingsUnclaimedPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatingsUnclaimedPlayerResponse from a JSON string
ratings_unclaimed_player_response_instance = RatingsUnclaimedPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(RatingsUnclaimedPlayerResponse.to_json())

# convert the object into a dict
ratings_unclaimed_player_response_dict = ratings_unclaimed_player_response_instance.to_dict()
# create an instance of RatingsUnclaimedPlayerResponse from a dict
ratings_unclaimed_player_response_from_dict = RatingsUnclaimedPlayerResponse.from_dict(ratings_unclaimed_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


