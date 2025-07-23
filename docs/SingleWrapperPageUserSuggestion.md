# SingleWrapperPageUserSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageUserSuggestion**](PageUserSuggestion.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_user_suggestion import SingleWrapperPageUserSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageUserSuggestion from a JSON string
single_wrapper_page_user_suggestion_instance = SingleWrapperPageUserSuggestion.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageUserSuggestion.to_json())

# convert the object into a dict
single_wrapper_page_user_suggestion_dict = single_wrapper_page_user_suggestion_instance.to_dict()
# create an instance of SingleWrapperPageUserSuggestion from a dict
single_wrapper_page_user_suggestion_from_dict = SingleWrapperPageUserSuggestion.from_dict(single_wrapper_page_user_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


