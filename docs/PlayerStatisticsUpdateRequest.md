# PlayerStatisticsUpdateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doubles** | [**MatchRatings**](MatchRatings.md) |  | [optional] 
**obfuscated_player_id** | **int** |  | 
**singles** | [**MatchRatings**](MatchRatings.md) |  | [optional] 

## Example

```python
from dupr_backend.models.player_statistics_update_request import PlayerStatisticsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerStatisticsUpdateRequest from a JSON string
player_statistics_update_request_instance = PlayerStatisticsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print PlayerStatisticsUpdateRequest.to_json()

# convert the object into a dict
player_statistics_update_request_dict = player_statistics_update_request_instance.to_dict()
# create an instance of PlayerStatisticsUpdateRequest from a dict
player_statistics_update_request_form_dict = player_statistics_update_request.from_dict(player_statistics_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


