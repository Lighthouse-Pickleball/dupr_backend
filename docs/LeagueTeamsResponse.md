# LeagueTeamsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_status** | **str** |  | [optional] 
**player1** | [**PlayerResponse**](PlayerResponse.md) |  | 
**player2** | [**PlayerResponse**](PlayerResponse.md) |  | [optional] 
**registration_id** | **int** |  | 
**team_status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_teams_response import LeagueTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueTeamsResponse from a JSON string
league_teams_response_instance = LeagueTeamsResponse.from_json(json)
# print the JSON string representation of the object
print LeagueTeamsResponse.to_json()

# convert the object into a dict
league_teams_response_dict = league_teams_response_instance.to_dict()
# create an instance of LeagueTeamsResponse from a dict
league_teams_response_form_dict = league_teams_response.from_dict(league_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


