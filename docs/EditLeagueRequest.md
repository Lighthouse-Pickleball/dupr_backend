# EditLeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**league_id** | **int** |  | 
**user_id** | **int** |  | 
**league_name** | **str** |  | 
**media_id** | **int** |  | [optional] 
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
**status** | **str** |  | [optional] 
**registration_url** | **str** |  | [optional] 
**start_date** | **date** |  | [optional] 
**end_date** | **date** |  | [optional] 

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


