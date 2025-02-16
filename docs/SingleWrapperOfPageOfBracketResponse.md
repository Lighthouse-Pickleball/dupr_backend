# SingleWrapperOfPageOfBracketResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfBracketResponse**](PageOfBracketResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_bracket_response import SingleWrapperOfPageOfBracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfBracketResponse from a JSON string
single_wrapper_of_page_of_bracket_response_instance = SingleWrapperOfPageOfBracketResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfPageOfBracketResponse.to_json()

# convert the object into a dict
single_wrapper_of_page_of_bracket_response_dict = single_wrapper_of_page_of_bracket_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfBracketResponse from a dict
single_wrapper_of_page_of_bracket_response_form_dict = single_wrapper_of_page_of_bracket_response.from_dict(single_wrapper_of_page_of_bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


