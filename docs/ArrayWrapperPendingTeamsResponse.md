# ArrayWrapperPendingTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[PendingTeamsResponse]**](PendingTeamsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_pending_teams_response import ArrayWrapperPendingTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperPendingTeamsResponse from a JSON string
array_wrapper_pending_teams_response_instance = ArrayWrapperPendingTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperPendingTeamsResponse.to_json())

# convert the object into a dict
array_wrapper_pending_teams_response_dict = array_wrapper_pending_teams_response_instance.to_dict()
# create an instance of ArrayWrapperPendingTeamsResponse from a dict
array_wrapper_pending_teams_response_from_dict = ArrayWrapperPendingTeamsResponse.from_dict(array_wrapper_pending_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


