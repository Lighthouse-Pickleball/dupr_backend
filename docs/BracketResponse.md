# BracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**league_id** | **int** |  | 
**name** | **str** |  | [optional] 
**custom_code** | **str** |  | [optional] 
**duration** | **List[str]** |  | 
**format** | **str** |  | [optional] 
**elimination** | **str** |  | [optional] 
**player_group** | **str** |  | [optional] 
**rating_bracket** | **List[float]** |  | [optional] 
**age_bracket** | **List[int]** |  | [optional] 
**description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**match_bonus_points** | **float** |  | [optional] 
**registration_date** | **List[str]** |  | [optional] 
**score_format** | **str** |  | 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | 
**max_team** | **int** |  | [optional] 
**wait_list** | **int** |  | 
**status** | **str** |  | [optional] 
**score_format_id** | **int** |  | 
**registration_status** | **str** |  | [optional] 
**duration_status** | **str** |  | [optional] 
**registration_details** | [**RegistrationResponse**](RegistrationResponse.md) |  | [optional] 
**league_name** | **str** |  | 
**league_address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**media_url** | **str** |  | [optional] 
**total_rounds** | **int** |  | [optional] 
**contact_details** | [**List[LeagueContactDetailResponse]**](LeagueContactDetailResponse.md) |  | [optional] 
**is_registered** | **bool** |  | 
**club_name** | **str** |  | 
**registered_members** | **int** |  | [optional] 
**is_match_seeded** | **bool** |  | [optional] 
**club_id** | **int** |  | 
**is_wait_list_full** | **bool** |  | 
**display_status** | **str** |  | [optional] 
**has_confirm_match** | **bool** |  | [optional] 
**has_queue** | **bool** |  | [optional] 
**is_queue_complete** | **bool** |  | [optional] 
**can_show_standings** | **bool** |  | [optional] 
**courts** | **int** |  | [optional] 
**registration_date_time** | **List[str]** |  | [optional] 
**duration_date_time** | **List[str]** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**zone_name** | **str** |  | [optional] 
**is_player_eligible** | **bool** |  | [optional] 
**draw_impacted** | **bool** |  | [optional] 
**payment_details** | [**PaymentDetailsResponse**](PaymentDetailsResponse.md) |  | [optional] 
**reg_user_id** | **int** |  | [optional] 
**payment_status** | **str** |  | 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**wait_list_full** | **bool** |  | [optional] 
**queue_complete** | **bool** |  | [optional] 
**player_eligible** | **bool** |  | [optional] 
**match_seeded** | **bool** |  | [optional] 
**registered** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.bracket_response import BracketResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BracketResponse from a JSON string
bracket_response_instance = BracketResponse.from_json(json)
# print the JSON string representation of the object
print(BracketResponse.to_json())

# convert the object into a dict
bracket_response_dict = bracket_response_instance.to_dict()
# create an instance of BracketResponse from a dict
bracket_response_from_dict = BracketResponse.from_dict(bracket_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


