# SearchLeaguesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **int** |  | 
**limit** | **int** |  | 
**query** | **str** |  | [optional] 
**lat** | **float** |  | 
**lng** | **float** |  | 
**radius_in_meters** | **float** |  | [optional] 
**filters** | [**LeagueFilter**](LeagueFilter.md) |  | [optional] 
**is_near_me** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.search_leagues_request import SearchLeaguesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SearchLeaguesRequest from a JSON string
search_leagues_request_instance = SearchLeaguesRequest.from_json(json)
# print the JSON string representation of the object
print(SearchLeaguesRequest.to_json())

# convert the object into a dict
search_leagues_request_dict = search_leagues_request_instance.to_dict()
# create an instance of SearchLeaguesRequest from a dict
search_leagues_request_from_dict = SearchLeaguesRequest.from_dict(search_leagues_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


