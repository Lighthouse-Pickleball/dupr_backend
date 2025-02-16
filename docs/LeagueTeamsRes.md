# LeagueTeamsRes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner_status** | **str** |  | [optional] 
**payment_status** | **str** |  | [optional] 
**player1** | [**PlayerRes**](PlayerRes.md) |  | [optional] 
**player2** | [**PlayerRes**](PlayerRes.md) |  | [optional] 
**registration_id** | **int** |  | 
**team_status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_teams_res import LeagueTeamsRes

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueTeamsRes from a JSON string
league_teams_res_instance = LeagueTeamsRes.from_json(json)
# print the JSON string representation of the object
print LeagueTeamsRes.to_json()

# convert the object into a dict
league_teams_res_dict = league_teams_res_instance.to_dict()
# create an instance of LeagueTeamsRes from a dict
league_teams_res_form_dict = league_teams_res.from_dict(league_teams_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


