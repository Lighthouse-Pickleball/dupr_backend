# LeagueMatchConfirmRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_match_id** | **int** |  | [optional] 
**match_id** | **int** |  | 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueMatchConfirmRequest from a JSON string
league_match_confirm_request_instance = LeagueMatchConfirmRequest.from_json(json)
# print the JSON string representation of the object
print LeagueMatchConfirmRequest.to_json()

# convert the object into a dict
league_match_confirm_request_dict = league_match_confirm_request_instance.to_dict()
# create an instance of LeagueMatchConfirmRequest from a dict
league_match_confirm_request_form_dict = league_match_confirm_request.from_dict(league_match_confirm_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


