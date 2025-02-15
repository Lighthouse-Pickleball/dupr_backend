# MiLPTeam


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**team_code** | **str** |  | [optional] 
**team_id** | **int** |  | 
**team_members** | [**List[TeamMember]**](TeamMember.md) |  | 
**team_name** | **str** |  | 

## Example

```python
from dupr_backend.models.mi_lp_team import MiLPTeam

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPTeam from a JSON string
mi_lp_team_instance = MiLPTeam.from_json(json)
# print the JSON string representation of the object
print(MiLPTeam.to_json())

# convert the object into a dict
mi_lp_team_dict = mi_lp_team_instance.to_dict()
# create an instance of MiLPTeam from a dict
mi_lp_team_from_dict = MiLPTeam.from_dict(mi_lp_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


