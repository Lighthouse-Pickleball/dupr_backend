# InstagramRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**token** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.instagram_request import InstagramRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstagramRequest from a JSON string
instagram_request_instance = InstagramRequest.from_json(json)
# print the JSON string representation of the object
print InstagramRequest.to_json()

# convert the object into a dict
instagram_request_dict = instagram_request_instance.to_dict()
# create an instance of InstagramRequest from a dict
instagram_request_form_dict = instagram_request.from_dict(instagram_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


