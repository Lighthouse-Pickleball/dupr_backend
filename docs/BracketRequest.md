# BracketRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bracket** | **List[int]** |  | [optional] 
**bracket_id** | **int** |  | 
**courts** | **int** |  | [optional] 
**custom_code** | **str** |  | [optional] 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**duration** | **List[date]** |  | 
**duration_date_time** | **List[str]** |  | [optional] 
**elimination** | **str** |  | 
**format** | **str** |  | 
**league_id** | **int** |  | [optional] 
**match_bonus_points** | **float** |  | [optional] 
**max_team** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**non_member_fee** | **float** |  | [optional] 
**player_group** | **str** |  | 
**rating_bracket** | **List[float]** |  | [optional] 
**registration_date** | **List[date]** |  | [optional] 
**registration_date_time** | **List[str]** |  | [optional] 
**score_format** | **int** |  | 
**time_zone** | **str** |  | [optional] 
**wait_list** | **int** |  | 
**zone_name** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_request import BracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketRequest from a JSON string
bracket_request_instance = BracketRequest.from_json(json)
# print the JSON string representation of the object
print BracketRequest.to_json()

# convert the object into a dict
bracket_request_dict = bracket_request_instance.to_dict()
# create an instance of BracketRequest from a dict
bracket_request_form_dict = bracket_request.from_dict(bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


