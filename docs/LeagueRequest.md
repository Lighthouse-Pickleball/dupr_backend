# LeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**user_id** | **int** |  | 
**league_name** | **str** |  | 
**media_id** | **int** |  | 
**liability_waiver_id** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | 
**long_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**short_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**additional_information** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**refund_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**safety_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | 
**type** | **str** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**advertise_start** | **date** |  | [optional] 
**advertise_end** | **date** |  | [optional] 
**brackets** | [**List[BracketRequest]**](BracketRequest.md) |  | [optional] 
**league_id** | **int** |  | [optional] 
**status** | **str** |  | [optional] 
**registration_url** | **str** |  | 
**start_date** | **date** |  | 
**end_date** | **date** |  | 

## Example

```python
from dupr_backend.models.league_request import LeagueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueRequest from a JSON string
league_request_instance = LeagueRequest.from_json(json)
# print the JSON string representation of the object
print(LeagueRequest.to_json())

# convert the object into a dict
league_request_dict = league_request_instance.to_dict()
# create an instance of LeagueRequest from a dict
league_request_from_dict = LeagueRequest.from_dict(league_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


