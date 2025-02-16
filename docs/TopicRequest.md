# TopicRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**functions** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from dupr_backend.models.topic_request import TopicRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TopicRequest from a JSON string
topic_request_instance = TopicRequest.from_json(json)
# print the JSON string representation of the object
print(TopicRequest.to_json())

# convert the object into a dict
topic_request_dict = topic_request_instance.to_dict()
# create an instance of TopicRequest from a dict
topic_request_from_dict = TopicRequest.from_dict(topic_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


