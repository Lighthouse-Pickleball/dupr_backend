# SingleWrapperOfPageOfLeagueStandingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfLeagueStandingResponse**](PageOfLeagueStandingResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_league_standing_response import SingleWrapperOfPageOfLeagueStandingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfLeagueStandingResponse from a JSON string
single_wrapper_of_page_of_league_standing_response_instance = SingleWrapperOfPageOfLeagueStandingResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfLeagueStandingResponse.to_json())

# convert the object into a dict
single_wrapper_of_page_of_league_standing_response_dict = single_wrapper_of_page_of_league_standing_response_instance.to_dict()
# create an instance of SingleWrapperOfPageOfLeagueStandingResponse from a dict
single_wrapper_of_page_of_league_standing_response_from_dict = SingleWrapperOfPageOfLeagueStandingResponse.from_dict(single_wrapper_of_page_of_league_standing_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


