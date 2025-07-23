# SingleWrapperChatTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**ChatTokenResponse**](ChatTokenResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_chat_token_response import SingleWrapperChatTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperChatTokenResponse from a JSON string
single_wrapper_chat_token_response_instance = SingleWrapperChatTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperChatTokenResponse.to_json())

# convert the object into a dict
single_wrapper_chat_token_response_dict = single_wrapper_chat_token_response_instance.to_dict()
# create an instance of SingleWrapperChatTokenResponse from a dict
single_wrapper_chat_token_response_from_dict = SingleWrapperChatTokenResponse.from_dict(single_wrapper_chat_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


