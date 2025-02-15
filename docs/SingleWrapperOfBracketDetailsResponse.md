# SingleWrapperOfBracketDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**BracketDetailsResponse**](BracketDetailsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_bracket_details_response import SingleWrapperOfBracketDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfBracketDetailsResponse from a JSON string
single_wrapper_of_bracket_details_response_instance = SingleWrapperOfBracketDetailsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfBracketDetailsResponse.to_json())

# convert the object into a dict
single_wrapper_of_bracket_details_response_dict = single_wrapper_of_bracket_details_response_instance.to_dict()
# create an instance of SingleWrapperOfBracketDetailsResponse from a dict
single_wrapper_of_bracket_details_response_from_dict = SingleWrapperOfBracketDetailsResponse.from_dict(single_wrapper_of_bracket_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


