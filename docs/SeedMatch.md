# SeedMatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **int** |  | 
**team1** | [**LeagueTeams**](LeagueTeams.md) |  | [optional] 
**team2** | [**LeagueTeams**](LeagueTeams.md) |  | [optional] 
**bye** | **bool** |  | 
**match_serial** | **int** |  | 

## Example

```python
from dupr_backend.models.seed_match import SeedMatch

# TODO update the JSON string below
json = "{}"
# create an instance of SeedMatch from a JSON string
seed_match_instance = SeedMatch.from_json(json)
# print the JSON string representation of the object
print(SeedMatch.to_json())

# convert the object into a dict
seed_match_dict = seed_match_instance.to_dict()
# create an instance of SeedMatch from a dict
seed_match_from_dict = SeedMatch.from_dict(seed_match_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


