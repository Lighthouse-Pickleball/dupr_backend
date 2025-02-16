# TopicResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | 

## Example

```python
from dupr_backend.models.topic_response import TopicResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TopicResponse from a JSON string
topic_response_instance = TopicResponse.from_json(json)
# print the JSON string representation of the object
print TopicResponse.to_json()

# convert the object into a dict
topic_response_dict = topic_response_instance.to_dict()
# create an instance of TopicResponse from a dict
topic_response_form_dict = topic_response.from_dict(topic_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


