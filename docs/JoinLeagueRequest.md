# JoinLeagueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**is_club_member** | **bool** |  | 
**partner_details** | [**AddPartnerRequest**](AddPartnerRequest.md) |  | [optional] 

## Example

```python
from dupr_backend.models.join_league_request import JoinLeagueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JoinLeagueRequest from a JSON string
join_league_request_instance = JoinLeagueRequest.from_json(json)
# print the JSON string representation of the object
print(JoinLeagueRequest.to_json())

# convert the object into a dict
join_league_request_dict = join_league_request_instance.to_dict()
# create an instance of JoinLeagueRequest from a dict
join_league_request_from_dict = JoinLeagueRequest.from_dict(join_league_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


