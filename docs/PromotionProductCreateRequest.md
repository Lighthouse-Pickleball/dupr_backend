# PromotionProductCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**products** | [**List[ProductRequest]**](ProductRequest.md) |  | 

## Example

```python
from dupr_backend.models.promotion_product_create_request import PromotionProductCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromotionProductCreateRequest from a JSON string
promotion_product_create_request_instance = PromotionProductCreateRequest.from_json(json)
# print the JSON string representation of the object
print(PromotionProductCreateRequest.to_json())

# convert the object into a dict
promotion_product_create_request_dict = promotion_product_create_request_instance.to_dict()
# create an instance of PromotionProductCreateRequest from a dict
promotion_product_create_request_from_dict = PromotionProductCreateRequest.from_dict(promotion_product_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


