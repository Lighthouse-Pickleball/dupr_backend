# ArrayWrapperPostReactionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[PostReactionResponse]**](PostReactionResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_post_reaction_response import ArrayWrapperPostReactionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperPostReactionResponse from a JSON string
array_wrapper_post_reaction_response_instance = ArrayWrapperPostReactionResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperPostReactionResponse.to_json())

# convert the object into a dict
array_wrapper_post_reaction_response_dict = array_wrapper_post_reaction_response_instance.to_dict()
# create an instance of ArrayWrapperPostReactionResponse from a dict
array_wrapper_post_reaction_response_from_dict = ArrayWrapperPostReactionResponse.from_dict(array_wrapper_post_reaction_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


