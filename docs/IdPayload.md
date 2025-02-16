# IdPayload


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 

## Example

```python
from dupr_backend.models.id_payload import IdPayload

# TODO update the JSON string below
json = "{}"
# create an instance of IdPayload from a JSON string
id_payload_instance = IdPayload.from_json(json)
# print the JSON string representation of the object
print IdPayload.to_json()

# convert the object into a dict
id_payload_dict = id_payload_instance.to_dict()
# create an instance of IdPayload from a dict
id_payload_form_dict = id_payload.from_dict(id_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


