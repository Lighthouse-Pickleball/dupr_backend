# SingleWrapperAccountStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**AccountStatusResponse**](AccountStatusResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_account_status_response import SingleWrapperAccountStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperAccountStatusResponse from a JSON string
single_wrapper_account_status_response_instance = SingleWrapperAccountStatusResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperAccountStatusResponse.to_json())

# convert the object into a dict
single_wrapper_account_status_response_dict = single_wrapper_account_status_response_instance.to_dict()
# create an instance of SingleWrapperAccountStatusResponse from a dict
single_wrapper_account_status_response_from_dict = SingleWrapperAccountStatusResponse.from_dict(single_wrapper_account_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


