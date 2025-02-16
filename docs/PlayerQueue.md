# PlayerQueue


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create_at** | **str** |  | [optional] 
**event** | [**OpenPlayEvent**](OpenPlayEvent.md) |  | [optional] 

## Example

```python
from dupr_backend.models.player_queue import PlayerQueue

# TODO update the JSON string below
json = "{}"
# create an instance of PlayerQueue from a JSON string
player_queue_instance = PlayerQueue.from_json(json)
# print the JSON string representation of the object
print PlayerQueue.to_json()

# convert the object into a dict
player_queue_dict = player_queue_instance.to_dict()
# create an instance of PlayerQueue from a dict
player_queue_form_dict = player_queue.from_dict(player_queue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


