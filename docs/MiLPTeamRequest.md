# MiLPTeamRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**team_name** | **str** |  | 
**team_captain_dupr_id** | **str** |  | 
**team_members_dupr_ids** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.mi_lp_team_request import MiLPTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPTeamRequest from a JSON string
mi_lp_team_request_instance = MiLPTeamRequest.from_json(json)
# print the JSON string representation of the object
print(MiLPTeamRequest.to_json())

# convert the object into a dict
mi_lp_team_request_dict = mi_lp_team_request_instance.to_dict()
# create an instance of MiLPTeamRequest from a dict
mi_lp_team_request_from_dict = MiLPTeamRequest.from_dict(mi_lp_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


