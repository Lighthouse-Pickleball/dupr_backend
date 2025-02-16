# BracketTeamSort


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order** | **str** |  | [optional] 
**parameter** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_team_sort import BracketTeamSort

# TODO update the JSON string below
json = "{}"
# create an instance of BracketTeamSort from a JSON string
bracket_team_sort_instance = BracketTeamSort.from_json(json)
# print the JSON string representation of the object
print BracketTeamSort.to_json()

# convert the object into a dict
bracket_team_sort_dict = bracket_team_sort_instance.to_dict()
# create an instance of BracketTeamSort from a dict
bracket_team_sort_form_dict = bracket_team_sort.from_dict(bracket_team_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


