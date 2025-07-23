# GameTrendResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**serial** | **int** |  | 
**month** | **str** |  | [optional] 
**game_won** | **int** |  | 
**game_lost** | **int** |  | 
**total_games** | **int** |  | 

## Example

```python
from dupr_backend.models.game_trend_response import GameTrendResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GameTrendResponse from a JSON string
game_trend_response_instance = GameTrendResponse.from_json(json)
# print the JSON string representation of the object
print(GameTrendResponse.to_json())

# convert the object into a dict
game_trend_response_dict = game_trend_response_instance.to_dict()
# create an instance of GameTrendResponse from a dict
game_trend_response_from_dict = GameTrendResponse.from_dict(game_trend_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


