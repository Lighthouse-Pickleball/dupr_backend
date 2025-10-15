# ProductRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_product_id** | **str** |  | 
**price_id** | **str** |  | 
**display_name** | **str** |  | 
**price** | **int** |  | 
**period** | **str** |  | 
**promotion** | [**Promotion**](Promotion.md) |  | 

## Example

```python
from dupr_backend.models.product_request import ProductRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProductRequest from a JSON string
product_request_instance = ProductRequest.from_json(json)
# print the JSON string representation of the object
print(ProductRequest.to_json())

# convert the object into a dict
product_request_dict = product_request_instance.to_dict()
# create an instance of ProductRequest from a dict
product_request_from_dict = ProductRequest.from_dict(product_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


