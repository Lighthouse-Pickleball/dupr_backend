# ArrayWrapperPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[PostResponse]**](PostResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_post_response import ArrayWrapperPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperPostResponse from a JSON string
array_wrapper_post_response_instance = ArrayWrapperPostResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperPostResponse.to_json())

# convert the object into a dict
array_wrapper_post_response_dict = array_wrapper_post_response_instance.to_dict()
# create an instance of ArrayWrapperPostResponse from a dict
array_wrapper_post_response_from_dict = ArrayWrapperPostResponse.from_dict(array_wrapper_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


