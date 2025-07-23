# PageLeagueStandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** | Offset value you sent in the request | 
**limit** | **int** | Limit value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**hits** | [**List[LeagueStandingResponse]**](LeagueStandingResponse.md) | Array of results, can be empty. | [optional] 
**total_value_relation** | **str** | Relation to total results available. | 
**has_previous** | **bool** | Is there any previous page | 
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 

## Example

```python
from dupr_backend.models.page_league_standing_response import PageLeagueStandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageLeagueStandingResponse from a JSON string
page_league_standing_response_instance = PageLeagueStandingResponse.from_json(json)
# print the JSON string representation of the object
print(PageLeagueStandingResponse.to_json())

# convert the object into a dict
page_league_standing_response_dict = page_league_standing_response_instance.to_dict()
# create an instance of PageLeagueStandingResponse from a dict
page_league_standing_response_from_dict = PageLeagueStandingResponse.from_dict(page_league_standing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


