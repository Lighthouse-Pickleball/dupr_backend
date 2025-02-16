# ShareMatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.share_match_request import ShareMatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ShareMatchRequest from a JSON string
share_match_request_instance = ShareMatchRequest.from_json(json)
# print the JSON string representation of the object
print(ShareMatchRequest.to_json())

# convert the object into a dict
share_match_request_dict = share_match_request_instance.to_dict()
# create an instance of ShareMatchRequest from a dict
share_match_request_from_dict = ShareMatchRequest.from_dict(share_match_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


