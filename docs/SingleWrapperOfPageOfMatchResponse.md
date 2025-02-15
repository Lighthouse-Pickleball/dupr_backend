# SingleWrapperOfPageOfMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfMatchResponse**](PageOfMatchResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_match_response import SingleWrapperOfPageOfMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfMatchResponse from a JSON string
single_wrapper_of_page_of_match_response_instance = SingleWrapperOfPageOfMatchResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfMatchResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_match_response_dict = single_wrapper_of_page_of_match_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfMatchResponse from a dict
single_wrapper_of_page_of_match_response_from_dict = SingleWrapperOfPageOfMatchResponse.from_dict(single_wrapper_of_page_of_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


