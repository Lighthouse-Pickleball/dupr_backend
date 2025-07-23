# SingleWrapperPostReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**PostReport**](PostReport.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_post_report import SingleWrapperPostReport

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperPostReport from a JSON string
single_wrapper_post_report_instance = SingleWrapperPostReport.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperPostReport.to_json())

# convert the object into a dict
single_wrapper_post_report_dict = single_wrapper_post_report_instance.to_dict()
# create an instance of SingleWrapperPostReport from a dict
single_wrapper_post_report_from_dict = SingleWrapperPostReport.from_dict(single_wrapper_post_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


