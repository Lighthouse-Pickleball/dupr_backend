# OpenPlayCreateRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_id** | **int** |  | 
**description** | **str** |  | [optional] 
**event_date** | **date** |  | 
**invited_players** | **List[str]** |  | [optional] 
**max_players** | **int** |  | 
**name** | **str** |  | 
**rating** | [**RatingRangeReq**](RatingRangeReq.md) |  | 
**time** | [**TimeRangeReq**](TimeRangeReq.md) |  | 

## Example

```python
from dupr_backend.models.open_play_create_request import OpenPlayCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenPlayCreateRequest from a JSON string
open_play_create_request_instance = OpenPlayCreateRequest.from_json(json)
# print the JSON string representation of the object
print OpenPlayCreateRequest.to_json()

# convert the object into a dict
open_play_create_request_dict = open_play_create_request_instance.to_dict()
# create an instance of OpenPlayCreateRequest from a dict
open_play_create_request_form_dict = open_play_create_request.from_dict(open_play_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


