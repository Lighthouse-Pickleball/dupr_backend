# SingleWrapperMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**MatchResponse**](MatchResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_match_response import SingleWrapperMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperMatchResponse from a JSON string
single_wrapper_match_response_instance = SingleWrapperMatchResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperMatchResponse.to_json())

# convert the object into a dict
single_wrapper_match_response_dict = single_wrapper_match_response_instance.to_dict()
# create an instance of SingleWrapperMatchResponse from a dict
single_wrapper_match_response_from_dict = SingleWrapperMatchResponse.from_dict(single_wrapper_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


