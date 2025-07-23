# BulkSetClubRestrictionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clubs** | [**List[SetClubRestrictionsRequest]**](SetClubRestrictionsRequest.md) |  | 

## Example

```python
from dupr_backend.models.bulk_set_club_restrictions_request import BulkSetClubRestrictionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkSetClubRestrictionsRequest from a JSON string
bulk_set_club_restrictions_request_instance = BulkSetClubRestrictionsRequest.from_json(json)
# print the JSON string representation of the object
print(BulkSetClubRestrictionsRequest.to_json())

# convert the object into a dict
bulk_set_club_restrictions_request_dict = bulk_set_club_restrictions_request_instance.to_dict()
# create an instance of BulkSetClubRestrictionsRequest from a dict
bulk_set_club_restrictions_request_from_dict = BulkSetClubRestrictionsRequest.from_dict(bulk_set_club_restrictions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


