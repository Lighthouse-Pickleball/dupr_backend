# PlayerRatingHistoryOvertimeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | Match event format | 
**start_date** | **date** | Start date | [optional] 
**end_date** | **date** | End date | [optional] 
**limit** | **int** | Data limitation | [optional] 
**offset** | **int** | Data offset | [optional] 
**sort_by** | **str** | Sort by type | [optional] 

## Example

```python
from dupr_backend.models.player_rating_history_overtime_request import PlayerRatingHistoryOvertimeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingHistoryOvertimeRequest from a JSON string
player_rating_history_overtime_request_instance = PlayerRatingHistoryOvertimeRequest.from_json(json)
# print the JSON string representation of the object
print(PlayerRatingHistoryOvertimeRequest.to_json())

# convert the object into a dict
player_rating_history_overtime_request_dict = player_rating_history_overtime_request_instance.to_dict()
# create an instance of PlayerRatingHistoryOvertimeRequest from a dict
player_rating_history_overtime_request_from_dict = PlayerRatingHistoryOvertimeRequest.from_dict(player_rating_history_overtime_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


