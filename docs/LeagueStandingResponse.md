# LeagueStandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**registration_id** | **int** |  | 
**round** | **int** |  | 
**match_won** | **int** |  | 
**match_lost** | **int** |  | 
**game_won** | **int** |  | 
**game_lost** | **int** |  | 
**points_scored** | **int** |  | 
**points_conceded** | **int** |  | 
**point_difference** | **int** |  | 
**point_diff_percentage** | **float** |  | 
**player1** | [**PlayerResponse**](PlayerResponse.md) |  | [optional] 
**player2** | [**PlayerResponse**](PlayerResponse.md) |  | [optional] 
**rank** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.league_standing_response import LeagueStandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueStandingResponse from a JSON string
league_standing_response_instance = LeagueStandingResponse.from_json(json)
# print the JSON string representation of the object
print(LeagueStandingResponse.to_json())

# convert the object into a dict
league_standing_response_dict = league_standing_response_instance.to_dict()
# create an instance of LeagueStandingResponse from a dict
league_standing_response_from_dict = LeagueStandingResponse.from_dict(league_standing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


