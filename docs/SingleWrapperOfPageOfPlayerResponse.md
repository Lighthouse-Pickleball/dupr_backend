# SingleWrapperOfPageOfPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfPlayerResponse**](PageOfPlayerResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfPlayerResponse from a JSON string
single_wrapper_of_page_of_player_response_instance = SingleWrapperOfPageOfPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfPlayerResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_player_response_dict = single_wrapper_of_page_of_player_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfPlayerResponse from a dict
single_wrapper_of_page_of_player_response_from_dict = SingleWrapperOfPageOfPlayerResponse.from_dict(single_wrapper_of_page_of_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


