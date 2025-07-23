# AddressResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**address_line** | **str** |  | [optional] 
**short_address** | **str** |  | 
**formatted_address** | **str** |  | 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**place_id** | **str** |  | [optional] 
**precision** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**types** | **str** |  | [optional] 
**create** | **datetime** |  | 

## Example

```python
from dupr_backend.models.address_response import AddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AddressResponse from a JSON string
address_response_instance = AddressResponse.from_json(json)
# print the JSON string representation of the object
print(AddressResponse.to_json())

# convert the object into a dict
address_response_dict = address_response_instance.to_dict()
# create an instance of AddressResponse from a dict
address_response_from_dict = AddressResponse.from_dict(address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


