# SingleWrapperPageUserLookupResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageUserLookupResponse**](PageUserLookupResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_user_lookup_response import SingleWrapperPageUserLookupResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageUserLookupResponse from a JSON string
single_wrapper_page_user_lookup_response_instance = SingleWrapperPageUserLookupResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageUserLookupResponse.to_json())

# convert the object into a dict
single_wrapper_page_user_lookup_response_dict = single_wrapper_page_user_lookup_response_instance.to_dict()
# create an instance of SingleWrapperPageUserLookupResponse from a dict
single_wrapper_page_user_lookup_response_from_dict = SingleWrapperPageUserLookupResponse.from_dict(single_wrapper_page_user_lookup_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


