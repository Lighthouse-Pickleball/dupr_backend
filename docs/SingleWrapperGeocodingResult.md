# SingleWrapperGeocodingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**GeocodingResult**](GeocodingResult.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_geocoding_result import SingleWrapperGeocodingResult

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperGeocodingResult from a JSON string
single_wrapper_geocoding_result_instance = SingleWrapperGeocodingResult.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperGeocodingResult.to_json())

# convert the object into a dict
single_wrapper_geocoding_result_dict = single_wrapper_geocoding_result_instance.to_dict()
# create an instance of SingleWrapperGeocodingResult from a dict
single_wrapper_geocoding_result_from_dict = SingleWrapperGeocodingResult.from_dict(single_wrapper_geocoding_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


