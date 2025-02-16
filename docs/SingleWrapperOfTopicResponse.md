# SingleWrapperOfTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**TopicResponse**](TopicResponse.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_topic_response import SingleWrapperOfTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfTopicResponse from a JSON string
single_wrapper_of_topic_response_instance = SingleWrapperOfTopicResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperOfTopicResponse.to_json())

# convert the object into a dict
single_wrapper_of_topic_response_dict = single_wrapper_of_topic_response_instance.to_dict()
# create an instance of SingleWrapperOfTopicResponse from a dict
single_wrapper_of_topic_response_from_dict = SingleWrapperOfTopicResponse.from_dict(single_wrapper_of_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


