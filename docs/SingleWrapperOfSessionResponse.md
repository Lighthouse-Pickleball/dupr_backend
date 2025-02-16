# SingleWrapperOfSessionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**SessionResponse**](SessionResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_session_response import SingleWrapperOfSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfSessionResponse from a JSON string
single_wrapper_of_session_response_instance = SingleWrapperOfSessionResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfSessionResponse.to_json())

# convert the object into a dict
single_wrapper_of_session_response_dict = single_wrapper_of_session_response_instance.to_dict()
# create an instance of SingleWrapperOfSessionResponse from a dict
single_wrapper_of_session_response_from_dict = SingleWrapperOfSessionResponse.from_dict(single_wrapper_of_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


