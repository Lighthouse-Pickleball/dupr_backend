# ReactDeleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**react** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.react_delete_request import ReactDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReactDeleteRequest from a JSON string
react_delete_request_instance = ReactDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(ReactDeleteRequest.to_json())

# convert the object into a dict
react_delete_request_dict = react_delete_request_instance.to_dict()
# create an instance of ReactDeleteRequest from a dict
react_delete_request_from_dict = ReactDeleteRequest.from_dict(react_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


