# PageUserSuggestion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[UserSuggestion]**](UserSuggestion.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_user_suggestion import PageUserSuggestion

# TODO update the JSON string below
json = "{}"
# create an instance of PageUserSuggestion from a JSON string
page_user_suggestion_instance = PageUserSuggestion.from_json(json)
# print the JSON string representation of the object
print(PageUserSuggestion.to_json())

# convert the object into a dict
page_user_suggestion_dict = page_user_suggestion_instance.to_dict()
# create an instance of PageUserSuggestion from a dict
page_user_suggestion_from_dict = PageUserSuggestion.from_dict(page_user_suggestion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


