# EditBracketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**league_id** | **int** |  | 
**name** | **str** |  | [optional] 
**custom_code** | **str** |  | [optional] 
**duration** | **List[date]** |  | [optional] 
**format** | **str** |  | [optional] 
**elimination** | **str** |  | [optional] 
**player_group** | **str** |  | [optional] 
**rating_bracket** | **List[float]** |  | [optional] 
**age_bracket** | **List[int]** |  | [optional] 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**match_bonus_points** | **float** |  | [optional] 
**registration_date** | **List[date]** |  | [optional] 
**status** | **str** |  | [optional] 
**score_format** | **int** |  | 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | 
**max_team** | **int** |  | [optional] 
**wait_list** | **int** |  | 
**courts** | **int** |  | 
**registration_date_time** | **List[datetime]** |  | [optional] 
**duration_date_time** | **List[datetime]** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**zone_name** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.edit_bracket_request import EditBracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditBracketRequest from a JSON string
edit_bracket_request_instance = EditBracketRequest.from_json(json)
# print the JSON string representation of the object
print(EditBracketRequest.to_json())

# convert the object into a dict
edit_bracket_request_dict = edit_bracket_request_instance.to_dict()
# create an instance of EditBracketRequest from a dict
edit_bracket_request_from_dict = EditBracketRequest.from_dict(edit_bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


