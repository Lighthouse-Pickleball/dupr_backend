# BracketRefundRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bracket_id** | **int** |  | 
**bracket_name** | **str** |  | 
**registration_id** | **int** |  | 
**process_refund** | **bool** |  | 
**withdraw_player** | **bool** |  | 
**refund_amount** | **float** |  | 

## Example

```python
from dupr_backend.models.bracket_refund_request import BracketRefundRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BracketRefundRequest from a JSON string
bracket_refund_request_instance = BracketRefundRequest.from_json(json)
# print the JSON string representation of the object
print(BracketRefundRequest.to_json())

# convert the object into a dict
bracket_refund_request_dict = bracket_refund_request_instance.to_dict()
# create an instance of BracketRefundRequest from a dict
bracket_refund_request_from_dict = BracketRefundRequest.from_dict(bracket_refund_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


