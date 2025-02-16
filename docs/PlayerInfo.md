# PlayerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**initial_rating** | **float** |  | [optional] 
**player_no** | **int** |  | 
**rating_change** | **float** |  | [optional] 
**simulated_rating** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.player_info import PlayerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerInfo from a JSON string
player_info_instance = PlayerInfo.from_json(json)
# print the JSON string representation of the object
print PlayerInfo.to_json()

# convert the object into a dict
player_info_dict = player_info_instance.to_dict()
# create an instance of PlayerInfo from a dict
player_info_form_dict = player_info.from_dict(player_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


