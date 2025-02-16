# LeagueContentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**content_id** | **int** |  | 
**content_type** | **str** |  | 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_content_response import LeagueContentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueContentResponse from a JSON string
league_content_response_instance = LeagueContentResponse.from_json(json)
# print the JSON string representation of the object
print(LeagueContentResponse.to_json())

# convert the object into a dict
league_content_response_dict = league_content_response_instance.to_dict()
# create an instance of LeagueContentResponse from a dict
league_content_response_from_dict = LeagueContentResponse.from_dict(league_content_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


