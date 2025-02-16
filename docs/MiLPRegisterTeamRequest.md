# MiLPRegisterTeamRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**division_id** | **int** |  | [optional] 
**event_id** | **int** |  | [optional] 
**team_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.mi_lp_register_team_request import MiLPRegisterTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MiLPRegisterTeamRequest from a JSON string
mi_lp_register_team_request_instance = MiLPRegisterTeamRequest.from_json(json)
# print the JSON string representation of the object
print MiLPRegisterTeamRequest.to_json()

# convert the object into a dict
mi_lp_register_team_request_dict = mi_lp_register_team_request_instance.to_dict()
# create an instance of MiLPRegisterTeamRequest from a dict
mi_lp_register_team_request_form_dict = mi_lp_register_team_request.from_dict(mi_lp_register_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


