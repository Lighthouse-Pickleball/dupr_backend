# LeagueTeams


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registration_id** | **int** |  | 
**player1** | [**Player**](Player.md) |  | [optional] 
**player2** | [**Player**](Player.md) |  | [optional] 
**team_status** | **str** |  | [optional] 
**partner_status** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_teams import LeagueTeams

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueTeams from a JSON string
league_teams_instance = LeagueTeams.from_json(json)
# print the JSON string representation of the object
print(LeagueTeams.to_json())

# convert the object into a dict
league_teams_dict = league_teams_instance.to_dict()
# create an instance of LeagueTeams from a dict
league_teams_from_dict = LeagueTeams.from_dict(league_teams_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


