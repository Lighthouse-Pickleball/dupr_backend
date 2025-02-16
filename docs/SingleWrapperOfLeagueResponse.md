# SingleWrapperOfLeagueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**LeagueResponse**](LeagueResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_league_response import SingleWrapperOfLeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfLeagueResponse from a JSON string
single_wrapper_of_league_response_instance = SingleWrapperOfLeagueResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfLeagueResponse.to_json())

# convert the object into a dict
single_wrapper_of_league_response_dict = single_wrapper_of_league_response_instance.to_dict()
# create an instance of SingleWrapperOfLeagueResponse from a dict
single_wrapper_of_league_response_from_dict = SingleWrapperOfLeagueResponse.from_dict(single_wrapper_of_league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


