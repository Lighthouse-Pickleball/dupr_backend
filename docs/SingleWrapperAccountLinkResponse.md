# SingleWrapperAccountLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**AccountLinkResponse**](AccountLinkResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_account_link_response import SingleWrapperAccountLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperAccountLinkResponse from a JSON string
single_wrapper_account_link_response_instance = SingleWrapperAccountLinkResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperAccountLinkResponse.to_json())

# convert the object into a dict
single_wrapper_account_link_response_dict = single_wrapper_account_link_response_instance.to_dict()
# create an instance of SingleWrapperAccountLinkResponse from a dict
single_wrapper_account_link_response_from_dict = SingleWrapperAccountLinkResponse.from_dict(single_wrapper_account_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


