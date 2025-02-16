# RatingOverviewResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | [**OverviewResponse**](OverviewResponse.md) |  | 
**doubles** | [**OverviewResponse**](OverviewResponse.md) |  | 
**singles** | [**OverviewResponse**](OverviewResponse.md) |  | 

## Example

```python
from dupr_backend.models.rating_overview_response import RatingOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatingOverviewResponse from a JSON string
rating_overview_response_instance = RatingOverviewResponse.from_json(json)
# print the JSON string representation of the object
print RatingOverviewResponse.to_json()

# convert the object into a dict
rating_overview_response_dict = rating_overview_response_instance.to_dict()
# create an instance of RatingOverviewResponse from a dict
rating_overview_response_form_dict = rating_overview_response.from_dict(rating_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


