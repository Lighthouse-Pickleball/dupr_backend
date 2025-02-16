# PlayerRatingOvertime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**player_id** | **int** |  | 
**rating_history** | [**List[History]**](History.md) |  | 
**type** | **str** |  | 

## Example

```python
from dupr_backend.models.player_rating_overtime import PlayerRatingOvertime

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingOvertime from a JSON string
player_rating_overtime_instance = PlayerRatingOvertime.from_json(json)
# print the JSON string representation of the object
print(PlayerRatingOvertime.to_json())

# convert the object into a dict
player_rating_overtime_dict = player_rating_overtime_instance.to_dict()
# create an instance of PlayerRatingOvertime from a dict
player_rating_overtime_from_dict = PlayerRatingOvertime.from_dict(player_rating_overtime_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


