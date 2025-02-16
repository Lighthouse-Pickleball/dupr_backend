# RevenueModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from dupr_backend.models.revenue_model import RevenueModel

# TODO update the JSON string below
json = "{}"
# create an instance of RevenueModel from a JSON string
revenue_model_instance = RevenueModel.from_json(json)
# print the JSON string representation of the object
print RevenueModel.to_json()

# convert the object into a dict
revenue_model_dict = revenue_model_instance.to_dict()
# create an instance of RevenueModel from a dict
revenue_model_form_dict = revenue_model.from_dict(revenue_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


