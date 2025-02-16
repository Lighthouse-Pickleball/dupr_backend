# SingleWrapperOfRevenueModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**RevenueModel**](RevenueModel.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_revenue_model import SingleWrapperOfRevenueModel

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfRevenueModel from a JSON string
single_wrapper_of_revenue_model_instance = SingleWrapperOfRevenueModel.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfRevenueModel.to_json()

# convert the object into a dict
single_wrapper_of_revenue_model_dict = single_wrapper_of_revenue_model_instance.to_dict()
# create an instance of SingleWrapperOfRevenueModel from a dict
single_wrapper_of_revenue_model_form_dict = single_wrapper_of_revenue_model.from_dict(single_wrapper_of_revenue_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


