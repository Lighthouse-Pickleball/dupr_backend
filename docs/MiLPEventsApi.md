# dupr_backend.MiLPEventsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event_info_using_get**](MiLPEventsApi.md#get_event_info_using_get) | **GET** /milp/event/{version}/{id} | getEventInfo
[**get_teams_using_get**](MiLPEventsApi.md#get_teams_using_get) | **GET** /milp/event/{version}/{id}/teams | getTeams
[**register_team_using_post**](MiLPEventsApi.md#register_team_using_post) | **POST** /milp/event/{version}/teams/checkout | registerTeam
[**save_using_post2**](MiLPEventsApi.md#save_using_post2) | **POST** /milp/event/{version}/save | save
[**search_event_using_post**](MiLPEventsApi.md#search_event_using_post) | **POST** /milp/event/{version}/search | searchEvent


# **get_event_info_using_get**
> SingleWrapperOfMiLPEvent get_event_info_using_get(authorization, id, version)

getEventInfo

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_mi_lp_event import SingleWrapperOfMiLPEvent
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getEventInfo
        api_response = api_instance.get_event_info_using_get(authorization, id, version)
        print("The response of MiLPEventsApi->get_event_info_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->get_event_info_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMiLPEvent**](SingleWrapperOfMiLPEvent.md)

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

# **get_teams_using_get**
> ArrayWrapperOfMiLPTeamDivision get_teams_using_get(authorization, id, version)

getTeams

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_mi_lp_team_division import ArrayWrapperOfMiLPTeamDivision
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getTeams
        api_response = api_instance.get_teams_using_get(authorization, id, version)
        print("The response of MiLPEventsApi->get_teams_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->get_teams_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfMiLPTeamDivision**](ArrayWrapperOfMiLPTeamDivision.md)

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

# **register_team_using_post**
> SingleWrapperOfSessionResponse register_team_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)

registerTeam

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_register_team_request import MiLPRegisterTeamRequest
from dupr_backend.models.single_wrapper_of_session_response import SingleWrapperOfSessionResponse
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MiLPRegisterTeamRequest() # MiLPRegisterTeamRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # registerTeam
        api_response = api_instance.register_team_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)
        print("The response of MiLPEventsApi->register_team_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->register_team_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MiLPRegisterTeamRequest**](MiLPRegisterTeamRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

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

# **save_using_post2**
> SingleWrapperOflong save_using_post2(authorization, version, request)

save

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_event_request import MiLPEventRequest
from dupr_backend.models.single_wrapper_oflong import SingleWrapperOflong
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MiLPEventRequest() # MiLPEventRequest | request

    try:
        # save
        api_response = api_instance.save_using_post2(authorization, version, request)
        print("The response of MiLPEventsApi->save_using_post2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->save_using_post2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MiLPEventRequest**](MiLPEventRequest.md)| request | 

### Return type

[**SingleWrapperOflong**](SingleWrapperOflong.md)

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

# **search_event_using_post**
> SingleWrapperOfPageOfMiLPEvent search_event_using_post(authorization, version, request)

searchEvent

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_event_search_request import MiLPEventSearchRequest
from dupr_backend.models.single_wrapper_of_page_of_mi_lp_event import SingleWrapperOfPageOfMiLPEvent
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
    api_instance = dupr_backend.MiLPEventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MiLPEventSearchRequest() # MiLPEventSearchRequest | request

    try:
        # searchEvent
        api_response = api_instance.search_event_using_post(authorization, version, request)
        print("The response of MiLPEventsApi->search_event_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPEventsApi->search_event_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MiLPEventSearchRequest**](MiLPEventSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfMiLPEvent**](SingleWrapperOfPageOfMiLPEvent.md)

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

