# OverviewResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**all** | **int** |  | 
**wins** | **int** |  | 
**losses** | **int** |  | 
**pending** | **int** |  | 

## Example

```python
from dupr_backend.models.overview_response import OverviewResponse

# TODO update the JSON string below
json = "{}"
# create an instance of OverviewResponse from a JSON string
overview_response_instance = OverviewResponse.from_json(json)
# print the JSON string representation of the object
print(OverviewResponse.to_json())

# convert the object into a dict
overview_response_dict = overview_response_instance.to_dict()
# create an instance of OverviewResponse from a dict
overview_response_from_dict = OverviewResponse.from_dict(overview_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


