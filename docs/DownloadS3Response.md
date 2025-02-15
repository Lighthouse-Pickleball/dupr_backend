# DownloadS3Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**s3_url** | **str** |  | 

## Example

```python
from dupr_backend.models.download_s3_response import DownloadS3Response

# TODO update the JSON string below
json = "{}"
# create an instance of DownloadS3Response from a JSON string
download_s3_response_instance = DownloadS3Response.from_json(json)
# print the JSON string representation of the object
print(DownloadS3Response.to_json())

# convert the object into a dict
download_s3_response_dict = download_s3_response_instance.to_dict()
# create an instance of DownloadS3Response from a dict
download_s3_response_from_dict = DownloadS3Response.from_dict(download_s3_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


