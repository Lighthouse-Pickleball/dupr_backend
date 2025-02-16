# GeocodingResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_components** | [**List[AddressComponent]**](AddressComponent.md) |  | [optional] 
**formatted_address** | **str** |  | [optional] 
**geometry** | [**Geometry**](Geometry.md) |  | [optional] 
**partial_match** | **bool** |  | [optional] 
**place_id** | **str** |  | [optional] 
**plus_code** | [**PlusCode**](PlusCode.md) |  | [optional] 
**postcode_localities** | **List[str]** |  | [optional] 
**types** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.geocoding_result import GeocodingResult

# TODO update the JSON string below
json = "{}"
# create an instance of GeocodingResult from a JSON string
geocoding_result_instance = GeocodingResult.from_json(json)
# print the JSON string representation of the object
print GeocodingResult.to_json()

# convert the object into a dict
geocoding_result_dict = geocoding_result_instance.to_dict()
# create an instance of GeocodingResult from a dict
geocoding_result_form_dict = geocoding_result.from_dict(geocoding_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


