# GetStreamPostResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**get_stream_post_v1** | [**GetStreamPostResponseV1Urn**](GetStreamPostResponseV1Urn.md) |  | 

## Example

```python
from dupr_backend.models.get_stream_post_response import GetStreamPostResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStreamPostResponse from a JSON string
get_stream_post_response_instance = GetStreamPostResponse.from_json(json)
# print the JSON string representation of the object
print(GetStreamPostResponse.to_json())

# convert the object into a dict
get_stream_post_response_dict = get_stream_post_response_instance.to_dict()
# create an instance of GetStreamPostResponse from a dict
get_stream_post_response_from_dict = GetStreamPostResponse.from_dict(get_stream_post_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


