# RatingLeaderboardRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_player_age** | **int** |  | 
**max_player_age** | **int** |  | 
**rating_type** | **str** |  | 
**gender** | **str** |  | 
**country** | **str** |  | 
**state** | **str** |  | 
**limit** | **int** |  | 

## Example

```python
from dupr_backend.models.rating_leaderboard_request import RatingLeaderboardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RatingLeaderboardRequest from a JSON string
rating_leaderboard_request_instance = RatingLeaderboardRequest.from_json(json)
# print the JSON string representation of the object
print(RatingLeaderboardRequest.to_json())

# convert the object into a dict
rating_leaderboard_request_dict = rating_leaderboard_request_instance.to_dict()
# create an instance of RatingLeaderboardRequest from a dict
rating_leaderboard_request_from_dict = RatingLeaderboardRequest.from_dict(rating_leaderboard_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


