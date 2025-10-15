# dupr_backend.EventsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_event**](EventsApi.md#checkout_event) | **GET** /event/{leagueId}/{version}/checkout | 
[**delete_league**](EventsApi.md#delete_league) | **DELETE** /event/{version}/{leagueId} | 
[**delete_text_content**](EventsApi.md#delete_text_content) | **DELETE** /event/{version}/media | 
[**draft**](EventsApi.md#draft) | **POST** /event/{version}/draft | 
[**edit_league**](EventsApi.md#edit_league) | **PUT** /event/{version}/edit | 
[**end_league**](EventsApi.md#end_league) | **GET** /event/{leagueId}/{version}/end | 
[**export_event_participants**](EventsApi.md#export_event_participants) | **GET** /event/{leagueId}/participant/{version}/export | 
[**export_event_payments**](EventsApi.md#export_event_payments) | **POST** /event/director/participant/payment/{version}/export | 
[**get_all_event_players**](EventsApi.md#get_all_event_players) | **POST** /event/director/participant/{version}/all | 
[**get_city_autocomplete**](EventsApi.md#get_city_autocomplete) | **GET** /event/city/{version}/autocomplete | 
[**get_club_leagues**](EventsApi.md#get_club_leagues) | **GET** /event/club/{version}/{clubId} | 
[**get_league**](EventsApi.md#get_league) | **GET** /event/{version}/{leagueId} | 
[**get_league_policy**](EventsApi.md#get_league_policy) | **GET** /event/policy/{version}/content | 
[**get_leagues_by_user_id**](EventsApi.md#get_leagues_by_user_id) | **POST** /event/{version}/user/{id} | 
[**get_my_leagues**](EventsApi.md#get_my_leagues) | **POST** /event/{version}/all | 
[**join_event**](EventsApi.md#join_event) | **POST** /event/{leagueId}/{version}/join | 
[**register_event1**](EventsApi.md#register_event1) | **POST** /event/{leagueId}/{version}/checkout | 
[**save2**](EventsApi.md#save2) | **POST** /event/{version}/save | 
[**search_leagues**](EventsApi.md#search_leagues) | **POST** /event/{version}/search | 


# **checkout_event**
> SingleWrapperSessionResponse checkout_event(version, league_id)

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.checkout_event(version, league_id)
        print("The response of EventsApi->checkout_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->checkout_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**SingleWrapperSessionResponse**](SingleWrapperSessionResponse.md)

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

# **delete_league**
> Wrapper delete_league(version, league_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.delete_league(version, league_id)
        print("The response of EventsApi->delete_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **delete_text_content**
> Wrapper delete_text_content(version, delete_event_media_request)

### Example


```python
import dupr_backend
from dupr_backend.models.delete_event_media_request import DeleteEventMediaRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    delete_event_media_request = dupr_backend.DeleteEventMediaRequest() # DeleteEventMediaRequest | 

    try:
        api_response = api_instance.delete_text_content(version, delete_event_media_request)
        print("The response of EventsApi->delete_text_content:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_text_content: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **delete_event_media_request** | [**DeleteEventMediaRequest**](DeleteEventMediaRequest.md)|  | 

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

# **draft**
> Wrapper draft(version, draft_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.draft_league_request import DraftLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    draft_league_request = dupr_backend.DraftLeagueRequest() # DraftLeagueRequest | 

    try:
        api_response = api_instance.draft(version, draft_league_request)
        print("The response of EventsApi->draft:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->draft: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **draft_league_request** | [**DraftLeagueRequest**](DraftLeagueRequest.md)|  | 

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

# **edit_league**
> SingleWrapperLeagueResponse edit_league(version, edit_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_league_request import EditLeagueRequest
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    edit_league_request = dupr_backend.EditLeagueRequest() # EditLeagueRequest | 

    try:
        api_response = api_instance.edit_league(version, edit_league_request)
        print("The response of EventsApi->edit_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->edit_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **edit_league_request** | [**EditLeagueRequest**](EditLeagueRequest.md)|  | 

### Return type

[**SingleWrapperLeagueResponse**](SingleWrapperLeagueResponse.md)

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

# **end_league**
> Wrapper end_league(version, league_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.end_league(version, league_id)
        print("The response of EventsApi->end_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->end_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **export_event_participants**
> SingleWrapperDownloadS3Response export_event_participants(version, league_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_download_s3_response import SingleWrapperDownloadS3Response
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.export_event_participants(version, league_id)
        print("The response of EventsApi->export_event_participants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->export_event_participants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**SingleWrapperDownloadS3Response**](SingleWrapperDownloadS3Response.md)

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

# **export_event_payments**
> SingleWrapperDownloadS3Response export_event_payments(version, export_event_payment_request)

### Example


```python
import dupr_backend
from dupr_backend.models.export_event_payment_request import ExportEventPaymentRequest
from dupr_backend.models.single_wrapper_download_s3_response import SingleWrapperDownloadS3Response
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    export_event_payment_request = dupr_backend.ExportEventPaymentRequest() # ExportEventPaymentRequest | 

    try:
        api_response = api_instance.export_event_payments(version, export_event_payment_request)
        print("The response of EventsApi->export_event_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->export_event_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **export_event_payment_request** | [**ExportEventPaymentRequest**](ExportEventPaymentRequest.md)|  | 

### Return type

[**SingleWrapperDownloadS3Response**](SingleWrapperDownloadS3Response.md)

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

# **get_all_event_players**
> SingleWrapperPagePlayerPaymentResponse get_all_event_players(version, offset, limit, search_league_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_page_player_payment_response import SingleWrapperPagePlayerPaymentResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    offset = 56 # int | 
    limit = 56 # int | 
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | 

    try:
        api_response = api_instance.get_all_event_players(version, offset, limit, search_league_player_request)
        print("The response of EventsApi->get_all_event_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_all_event_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerPaymentResponse**](SingleWrapperPagePlayerPaymentResponse.md)

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

# **get_city_autocomplete**
> ArrayWrapperString get_city_autocomplete(version, search=search)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_string import ArrayWrapperString
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    search = 'search_example' # str |  (optional)

    try:
        api_response = api_instance.get_city_autocomplete(version, search=search)
        print("The response of EventsApi->get_city_autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_city_autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **search** | **str**|  | [optional] 

### Return type

[**ArrayWrapperString**](ArrayWrapperString.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_leagues**
> SingleWrapperPageLeagueResponse get_club_leagues(version, club_id, offset, limit, include_draft_events=include_draft_events)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_response import SingleWrapperPageLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 
    include_draft_events = True # bool |  (optional)

    try:
        api_response = api_instance.get_club_leagues(version, club_id, offset, limit, include_draft_events=include_draft_events)
        print("The response of EventsApi->get_club_leagues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_club_leagues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **include_draft_events** | **bool**|  | [optional] 

### Return type

[**SingleWrapperPageLeagueResponse**](SingleWrapperPageLeagueResponse.md)

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

# **get_league**
> SingleWrapperLeagueResponse get_league(version, league_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.get_league(version, league_id)
        print("The response of EventsApi->get_league:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_league: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**SingleWrapperLeagueResponse**](SingleWrapperLeagueResponse.md)

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

# **get_league_policy**
> SingleWrapperPolicyDetailsResponse get_league_policy(version, league_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_policy_details_response import SingleWrapperPolicyDetailsResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 

    try:
        api_response = api_instance.get_league_policy(version, league_id)
        print("The response of EventsApi->get_league_policy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_league_policy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 

### Return type

[**SingleWrapperPolicyDetailsResponse**](SingleWrapperPolicyDetailsResponse.md)

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

# **get_leagues_by_user_id**
> SingleWrapperPageLeagueResponse get_leagues_by_user_id(version, id, my_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.my_league_request import MyLeagueRequest
from dupr_backend.models.single_wrapper_page_league_response import SingleWrapperPageLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    my_league_request = dupr_backend.MyLeagueRequest() # MyLeagueRequest | 

    try:
        api_response = api_instance.get_leagues_by_user_id(version, id, my_league_request)
        print("The response of EventsApi->get_leagues_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_leagues_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **my_league_request** | [**MyLeagueRequest**](MyLeagueRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueResponse**](SingleWrapperPageLeagueResponse.md)

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

# **get_my_leagues**
> SingleWrapperPageLeagueResponse get_my_leagues(version, my_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.my_league_request import MyLeagueRequest
from dupr_backend.models.single_wrapper_page_league_response import SingleWrapperPageLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    my_league_request = dupr_backend.MyLeagueRequest() # MyLeagueRequest | 

    try:
        api_response = api_instance.get_my_leagues(version, my_league_request)
        print("The response of EventsApi->get_my_leagues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_my_leagues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **my_league_request** | [**MyLeagueRequest**](MyLeagueRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueResponse**](SingleWrapperPageLeagueResponse.md)

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

# **join_event**
> SingleWrapperJoinLeagueResponse join_event(version, league_id, join_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.join_league_request import JoinLeagueRequest
from dupr_backend.models.single_wrapper_join_league_response import SingleWrapperJoinLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 
    join_league_request = [dupr_backend.JoinLeagueRequest()] # List[JoinLeagueRequest] | 

    try:
        api_response = api_instance.join_event(version, league_id, join_league_request)
        print("The response of EventsApi->join_event:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->join_event: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 
 **join_league_request** | [**List[JoinLeagueRequest]**](JoinLeagueRequest.md)|  | 

### Return type

[**SingleWrapperJoinLeagueResponse**](SingleWrapperJoinLeagueResponse.md)

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

# **register_event1**
> SingleWrapperSessionResponse register_event1(version, league_id, join_league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.join_league_request import JoinLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_id = 56 # int | 
    join_league_request = [dupr_backend.JoinLeagueRequest()] # List[JoinLeagueRequest] | 

    try:
        api_response = api_instance.register_event1(version, league_id, join_league_request)
        print("The response of EventsApi->register_event1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->register_event1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_id** | **int**|  | 
 **join_league_request** | [**List[JoinLeagueRequest]**](JoinLeagueRequest.md)|  | 

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

# **save2**
> Wrapper save2(version, league_request)

### Example


```python
import dupr_backend
from dupr_backend.models.league_request import LeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    league_request = dupr_backend.LeagueRequest() # LeagueRequest | 

    try:
        api_response = api_instance.save2(version, league_request)
        print("The response of EventsApi->save2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->save2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **league_request** | [**LeagueRequest**](LeagueRequest.md)|  | 

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

# **search_leagues**
> SingleWrapperPageLeagueResponse search_leagues(version, search_leagues_request)

### Example


```python
import dupr_backend
from dupr_backend.models.search_leagues_request import SearchLeaguesRequest
from dupr_backend.models.single_wrapper_page_league_response import SingleWrapperPageLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    search_leagues_request = dupr_backend.SearchLeaguesRequest() # SearchLeaguesRequest | 

    try:
        api_response = api_instance.search_leagues(version, search_leagues_request)
        print("The response of EventsApi->search_leagues:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->search_leagues: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **search_leagues_request** | [**SearchLeaguesRequest**](SearchLeaguesRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueResponse**](SingleWrapperPageLeagueResponse.md)

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

