# SingleWrapperPagePostReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PagePostReport**](PagePostReport.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_page_post_report import SingleWrapperPagePostReport

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPagePostReport from a JSON string
single_wrapper_page_post_report_instance = SingleWrapperPagePostReport.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPagePostReport.to_json())

# convert the object into a dict
single_wrapper_page_post_report_dict = single_wrapper_page_post_report_instance.to_dict()
# create an instance of SingleWrapperPagePostReport from a dict
single_wrapper_page_post_report_from_dict = SingleWrapperPagePostReport.from_dict(single_wrapper_page_post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


