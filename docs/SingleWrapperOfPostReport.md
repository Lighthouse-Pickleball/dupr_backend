# SingleWrapperOfPostReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PostReport**](PostReport.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_post_report import SingleWrapperOfPostReport

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPostReport from a JSON string
single_wrapper_of_post_report_instance = SingleWrapperOfPostReport.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPostReport.to_json())

# convert the object into a dict
single_wrapper_of_post_report_dict = single_wrapper_of_post_report_instance.to_dict()
# create an instance of SingleWrapperOfPostReport from a dict
single_wrapper_of_post_report_from_dict = SingleWrapperOfPostReport.from_dict(single_wrapper_of_post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


