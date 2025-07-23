# MatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**venue** | **str** | Since 2022, we are only using location field based on autocomplete | [optional] 
**location** | **str** |  | [optional] 
**tournament** | **str** |  | [optional] 
**league** | **str** |  | [optional] 
**event_date** | **date** |  | 
**team1** | [**Team**](Team.md) |  | 
**team2** | [**Team**](Team.md) |  | 
**score_format_id** | **int** |  | [optional] 
**format** | **str** |  | 
**event** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**club_id** | **int** |  | [optional] 
**notify** | **bool** |  | 
**scores** | [**List[PairIntegerInteger]**](PairIntegerInteger.md) |  | 

## Example

```python
from dupr_backend.models.match_request import MatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRequest from a JSON string
match_request_instance = MatchRequest.from_json(json)
# print the JSON string representation of the object
print(MatchRequest.to_json())

# convert the object into a dict
match_request_dict = match_request_instance.to_dict()
# create an instance of MatchRequest from a dict
match_request_from_dict = MatchRequest.from_dict(match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


