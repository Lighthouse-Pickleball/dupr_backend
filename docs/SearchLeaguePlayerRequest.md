# SearchLeaguePlayerRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**filters** | [**Filters**](Filters.md) |  | [optional] 
**league_id** | **int** |  | [optional] 
**query** | **str** |  | 
**sort** | [**PlayerSort**](PlayerSort.md) |  | [optional] 

## Example

```python
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLeaguePlayerRequest from a JSON string
search_league_player_request_instance = SearchLeaguePlayerRequest.from_json(json)
# print the JSON string representation of the object
print SearchLeaguePlayerRequest.to_json()

# convert the object into a dict
search_league_player_request_dict = search_league_player_request_instance.to_dict()
# create an instance of SearchLeaguePlayerRequest from a dict
search_league_player_request_form_dict = search_league_player_request.from_dict(search_league_player_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


