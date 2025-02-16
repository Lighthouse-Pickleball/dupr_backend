# SingleWrapperOfPostResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PostResponse**](PostResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_post_response import SingleWrapperOfPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPostResponse from a JSON string
single_wrapper_of_post_response_instance = SingleWrapperOfPostResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfPostResponse.to_json()

# convert the object into a dict
single_wrapper_of_post_response_dict = single_wrapper_of_post_response_instance.to_dict()
# create an instance of SingleWrapperOfPostResponse from a dict
single_wrapper_of_post_response_form_dict = single_wrapper_of_post_response.from_dict(single_wrapper_of_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


