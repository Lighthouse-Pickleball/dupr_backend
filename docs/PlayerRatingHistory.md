# PlayerRatingHistory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rating_history_id** | **int** |  | 
**user_id** | **int** |  | 
**user_name** | **str** |  | 
**user_email** | **str** |  | 
**singles** | **float** |  | [optional] 
**singles_provisional** | **bool** |  | 
**doubles** | **float** |  | [optional] 
**doubles_provisional** | **bool** |  | 
**changed_by_admin** | **bool** |  | 
**created** | **datetime** |  | 
**match_date** | **date** |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.player_rating_history import PlayerRatingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingHistory from a JSON string
player_rating_history_instance = PlayerRatingHistory.from_json(json)
# print the JSON string representation of the object
print(PlayerRatingHistory.to_json())

# convert the object into a dict
player_rating_history_dict = player_rating_history_instance.to_dict()
# create an instance of PlayerRatingHistory from a dict
player_rating_history_from_dict = PlayerRatingHistory.from_dict(player_rating_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


