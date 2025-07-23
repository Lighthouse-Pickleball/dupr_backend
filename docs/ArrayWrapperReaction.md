# ArrayWrapperReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[Reaction]**](Reaction.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_reaction import ArrayWrapperReaction

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperReaction from a JSON string
array_wrapper_reaction_instance = ArrayWrapperReaction.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperReaction.to_json())

# convert the object into a dict
array_wrapper_reaction_dict = array_wrapper_reaction_instance.to_dict()
# create an instance of ArrayWrapperReaction from a dict
array_wrapper_reaction_from_dict = ArrayWrapperReaction.from_dict(array_wrapper_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


