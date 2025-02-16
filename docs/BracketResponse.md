# BracketResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**age_bracket** | **List[int]** |  | [optional] 
**bracket_id** | **int** |  | 
**can_show_standings** | **bool** |  | [optional] 
**club_id** | **int** |  | 
**club_name** | **str** |  | 
**contact_details** | [**List[LeagueContactDetailResponse]**](LeagueContactDetailResponse.md) |  | [optional] 
**courts** | **int** |  | [optional] 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**custom_code** | **str** |  | [optional] 
**description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**display_status** | **str** |  | [optional] 
**draw_impacted** | **bool** |  | [optional] 
**duration** | **List[str]** |  | 
**duration_date_time** | **List[str]** |  | [optional] 
**duration_status** | **str** |  | [optional] 
**elimination** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**has_confirm_match** | **bool** |  | [optional] 
**has_queue** | **bool** |  | [optional] 
**is_match_seeded** | **bool** |  | [optional] 
**is_player_eligible** | **bool** |  | [optional] 
**is_queue_complete** | **bool** |  | [optional] 
**is_registered** | **bool** |  | 
**is_wait_list_full** | **bool** |  | 
**league_address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**league_id** | **int** |  | 
**league_name** | **str** |  | 
**match_bonus_points** | **float** |  | [optional] 
**max_team** | **int** |  | [optional] 
**media_url** | **str** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**non_member_fee** | **float** |  | 
**payment_details** | [**PaymentDetailsResponse**](PaymentDetailsResponse.md) |  | [optional] 
**payment_status** | **str** |  | 
**player_group** | **str** |  | [optional] 
**rating_bracket** | **List[float]** |  | [optional] 
**reg_user_id** | **int** |  | [optional] 
**registered_members** | **int** |  | [optional] 
**registration_date** | **List[str]** |  | [optional] 
**registration_date_time** | **List[str]** |  | [optional] 
**registration_details** | [**RegistrationResponse**](RegistrationResponse.md) |  | [optional] 
**registration_status** | **str** |  | [optional] 
**score_format** | **str** |  | 
**score_format_id** | **int** |  | 
**status** | **str** |  | [optional] 
**time_zone** | **str** |  | [optional] 
**total_rounds** | **int** |  | [optional] 
**wait_list** | **int** |  | 
**zone_name** | **str** |  | [optional] 

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


