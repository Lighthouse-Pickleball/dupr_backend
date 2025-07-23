# UnknownTimestampV1Urn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**path** | **str** |  | 
**type** | **str** |  | 
**version** | **str** |  | 
**id** | **str** |  | 
**nid** | **str** |  | 

## Example

```python
from dupr_backend.models.unknown_timestamp_v1_urn import UnknownTimestampV1Urn

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownTimestampV1Urn from a JSON string
unknown_timestamp_v1_urn_instance = UnknownTimestampV1Urn.from_json(json)
# print the JSON string representation of the object
print(UnknownTimestampV1Urn.to_json())

# convert the object into a dict
unknown_timestamp_v1_urn_dict = unknown_timestamp_v1_urn_instance.to_dict()
# create an instance of UnknownTimestampV1Urn from a dict
unknown_timestamp_v1_urn_from_dict = UnknownTimestampV1Urn.from_dict(unknown_timestamp_v1_urn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


