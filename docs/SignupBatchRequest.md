# SignupBatchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document** | **bytearray** |  | 

## Example

```python
from dupr_backend.models.signup_batch_request import SignupBatchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SignupBatchRequest from a JSON string
signup_batch_request_instance = SignupBatchRequest.from_json(json)
# print the JSON string representation of the object
print(SignupBatchRequest.to_json())

# convert the object into a dict
signup_batch_request_dict = signup_batch_request_instance.to_dict()
# create an instance of SignupBatchRequest from a dict
signup_batch_request_from_dict = SignupBatchRequest.from_dict(signup_batch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


