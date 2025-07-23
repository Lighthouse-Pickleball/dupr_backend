# ArrayWrapperLeagueMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[LeagueMatchResponse]**](LeagueMatchResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_league_match_response import ArrayWrapperLeagueMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperLeagueMatchResponse from a JSON string
array_wrapper_league_match_response_instance = ArrayWrapperLeagueMatchResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperLeagueMatchResponse.to_json())

# convert the object into a dict
array_wrapper_league_match_response_dict = array_wrapper_league_match_response_instance.to_dict()
# create an instance of ArrayWrapperLeagueMatchResponse from a dict
array_wrapper_league_match_response_from_dict = ArrayWrapperLeagueMatchResponse.from_dict(array_wrapper_league_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


