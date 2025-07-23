# SingleWrapperPageBracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageBracketResponse**](PageBracketResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_bracket_response import SingleWrapperPageBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageBracketResponse from a JSON string
single_wrapper_page_bracket_response_instance = SingleWrapperPageBracketResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageBracketResponse.to_json())

# convert the object into a dict
single_wrapper_page_bracket_response_dict = single_wrapper_page_bracket_response_instance.to_dict()
# create an instance of SingleWrapperPageBracketResponse from a dict
single_wrapper_page_bracket_response_from_dict = SingleWrapperPageBracketResponse.from_dict(single_wrapper_page_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


