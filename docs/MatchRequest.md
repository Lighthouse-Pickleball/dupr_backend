# MatchRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**club_id** | **int** |  | [optional] 
**event** | **str** |  | [optional] 
**event_date** | **date** |  | 
**format** | **str** |  | 
**league** | **str** |  | [optional] 
**location** | **str** |  | [optional] 
**match_type** | **str** |  | [optional] 
**notify** | **bool** |  | [optional] 
**score_format_id** | **int** |  | [optional] 
**scores** | [**List[PairOfintAndint]**](PairOfintAndint.md) |  | 
**team1** | [**Team**](Team.md) |  | 
**team2** | [**Team**](Team.md) |  | 
**tournament** | **str** |  | [optional] 
**venue** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.match_request import MatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MatchRequest from a JSON string
match_request_instance = MatchRequest.from_json(json)
# print the JSON string representation of the object
print MatchRequest.to_json()

# convert the object into a dict
match_request_dict = match_request_instance.to_dict()
# create an instance of MatchRequest from a dict
match_request_form_dict = match_request.from_dict(match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


