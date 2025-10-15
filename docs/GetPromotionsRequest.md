# GetPromotionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**promotion_id** | **str** |  | 

## Example

```python
from dupr_backend.models.get_promotions_request import GetPromotionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetPromotionsRequest from a JSON string
get_promotions_request_instance = GetPromotionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetPromotionsRequest.to_json())

# convert the object into a dict
get_promotions_request_dict = get_promotions_request_instance.to_dict()
# create an instance of GetPromotionsRequest from a dict
get_promotions_request_from_dict = GetPromotionsRequest.from_dict(get_promotions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


