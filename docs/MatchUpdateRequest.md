# MatchUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | [optional] 
**confirmed** | **bool** |  | [optional] 
**created** | **str** |  | [optional] 
**event_date** | **str** |  | [optional] 
**event_name** | **str** |  | [optional] 
**league** | **str** |  | [optional] 
**league_id** | **int** |  | [optional] 
**league_match_id** | **int** |  | [optional] 
**location** | **str** |  | [optional] 
**match_id** | **int** |  | [optional] 
**match_source** | **str** |  | [optional] 
**reason** | **str** |  | [optional] 
**requested_by** | **str** |  | [optional] 
**teams** | [**List[TeamUpdateRequest]**](TeamUpdateRequest.md) |  | 
**venue** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.match_update_request import MatchUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchUpdateRequest from a JSON string
match_update_request_instance = MatchUpdateRequest.from_json(json)
# print the JSON string representation of the object
print MatchUpdateRequest.to_json()

# convert the object into a dict
match_update_request_dict = match_update_request_instance.to_dict()
# create an instance of MatchUpdateRequest from a dict
match_update_request_form_dict = match_update_request.from_dict(match_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


