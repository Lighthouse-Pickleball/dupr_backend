# SingleWrapperOfPageOfLeagueTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfLeagueTeamsResponse**](PageOfLeagueTeamsResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_league_teams_response import SingleWrapperOfPageOfLeagueTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfLeagueTeamsResponse from a JSON string
single_wrapper_of_page_of_league_teams_response_instance = SingleWrapperOfPageOfLeagueTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfLeagueTeamsResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_league_teams_response_dict = single_wrapper_of_page_of_league_teams_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfLeagueTeamsResponse from a dict
single_wrapper_of_page_of_league_teams_response_from_dict = SingleWrapperOfPageOfLeagueTeamsResponse.from_dict(single_wrapper_of_page_of_league_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


