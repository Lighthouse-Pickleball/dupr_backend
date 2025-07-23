# AnnouncementContent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**header** | **str** |  | [optional] 
**header_type** | **str** |  | [optional] 
**content** | **str** |  | 
**content_type** | **str** |  | 
**footer** | **str** |  | [optional] 
**footer_type** | **str** |  | [optional] 
**content_id** | **int** |  | [optional] 

## Example

```python
from dupr_backend.models.announcement_content import AnnouncementContent

# TODO update the JSON string below
json = "{}"
# create an instance of AnnouncementContent from a JSON string
announcement_content_instance = AnnouncementContent.from_json(json)
# print the JSON string representation of the object
print(AnnouncementContent.to_json())

# convert the object into a dict
announcement_content_dict = announcement_content_instance.to_dict()
# create an instance of AnnouncementContent from a dict
announcement_content_from_dict = AnnouncementContent.from_dict(announcement_content_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


