# SingleWrapperOfGeocodingResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**GeocodingResult**](GeocodingResult.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_geocoding_result import SingleWrapperOfGeocodingResult

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfGeocodingResult from a JSON string
single_wrapper_of_geocoding_result_instance = SingleWrapperOfGeocodingResult.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfGeocodingResult.to_json())

# convert the object into a dict
single_wrapper_of_geocoding_result_dict = single_wrapper_of_geocoding_result_instance.to_dict()
# create an instance of SingleWrapperOfGeocodingResult from a dict
single_wrapper_of_geocoding_result_from_dict = SingleWrapperOfGeocodingResult.from_dict(single_wrapper_of_geocoding_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


