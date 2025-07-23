# SingleWrapperPageLeagueMatchResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageLeagueMatchResponse**](PageLeagueMatchResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_league_match_response import SingleWrapperPageLeagueMatchResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageLeagueMatchResponse from a JSON string
single_wrapper_page_league_match_response_instance = SingleWrapperPageLeagueMatchResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageLeagueMatchResponse.to_json())

# convert the object into a dict
single_wrapper_page_league_match_response_dict = single_wrapper_page_league_match_response_instance.to_dict()
# create an instance of SingleWrapperPageLeagueMatchResponse from a dict
single_wrapper_page_league_match_response_from_dict = SingleWrapperPageLeagueMatchResponse.from_dict(single_wrapper_page_league_match_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


