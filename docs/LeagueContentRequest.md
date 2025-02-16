# LeagueContentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | 
**content_id** | **int** |  | [optional] 
**content_type** | **str** |  | 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.league_content_request import LeagueContentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueContentRequest from a JSON string
league_content_request_instance = LeagueContentRequest.from_json(json)
# print the JSON string representation of the object
print LeagueContentRequest.to_json()

# convert the object into a dict
league_content_request_dict = league_content_request_instance.to_dict()
# create an instance of LeagueContentRequest from a dict
league_content_request_form_dict = league_content_request.from_dict(league_content_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


