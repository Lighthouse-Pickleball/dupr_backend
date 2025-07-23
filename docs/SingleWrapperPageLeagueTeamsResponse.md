# SingleWrapperPageLeagueTeamsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageLeagueTeamsResponse**](PageLeagueTeamsResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_league_teams_response import SingleWrapperPageLeagueTeamsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageLeagueTeamsResponse from a JSON string
single_wrapper_page_league_teams_response_instance = SingleWrapperPageLeagueTeamsResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageLeagueTeamsResponse.to_json())

# convert the object into a dict
single_wrapper_page_league_teams_response_dict = single_wrapper_page_league_teams_response_instance.to_dict()
# create an instance of SingleWrapperPageLeagueTeamsResponse from a dict
single_wrapper_page_league_teams_response_from_dict = SingleWrapperPageLeagueTeamsResponse.from_dict(single_wrapper_page_league_teams_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


