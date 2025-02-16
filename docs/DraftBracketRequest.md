# DraftBracketRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bracket** | **List[int]** |  | [optional] 
**bracket_id** | **int** |  | 
**courts** | **int** |  | [optional] 
**custom_code** | **str** |  | [optional] 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**duration** | **List[date]** |  | [optional] 
**duration_date_time** | **List[str]** |  | [optional] 
**elimination** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**league_id** | **int** |  | [optional] 
**match_bonus_points** | **float** |  | [optional] 
**max_team** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**non_member_fee** | **float** |  | [optional] 
**player_group** | **str** |  | [optional] 
**rating_bracket** | **List[float]** |  | [optional] 
**registration_date** | **List[date]** |  | [optional] 
**registration_date_time** | **List[str]** |  | [optional] 
**score_format** | **int** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**wait_list** | **int** |  | [optional] 
**zone_name** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.draft_bracket_request import DraftBracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftBracketRequest from a JSON string
draft_bracket_request_instance = DraftBracketRequest.from_json(json)
# print the JSON string representation of the object
print DraftBracketRequest.to_json()

# convert the object into a dict
draft_bracket_request_dict = draft_bracket_request_instance.to_dict()
# create an instance of DraftBracketRequest from a dict
draft_bracket_request_form_dict = draft_bracket_request.from_dict(draft_bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


