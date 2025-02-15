# SingleWrapperOfReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**Reaction**](Reaction.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_reaction import SingleWrapperOfReaction

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfReaction from a JSON string
single_wrapper_of_reaction_instance = SingleWrapperOfReaction.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfReaction.to_json())

# convert the object into a dict
single_wrapper_of_reaction_dict = single_wrapper_of_reaction_instance.to_dict()
# create an instance of SingleWrapperOfReaction from a dict
single_wrapper_of_reaction_from_dict = SingleWrapperOfReaction.from_dict(single_wrapper_of_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


