# SingleWrapperUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**UserResponse**](UserResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_user_response import SingleWrapperUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperUserResponse from a JSON string
single_wrapper_user_response_instance = SingleWrapperUserResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperUserResponse.to_json())

# convert the object into a dict
single_wrapper_user_response_dict = single_wrapper_user_response_instance.to_dict()
# create an instance of SingleWrapperUserResponse from a dict
single_wrapper_user_response_from_dict = SingleWrapperUserResponse.from_dict(single_wrapper_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


