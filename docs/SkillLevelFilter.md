# SkillLevelFilter


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_rating** | **float** |  | [optional] 
**min_rating** | **float** |  | [optional] 

## Example

```python
from dupr_backend.models.skill_level_filter import SkillLevelFilter

# TODO update the JSON string below
json = "{}"
# create an instance of SkillLevelFilter from a JSON string
skill_level_filter_instance = SkillLevelFilter.from_json(json)
# print the JSON string representation of the object
print SkillLevelFilter.to_json()

# convert the object into a dict
skill_level_filter_dict = skill_level_filter_instance.to_dict()
# create an instance of SkillLevelFilter from a dict
skill_level_filter_form_dict = skill_level_filter.from_dict(skill_level_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


