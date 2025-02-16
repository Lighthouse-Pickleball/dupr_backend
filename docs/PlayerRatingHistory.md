# PlayerRatingHistory


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changed_by_admin** | **bool** |  | 
**created** | **str** |  | 
**doubles** | **float** |  | [optional] 
**doubles_provisional** | **bool** |  | 
**match_date** | **str** |  | [optional] 
**rating_history_id** | **int** |  | 
**singles** | **float** |  | [optional] 
**singles_provisional** | **bool** |  | 
**status** | **str** |  | [optional] 
**user_email** | **str** |  | 
**user_id** | **int** |  | 
**user_name** | **str** |  | 

## Example

```python
from dupr_backend.models.player_rating_history import PlayerRatingHistory

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerRatingHistory from a JSON string
player_rating_history_instance = PlayerRatingHistory.from_json(json)
# print the JSON string representation of the object
print PlayerRatingHistory.to_json()

# convert the object into a dict
player_rating_history_dict = player_rating_history_instance.to_dict()
# create an instance of PlayerRatingHistory from a dict
player_rating_history_form_dict = player_rating_history.from_dict(player_rating_history_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


