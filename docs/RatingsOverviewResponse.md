# RatingsOverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**losses** | **int** |  | 
**pending** | **int** |  | 
**wins** | **int** |  | 

## Example

```python
from dupr_backend.models.ratings_overview_response import RatingsOverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of RatingsOverviewResponse from a JSON string
ratings_overview_response_instance = RatingsOverviewResponse.from_json(json)
# print the JSON string representation of the object
print(RatingsOverviewResponse.to_json())

# convert the object into a dict
ratings_overview_response_dict = ratings_overview_response_instance.to_dict()
# create an instance of RatingsOverviewResponse from a dict
ratings_overview_response_from_dict = RatingsOverviewResponse.from_dict(ratings_overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


