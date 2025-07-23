# OpenPlayUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**event_date** | **date** |  | 
**time** | [**TimeRange**](TimeRange.md) |  | 
**address_id** | **int** |  | 
**status** | **str** |  | 
**rating** | [**RatingRange**](RatingRange.md) |  | 
**description** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.open_play_update_request import OpenPlayUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayUpdateRequest from a JSON string
open_play_update_request_instance = OpenPlayUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OpenPlayUpdateRequest.to_json())

# convert the object into a dict
open_play_update_request_dict = open_play_update_request_instance.to_dict()
# create an instance of OpenPlayUpdateRequest from a dict
open_play_update_request_from_dict = OpenPlayUpdateRequest.from_dict(open_play_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


