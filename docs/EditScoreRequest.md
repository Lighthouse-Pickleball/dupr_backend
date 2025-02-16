# EditScoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**game1** | **int** |  | 
**game2** | **int** |  | [optional] 
**game3** | **int** |  | [optional] 
**game4** | **int** |  | [optional] 
**game5** | **int** |  | [optional] 
**team_id** | **int** |  | 
**winner** | **bool** |  | 

## Example

```python
from dupr_backend.models.edit_score_request import EditScoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditScoreRequest from a JSON string
edit_score_request_instance = EditScoreRequest.from_json(json)
# print the JSON string representation of the object
print(EditScoreRequest.to_json())

# convert the object into a dict
edit_score_request_dict = edit_score_request_instance.to_dict()
# create an instance of EditScoreRequest from a dict
edit_score_request_from_dict = EditScoreRequest.from_dict(edit_score_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


