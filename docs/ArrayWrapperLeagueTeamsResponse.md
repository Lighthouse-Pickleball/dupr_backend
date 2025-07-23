# ArrayWrapperLeagueTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[LeagueTeamsResponse]**](LeagueTeamsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_league_teams_response import ArrayWrapperLeagueTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperLeagueTeamsResponse from a JSON string
array_wrapper_league_teams_response_instance = ArrayWrapperLeagueTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperLeagueTeamsResponse.to_json())

# convert the object into a dict
array_wrapper_league_teams_response_dict = array_wrapper_league_teams_response_instance.to_dict()
# create an instance of ArrayWrapperLeagueTeamsResponse from a dict
array_wrapper_league_teams_response_from_dict = ArrayWrapperLeagueTeamsResponse.from_dict(array_wrapper_league_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


