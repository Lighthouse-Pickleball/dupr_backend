# dupr_backend.OpenPlayApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation_using_post**](OpenPlayApi.md#accept_invitation_using_post) | **POST** /event/{version}/open-play/{id}/invitation/accept | acceptInvitation
[**create_using_post**](OpenPlayApi.md#create_using_post) | **POST** /event/{version}/open-play/create | create
[**get_event_detail_using_get**](OpenPlayApi.md#get_event_detail_using_get) | **GET** /event/{version}/open-play/{id} | getEventDetail
[**get_events_members_using_get**](OpenPlayApi.md#get_events_members_using_get) | **GET** /event/{version}/open-play/{id}/participants | getEventsMembers
[**get_events_near_by_using_get**](OpenPlayApi.md#get_events_near_by_using_get) | **GET** /event/{version}/open-play/near-by | getEventsNearBy
[**get_invitation_by_player_using_get**](OpenPlayApi.md#get_invitation_by_player_using_get) | **GET** /event/{version}/open-play/invitation/player | getInvitationByPlayer
[**get_waitlist_by_player_using_get**](OpenPlayApi.md#get_waitlist_by_player_using_get) | **GET** /event/{version}/open-play/waitlist/player | getWaitlistByPlayer
[**join_waitlist_using_post**](OpenPlayApi.md#join_waitlist_using_post) | **POST** /event/{version}/open-play/{id}/join-waitlist | joinWaitlist
[**register_event_using_post1**](OpenPlayApi.md#register_event_using_post1) | **POST** /event/{version}/open-play/{id}/register | registerEvent
[**reject_invitation_using_post**](OpenPlayApi.md#reject_invitation_using_post) | **POST** /event/{version}/open-play/{id}/invitation/reject | rejectInvitation
[**update_using_put**](OpenPlayApi.md#update_using_put) | **PUT** /event/{version}/open-play/{id}/{version}/update | update
[**withdraw_event_using_delete**](OpenPlayApi.md#withdraw_event_using_delete) | **DELETE** /event/{version}/open-play/{id}/withdraw | withdrawEvent


# **accept_invitation_using_post**
> SingleWrapperOfUnit accept_invitation_using_post(authorization, id, version)

acceptInvitation

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # acceptInvitation
        api_response = api_instance.accept_invitation_using_post(authorization, id, version)
        print("The response of OpenPlayApi->accept_invitation_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->accept_invitation_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post**
> SingleWrapperOfUnit create_using_post(authorization, version, request)

create

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.open_play_create_request import OpenPlayCreateRequest
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.OpenPlayCreateRequest() # OpenPlayCreateRequest | request

    try:
        # create
        api_response = api_instance.create_using_post(authorization, version, request)
        print("The response of OpenPlayApi->create_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->create_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**OpenPlayCreateRequest**](OpenPlayCreateRequest.md)| request | 

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

# **get_event_detail_using_get**
> SingleWrapperOfOpenPlayEvent get_event_detail_using_get(authorization, id, version)

getEventDetail

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_open_play_event import SingleWrapperOfOpenPlayEvent
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getEventDetail
        api_response = api_instance.get_event_detail_using_get(authorization, id, version)
        print("The response of OpenPlayApi->get_event_detail_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_event_detail_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfOpenPlayEvent**](SingleWrapperOfOpenPlayEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_members_using_get**
> SingleWrapperOfPageOfOpenPlayMember get_events_members_using_get(authorization, id, limit, offset, version)

getEventsMembers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_open_play_member import SingleWrapperOfPageOfOpenPlayMember
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getEventsMembers
        api_response = api_instance.get_events_members_using_get(authorization, id, limit, offset, version)
        print("The response of OpenPlayApi->get_events_members_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_events_members_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfOpenPlayMember**](SingleWrapperOfPageOfOpenPlayMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_near_by_using_get**
> SingleWrapperOfPageOfOpenPlayEvent get_events_near_by_using_get(authorization, limit, offset, version, latitude=latitude, longitude=longitude, query=query, radius=radius)

getEventsNearBy

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_open_play_event import SingleWrapperOfPageOfOpenPlayEvent
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    latitude = 3.4 # float | latitude (optional)
    longitude = 3.4 # float | longitude (optional)
    query = 'query_example' # str | query (optional)
    radius = 3.4 # float | radius (optional)

    try:
        # getEventsNearBy
        api_response = api_instance.get_events_near_by_using_get(authorization, limit, offset, version, latitude=latitude, longitude=longitude, query=query, radius=radius)
        print("The response of OpenPlayApi->get_events_near_by_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_events_near_by_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **latitude** | **float**| latitude | [optional] 
 **longitude** | **float**| longitude | [optional] 
 **query** | **str**| query | [optional] 
 **radius** | **float**| radius | [optional] 

### Return type

[**SingleWrapperOfPageOfOpenPlayEvent**](SingleWrapperOfPageOfOpenPlayEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_by_player_using_get**
> SingleWrapperOfPageOfPlayerQueue get_invitation_by_player_using_get(authorization, limit, offset, version)

getInvitationByPlayer

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_queue import SingleWrapperOfPageOfPlayerQueue
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getInvitationByPlayer
        api_response = api_instance.get_invitation_by_player_using_get(authorization, limit, offset, version)
        print("The response of OpenPlayApi->get_invitation_by_player_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_invitation_by_player_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfPlayerQueue**](SingleWrapperOfPageOfPlayerQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waitlist_by_player_using_get**
> SingleWrapperOfPageOfPlayerQueue get_waitlist_by_player_using_get(authorization, limit, offset, version)

getWaitlistByPlayer

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_queue import SingleWrapperOfPageOfPlayerQueue
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getWaitlistByPlayer
        api_response = api_instance.get_waitlist_by_player_using_get(authorization, limit, offset, version)
        print("The response of OpenPlayApi->get_waitlist_by_player_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_waitlist_by_player_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfPlayerQueue**](SingleWrapperOfPageOfPlayerQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_waitlist_using_post**
> SingleWrapperOfOpenPlayEventWaitlist join_waitlist_using_post(authorization, id, version)

joinWaitlist

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_open_play_event_waitlist import SingleWrapperOfOpenPlayEventWaitlist
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # joinWaitlist
        api_response = api_instance.join_waitlist_using_post(authorization, id, version)
        print("The response of OpenPlayApi->join_waitlist_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->join_waitlist_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfOpenPlayEventWaitlist**](SingleWrapperOfOpenPlayEventWaitlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_event_using_post1**
> SingleWrapperOfUnit register_event_using_post1(authorization, id, version)

registerEvent

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # registerEvent
        api_response = api_instance.register_event_using_post1(authorization, id, version)
        print("The response of OpenPlayApi->register_event_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->register_event_using_post1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_invitation_using_post**
> SingleWrapperOfUnit reject_invitation_using_post(authorization, id, version)

rejectInvitation

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # rejectInvitation
        api_response = api_instance.reject_invitation_using_post(authorization, id, version)
        print("The response of OpenPlayApi->reject_invitation_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->reject_invitation_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put**
> SingleWrapperOfUnit update_using_put(authorization, id, version, request)

update

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.open_play_update_request import OpenPlayUpdateRequest
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.OpenPlayUpdateRequest() # OpenPlayUpdateRequest | request

    try:
        # update
        api_response = api_instance.update_using_put(authorization, id, version, request)
        print("The response of OpenPlayApi->update_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->update_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**OpenPlayUpdateRequest**](OpenPlayUpdateRequest.md)| request | 

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

# **withdraw_event_using_delete**
> SingleWrapperOfUnit withdraw_event_using_delete(authorization, id, version)

withdrawEvent

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.OpenPlayApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # withdrawEvent
        api_response = api_instance.withdraw_event_using_delete(authorization, id, version)
        print("The response of OpenPlayApi->withdraw_event_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->withdraw_event_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

