# SingleWrapperPageMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageMatchResponse**](PageMatchResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_match_response import SingleWrapperPageMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageMatchResponse from a JSON string
single_wrapper_page_match_response_instance = SingleWrapperPageMatchResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageMatchResponse.to_json())

# convert the object into a dict
single_wrapper_page_match_response_dict = single_wrapper_page_match_response_instance.to_dict()
# create an instance of SingleWrapperPageMatchResponse from a dict
single_wrapper_page_match_response_from_dict = SingleWrapperPageMatchResponse.from_dict(single_wrapper_page_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


