# SingleWrapperJoinLeagueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**JoinLeagueResponse**](JoinLeagueResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_join_league_response import SingleWrapperJoinLeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperJoinLeagueResponse from a JSON string
single_wrapper_join_league_response_instance = SingleWrapperJoinLeagueResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperJoinLeagueResponse.to_json())

# convert the object into a dict
single_wrapper_join_league_response_dict = single_wrapper_join_league_response_instance.to_dict()
# create an instance of SingleWrapperJoinLeagueResponse from a dict
single_wrapper_join_league_response_from_dict = SingleWrapperJoinLeagueResponse.from_dict(single_wrapper_join_league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


