# BracketSearchTeamsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**only_non_wait_listed** | **bool** |  | [optional] 
**only_wait_listed** | **bool** |  | [optional] 
**sort** | [**BracketTeamSort**](BracketTeamSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_search_teams_request import BracketSearchTeamsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketSearchTeamsRequest from a JSON string
bracket_search_teams_request_instance = BracketSearchTeamsRequest.from_json(json)
# print the JSON string representation of the object
print(BracketSearchTeamsRequest.to_json())

# convert the object into a dict
bracket_search_teams_request_dict = bracket_search_teams_request_instance.to_dict()
# create an instance of BracketSearchTeamsRequest from a dict
bracket_search_teams_request_from_dict = BracketSearchTeamsRequest.from_dict(bracket_search_teams_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


