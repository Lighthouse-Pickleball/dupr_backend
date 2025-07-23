# UserComplianceDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compliance_data** | **Dict[str, str]** |  | 

## Example

```python
from dupr_backend.models.user_compliance_data_response import UserComplianceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UserComplianceDataResponse from a JSON string
user_compliance_data_response_instance = UserComplianceDataResponse.from_json(json)
# print the JSON string representation of the object
print(UserComplianceDataResponse.to_json())

# convert the object into a dict
user_compliance_data_response_dict = user_compliance_data_response_instance.to_dict()
# create an instance of UserComplianceDataResponse from a dict
user_compliance_data_response_from_dict = UserComplianceDataResponse.from_dict(user_compliance_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


