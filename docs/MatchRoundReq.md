# MatchRoundReq


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** |  | [optional] 
**matches** | [**List[SeedMatchReq]**](SeedMatchReq.md) |  | 
**serial** | **int** |  | 
**start_date** | **date** |  | 
**team_ids** | **List[int]** |  | [optional] 

## Example

```python
from dupr_backend.models.match_round_req import MatchRoundReq

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRoundReq from a JSON string
match_round_req_instance = MatchRoundReq.from_json(json)
# print the JSON string representation of the object
print(MatchRoundReq.to_json())

# convert the object into a dict
match_round_req_dict = match_round_req_instance.to_dict()
# create an instance of MatchRoundReq from a dict
match_round_req_from_dict = MatchRoundReq.from_dict(match_round_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


