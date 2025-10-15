# ResultString


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | **List[str]** |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_string import ResultString

# TODO update the JSON string below
json = "{}"
# create an instance of ResultString from a JSON string
result_string_instance = ResultString.from_json(json)
# print the JSON string representation of the object
print(ResultString.to_json())

# convert the object into a dict
result_string_dict = result_string_instance.to_dict()
# create an instance of ResultString from a dict
result_string_from_dict = ResultString.from_dict(result_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


