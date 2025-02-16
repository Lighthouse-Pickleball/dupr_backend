# LeagueResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**age_string** | **str** |  | [optional] 
**attributes** | **object** |  | [optional] 
**brackets** | [**List[BracketResponse]**](BracketResponse.md) |  | 
**can_show_standings** | **bool** |  | [optional] 
**club_id** | **int** |  | 
**club_name** | **str** |  | [optional] 
**contact_details** | [**List[LeagueContactDetailResponse]**](LeagueContactDetailResponse.md) |  | [optional] 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**display_status** | **str** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**duration** | **List[str]** |  | 
**duration_date_time** | **List[str]** |  | [optional] 
**duration_date_time_utc** | **List[str]** |  | [optional] 
**duration_status** | **str** |  | [optional] 
**duration_string** | **str** |  | [optional] 
**elimination_string** | **str** |  | [optional] 
**end_date** | **datetime** |  | 
**event_format_string** | **str** |  | [optional] 
**is_registered** | **bool** |  | [optional] 
**league_id** | **int** |  | 
**league_name** | **str** |  | 
**league_price** | **str** |  | [optional] 
**liability_waiver_id** | **int** |  | 
**liability_waiver_url** | **str** |  | [optional] 
**long_description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**media_id** | **int** |  | 
**media_url** | **str** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**non_member_fee** | **float** |  | 
**player_group** | **str** |  | [optional] 
**refund_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**registered_members** | **int** |  | [optional] 
**registration_date** | **List[str]** |  | 
**registration_date_time** | **List[str]** |  | [optional] 
**registration_date_time_utc** | **List[str]** |  | [optional] 
**registration_status** | **str** |  | [optional] 
**registration_string** | **str** |  | [optional] 
**registration_url** | **str** |  | [optional] 
**safety_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**short_address** | **str** |  | [optional] 
**short_description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**skill_level** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.league_response import LeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueResponse from a JSON string
league_response_instance = LeagueResponse.from_json(json)
# print the JSON string representation of the object
print LeagueResponse.to_json()

# convert the object into a dict
league_response_dict = league_response_instance.to_dict()
# create an instance of LeagueResponse from a dict
league_response_form_dict = league_response.from_dict(league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


