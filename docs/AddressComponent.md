# AddressComponent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**long_name** | **str** |  | [optional] 
**short_name** | **str** |  | [optional] 
**types** | **List[str]** |  | [optional] 

## Example

```python
from dupr_backend.models.address_component import AddressComponent

# TODO update the JSON string below
json = "{}"
# create an instance of AddressComponent from a JSON string
address_component_instance = AddressComponent.from_json(json)
# print the JSON string representation of the object
print(AddressComponent.to_json())

# convert the object into a dict
address_component_dict = address_component_instance.to_dict()
# create an instance of AddressComponent from a dict
address_component_from_dict = AddressComponent.from_dict(address_component_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


