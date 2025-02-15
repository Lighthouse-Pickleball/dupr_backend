# ForfeitMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**club_id** | **int** |  | 
**league_match_id** | **int** |  | 
**match_id** | **int** |  | 
**team1** | [**ForfeitTeamRequest**](ForfeitTeamRequest.md) |  | 
**team2** | [**ForfeitTeamRequest**](ForfeitTeamRequest.md) |  | 

## Example

```python
from dupr_backend.models.forfeit_match_request import ForfeitMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ForfeitMatchRequest from a JSON string
forfeit_match_request_instance = ForfeitMatchRequest.from_json(json)
# print the JSON string representation of the object
print(ForfeitMatchRequest.to_json())

# convert the object into a dict
forfeit_match_request_dict = forfeit_match_request_instance.to_dict()
# create an instance of ForfeitMatchRequest from a dict
forfeit_match_request_from_dict = ForfeitMatchRequest.from_dict(forfeit_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


