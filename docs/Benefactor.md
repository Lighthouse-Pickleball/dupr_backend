# Benefactor


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**display_name** | **str** |  | 

## Example

```python
from dupr_backend.models.benefactor import Benefactor

# TODO update the JSON string below
json = "{}"
# create an instance of Benefactor from a JSON string
benefactor_instance = Benefactor.from_json(json)
# print the JSON string representation of the object
print(Benefactor.to_json())

# convert the object into a dict
benefactor_dict = benefactor_instance.to_dict()
# create an instance of Benefactor from a dict
benefactor_from_dict = Benefactor.from_dict(benefactor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


