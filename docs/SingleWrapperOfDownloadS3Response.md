# SingleWrapperOfDownloadS3Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**DownloadS3Response**](DownloadS3Response.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_download_s3_response import SingleWrapperOfDownloadS3Response

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfDownloadS3Response from a JSON string
single_wrapper_of_download_s3_response_instance = SingleWrapperOfDownloadS3Response.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfDownloadS3Response.to_json())

# convert the object into a dict
single_wrapper_of_download_s3_response_dict = single_wrapper_of_download_s3_response_instance.to_dict()
# create an instance of SingleWrapperOfDownloadS3Response from a dict
single_wrapper_of_download_s3_response_from_dict = SingleWrapperOfDownloadS3Response.from_dict(single_wrapper_of_download_s3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


