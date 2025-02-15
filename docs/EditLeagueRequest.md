# EditLeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**additional_information** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**address_id** | **int** |  | 
**advertise_end** | **date** |  | [optional] 
**advertise_start** | **date** |  | [optional] 
**attributes** | [**Dict[str, Attribute]**](Attribute.md) |  | [optional] 
**league_id** | **int** |  | 
**league_name** | **str** |  | 
**liability_waiver_id** | **int** |  | [optional] 
**long_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**media_id** | **int** |  | [optional] 
**member_fee** | **float** |  | [optional] 
**membership_permission** | **str** |  | [optional] 
**non_member_fee** | **float** |  | 
**refund_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**registration_url** | **str** |  | [optional] 
**safety_policy** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**short_description** | [**LeagueContentRequest**](LeagueContentRequest.md) |  | [optional] 
**status** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**user_id** | **int** |  | 

## Example

```python
from dupr_backend.models.edit_league_request import EditLeagueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EditLeagueRequest from a JSON string
edit_league_request_instance = EditLeagueRequest.from_json(json)
# print the JSON string representation of the object
print(EditLeagueRequest.to_json())

# convert the object into a dict
edit_league_request_dict = edit_league_request_instance.to_dict()
# create an instance of EditLeagueRequest from a dict
edit_league_request_from_dict = EditLeagueRequest.from_dict(edit_league_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


