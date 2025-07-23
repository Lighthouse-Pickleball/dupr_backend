# ArrayWrapperMatchRound


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[MatchRound]**](MatchRound.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_match_round import ArrayWrapperMatchRound

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperMatchRound from a JSON string
array_wrapper_match_round_instance = ArrayWrapperMatchRound.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperMatchRound.to_json())

# convert the object into a dict
array_wrapper_match_round_dict = array_wrapper_match_round_instance.to_dict()
# create an instance of ArrayWrapperMatchRound from a dict
array_wrapper_match_round_from_dict = ArrayWrapperMatchRound.from_dict(array_wrapper_match_round_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


