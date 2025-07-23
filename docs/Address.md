# Address


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**address_line** | **str** |  | [optional] 
**formatted_address** | **str** |  | 
**types** | **str** |  | [optional] 
**place_id** | **str** |  | [optional] 
**precision** | **str** |  | [optional] 
**latitude** | **float** |  | 
**longitude** | **float** |  | 
**components** | [**List[Component]**](Component.md) |  | [optional] 
**status** | **str** |  | [optional] 
**create** | **datetime** |  | [optional] 

## Example

```python
from dupr_backend.models.address import Address

# TODO update the JSON string below
json = "{}"
# create an instance of Address from a JSON string
address_instance = Address.from_json(json)
# print the JSON string representation of the object
print(Address.to_json())

# convert the object into a dict
address_dict = address_instance.to_dict()
# create an instance of Address from a dict
address_from_dict = Address.from_dict(address_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


