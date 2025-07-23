# ResultUnit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_unit import ResultUnit

# TODO update the JSON string below
json = "{}"
# create an instance of ResultUnit from a JSON string
result_unit_instance = ResultUnit.from_json(json)
# print the JSON string representation of the object
print(ResultUnit.to_json())

# convert the object into a dict
result_unit_dict = result_unit_instance.to_dict()
# create an instance of ResultUnit from a dict
result_unit_from_dict = ResultUnit.from_dict(result_unit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


