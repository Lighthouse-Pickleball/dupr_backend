# DuprDiscount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**price_reduction** | **int** |  | 
**trial_days** | **int** |  | 

## Example

```python
from dupr_backend.models.dupr_discount import DuprDiscount

# TODO update the JSON string below
json = "{}"
# create an instance of DuprDiscount from a JSON string
dupr_discount_instance = DuprDiscount.from_json(json)
# print the JSON string representation of the object
print(DuprDiscount.to_json())

# convert the object into a dict
dupr_discount_dict = dupr_discount_instance.to_dict()
# create an instance of DuprDiscount from a dict
dupr_discount_from_dict = DuprDiscount.from_dict(dupr_discount_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


