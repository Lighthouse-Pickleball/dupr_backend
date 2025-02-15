# Bounds


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**northeast** | [**LatLng**](LatLng.md) |  | [optional] 
**southwest** | [**LatLng**](LatLng.md) |  | [optional] 

## Example

```python
from dupr_backend.models.bounds import Bounds

# TODO update the JSON string below
json = "{}"
# create an instance of Bounds from a JSON string
bounds_instance = Bounds.from_json(json)
# print the JSON string representation of the object
print(Bounds.to_json())

# convert the object into a dict
bounds_dict = bounds_instance.to_dict()
# create an instance of Bounds from a dict
bounds_from_dict = Bounds.from_dict(bounds_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


