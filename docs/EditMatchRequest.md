# EditMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | [optional] 
**is_forfeited** | **bool** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**match_date** | **date** |  | 
**match_id** | **int** |  | 
**team1_score** | [**EditScoreRequest**](EditScoreRequest.md) |  | 
**team2_score** | [**EditScoreRequest**](EditScoreRequest.md) |  | 

## Example

```python
from dupr_backend.models.edit_match_request import EditMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditMatchRequest from a JSON string
edit_match_request_instance = EditMatchRequest.from_json(json)
# print the JSON string representation of the object
print(EditMatchRequest.to_json())

# convert the object into a dict
edit_match_request_dict = edit_match_request_instance.to_dict()
# create an instance of EditMatchRequest from a dict
edit_match_request_from_dict = EditMatchRequest.from_dict(edit_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


