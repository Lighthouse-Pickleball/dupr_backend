# ArrayWrapperOfGeocodingResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**results** | [**List[GeocodingResult]**](GeocodingResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.array_wrapper_of_geocoding_result import ArrayWrapperOfGeocodingResult

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayWrapperOfGeocodingResult from a JSON string
array_wrapper_of_geocoding_result_instance = ArrayWrapperOfGeocodingResult.from_json(json)
# print the JSON string representation of the object
print ArrayWrapperOfGeocodingResult.to_json()

# convert the object into a dict
array_wrapper_of_geocoding_result_dict = array_wrapper_of_geocoding_result_instance.to_dict()
# create an instance of ArrayWrapperOfGeocodingResult from a dict
array_wrapper_of_geocoding_result_form_dict = array_wrapper_of_geocoding_result.from_dict(array_wrapper_of_geocoding_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


