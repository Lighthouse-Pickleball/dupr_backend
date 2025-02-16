# PostReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count_report** | **int** |  | 
**created_at** | **int** |  | 
**id** | **str** |  | 
**note** | **str** |  | [optional] 
**report_reason** | **str** |  | 
**report_type** | **str** |  | 
**reported_id** | **str** |  | 
**reporter_id** | **int** |  | 
**status** | **str** |  | 
**updated_at** | **int** |  | 

## Example

```python
from dupr_backend.models.post_report import PostReport

# TODO update the JSON string below
json = "{}"
# create an instance of PostReport from a JSON string
post_report_instance = PostReport.from_json(json)
# print the JSON string representation of the object
print PostReport.to_json()

# convert the object into a dict
post_report_dict = post_report_instance.to_dict()
# create an instance of PostReport from a dict
post_report_form_dict = post_report.from_dict(post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


