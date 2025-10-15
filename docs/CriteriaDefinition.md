# CriteriaDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**operator** | **str** |  | 
**value** | **str** |  | 
**data_type** | **str** |  | 

## Example

```python
from dupr_backend.models.criteria_definition import CriteriaDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of CriteriaDefinition from a JSON string
criteria_definition_instance = CriteriaDefinition.from_json(json)
# print the JSON string representation of the object
print(CriteriaDefinition.to_json())

# convert the object into a dict
criteria_definition_dict = criteria_definition_instance.to_dict()
# create an instance of CriteriaDefinition from a dict
criteria_definition_from_dict = CriteriaDefinition.from_dict(criteria_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


