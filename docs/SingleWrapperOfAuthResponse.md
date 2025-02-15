# SingleWrapperOfAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**AuthResponse0**](AuthResponse0.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_auth_response import SingleWrapperOfAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfAuthResponse from a JSON string
single_wrapper_of_auth_response_instance = SingleWrapperOfAuthResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfAuthResponse.to_json())

# convert the object into a dict
single_wrapper_of_auth_response_dict = single_wrapper_of_auth_response_instance.to_dict()
# create an instance of SingleWrapperOfAuthResponse from a dict
single_wrapper_of_auth_response_from_dict = SingleWrapperOfAuthResponse.from_dict(single_wrapper_of_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


