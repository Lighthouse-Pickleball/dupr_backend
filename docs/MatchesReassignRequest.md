# MatchesReassignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**match_code** | **str** |  | 
**source** | **str** |  | 
**source_merge_input_type** | **str** |  | 
**target** | **str** |  | 
**target_merge_input_type** | **str** |  | 
**notify** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.matches_reassign_request import MatchesReassignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchesReassignRequest from a JSON string
matches_reassign_request_instance = MatchesReassignRequest.from_json(json)
# print the JSON string representation of the object
print(MatchesReassignRequest.to_json())

# convert the object into a dict
matches_reassign_request_dict = matches_reassign_request_instance.to_dict()
# create an instance of MatchesReassignRequest from a dict
matches_reassign_request_from_dict = MatchesReassignRequest.from_dict(matches_reassign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


