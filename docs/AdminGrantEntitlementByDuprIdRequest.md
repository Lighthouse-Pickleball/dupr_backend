# AdminGrantEntitlementByDuprIdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dupr_ids** | **List[str]** |  | 
**entitlements** | **List[str]** |  | 
**end_date** | **int** |  | 
**club_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.admin_grant_entitlement_by_dupr_id_request import AdminGrantEntitlementByDuprIdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdminGrantEntitlementByDuprIdRequest from a JSON string
admin_grant_entitlement_by_dupr_id_request_instance = AdminGrantEntitlementByDuprIdRequest.from_json(json)
# print the JSON string representation of the object
print(AdminGrantEntitlementByDuprIdRequest.to_json())

# convert the object into a dict
admin_grant_entitlement_by_dupr_id_request_dict = admin_grant_entitlement_by_dupr_id_request_instance.to_dict()
# create an instance of AdminGrantEntitlementByDuprIdRequest from a dict
admin_grant_entitlement_by_dupr_id_request_from_dict = AdminGrantEntitlementByDuprIdRequest.from_dict(admin_grant_entitlement_by_dupr_id_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


