# OpenPlayEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creator** | [**Creator**](Creator.md) |  | 
**var_date** | **str** |  | 
**description** | **str** |  | [optional] 
**id** | **int** |  | 
**location** | **str** |  | [optional] 
**max_players** | **int** |  | 
**name** | **str** |  | [optional] 
**rating** | [**RatingRangeRes**](RatingRangeRes.md) |  | [optional] 
**registered_players** | **int** |  | [optional] 
**time** | [**TimeRangeRes**](TimeRangeRes.md) |  | 

## Example

```python
from dupr_backend.models.open_play_event import OpenPlayEvent

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayEvent from a JSON string
open_play_event_instance = OpenPlayEvent.from_json(json)
# print the JSON string representation of the object
print(OpenPlayEvent.to_json())

# convert the object into a dict
open_play_event_dict = open_play_event_instance.to_dict()
# create an instance of OpenPlayEvent from a dict
open_play_event_from_dict = OpenPlayEvent.from_dict(open_play_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


