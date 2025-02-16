# EventFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**distance** | [**Distance**](Distance.md) |  | [optional] 
**division** | **str** |  | [optional] 
**geo_point** | [**GeoPoint**](GeoPoint.md) |  | [optional] 
**name** | **str** |  | [optional] 
**place_id** | **str** |  | [optional] 
**statuses** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.event_filter import EventFilter

# TODO update the JSON string below
json = "{}"
# create an instance of EventFilter from a JSON string
event_filter_instance = EventFilter.from_json(json)
# print the JSON string representation of the object
print EventFilter.to_json()

# convert the object into a dict
event_filter_dict = event_filter_instance.to_dict()
# create an instance of EventFilter from a dict
event_filter_form_dict = event_filter.from_dict(event_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


