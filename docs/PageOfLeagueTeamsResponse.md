# PageOfLeagueTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**empty** | **bool** | Are results empty | 
**has_more** | **bool** | Are there any more results to fetch | 
**has_previous** | **bool** | Is there any previous page | 
**hits** | [**List[LeagueTeamsResponse]**](LeagueTeamsResponse.md) | Array of results, can be empty. | [optional] 
**limit** | **int** | Limit value you sent in the request | 
**offset** | **int** | Offset value you sent in the request | 
**total** | **int** | Total number of results available in database | 
**total_value_relation** | **str** | Relation to total results available. | 

## Example

```python
from dupr_backend.models.page_of_league_teams_response import PageOfLeagueTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PageOfLeagueTeamsResponse from a JSON string
page_of_league_teams_response_instance = PageOfLeagueTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(PageOfLeagueTeamsResponse.to_json())

# convert the object into a dict
page_of_league_teams_response_dict = page_of_league_teams_response_instance.to_dict()
# create an instance of PageOfLeagueTeamsResponse from a dict
page_of_league_teams_response_from_dict = PageOfLeagueTeamsResponse.from_dict(page_of_league_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


