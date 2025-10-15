# PromotionCampaignRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**client_key_id** | **int** |  | 
**criteria** | [**List[CriteriaDefinition]**](CriteriaDefinition.md) |  | 
**product_ids** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.promotion_campaign_request import PromotionCampaignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PromotionCampaignRequest from a JSON string
promotion_campaign_request_instance = PromotionCampaignRequest.from_json(json)
# print the JSON string representation of the object
print(PromotionCampaignRequest.to_json())

# convert the object into a dict
promotion_campaign_request_dict = promotion_campaign_request_instance.to_dict()
# create an instance of PromotionCampaignRequest from a dict
promotion_campaign_request_from_dict = PromotionCampaignRequest.from_dict(promotion_campaign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


