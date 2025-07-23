# AgeFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_age** | **float** |  | 
**max_age** | **float** |  | 

## Example

```python
from dupr_backend.models.age_filter import AgeFilter

# TODO update the JSON string below
json = "{}"
# create an instance of AgeFilter from a JSON string
age_filter_instance = AgeFilter.from_json(json)
# print the JSON string representation of the object
print(AgeFilter.to_json())

# convert the object into a dict
age_filter_dict = age_filter_instance.to_dict()
# create an instance of AgeFilter from a dict
age_filter_from_dict = AgeFilter.from_dict(age_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


