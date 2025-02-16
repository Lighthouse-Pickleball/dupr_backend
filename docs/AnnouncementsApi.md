# dupr_backend.AnnouncementsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**draft_using_post**](AnnouncementsApi.md#draft_using_post) | **POST** /event/announcement/{version}/draft | draft
[**edit_using_post**](AnnouncementsApi.md#edit_using_post) | **POST** /event/announcement/{version}/edit | edit
[**get_announcements_using_post**](AnnouncementsApi.md#get_announcements_using_post) | **POST** /event/announcement/{version}/all | getAnnouncements
[**save_using_post**](AnnouncementsApi.md#save_using_post) | **POST** /event/announcement/{version}/save | save
[**sent_notification_using_post**](AnnouncementsApi.md#sent_notification_using_post) | **POST** /event/announcement/send/{version}/test | sentNotification


# **draft_using_post**
> Wrapper draft_using_post(authorization, version, request)

draft

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request

    try:
        # draft
        api_response = api_instance.draft_using_post(authorization, version, request)
        print("The response of AnnouncementsApi->draft_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->draft_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_using_post**
> Wrapper edit_using_post(authorization, version, request)

edit

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request

    try:
        # edit
        api_response = api_instance.edit_using_post(authorization, version, request)
        print("The response of AnnouncementsApi->edit_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->edit_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_announcements_using_post**
> SingleWrapperOfPageOfEventAnnouncementsResponse get_announcements_using_post(authorization, version, request)

getAnnouncements

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.announcement_history_request import AnnouncementHistoryRequest
from dupr_backend.models.single_wrapper_of_page_of_event_announcements_response import SingleWrapperOfPageOfEventAnnouncementsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AnnouncementHistoryRequest() # AnnouncementHistoryRequest | request

    try:
        # getAnnouncements
        api_response = api_instance.get_announcements_using_post(authorization, version, request)
        print("The response of AnnouncementsApi->get_announcements_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->get_announcements_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AnnouncementHistoryRequest**](AnnouncementHistoryRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfEventAnnouncementsResponse**](SingleWrapperOfPageOfEventAnnouncementsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_using_post**
> Wrapper save_using_post(authorization, version, request)

save

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.event_announcement_request import EventAnnouncementRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EventAnnouncementRequest() # EventAnnouncementRequest | request

    try:
        # save
        api_response = api_instance.save_using_post(authorization, version, request)
        print("The response of AnnouncementsApi->save_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->save_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EventAnnouncementRequest**](EventAnnouncementRequest.md)| request | 

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sent_notification_using_post**
> SingleWrapperOfUnit sent_notification_using_post(authorization, version, request)

sentNotification

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.announcements_notifications import AnnouncementsNotifications
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://https://backend.mydupr.com
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "http://https://backend.mydupr.com"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.AnnouncementsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AnnouncementsNotifications() # AnnouncementsNotifications | request

    try:
        # sentNotification
        api_response = api_instance.sent_notification_using_post(authorization, version, request)
        print("The response of AnnouncementsApi->sent_notification_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnouncementsApi->sent_notification_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AnnouncementsNotifications**](AnnouncementsNotifications.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

