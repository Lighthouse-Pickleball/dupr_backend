# SingleWrapperTopicResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**TopicResponse**](TopicResponse.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_topic_response import SingleWrapperTopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperTopicResponse from a JSON string
single_wrapper_topic_response_instance = SingleWrapperTopicResponse.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperTopicResponse.to_json())

# convert the object into a dict
single_wrapper_topic_response_dict = single_wrapper_topic_response_instance.to_dict()
# create an instance of SingleWrapperTopicResponse from a dict
single_wrapper_topic_response_from_dict = SingleWrapperTopicResponse.from_dict(single_wrapper_topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


