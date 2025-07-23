# SingleWrapperPageLeagueStandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PageLeagueStandingResponse**](PageLeagueStandingResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_league_standing_response import SingleWrapperPageLeagueStandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPageLeagueStandingResponse from a JSON string
single_wrapper_page_league_standing_response_instance = SingleWrapperPageLeagueStandingResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPageLeagueStandingResponse.to_json())

# convert the object into a dict
single_wrapper_page_league_standing_response_dict = single_wrapper_page_league_standing_response_instance.to_dict()
# create an instance of SingleWrapperPageLeagueStandingResponse from a dict
single_wrapper_page_league_standing_response_from_dict = SingleWrapperPageLeagueStandingResponse.from_dict(single_wrapper_page_league_standing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


