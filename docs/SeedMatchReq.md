# SeedMatchReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bye** | **bool** |  | [optional] 
**match_serial** | **int** |  | [optional] 
**serial** | **int** |  | 
**team1** | [**LeagueTeamsReq**](LeagueTeamsReq.md) |  | [optional] 
**team2** | [**LeagueTeamsReq**](LeagueTeamsReq.md) |  | [optional] 

## Example

```python
from dupr_backend.models.seed_match_req import SeedMatchReq

# TODO update the JSON string below
json = "{}"
# create an instance of SeedMatchReq from a JSON string
seed_match_req_instance = SeedMatchReq.from_json(json)
# print the JSON string representation of the object
print(SeedMatchReq.to_json())

# convert the object into a dict
seed_match_req_dict = seed_match_req_instance.to_dict()
# create an instance of SeedMatchReq from a dict
seed_match_req_from_dict = SeedMatchReq.from_dict(seed_match_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


