# dupr_backend.AnnouncementsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft1**](AnnouncementsApi.md#draft1) | **POST** /event/announcement/{version}/draft | 
[**edit**](AnnouncementsApi.md#edit) | **POST** /event/announcement/{version}/edit | 
[**get_announcements**](AnnouncementsApi.md#get_announcements) | **POST** /event/announcement/{version}/all | 
[**save3**](AnnouncementsApi.md#save3) | **POST** /event/announcement/{version}/save | 
[**sent_notification**](AnnouncementsApi.md#sent_notification) | **POST** /event/announcement/send/{version}/test | 


# **draft1**
> Wrapper draft1(version, event_announcement_request)

### Example


```python
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    version = 'version_example' # str | 
    event_announcement_request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | 

    try:
        api_response = api_instance.draft1(version, event_announcement_request)
        print("The response of AnnouncementsApi->draft1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->draft1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **event_announcement_request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit**
> Wrapper edit(version, event_announcement_request)

### Example


```python
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    version = 'version_example' # str | 
    event_announcement_request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | 

    try:
        api_response = api_instance.edit(version, event_announcement_request)
        print("The response of AnnouncementsApi->edit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->edit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **event_announcement_request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcements**
> SingleWrapperPageEventAnnouncementsResponse get_announcements(version, announcement_history_request)

### Example


```python
import dupr_backend
from dupr_backend.models.announcement_history_request import AnnouncementHistoryRequest
from dupr_backend.models.single_wrapper_page_event_announcements_response import SingleWrapperPageEventAnnouncementsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    version = 'version_example' # str | 
    announcement_history_request = dupr_backend.AnnouncementHistoryRequest() # AnnouncementHistoryRequest | 

    try:
        api_response = api_instance.get_announcements(version, announcement_history_request)
        print("The response of AnnouncementsApi->get_announcements:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->get_announcements: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **announcement_history_request** | [**AnnouncementHistoryRequest**](AnnouncementHistoryRequest.md)|  | 

### Return type

[**SingleWrapperPageEventAnnouncementsResponse**](SingleWrapperPageEventAnnouncementsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save3**
> Wrapper save3(version, event_announcement_request)

### Example


```python
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    version = 'version_example' # str | 
    event_announcement_request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | 

    try:
        api_response = api_instance.save3(version, event_announcement_request)
        print("The response of AnnouncementsApi->save3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->save3: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **event_announcement_request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sent_notification**
> SingleWrapperUnit sent_notification(version, announcements_notifications)

### Example


```python
import dupr_backend
from dupr_backend.models.announcements_notifications import AnnouncementsNotifications
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    version = 'version_example' # str | 
    announcements_notifications = dupr_backend.AnnouncementsNotifications() # AnnouncementsNotifications | 

    try:
        api_response = api_instance.sent_notification(version, announcements_notifications)
        print("The response of AnnouncementsApi->sent_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->sent_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **announcements_notifications** | [**AnnouncementsNotifications**](AnnouncementsNotifications.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

