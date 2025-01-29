# dupr_backend.AdminEventApi

All URIs are relative to *https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteAllLeague
    api_response = api_instance.delete_all_league_using_delete(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->delete_all_league_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_event_players_using_delete**
> Wrapper delete_event_players_using_delete(authorization, version)

deleteEventPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteEventPlayers
    api_response = api_instance.delete_event_players_using_delete(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->delete_event_players_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **force_delete_league_using_delete**
> Wrapper force_delete_league_using_delete(authorization, league_id, version)

forceDeleteLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # forceDeleteLeague
    api_response = api_instance.force_delete_league_using_delete(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->force_delete_league_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_all_leagues_using_get**
> Wrapper index_all_leagues_using_get(authorization, version)

indexAllLeagues

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # indexAllLeagues
    api_response = api_instance.index_all_leagues_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->index_all_leagues_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_league_players_using_get**
> Wrapper index_league_players_using_get(authorization, version)

indexLeaguePlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # indexLeaguePlayers
    api_response = api_instance.index_league_players_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->index_league_players_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_leagues_by_id_using_get**
> Wrapper index_leagues_by_id_using_get(authorization, league_id, version)

indexLeaguesById

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # indexLeaguesById
    api_response = api_instance.index_leagues_by_id_using_get(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->index_leagues_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registered_to_bracket_using_post**
> SingleWrapperOfJoinLeagueResponse registered_to_bracket_using_post(body, authorization, bracket_id, version)

registeredToBracket

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
body = dupr_backend.RegisteredEventAdminRequest() # RegisteredEventAdminRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # registeredToBracket
    api_response = api_instance.registered_to_bracket_using_post(body, authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->registered_to_bracket_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisteredEventAdminRequest**](RegisteredEventAdminRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfJoinLeagueResponse**](SingleWrapperOfJoinLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_deleted_league_using_post**
> Wrapper restore_deleted_league_using_post(authorization, league_id, version)

restoreDeletedLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # restoreDeletedLeague
    api_response = api_instance.restore_deleted_league_using_post(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->restore_deleted_league_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_league_fees_using_put**
> SingleWrapperOfLeagueResponse update_league_fees_using_put(body, authorization, league_id, version)

updateLeagueFees

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminEventApi()
body = dupr_backend.LeagueFeesRequest() # LeagueFeesRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # updateLeagueFees
    api_response = api_instance.update_league_fees_using_put(body, authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminEventApi->update_league_fees_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueFeesRequest**](LeagueFeesRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

