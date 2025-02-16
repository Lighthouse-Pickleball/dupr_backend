# SingleWrapperOfIdPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**result** | [**IdPayload**](IdPayload.md) |  | [optional] 
**status** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_of_id_payload import SingleWrapperOfIdPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperOfIdPayload from a JSON string
single_wrapper_of_id_payload_instance = SingleWrapperOfIdPayload.from_json(json)
# print the JSON string representation of the object
print SingleWrapperOfIdPayload.to_json()

# convert the object into a dict
single_wrapper_of_id_payload_dict = single_wrapper_of_id_payload_instance.to_dict()
# create an instance of SingleWrapperOfIdPayload from a dict
single_wrapper_of_id_payload_form_dict = single_wrapper_of_id_payload.from_dict(single_wrapper_of_id_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


