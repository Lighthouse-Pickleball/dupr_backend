# ConfirmTeamRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**registration_id** | **int** |  | 

## Example

```python
from dupr_backend.models.confirm_team_request import ConfirmTeamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmTeamRequest from a JSON string
confirm_team_request_instance = ConfirmTeamRequest.from_json(json)
# print the JSON string representation of the object
print ConfirmTeamRequest.to_json()

# convert the object into a dict
confirm_team_request_dict = confirm_team_request_instance.to_dict()
# create an instance of ConfirmTeamRequest from a dict
confirm_team_request_form_dict = confirm_team_request.from_dict(confirm_team_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


