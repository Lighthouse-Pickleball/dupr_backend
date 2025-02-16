# LeagueFeesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_fee** | **float** |  | 
**non_member_fee** | **float** |  | 

## Example

```python
from dupr_backend.models.league_fees_request import LeagueFeesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LeagueFeesRequest from a JSON string
league_fees_request_instance = LeagueFeesRequest.from_json(json)
# print the JSON string representation of the object
print(LeagueFeesRequest.to_json())

# convert the object into a dict
league_fees_request_dict = league_fees_request_instance.to_dict()
# create an instance of LeagueFeesRequest from a dict
league_fees_request_from_dict = LeagueFeesRequest.from_dict(league_fees_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


