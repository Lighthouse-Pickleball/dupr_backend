# DraftLeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | [optional] 
**advertise_end** | **date** |  | [optional] 
**advertise_start** | **date** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**brackets** | [**List[DraftBracketRequest]**](DraftBracketRequest.md) |  | [optional] 
**club_id** | **int** |  | 
**league_id** | **int** |  | 
**league_name** | **str** |  | [optional] 
**liability_waiver_id** | **int** |  | [optional] 
**long_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**media_id** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**non_member_fee** | **float** |  | [optional] 
**refund_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**safety_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**short_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** |  | 

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


