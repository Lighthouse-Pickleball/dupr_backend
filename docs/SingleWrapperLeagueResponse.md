# SingleWrapperLeagueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**LeagueResponse**](LeagueResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperLeagueResponse from a JSON string
single_wrapper_league_response_instance = SingleWrapperLeagueResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperLeagueResponse.to_json())

# convert the object into a dict
single_wrapper_league_response_dict = single_wrapper_league_response_instance.to_dict()
# create an instance of SingleWrapperLeagueResponse from a dict
single_wrapper_league_response_from_dict = SingleWrapperLeagueResponse.from_dict(single_wrapper_league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


