# SingleWrapperOfRegistrationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**RegistrationResponse**](RegistrationResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_registration_response import SingleWrapperOfRegistrationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfRegistrationResponse from a JSON string
single_wrapper_of_registration_response_instance = SingleWrapperOfRegistrationResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfRegistrationResponse.to_json())

# convert the object into a dict
single_wrapper_of_registration_response_dict = single_wrapper_of_registration_response_instance.to_dict()
# create an instance of SingleWrapperOfRegistrationResponse from a dict
single_wrapper_of_registration_response_from_dict = SingleWrapperOfRegistrationResponse.from_dict(single_wrapper_of_registration_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


