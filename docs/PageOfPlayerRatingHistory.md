# PageOfPlayerRatingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 
**has_previous** | **bool** | Is there any previous page | 
**hits** | [**List[PlayerRatingHistory]**](PlayerRatingHistory.md) | Array of results, can be empty. | [optional] 
**limit** | **int** | Limit value you sent in the request | 
**offset** | **int** | Offset value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**total_value_relation** | **str** | Relation to total results available. | 

## Example

```python
from dupr_backend.models.page_of_player_rating_history import PageOfPlayerRatingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PageOfPlayerRatingHistory from a JSON string
page_of_player_rating_history_instance = PageOfPlayerRatingHistory.from_json(json)
# print the JSON string representation of the object
print(PageOfPlayerRatingHistory.to_json())

# convert the object into a dict
page_of_player_rating_history_dict = page_of_player_rating_history_instance.to_dict()
# create an instance of PageOfPlayerRatingHistory from a dict
page_of_player_rating_history_from_dict = PageOfPlayerRatingHistory.from_dict(page_of_player_rating_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


