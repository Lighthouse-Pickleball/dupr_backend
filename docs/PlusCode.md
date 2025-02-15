# PlusCode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compound_code** | **str** |  | [optional] 
**global_code** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.plus_code import PlusCode

# TODO update the JSON string below
json = "{}"
# create an instance of PlusCode from a JSON string
plus_code_instance = PlusCode.from_json(json)
# print the JSON string representation of the object
print(PlusCode.to_json())

# convert the object into a dict
plus_code_dict = plus_code_instance.to_dict()
# create an instance of PlusCode from a dict
plus_code_from_dict = PlusCode.from_dict(plus_code_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


