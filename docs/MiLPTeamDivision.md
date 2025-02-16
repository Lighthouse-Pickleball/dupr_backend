# MiLPTeamDivision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**division_type** | **str** |  | 
**teams** | [**List[MiLPTeam]**](MiLPTeam.md) |  | 

## Example

```python
from dupr_backend.models.mi_lp_team_division import MiLPTeamDivision

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPTeamDivision from a JSON string
mi_lp_team_division_instance = MiLPTeamDivision.from_json(json)
# print the JSON string representation of the object
print(MiLPTeamDivision.to_json())

# convert the object into a dict
mi_lp_team_division_dict = mi_lp_team_division_instance.to_dict()
# create an instance of MiLPTeamDivision from a dict
mi_lp_team_division_from_dict = MiLPTeamDivision.from_dict(mi_lp_team_division_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


