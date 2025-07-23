# SingleWrapperIdPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**result** | [**IdPayload**](IdPayload.md) |  | [optional] 

## Example

```python
from dupr_backend.models.single_wrapper_id_payload import SingleWrapperIdPayload

# TODO update the JSON string below
json = "{}"
# create an instance of SingleWrapperIdPayload from a JSON string
single_wrapper_id_payload_instance = SingleWrapperIdPayload.from_json(json)
# print the JSON string representation of the object
print(SingleWrapperIdPayload.to_json())

# convert the object into a dict
single_wrapper_id_payload_dict = single_wrapper_id_payload_instance.to_dict()
# create an instance of SingleWrapperIdPayload from a dict
single_wrapper_id_payload_from_dict = SingleWrapperIdPayload.from_dict(single_wrapper_id_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


