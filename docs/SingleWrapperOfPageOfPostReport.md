# SingleWrapperOfPageOfPostReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**PageOfPostReport**](PageOfPostReport.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_page_of_post_report import SingleWrapperOfPageOfPostReport

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfPageOfPostReport from a JSON string
single_wrapper_of_page_of_post_report_instance = SingleWrapperOfPageOfPostReport.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfPageOfPostReport.to_json())

# convert the object into a dict
single_wrapper_of_page_of_post_report_dict = single_wrapper_of_page_of_post_report_instance.to_dict()
# create an instance of SingleWrapperOfPageOfPostReport from a dict
single_wrapper_of_page_of_post_report_from_dict = SingleWrapperOfPageOfPostReport.from_dict(single_wrapper_of_page_of_post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


