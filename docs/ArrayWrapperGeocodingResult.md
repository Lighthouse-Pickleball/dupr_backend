# ArrayWrapperGeocodingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**results** | [**List[GeocodingResult]**](GeocodingResult.md) |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_geocoding_result import ArrayWrapperGeocodingResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperGeocodingResult from a JSON string
array_wrapper_geocoding_result_instance = ArrayWrapperGeocodingResult.from_json(json)
# print the JSON string representation of the object
print(ArrayWrapperGeocodingResult.to_json())

# convert the object into a dict
array_wrapper_geocoding_result_dict = array_wrapper_geocoding_result_instance.to_dict()
# create an instance of ArrayWrapperGeocodingResult from a dict
array_wrapper_geocoding_result_from_dict = ArrayWrapperGeocodingResult.from_dict(array_wrapper_geocoding_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


