# Urn


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
from dupr_backend.models.urn import Urn

# TODO update the JSON string below
json = "{}"
# create an instance of Urn from a JSON string
urn_instance = Urn.from_json(json)
# print the JSON string representation of the object
print(Urn.to_json())

# convert the object into a dict
urn_dict = urn_instance.to_dict()
# create an instance of Urn from a dict
urn_from_dict = Urn.from_dict(urn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


