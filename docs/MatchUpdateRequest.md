# MatchUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_source** | **str** |  | 
**match_id** | **int** |  | 
**requested_by** | **str** |  | 
**reason** | **str** |  | 
**league_id** | **int** |  | [optional] 
**bracket_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**venue** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**league** | **str** |  | [optional] 
**event_date** | **date** |  | [optional] 
**confirmed** | **bool** |  | [optional] 
**teams** | [**List[TeamUpdateRequest]**](TeamUpdateRequest.md) |  | 
**created** | **datetime** |  | [optional] 
**event_name** | **str** |  | [optional] 
**player_ids** | **List[int]** |  | 

## Example

```python
from dupr_backend.models.match_update_request import MatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchUpdateRequest from a JSON string
match_update_request_instance = MatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MatchUpdateRequest.to_json())

# convert the object into a dict
match_update_request_dict = match_update_request_instance.to_dict()
# create an instance of MatchUpdateRequest from a dict
match_update_request_from_dict = MatchUpdateRequest.from_dict(match_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


