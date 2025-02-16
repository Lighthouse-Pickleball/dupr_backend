# EmailExistRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 

## Example

```python
from dupr_backend.models.email_exist_request import EmailExistRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EmailExistRequest from a JSON string
email_exist_request_instance = EmailExistRequest.from_json(json)
# print the JSON string representation of the object
print EmailExistRequest.to_json()

# convert the object into a dict
email_exist_request_dict = email_exist_request_instance.to_dict()
# create an instance of EmailExistRequest from a dict
email_exist_request_form_dict = email_exist_request.from_dict(email_exist_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


