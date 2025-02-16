# TimeRangeReq


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **str** |  | 
**start** | **str** |  | 

## Example

```python
from dupr_backend.models.time_range_req import TimeRangeReq

# TODO update the JSON string below
json = "{}"
# create an instance of TimeRangeReq from a JSON string
time_range_req_instance = TimeRangeReq.from_json(json)
# print the JSON string representation of the object
print TimeRangeReq.to_json()

# convert the object into a dict
time_range_req_dict = time_range_req_instance.to_dict()
# create an instance of TimeRangeReq from a dict
time_range_req_form_dict = time_range_req.from_dict(time_range_req_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


