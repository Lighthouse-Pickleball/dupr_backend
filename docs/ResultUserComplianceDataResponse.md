# ResultUserComplianceDataResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**results** | [**List[UserComplianceDataResponse]**](UserComplianceDataResponse.md) |  | 
**errors** | [**List[Error]**](Error.md) |  | 

## Example

```python
from dupr_backend.models.result_user_compliance_data_response import ResultUserComplianceDataResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ResultUserComplianceDataResponse from a JSON string
result_user_compliance_data_response_instance = ResultUserComplianceDataResponse.from_json(json)
# print the JSON string representation of the object
print(ResultUserComplianceDataResponse.to_json())

# convert the object into a dict
result_user_compliance_data_response_dict = result_user_compliance_data_response_instance.to_dict()
# create an instance of ResultUserComplianceDataResponse from a dict
result_user_compliance_data_response_from_dict = ResultUserComplianceDataResponse.from_dict(result_user_compliance_data_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


