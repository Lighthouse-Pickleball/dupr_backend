# MatchRoundRes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **date** |  | [optional] 
**matches** | [**List[SeedMatchRes]**](SeedMatchRes.md) |  | 
**serial** | **int** |  | 
**start_date** | **date** |  | 
**team_ids** | **List[int]** |  | [optional] 

## Example

```python
from dupr_backend.models.match_round_res import MatchRoundRes

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRoundRes from a JSON string
match_round_res_instance = MatchRoundRes.from_json(json)
# print the JSON string representation of the object
print(MatchRoundRes.to_json())

# convert the object into a dict
match_round_res_dict = match_round_res_instance.to_dict()
# create an instance of MatchRoundRes from a dict
match_round_res_from_dict = MatchRoundRes.from_dict(match_round_res_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


