# SingleWrapperOfPageOfUserSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfUserSuggestion**](PageOfUserSuggestion.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_user_suggestion import SingleWrapperOfPageOfUserSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfUserSuggestion from a JSON string
single_wrapper_of_page_of_user_suggestion_instance = SingleWrapperOfPageOfUserSuggestion.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfUserSuggestion.to_json())

# convert the object into a dict
single_wrapper_of_page_of_user_suggestion_dict = single_wrapper_of_page_of_user_suggestion_instance.to_dict()
# create an instance of SingleWrapperOfPageOfUserSuggestion from a dict
single_wrapper_of_page_of_user_suggestion_from_dict = SingleWrapperOfPageOfUserSuggestion.from_dict(single_wrapper_of_page_of_user_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


