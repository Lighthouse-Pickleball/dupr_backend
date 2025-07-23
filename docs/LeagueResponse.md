# LeagueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **int** |  | 
**club_id** | **int** |  | 
**user_id** | **int** |  | 
**league_name** | **str** |  | 
**media_url** | **str** |  | [optional] 
**liability_waiver_url** | **str** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | 
**membership_permission** | **str** |  | [optional] 
**short_description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**long_description** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**additional_information** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**refund_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**safety_policy** | [**LeagueContentResponse**](LeagueContentResponse.md) |  | [optional] 
**address** | [**AddressResponse**](AddressResponse.md) |  | [optional] 
**duration** | **List[str]** |  | 
**registration_date** | **List[str]** |  | 
**type** | **str** |  | [optional] 
**attributes** | **Dict[str, object]** |  | [optional] 
**brackets** | [**List[BracketResponse]**](BracketResponse.md) |  | 
**status** | **str** |  | [optional] 
**distance** | **str** |  | [optional] 
**distance_in_miles** | **float** |  | [optional] 
**league_price** | **str** |  | [optional] 
**skill_level** | **str** |  | [optional] 
**age_string** | **str** |  | [optional] 
**player_group** | **str** |  | [optional] 
**duration_string** | **str** |  | [optional] 
**registration_string** | **str** |  | [optional] 
**registration_status** | **str** |  | [optional] 
**event_format_string** | **str** |  | [optional] 
**elimination_string** | **str** |  | [optional] 
**short_address** | **str** |  | [optional] 
**club_name** | **str** |  | [optional] 
**contact_details** | [**List[LeagueContactDetailResponse]**](LeagueContactDetailResponse.md) |  | [optional] 
**registered_members** | **int** |  | [optional] 
**duration_status** | **str** |  | [optional] 
**display_status** | **str** |  | [optional] 
**is_registered** | **bool** |  | [optional] 
**can_show_standings** | **bool** |  | [optional] 
**liability_waiver_id** | **int** |  | 
**media_id** | **int** |  | 
**registration_date_time** | **List[str]** |  | [optional] 
**duration_date_time** | **List[str]** |  | [optional] 
**registration_date_time_utc** | **List[str]** |  | [optional] 
**duration_date_time_utc** | **List[str]** |  | [optional] 
**currency_details** | [**CurrencyDetailsResponse**](CurrencyDetailsResponse.md) |  | [optional] 
**registration_url** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | 
**registered** | **bool** |  | [optional] 

## Example

```python
from dupr_backend.models.league_response import LeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueResponse from a JSON string
league_response_instance = LeagueResponse.from_json(json)
# print the JSON string representation of the object
print(LeagueResponse.to_json())

# convert the object into a dict
league_response_dict = league_response_instance.to_dict()
# create an instance of LeagueResponse from a dict
league_response_from_dict = LeagueResponse.from_dict(league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


