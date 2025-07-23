# BulkCoppaEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_email** | **str** |  | [optional] 
**dupr_ids** | **List[str]** |  | 

## Example

```python
from dupr_backend.models.bulk_coppa_email_request import BulkCoppaEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkCoppaEmailRequest from a JSON string
bulk_coppa_email_request_instance = BulkCoppaEmailRequest.from_json(json)
# print the JSON string representation of the object
print(BulkCoppaEmailRequest.to_json())

# convert the object into a dict
bulk_coppa_email_request_dict = bulk_coppa_email_request_instance.to_dict()
# create an instance of BulkCoppaEmailRequest from a dict
bulk_coppa_email_request_from_dict = BulkCoppaEmailRequest.from_dict(bulk_coppa_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


