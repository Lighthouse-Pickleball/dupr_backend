# SingleWrapperCreateClientResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**CreateClientResponse**](CreateClientResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_create_client_response import SingleWrapperCreateClientResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperCreateClientResponse from a JSON string
single_wrapper_create_client_response_instance = SingleWrapperCreateClientResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperCreateClientResponse.to_json())

# convert the object into a dict
single_wrapper_create_client_response_dict = single_wrapper_create_client_response_instance.to_dict()
# create an instance of SingleWrapperCreateClientResponse from a dict
single_wrapper_create_client_response_from_dict = SingleWrapperCreateClientResponse.from_dict(single_wrapper_create_client_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


