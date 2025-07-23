# SingleWrapperRevenueModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**RevenueModel**](RevenueModel.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_revenue_model import SingleWrapperRevenueModel

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperRevenueModel from a JSON string
single_wrapper_revenue_model_instance = SingleWrapperRevenueModel.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperRevenueModel.to_json())

# convert the object into a dict
single_wrapper_revenue_model_dict = single_wrapper_revenue_model_instance.to_dict()
# create an instance of SingleWrapperRevenueModel from a dict
single_wrapper_revenue_model_from_dict = SingleWrapperRevenueModel.from_dict(single_wrapper_revenue_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


