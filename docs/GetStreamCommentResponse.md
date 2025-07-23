# GetStreamCommentResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_stream_comment_v1** | [**GetStreamCommentResponseV1Urn**](GetStreamCommentResponseV1Urn.md) |  | 

## Example

```python
from dupr_backend.models.get_stream_comment_response import GetStreamCommentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStreamCommentResponse from a JSON string
get_stream_comment_response_instance = GetStreamCommentResponse.from_json(json)
# print the JSON string representation of the object
print(GetStreamCommentResponse.to_json())

# convert the object into a dict
get_stream_comment_response_dict = get_stream_comment_response_instance.to_dict()
# create an instance of GetStreamCommentResponse from a dict
get_stream_comment_response_from_dict = GetStreamCommentResponse.from_dict(get_stream_comment_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


