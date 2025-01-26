# dupr_backend.AnnouncementsApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_using_post**](AnnouncementsApi.md#draft_using_post) | **POST** /event/announcement/{version}/draft | draft
[**edit_using_post**](AnnouncementsApi.md#edit_using_post) | **POST** /event/announcement/{version}/edit | edit
[**get_announcements_using_post**](AnnouncementsApi.md#get_announcements_using_post) | **POST** /event/announcement/{version}/all | getAnnouncements
[**save_using_post**](AnnouncementsApi.md#save_using_post) | **POST** /event/announcement/{version}/save | save
[**sent_notification_using_post**](AnnouncementsApi.md#sent_notification_using_post) | **POST** /event/announcement/send/{version}/test | sentNotification

# **draft_using_post**
> Wrapper draft_using_post(body, authorization, version)

draft

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AnnouncementsApi()
body = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # draft
    api_response = api_instance.draft_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnouncementsApi->draft_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_using_post**
> Wrapper edit_using_post(body, authorization, version)

edit

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AnnouncementsApi()
body = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # edit
    api_response = api_instance.edit_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnouncementsApi->edit_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcements_using_post**
> SingleWrapperOfPageOfEventAnnouncementsResponse get_announcements_using_post(body, authorization, version)

getAnnouncements

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AnnouncementsApi()
body = dupr_backend.AnnouncementHistoryRequest() # AnnouncementHistoryRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAnnouncements
    api_response = api_instance.get_announcements_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnouncementsApi->get_announcements_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnouncementHistoryRequest**](AnnouncementHistoryRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfEventAnnouncementsResponse**](SingleWrapperOfPageOfEventAnnouncementsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_using_post**
> Wrapper save_using_post(body, authorization, version)

save

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AnnouncementsApi()
body = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # save
    api_response = api_instance.save_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnouncementsApi->save_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sent_notification_using_post**
> SingleWrapperOfUnit sent_notification_using_post(body, authorization, version)

sentNotification

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AnnouncementsApi()
body = dupr_backend.AnnouncementsNotifications() # AnnouncementsNotifications | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # sentNotification
    api_response = api_instance.sent_notification_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnnouncementsApi->sent_notification_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnnouncementsNotifications**](AnnouncementsNotifications.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

