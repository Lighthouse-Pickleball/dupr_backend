# Description


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**content_type** | **str** |  | [optional] 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 

## Example

```python
from dupr_backend.models.description import Description

# TODO update the JSON string below
json = "{}"
# create an instance of Description from a JSON string
description_instance = Description.from_json(json)
# print the JSON string representation of the object
print(Description.to_json())

# convert the object into a dict
description_dict = description_instance.to_dict()
# create an instance of Description from a dict
description_from_dict = Description.from_dict(description_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


