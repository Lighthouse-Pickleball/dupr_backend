# dupr_backend.MiLPEventsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_info**](MiLPEventsApi.md#get_event_info) | **GET** /milp/event/{version}/{id} | 
[**get_teams**](MiLPEventsApi.md#get_teams) | **GET** /milp/event/{version}/{id}/teams | 
[**register_team**](MiLPEventsApi.md#register_team) | **POST** /milp/event/{version}/teams/checkout | 
[**save1**](MiLPEventsApi.md#save1) | **POST** /milp/event/{version}/save | 
[**search_event**](MiLPEventsApi.md#search_event) | **POST** /milp/event/{version}/search | 


# **get_event_info**
> SingleWrapperMiLPEvent get_event_info(version, id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_mi_lp_event import SingleWrapperMiLPEvent
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.get_event_info(version, id)
        print("The response of MiLPEventsApi->get_event_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->get_event_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**SingleWrapperMiLPEvent**](SingleWrapperMiLPEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams**
> ArrayWrapperMiLPTeamDivision get_teams(version, id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_mi_lp_team_division import ArrayWrapperMiLPTeamDivision
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 

    try:
        api_response = api_instance.get_teams(version, id)
        print("The response of MiLPEventsApi->get_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->get_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 

### Return type

[**ArrayWrapperMiLPTeamDivision**](ArrayWrapperMiLPTeamDivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_team**
> SingleWrapperSessionResponse register_team(version, mi_lp_register_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_register_team_request import MiLPRegisterTeamRequest
from dupr_backend.models.single_wrapper_session_response import SingleWrapperSessionResponse
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    mi_lp_register_team_request = dupr_backend.MiLPRegisterTeamRequest() # MiLPRegisterTeamRequest | 

    try:
        api_response = api_instance.register_team(version, mi_lp_register_team_request)
        print("The response of MiLPEventsApi->register_team:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->register_team: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **mi_lp_register_team_request** | [**MiLPRegisterTeamRequest**](MiLPRegisterTeamRequest.md)|  | 

### Return type

[**SingleWrapperSessionResponse**](SingleWrapperSessionResponse.md)

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

# **save1**
> SingleWrapperLong save1(version, mi_lp_event_request)

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_event_request import MiLPEventRequest
from dupr_backend.models.single_wrapper_long import SingleWrapperLong
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    mi_lp_event_request = dupr_backend.MiLPEventRequest() # MiLPEventRequest | 

    try:
        api_response = api_instance.save1(version, mi_lp_event_request)
        print("The response of MiLPEventsApi->save1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->save1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **mi_lp_event_request** | [**MiLPEventRequest**](MiLPEventRequest.md)|  | 

### Return type

[**SingleWrapperLong**](SingleWrapperLong.md)

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

# **search_event**
> SingleWrapperPageMiLPEvent search_event(version, mi_lp_event_search_request)

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_event_search_request import MiLPEventSearchRequest
from dupr_backend.models.single_wrapper_page_mi_lp_event import SingleWrapperPageMiLPEvent
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    mi_lp_event_search_request = dupr_backend.MiLPEventSearchRequest() # MiLPEventSearchRequest | 

    try:
        api_response = api_instance.search_event(version, mi_lp_event_search_request)
        print("The response of MiLPEventsApi->search_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->search_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **mi_lp_event_search_request** | [**MiLPEventSearchRequest**](MiLPEventSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageMiLPEvent**](SingleWrapperPageMiLPEvent.md)

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

