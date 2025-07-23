# LeagueFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**skill_level** | [**SkillLevelFilter**](SkillLevelFilter.md) |  | [optional] 
**elimination** | **List[str]** |  | [optional] 
**event_format** | **List[str]** |  | [optional] 
**player_group** | **List[str]** |  | [optional] 
**city** | **List[str]** |  | [optional] 
**status** | **List[str]** |  | [optional] 
**duration_status** | **List[str]** |  | [optional] 
**registration_status** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.league_filter import LeagueFilter

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueFilter from a JSON string
league_filter_instance = LeagueFilter.from_json(json)
# print the JSON string representation of the object
print(LeagueFilter.to_json())

# convert the object into a dict
league_filter_dict = league_filter_instance.to_dict()
# create an instance of LeagueFilter from a dict
league_filter_from_dict = LeagueFilter.from_dict(league_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


