# ArrayWrapperOfPostReactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[PostReactionResponse]**](PostReactionResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_post_reaction_response import ArrayWrapperOfPostReactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfPostReactionResponse from a JSON string
array_wrapper_of_post_reaction_response_instance = ArrayWrapperOfPostReactionResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfPostReactionResponse.to_json())

# convert the object into a dict
array_wrapper_of_post_reaction_response_dict = array_wrapper_of_post_reaction_response_instance.to_dict()
# create an instance of ArrayWrapperOfPostReactionResponse from a dict
array_wrapper_of_post_reaction_response_from_dict = ArrayWrapperOfPostReactionResponse.from_dict(array_wrapper_of_post_reaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


