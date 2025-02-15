# SingleWrapperOfAccountLinkResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**AccountLinkResponse**](AccountLinkResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_account_link_response import SingleWrapperOfAccountLinkResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfAccountLinkResponse from a JSON string
single_wrapper_of_account_link_response_instance = SingleWrapperOfAccountLinkResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfAccountLinkResponse.to_json())

# convert the object into a dict
single_wrapper_of_account_link_response_dict = single_wrapper_of_account_link_response_instance.to_dict()
# create an instance of SingleWrapperOfAccountLinkResponse from a dict
single_wrapper_of_account_link_response_from_dict = SingleWrapperOfAccountLinkResponse.from_dict(single_wrapper_of_account_link_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


