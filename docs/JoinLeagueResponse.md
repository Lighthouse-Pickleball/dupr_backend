# JoinLeagueResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **List[int]** |  | 
**failed** | **List[int]** |  | 
**session** | [**SessionResponse**](SessionResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.join_league_response import JoinLeagueResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JoinLeagueResponse from a JSON string
join_league_response_instance = JoinLeagueResponse.from_json(json)
# print the JSON string representation of the object
print(JoinLeagueResponse.to_json())

# convert the object into a dict
join_league_response_dict = join_league_response_instance.to_dict()
# create an instance of JoinLeagueResponse from a dict
join_league_response_from_dict = JoinLeagueResponse.from_dict(join_league_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


