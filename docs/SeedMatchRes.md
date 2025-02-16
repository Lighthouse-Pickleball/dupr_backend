# SeedMatchRes


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bye** | **bool** |  | [optional] 
**match_serial** | **int** |  | [optional] 
**serial** | **int** |  | 
**team1** | [**LeagueTeamsRes**](LeagueTeamsRes.md) |  | [optional] 
**team2** | [**LeagueTeamsRes**](LeagueTeamsRes.md) |  | [optional] 

## Example

```python
from dupr_backend.models.seed_match_res import SeedMatchRes

# TODO update the JSON string below
json = "{}"
# create an instance of SeedMatchRes from a JSON string
seed_match_res_instance = SeedMatchRes.from_json(json)
# print the JSON string representation of the object
print SeedMatchRes.to_json()

# convert the object into a dict
seed_match_res_dict = seed_match_res_instance.to_dict()
# create an instance of SeedMatchRes from a dict
seed_match_res_form_dict = seed_match_res.from_dict(seed_match_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


