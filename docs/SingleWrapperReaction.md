# SingleWrapperReaction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**Reaction**](Reaction.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_reaction import SingleWrapperReaction

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperReaction from a JSON string
single_wrapper_reaction_instance = SingleWrapperReaction.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperReaction.to_json())

# convert the object into a dict
single_wrapper_reaction_dict = single_wrapper_reaction_instance.to_dict()
# create an instance of SingleWrapperReaction from a dict
single_wrapper_reaction_from_dict = SingleWrapperReaction.from_dict(single_wrapper_reaction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


