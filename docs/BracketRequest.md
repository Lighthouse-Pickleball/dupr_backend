# BracketRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_code** | **str** |  | [optional] 
**duration** | **List[date]** |  | 
**format** | **str** |  | 
**elimination** | **str** |  | 
**player_group** | **str** |  | 
**rating_bracket** | **List[float]** |  | [optional] 
**age_bracket** | **List[int]** |  | [optional] 
**description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**match_bonus_points** | **float** |  | [optional] 
**registration_date** | **List[date]** |  | [optional] 
**score_format** | **int** |  | 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | [optional] 
**max_team** | **int** |  | [optional] 
**wait_list** | **int** |  | 
**league_id** | **int** |  | [optional] 
**bracket_id** | **int** |  | 
**name** | **str** |  | [optional] 
**courts** | **int** |  | [optional] 
**registration_date_time** | **List[datetime]** |  | [optional] 
**duration_date_time** | **List[datetime]** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**zone_name** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_request import BracketRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketRequest from a JSON string
bracket_request_instance = BracketRequest.from_json(json)
# print the JSON string representation of the object
print(BracketRequest.to_json())

# convert the object into a dict
bracket_request_dict = bracket_request_instance.to_dict()
# create an instance of BracketRequest from a dict
bracket_request_from_dict = BracketRequest.from_dict(bracket_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


