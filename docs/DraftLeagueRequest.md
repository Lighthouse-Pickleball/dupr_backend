# DraftLeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | 
**user_id** | **int** |  | 
**league_name** | **str** |  | [optional] 
**media_id** | **int** |  | [optional] 
**liability_waiver_id** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**non_member_fee** | **float** |  | [optional] 
**long_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**short_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**additional_information** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**refund_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**safety_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**advertise_start** | **date** |  | [optional] 
**advertise_end** | **date** |  | [optional] 
**brackets** | [**List[DraftBracketRequest]**](DraftBracketRequest.md) |  | [optional] 
**league_id** | **int** |  | 

## Example

```python
from dupr_backend.models.draft_league_request import DraftLeagueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DraftLeagueRequest from a JSON string
draft_league_request_instance = DraftLeagueRequest.from_json(json)
# print the JSON string representation of the object
print(DraftLeagueRequest.to_json())

# convert the object into a dict
draft_league_request_dict = draft_league_request_instance.to_dict()
# create an instance of DraftLeagueRequest from a dict
draft_league_request_from_dict = DraftLeagueRequest.from_dict(draft_league_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


