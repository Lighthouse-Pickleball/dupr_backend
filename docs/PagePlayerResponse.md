# PagePlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[PlayerResponse]**](PlayerResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**empty** | **bool** | Are results empty | 
**has_previous** | **bool** | Is there any previous page | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_player_response import PagePlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PagePlayerResponse from a JSON string
page_player_response_instance = PagePlayerResponse.from_json(json)
# print the JSON string representation of the object
print(PagePlayerResponse.to_json())

# convert the object into a dict
page_player_response_dict = page_player_response_instance.to_dict()
# create an instance of PagePlayerResponse from a dict
page_player_response_from_dict = PagePlayerResponse.from_dict(page_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


