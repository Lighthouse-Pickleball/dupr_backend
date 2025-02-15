# FacebookRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.facebook_request import FacebookRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FacebookRequest from a JSON string
facebook_request_instance = FacebookRequest.from_json(json)
# print the JSON string representation of the object
print(FacebookRequest.to_json())

# convert the object into a dict
facebook_request_dict = facebook_request_instance.to_dict()
# create an instance of FacebookRequest from a dict
facebook_request_from_dict = FacebookRequest.from_dict(facebook_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


