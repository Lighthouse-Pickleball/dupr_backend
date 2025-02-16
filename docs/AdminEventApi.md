# dupr_backend.AdminEventApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_all_league_using_delete**](AdminEventApi.md#delete_all_league_using_delete) | **DELETE** /admin/event/{version}/all | deleteAllLeague
[**delete_event_players_using_delete**](AdminEventApi.md#delete_event_players_using_delete) | **DELETE** /admin/event/player/{version}/all | deleteEventPlayers
[**force_delete_league_using_delete**](AdminEventApi.md#force_delete_league_using_delete) | **DELETE** /admin/event/{version}/{leagueId} | forceDeleteLeague
[**index_all_leagues_using_get**](AdminEventApi.md#index_all_leagues_using_get) | **GET** /admin/event/{version}/index | indexAllLeagues
[**index_league_players_using_get**](AdminEventApi.md#index_league_players_using_get) | **GET** /admin/event/player/{version}/index | indexLeaguePlayers
[**index_leagues_by_id_using_get**](AdminEventApi.md#index_leagues_by_id_using_get) | **GET** /admin/event/{leagueId}/{version}/index | indexLeaguesById
[**registered_to_bracket_using_post**](AdminEventApi.md#registered_to_bracket_using_post) | **POST** /admin/event/{bracketId}/{version}/join | registeredToBracket
[**restore_deleted_league_using_post**](AdminEventApi.md#restore_deleted_league_using_post) | **POST** /admin/event/{version}/restore/{leagueId} | restoreDeletedLeague
[**update_league_fees_using_put**](AdminEventApi.md#update_league_fees_using_put) | **PUT** /admin/event/{version}/{leagueId}/fees | updateLeagueFees


# **delete_all_league_using_delete**
> Wrapper delete_all_league_using_delete(authorization, version)

deleteAllLeague

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteAllLeague
        api_response = api_instance.delete_all_league_using_delete(authorization, version)
        print("The response of AdminEventApi->delete_all_league_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->delete_all_league_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_players_using_delete**
> Wrapper delete_event_players_using_delete(authorization, version)

deleteEventPlayers

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteEventPlayers
        api_response = api_instance.delete_event_players_using_delete(authorization, version)
        print("The response of AdminEventApi->delete_event_players_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->delete_event_players_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_league_using_delete**
> Wrapper force_delete_league_using_delete(authorization, league_id, version)

forceDeleteLeague

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # forceDeleteLeague
        api_response = api_instance.force_delete_league_using_delete(authorization, league_id, version)
        print("The response of AdminEventApi->force_delete_league_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->force_delete_league_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_all_leagues_using_get**
> Wrapper index_all_leagues_using_get(authorization, version)

indexAllLeagues

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexAllLeagues
        api_response = api_instance.index_all_leagues_using_get(authorization, version)
        print("The response of AdminEventApi->index_all_leagues_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_all_leagues_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_league_players_using_get**
> Wrapper index_league_players_using_get(authorization, version)

indexLeaguePlayers

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexLeaguePlayers
        api_response = api_instance.index_league_players_using_get(authorization, version)
        print("The response of AdminEventApi->index_league_players_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_league_players_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_leagues_by_id_using_get**
> Wrapper index_leagues_by_id_using_get(authorization, league_id, version)

indexLeaguesById

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexLeaguesById
        api_response = api_instance.index_leagues_by_id_using_get(authorization, league_id, version)
        print("The response of AdminEventApi->index_leagues_by_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->index_leagues_by_id_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registered_to_bracket_using_post**
> SingleWrapperOfJoinLeagueResponse registered_to_bracket_using_post(authorization, bracket_id, version, request)

registeredToBracket

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.registered_event_admin_request import RegisteredEventAdminRequest
from dupr_backend.models.single_wrapper_of_join_league_response import SingleWrapperOfJoinLeagueResponse
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.RegisteredEventAdminRequest() # RegisteredEventAdminRequest | request

    try:
        # registeredToBracket
        api_response = api_instance.registered_to_bracket_using_post(authorization, bracket_id, version, request)
        print("The response of AdminEventApi->registered_to_bracket_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->registered_to_bracket_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**RegisteredEventAdminRequest**](RegisteredEventAdminRequest.md)| request | 

### Return type

[**SingleWrapperOfJoinLeagueResponse**](SingleWrapperOfJoinLeagueResponse.md)

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

# **restore_deleted_league_using_post**
> Wrapper restore_deleted_league_using_post(authorization, league_id, version)

restoreDeletedLeague

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # restoreDeletedLeague
        api_response = api_instance.restore_deleted_league_using_post(authorization, league_id, version)
        print("The response of AdminEventApi->restore_deleted_league_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->restore_deleted_league_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_league_fees_using_put**
> SingleWrapperOfLeagueResponse update_league_fees_using_put(authorization, league_id, version, request)

updateLeagueFees

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.league_fees_request import LeagueFeesRequest
from dupr_backend.models.single_wrapper_of_league_response import SingleWrapperOfLeagueResponse
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
    api_instance = dupr_backend.AdminEventApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueFeesRequest() # LeagueFeesRequest | request

    try:
        # updateLeagueFees
        api_response = api_instance.update_league_fees_using_put(authorization, league_id, version, request)
        print("The response of AdminEventApi->update_league_fees_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminEventApi->update_league_fees_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueFeesRequest**](LeagueFeesRequest.md)| request | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

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

