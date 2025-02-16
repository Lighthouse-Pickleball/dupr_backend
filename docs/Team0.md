# Team0


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delta** | **float** |  | [optional] 
**game1** | **int** |  | [optional] 
**game2** | **int** |  | [optional] 
**game3** | **int** |  | [optional] 
**game4** | **int** |  | [optional] 
**game5** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**league_match_team_id** | **int** |  | [optional] 
**player1** | [**Player**](Player.md) |  | [optional] 
**player1_doubles_rating** | **float** |  | [optional] 
**player1_singles_rating** | **float** |  | [optional] 
**player2** | [**Player**](Player.md) |  | [optional] 
**player2_doubles_rating** | **float** |  | [optional] 
**player2_singles_rating** | **float** |  | [optional] 
**player_ids** | **List[int]** |  | 
**pre_match_rating_and_impact** | [**PreMatchRatingAndImpact**](PreMatchRatingAndImpact.md) |  | [optional] 
**priority** | **int** |  | 
**team_player1** | [**TeamPlayer**](TeamPlayer.md) |  | [optional] 
**team_player2** | [**TeamPlayer**](TeamPlayer.md) |  | [optional] 
**team_rating** | **float** |  | [optional] 
**winner** | **bool** |  | 

## Example

```python
from dupr_backend.models.team0 import Team0

# TODO update the JSON string below
json = "{}"
# create an instance of Team0 from a JSON string
team0_instance = Team0.from_json(json)
# print the JSON string representation of the object
print Team0.to_json()

# convert the object into a dict
team0_dict = team0_instance.to_dict()
# create an instance of Team0 from a dict
team0_form_dict = team0.from_dict(team0_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


