# PromotionCampaign


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**promotion_id** | **str** |  | 
**name** | **str** |  | 
**criteria** | [**List[CriteriaDefinition]**](CriteriaDefinition.md) |  | 
**products** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.promotion_campaign import PromotionCampaign

# TODO update the JSON string below
json = "{}"
# create an instance of PromotionCampaign from a JSON string
promotion_campaign_instance = PromotionCampaign.from_json(json)
# print the JSON string representation of the object
print(PromotionCampaign.to_json())

# convert the object into a dict
promotion_campaign_dict = promotion_campaign_instance.to_dict()
# create an instance of PromotionCampaign from a dict
promotion_campaign_from_dict = PromotionCampaign.from_dict(promotion_campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


