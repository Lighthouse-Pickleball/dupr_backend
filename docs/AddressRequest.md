# AddressRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address_line** | **str** |  | [optional] 
**geocode** | [**GeocodingResult**](GeocodingResult.md) |  | [optional] 
**place_id** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.address_request import AddressRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AddressRequest from a JSON string
address_request_instance = AddressRequest.from_json(json)
# print the JSON string representation of the object
print AddressRequest.to_json()

# convert the object into a dict
address_request_dict = address_request_instance.to_dict()
# create an instance of AddressRequest from a dict
address_request_form_dict = address_request.from_dict(address_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


