# SingleWrapperPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PostResponse**](PostResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_post_response import SingleWrapperPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPostResponse from a JSON string
single_wrapper_post_response_instance = SingleWrapperPostResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPostResponse.to_json())

# convert the object into a dict
single_wrapper_post_response_dict = single_wrapper_post_response_instance.to_dict()
# create an instance of SingleWrapperPostResponse from a dict
single_wrapper_post_response_from_dict = SingleWrapperPostResponse.from_dict(single_wrapper_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


