# ResultBoolean


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | **List[bool]** |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_boolean import ResultBoolean

# TODO update the JSON string below
json = "{}"
# create an instance of ResultBoolean from a JSON string
result_boolean_instance = ResultBoolean.from_json(json)
# print the JSON string representation of the object
print(ResultBoolean.to_json())

# convert the object into a dict
result_boolean_dict = result_boolean_instance.to_dict()
# create an instance of ResultBoolean from a dict
result_boolean_from_dict = ResultBoolean.from_dict(result_boolean_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


