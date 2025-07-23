# MatchRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **int** |  | 
**matches** | [**List[SeedMatch]**](SeedMatch.md) |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | [optional] 
**team_ids** | **List[int]** |  | [optional] 

## Example

```python
from dupr_backend.models.match_round import MatchRound

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRound from a JSON string
match_round_instance = MatchRound.from_json(json)
# print the JSON string representation of the object
print(MatchRound.to_json())

# convert the object into a dict
match_round_dict = match_round_instance.to_dict()
# create an instance of MatchRound from a dict
match_round_from_dict = MatchRound.from_dict(match_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


