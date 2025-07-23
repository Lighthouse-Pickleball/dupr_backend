# SingleWrapperAuthResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**AuthResponse**](AuthResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_auth_response import SingleWrapperAuthResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperAuthResponse from a JSON string
single_wrapper_auth_response_instance = SingleWrapperAuthResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperAuthResponse.to_json())

# convert the object into a dict
single_wrapper_auth_response_dict = single_wrapper_auth_response_instance.to_dict()
# create an instance of SingleWrapperAuthResponse from a dict
single_wrapper_auth_response_from_dict = SingleWrapperAuthResponse.from_dict(single_wrapper_auth_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


