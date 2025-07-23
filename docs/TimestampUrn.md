# TimestampUrn


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
from dupr_backend.models.timestamp_urn import TimestampUrn

# TODO update the JSON string below
json = "{}"
# create an instance of TimestampUrn from a JSON string
timestamp_urn_instance = TimestampUrn.from_json(json)
# print the JSON string representation of the object
print(TimestampUrn.to_json())

# convert the object into a dict
timestamp_urn_dict = timestamp_urn_instance.to_dict()
# create an instance of TimestampUrn from a dict
timestamp_urn_from_dict = TimestampUrn.from_dict(timestamp_urn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


