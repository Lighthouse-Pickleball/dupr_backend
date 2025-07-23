# SingleWrapperRegistrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**RegistrationResponse**](RegistrationResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_registration_response import SingleWrapperRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperRegistrationResponse from a JSON string
single_wrapper_registration_response_instance = SingleWrapperRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperRegistrationResponse.to_json())

# convert the object into a dict
single_wrapper_registration_response_dict = single_wrapper_registration_response_instance.to_dict()
# create an instance of SingleWrapperRegistrationResponse from a dict
single_wrapper_registration_response_from_dict = SingleWrapperRegistrationResponse.from_dict(single_wrapper_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


