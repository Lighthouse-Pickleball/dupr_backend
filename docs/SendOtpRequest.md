# SendOtpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number** | **str** |  | 

## Example

```python
from dupr_backend.models.send_otp_request import SendOtpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendOtpRequest from a JSON string
send_otp_request_instance = SendOtpRequest.from_json(json)
# print the JSON string representation of the object
print(SendOtpRequest.to_json())

# convert the object into a dict
send_otp_request_dict = send_otp_request_instance.to_dict()
# create an instance of SendOtpRequest from a dict
send_otp_request_from_dict = SendOtpRequest.from_dict(send_otp_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


