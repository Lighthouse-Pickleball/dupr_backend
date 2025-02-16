# S3Object


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bucket** | **str** |  | 
**key** | **str** |  | 

## Example

```python
from dupr_backend.models.s3_object import S3Object

# TODO update the JSON string below
json = "{}"
# create an instance of S3Object from a JSON string
s3_object_instance = S3Object.from_json(json)
# print the JSON string representation of the object
print S3Object.to_json()

# convert the object into a dict
s3_object_dict = s3_object_instance.to_dict()
# create an instance of S3Object from a dict
s3_object_form_dict = s3_object.from_dict(s3_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


