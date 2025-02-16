# CheckInLocation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | [**AddressRequest**](AddressRequest.md) |  | [optional] 
**id** | **int** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.check_in_location import CheckInLocation

# TODO update the JSON string below
json = "{}"
# create an instance of CheckInLocation from a JSON string
check_in_location_instance = CheckInLocation.from_json(json)
# print the JSON string representation of the object
print CheckInLocation.to_json()

# convert the object into a dict
check_in_location_dict = check_in_location_instance.to_dict()
# create an instance of CheckInLocation from a dict
check_in_location_form_dict = check_in_location.from_dict(check_in_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


