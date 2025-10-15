# dupr_backend.AdminEventApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_league**](AdminEventApi.md#delete_all_league) | **DELETE** /admin/event/{version}/all | 
[**delete_event_players**](AdminEventApi.md#delete_event_players) | **DELETE** /admin/event/player/{version}/all | 
[**force_delete_league**](AdminEventApi.md#force_delete_league) | **DELETE** /admin/event/{version}/{leagueId} | 
[**index_all_leagues**](AdminEventApi.md#index_all_leagues) | **GET** /admin/event/{version}/index | 
[**index_league_players**](AdminEventApi.md#index_league_players) | **GET** /admin/event/player/{version}/index | 
[**index_leagues_by_id**](AdminEventApi.md#index_leagues_by_id) | **GET** /admin/event/{leagueId}/{version}/index | 
[**registered_to_bracket**](AdminEventApi.md#registered_to_bracket) | **POST** /admin/event/{bracketId}/{version}/join | 
[**restore_deleted_league**](AdminEventApi.md#restore_deleted_league) | **POST** /admin/event/{version}/restore/{leagueId} | 
[**update_league_fees**](AdminEventApi.md#update_league_fees) | **PUT** /admin/event/{version}/{leagueId}/fees | 


# **delete_all_league**
> Wrapper delete_all_league(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.delete_all_league(version)
        print("The response of AdminEventApi->delete_all_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->delete_all_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_players**
> Wrapper delete_event_players(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.delete_event_players(version)
        print("The response of AdminEventApi->delete_event_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->delete_event_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_league**
> Wrapper force_delete_league(version, league_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.force_delete_league(version, league_id)
        print("The response of AdminEventApi->force_delete_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->force_delete_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_all_leagues**
> Wrapper index_all_leagues(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.index_all_leagues(version)
        print("The response of AdminEventApi->index_all_leagues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_all_leagues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_league_players**
> Wrapper index_league_players(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.index_league_players(version)
        print("The response of AdminEventApi->index_league_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_league_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_leagues_by_id**
> Wrapper index_leagues_by_id(version, league_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.index_leagues_by_id(version, league_id)
        print("The response of AdminEventApi->index_leagues_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_leagues_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registered_to_bracket**
> SingleWrapperJoinLeagueResponse registered_to_bracket(version, bracket_id, registered_event_admin_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.registered_event_admin_request import RegisteredEventAdminRequest
from dupr_backend.models.single_wrapper_join_league_response import SingleWrapperJoinLeagueResponse
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    bracket_id = 56 # int | 
    registered_event_admin_request = dupr_backend.RegisteredEventAdminRequest() # RegisteredEventAdminRequest | 

    try:
        api_response = api_instance.registered_to_bracket(version, bracket_id, registered_event_admin_request)
        print("The response of AdminEventApi->registered_to_bracket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->registered_to_bracket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **bracket_id** | **int**|  | 
 **registered_event_admin_request** | [**RegisteredEventAdminRequest**](RegisteredEventAdminRequest.md)|  | 

### Return type

[**SingleWrapperJoinLeagueResponse**](SingleWrapperJoinLeagueResponse.md)

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

# **restore_deleted_league**
> Wrapper restore_deleted_league(version, league_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.wrapper import Wrapper
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.restore_deleted_league(version, league_id)
        print("The response of AdminEventApi->restore_deleted_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->restore_deleted_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_league_fees**
> SingleWrapperLeagueResponse update_league_fees(version, league_id, league_fees_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.league_fees_request import LeagueFeesRequest
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 
    league_fees_request = dupr_backend.LeagueFeesRequest() # LeagueFeesRequest | 

    try:
        api_response = api_instance.update_league_fees(version, league_id, league_fees_request)
        print("The response of AdminEventApi->update_league_fees:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->update_league_fees: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 
 **league_fees_request** | [**LeagueFeesRequest**](LeagueFeesRequest.md)|  | 

### Return type

[**SingleWrapperLeagueResponse**](SingleWrapperLeagueResponse.md)

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

