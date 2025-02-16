# ArrayWrapperOfPendingTeamsResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[PendingTeamsResponse]**](PendingTeamsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_pending_teams_response import ArrayWrapperOfPendingTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfPendingTeamsResponse from a JSON string
array_wrapper_of_pending_teams_response_instance = ArrayWrapperOfPendingTeamsResponse.from_json(json)
# print the JSON string representation of the object
print ArrayWrapperOfPendingTeamsResponse.to_json()

# convert the object into a dict
array_wrapper_of_pending_teams_response_dict = array_wrapper_of_pending_teams_response_instance.to_dict()
# create an instance of ArrayWrapperOfPendingTeamsResponse from a dict
array_wrapper_of_pending_teams_response_form_dict = array_wrapper_of_pending_teams_response.from_dict(array_wrapper_of_pending_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


