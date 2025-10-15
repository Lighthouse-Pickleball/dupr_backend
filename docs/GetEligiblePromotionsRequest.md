# GetEligiblePromotionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_client_key** | **str** |  | 

## Example

```python
from dupr_backend.models.get_eligible_promotions_request import GetEligiblePromotionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetEligiblePromotionsRequest from a JSON string
get_eligible_promotions_request_instance = GetEligiblePromotionsRequest.from_json(json)
# print the JSON string representation of the object
print(GetEligiblePromotionsRequest.to_json())

# convert the object into a dict
get_eligible_promotions_request_dict = get_eligible_promotions_request_instance.to_dict()
# create an instance of GetEligiblePromotionsRequest from a dict
get_eligible_promotions_request_from_dict = GetEligiblePromotionsRequest.from_dict(get_eligible_promotions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


