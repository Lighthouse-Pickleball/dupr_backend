# SingleWrapperOfAccountStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**AccountStatusResponse**](AccountStatusResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_account_status_response import SingleWrapperOfAccountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfAccountStatusResponse from a JSON string
single_wrapper_of_account_status_response_instance = SingleWrapperOfAccountStatusResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfAccountStatusResponse.to_json())

# convert the object into a dict
single_wrapper_of_account_status_response_dict = single_wrapper_of_account_status_response_instance.to_dict()
# create an instance of SingleWrapperOfAccountStatusResponse from a dict
single_wrapper_of_account_status_response_from_dict = SingleWrapperOfAccountStatusResponse.from_dict(single_wrapper_of_account_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


