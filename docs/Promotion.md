# Promotion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_discount** | [**DuprDiscount**](DuprDiscount.md) |  | 
**benefactor** | [**Benefactor**](Benefactor.md) |  | 

## Example

```python
from dupr_backend.models.promotion import Promotion

# TODO update the JSON string below
json = "{}"
# create an instance of Promotion from a JSON string
promotion_instance = Promotion.from_json(json)
# print the JSON string representation of the object
print(Promotion.to_json())

# convert the object into a dict
promotion_dict = promotion_instance.to_dict()
# create an instance of Promotion from a dict
promotion_from_dict = Promotion.from_dict(promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


