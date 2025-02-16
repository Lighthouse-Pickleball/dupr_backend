# SingleWrapperOfMatchResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**MatchResponse**](MatchResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_match_response import SingleWrapperOfMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfMatchResponse from a JSON string
single_wrapper_of_match_response_instance = SingleWrapperOfMatchResponse.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfMatchResponse.to_json()

# convert the object into a dict
single_wrapper_of_match_response_dict = single_wrapper_of_match_response_instance.to_dict()
# create an instance of SingleWrapperOfMatchResponse from a dict
single_wrapper_of_match_response_form_dict = single_wrapper_of_match_response.from_dict(single_wrapper_of_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


