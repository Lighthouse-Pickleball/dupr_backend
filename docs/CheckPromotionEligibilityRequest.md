# CheckPromotionEligibilityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base64_client_key** | **str** |  | 
**promotion_id** | **str** |  | 

## Example

```python
from dupr_backend.models.check_promotion_eligibility_request import CheckPromotionEligibilityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckPromotionEligibilityRequest from a JSON string
check_promotion_eligibility_request_instance = CheckPromotionEligibilityRequest.from_json(json)
# print the JSON string representation of the object
print(CheckPromotionEligibilityRequest.to_json())

# convert the object into a dict
check_promotion_eligibility_request_dict = check_promotion_eligibility_request_instance.to_dict()
# create an instance of CheckPromotionEligibilityRequest from a dict
check_promotion_eligibility_request_from_dict = CheckPromotionEligibilityRequest.from_dict(check_promotion_eligibility_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


