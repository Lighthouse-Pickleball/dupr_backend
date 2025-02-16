# SingleWrapperOfChatTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**ChatTokenResponse**](ChatTokenResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_chat_token_response import SingleWrapperOfChatTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfChatTokenResponse from a JSON string
single_wrapper_of_chat_token_response_instance = SingleWrapperOfChatTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfChatTokenResponse.to_json())

# convert the object into a dict
single_wrapper_of_chat_token_response_dict = single_wrapper_of_chat_token_response_instance.to_dict()
# create an instance of SingleWrapperOfChatTokenResponse from a dict
single_wrapper_of_chat_token_response_from_dict = SingleWrapperOfChatTokenResponse.from_dict(single_wrapper_of_chat_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


