# PostReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**reporter_id** | **int** |  | 
**reported_id** | **str** |  | 
**report_type** | **str** |  | 
**report_reason** | **str** |  | 
**note** | **str** |  | [optional] 
**status** | **str** |  | 
**created_at** | **int** |  | 
**updated_at** | **int** |  | 
**count_report** | **int** |  | 

## Example

```python
from dupr_backend.models.post_report import PostReport

# TODO update the JSON string below
json = "{}"
# create an instance of PostReport from a JSON string
post_report_instance = PostReport.from_json(json)
# print the JSON string representation of the object
print(PostReport.to_json())

# convert the object into a dict
post_report_dict = post_report_instance.to_dict()
# create an instance of PostReport from a dict
post_report_from_dict = PostReport.from_dict(post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


