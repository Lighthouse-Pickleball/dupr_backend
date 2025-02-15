# ArrayWrapperOfReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[Reaction]**](Reaction.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_reaction import ArrayWrapperOfReaction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfReaction from a JSON string
array_wrapper_of_reaction_instance = ArrayWrapperOfReaction.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfReaction.to_json())

# convert the object into a dict
array_wrapper_of_reaction_dict = array_wrapper_of_reaction_instance.to_dict()
# create an instance of ArrayWrapperOfReaction from a dict
array_wrapper_of_reaction_from_dict = ArrayWrapperOfReaction.from_dict(array_wrapper_of_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


