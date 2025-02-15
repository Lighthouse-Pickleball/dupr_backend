# LeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | 
**advertise_end** | **date** |  | [optional] 
**advertise_start** | **date** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**brackets** | [**List[BracketRequest]**](BracketRequest.md) |  | [optional] 
**club_id** | **int** |  | 
**end_date** | **date** |  | 
**league_id** | **int** |  | [optional] 
**league_name** | **str** |  | 
**liability_waiver_id** | **int** |  | [optional] 
**long_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**media_id** | **int** |  | 
**member_fee** | **float** |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**non_member_fee** | **float** |  | 
**refund_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**registration_url** | **str** |  | 
**safety_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**short_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**start_date** | **date** |  | 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** |  | 

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


