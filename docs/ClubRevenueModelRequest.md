# ClubRevenueModelRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_type** | **str** |  | 
**value** | **float** |  | 

## Example

```python
from dupr_backend.models.club_revenue_model_request import ClubRevenueModelRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ClubRevenueModelRequest from a JSON string
club_revenue_model_request_instance = ClubRevenueModelRequest.from_json(json)
# print the JSON string representation of the object
print ClubRevenueModelRequest.to_json()

# convert the object into a dict
club_revenue_model_request_dict = club_revenue_model_request_instance.to_dict()
# create an instance of ClubRevenueModelRequest from a dict
club_revenue_model_request_form_dict = club_revenue_model_request.from_dict(club_revenue_model_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


