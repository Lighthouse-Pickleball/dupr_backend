# PageUnclaimedPlayerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[UnclaimedPlayerResponse]**](UnclaimedPlayerResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_unclaimed_player_response import PageUnclaimedPlayerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageUnclaimedPlayerResponse from a JSON string
page_unclaimed_player_response_instance = PageUnclaimedPlayerResponse.from_json(json)
# print the JSON string representation of the object
print(PageUnclaimedPlayerResponse.to_json())

# convert the object into a dict
page_unclaimed_player_response_dict = page_unclaimed_player_response_instance.to_dict()
# create an instance of PageUnclaimedPlayerResponse from a dict
page_unclaimed_player_response_from_dict = PageUnclaimedPlayerResponse.from_dict(page_unclaimed_player_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


