# DeviceRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**platform** | **str** |  | 
**token** | **str** |  | 
**user_id** | **int** |  | [optional] 
**uuid** | **str** |  | 

## Example

```python
from dupr_backend.models.device_request import DeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeviceRequest from a JSON string
device_request_instance = DeviceRequest.from_json(json)
# print the JSON string representation of the object
print DeviceRequest.to_json()

# convert the object into a dict
device_request_dict = device_request_instance.to_dict()
# create an instance of DeviceRequest from a dict
device_request_form_dict = device_request.from_dict(device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


