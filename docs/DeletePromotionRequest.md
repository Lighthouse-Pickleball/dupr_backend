# DeletePromotionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **str** |  | 

## Example

```python
from dupr_backend.models.delete_promotion_request import DeletePromotionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePromotionRequest from a JSON string
delete_promotion_request_instance = DeletePromotionRequest.from_json(json)
# print the JSON string representation of the object
print(DeletePromotionRequest.to_json())

# convert the object into a dict
delete_promotion_request_dict = delete_promotion_request_instance.to_dict()
# create an instance of DeletePromotionRequest from a dict
delete_promotion_request_from_dict = DeletePromotionRequest.from_dict(delete_promotion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


