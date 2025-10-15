# DuprProduct


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_id** | **str** |  | 
**external_product_id** | **str** |  | 
**price_id** | **str** |  | 
**display_name** | **str** |  | 
**price** | **int** |  | 
**period** | **str** |  | 
**promotion** | [**Promotion**](Promotion.md) |  | 

## Example

```python
from dupr_backend.models.dupr_product import DuprProduct

# TODO update the JSON string below
json = "{}"
# create an instance of DuprProduct from a JSON string
dupr_product_instance = DuprProduct.from_json(json)
# print the JSON string representation of the object
print(DuprProduct.to_json())

# convert the object into a dict
dupr_product_dict = dupr_product_instance.to_dict()
# create an instance of DuprProduct from a dict
dupr_product_from_dict = DuprProduct.from_dict(dupr_product_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


