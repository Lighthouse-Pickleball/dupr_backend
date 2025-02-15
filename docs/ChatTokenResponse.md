# ChatTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**full_name** | **str** |  | 
**id** | **int** |  | [optional] 
**image_url** | **str** |  | [optional] 
**token** | **str** |  | 

## Example

```python
from dupr_backend.models.chat_token_response import ChatTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChatTokenResponse from a JSON string
chat_token_response_instance = ChatTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ChatTokenResponse.to_json())

# convert the object into a dict
chat_token_response_dict = chat_token_response_instance.to_dict()
# create an instance of ChatTokenResponse from a dict
chat_token_response_from_dict = ChatTokenResponse.from_dict(chat_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


