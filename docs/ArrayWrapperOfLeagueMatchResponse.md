# ArrayWrapperOfLeagueMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[LeagueMatchResponse]**](LeagueMatchResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_league_match_response import ArrayWrapperOfLeagueMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfLeagueMatchResponse from a JSON string
array_wrapper_of_league_match_response_instance = ArrayWrapperOfLeagueMatchResponse.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperOfLeagueMatchResponse.to_json())

# convert the object into a dict
array_wrapper_of_league_match_response_dict = array_wrapper_of_league_match_response_instance.to_dict()
# create an instance of ArrayWrapperOfLeagueMatchResponse from a dict
array_wrapper_of_league_match_response_from_dict = ArrayWrapperOfLeagueMatchResponse.from_dict(array_wrapper_of_league_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


