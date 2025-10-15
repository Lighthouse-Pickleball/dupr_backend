# dupr_backend.OpenPlayApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation**](OpenPlayApi.md#accept_invitation) | **POST** /event/{version}/open-play/{id}/invitation/accept | 
[**create**](OpenPlayApi.md#create) | **POST** /event/{version}/open-play/create | 
[**get_event_detail**](OpenPlayApi.md#get_event_detail) | **GET** /event/{version}/open-play/{id} | 
[**get_events_members**](OpenPlayApi.md#get_events_members) | **GET** /event/{version}/open-play/{id}/participants | 
[**get_events_near_by**](OpenPlayApi.md#get_events_near_by) | **GET** /event/{version}/open-play/near-by | 
[**get_invitation_by_player**](OpenPlayApi.md#get_invitation_by_player) | **GET** /event/{version}/open-play/invitation/player | 
[**get_waitlist_by_player**](OpenPlayApi.md#get_waitlist_by_player) | **GET** /event/{version}/open-play/waitlist/player | 
[**join_waitlist**](OpenPlayApi.md#join_waitlist) | **POST** /event/{version}/open-play/{id}/join-waitlist | 
[**register_event**](OpenPlayApi.md#register_event) | **POST** /event/{version}/open-play/{id}/register | 
[**reject_invitation**](OpenPlayApi.md#reject_invitation) | **POST** /event/{version}/open-play/{id}/invitation/reject | 
[**update**](OpenPlayApi.md#update) | **PUT** /event/{version}/open-play/{id}/{version}/update | 
[**withdraw_event**](OpenPlayApi.md#withdraw_event) | **DELETE** /event/{version}/open-play/{id}/withdraw | 


# **accept_invitation**
> SingleWrapperUnit accept_invitation(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.accept_invitation(version, id)
        print("The response of OpenPlayApi->accept_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->accept_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create**
> SingleWrapperUnit create(version, open_play_create_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.open_play_create_request import OpenPlayCreateRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    open_play_create_request = dupr_backend.OpenPlayCreateRequest() # OpenPlayCreateRequest | 

    try:
        api_response = api_instance.create(version, open_play_create_request)
        print("The response of OpenPlayApi->create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **open_play_create_request** | [**OpenPlayCreateRequest**](OpenPlayCreateRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_detail**
> SingleWrapperOpenPlayEvent get_event_detail(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_open_play_event import SingleWrapperOpenPlayEvent
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.get_event_detail(version, id)
        print("The response of OpenPlayApi->get_event_detail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_event_detail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperOpenPlayEvent**](SingleWrapperOpenPlayEvent.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_members**
> SingleWrapperPageOpenPlayMember get_events_members(version, id, limit, offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_open_play_member import SingleWrapperPageOpenPlayMember
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    limit = 56 # int | 
    offset = 56 # int | 

    try:
        api_response = api_instance.get_events_members(version, id, limit, offset)
        print("The response of OpenPlayApi->get_events_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_events_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **limit** | **int**|  | 
 **offset** | **int**|  | 

### Return type

[**SingleWrapperPageOpenPlayMember**](SingleWrapperPageOpenPlayMember.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_near_by**
> SingleWrapperPageOpenPlayEvent get_events_near_by(version, limit, offset, longitude=longitude, latitude=latitude, radius=radius, query=query)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_open_play_event import SingleWrapperPageOpenPlayEvent
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    limit = 56 # int | 
    offset = 56 # int | 
    longitude = 3.4 # float |  (optional)
    latitude = 3.4 # float |  (optional)
    radius = 3.4 # float |  (optional)
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.get_events_near_by(version, limit, offset, longitude=longitude, latitude=latitude, radius=radius, query=query)
        print("The response of OpenPlayApi->get_events_near_by:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_events_near_by: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **limit** | **int**|  | 
 **offset** | **int**|  | 
 **longitude** | **float**|  | [optional] 
 **latitude** | **float**|  | [optional] 
 **radius** | **float**|  | [optional] 
 **query** | **str**|  | [optional] 

### Return type

[**SingleWrapperPageOpenPlayEvent**](SingleWrapperPageOpenPlayEvent.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_by_player**
> SingleWrapperPagePlayerQueue get_invitation_by_player(version, limit, offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_queue import SingleWrapperPagePlayerQueue
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    limit = 56 # int | 
    offset = 56 # int | 

    try:
        api_response = api_instance.get_invitation_by_player(version, limit, offset)
        print("The response of OpenPlayApi->get_invitation_by_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_invitation_by_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **limit** | **int**|  | 
 **offset** | **int**|  | 

### Return type

[**SingleWrapperPagePlayerQueue**](SingleWrapperPagePlayerQueue.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waitlist_by_player**
> SingleWrapperPagePlayerQueue get_waitlist_by_player(version, limit, offset)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_queue import SingleWrapperPagePlayerQueue
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    limit = 56 # int | 
    offset = 56 # int | 

    try:
        api_response = api_instance.get_waitlist_by_player(version, limit, offset)
        print("The response of OpenPlayApi->get_waitlist_by_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->get_waitlist_by_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **limit** | **int**|  | 
 **offset** | **int**|  | 

### Return type

[**SingleWrapperPagePlayerQueue**](SingleWrapperPagePlayerQueue.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_waitlist**
> SingleWrapperOpenPlayEventWaitlist join_waitlist(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_open_play_event_waitlist import SingleWrapperOpenPlayEventWaitlist
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.join_waitlist(version, id)
        print("The response of OpenPlayApi->join_waitlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->join_waitlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperOpenPlayEventWaitlist**](SingleWrapperOpenPlayEventWaitlist.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_event**
> SingleWrapperUnit register_event(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.register_event(version, id)
        print("The response of OpenPlayApi->register_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->register_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_invitation**
> SingleWrapperUnit reject_invitation(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.reject_invitation(version, id)
        print("The response of OpenPlayApi->reject_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->reject_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> SingleWrapperUnit update(version, id, open_play_update_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.open_play_update_request import OpenPlayUpdateRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    open_play_update_request = dupr_backend.OpenPlayUpdateRequest() # OpenPlayUpdateRequest | 

    try:
        api_response = api_instance.update(version, id, open_play_update_request)
        print("The response of OpenPlayApi->update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **open_play_update_request** | [**OpenPlayUpdateRequest**](OpenPlayUpdateRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_event**
> SingleWrapperUnit withdraw_event(version, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): bearerAuth
configuration = dupr_backend.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.OpenPlayApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.withdraw_event(version, id)
        print("The response of OpenPlayApi->withdraw_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OpenPlayApi->withdraw_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

