# ArrayWrapperOfPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[PostResponse]**](PostResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_post_response import ArrayWrapperOfPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfPostResponse from a JSON string
array_wrapper_of_post_response_instance = ArrayWrapperOfPostResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfPostResponse.to_json())

# convert the object into a dict
array_wrapper_of_post_response_dict = array_wrapper_of_post_response_instance.to_dict()
# create an instance of ArrayWrapperOfPostResponse from a dict
array_wrapper_of_post_response_from_dict = ArrayWrapperOfPostResponse.from_dict(array_wrapper_of_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


