# dupr_backend.EventsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**checkout_event_using_get**](EventsApi.md#checkout_event_using_get) | **GET** /event/{leagueId}/{version}/checkout | checkoutEvent
[**delete_league_using_delete1**](EventsApi.md#delete_league_using_delete1) | **DELETE** /event/{version}/{leagueId} | deleteLeague
[**delete_text_content_using_delete**](EventsApi.md#delete_text_content_using_delete) | **DELETE** /event/{version}/media | deleteTextContent
[**draft_using_post1**](EventsApi.md#draft_using_post1) | **POST** /event/{version}/draft | draft
[**edit_league_using_put**](EventsApi.md#edit_league_using_put) | **PUT** /event/{version}/edit | editLeague
[**end_league_using_get1**](EventsApi.md#end_league_using_get1) | **GET** /event/{leagueId}/{version}/end | endLeague
[**export_event_participants_using_get**](EventsApi.md#export_event_participants_using_get) | **GET** /event/{leagueId}/participant/{version}/export | exportEventParticipants
[**export_event_payments_using_post**](EventsApi.md#export_event_payments_using_post) | **POST** /event/director/participant/payment/{version}/export | exportEventPayments
[**get_all_event_players_using_post1**](EventsApi.md#get_all_event_players_using_post1) | **POST** /event/director/participant/{version}/all | getAllEventPlayers
[**get_city_autocomplete_using_get**](EventsApi.md#get_city_autocomplete_using_get) | **GET** /event/city/{version}/autocomplete | getCityAutocomplete
[**get_club_leagues_using_get**](EventsApi.md#get_club_leagues_using_get) | **GET** /event/club/{version}/{clubId} | getClubLeagues
[**get_league_policy_using_get**](EventsApi.md#get_league_policy_using_get) | **GET** /event/policy/{version}/content | getLeaguePolicy
[**get_league_using_get**](EventsApi.md#get_league_using_get) | **GET** /event/{version}/{leagueId} | getLeague
[**get_leagues_by_user_id_using_post**](EventsApi.md#get_leagues_by_user_id_using_post) | **POST** /event/{version}/user/{id} | getLeaguesByUserId
[**get_my_leagues_using_post**](EventsApi.md#get_my_leagues_using_post) | **POST** /event/{version}/all | getMyLeagues
[**join_event_using_post**](EventsApi.md#join_event_using_post) | **POST** /event/{leagueId}/{version}/join | joinEvent
[**register_event_using_post**](EventsApi.md#register_event_using_post) | **POST** /event/{leagueId}/{version}/checkout | registerEvent
[**save_using_post1**](EventsApi.md#save_using_post1) | **POST** /event/{version}/save | save
[**search_leagues_using_post**](EventsApi.md#search_leagues_using_post) | **POST** /event/{version}/search | searchLeagues


# **checkout_event_using_get**
> SingleWrapperOfSessionResponse checkout_event_using_get(authorization, league_id, version, x_forwarded_for=x_forwarded_for)

checkoutEvent

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # checkoutEvent
        api_response = api_instance.checkout_event_using_get(authorization, league_id, version, x_forwarded_for=x_forwarded_for)
        print("The response of EventsApi->checkout_event_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->checkout_event_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

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

# **delete_league_using_delete1**
> Wrapper delete_league_using_delete1(authorization, league_id, version)

deleteLeague

### Example


```python
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteLeague
        api_response = api_instance.delete_league_using_delete1(authorization, league_id, version)
        print("The response of EventsApi->delete_league_using_delete1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_league_using_delete1: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_text_content_using_delete**
> Wrapper delete_text_content_using_delete(authorization, version, request)

deleteTextContent

### Example


```python
import dupr_backend
from dupr_backend.models.delete_event_media_request import DeleteEventMediaRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DeleteEventMediaRequest() # DeleteEventMediaRequest | request

    try:
        # deleteTextContent
        api_response = api_instance.delete_text_content_using_delete(authorization, version, request)
        print("The response of EventsApi->delete_text_content_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->delete_text_content_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeleteEventMediaRequest**](DeleteEventMediaRequest.md)| request | 

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
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_using_post1**
> Wrapper draft_using_post1(authorization, version, request)

draft

### Example


```python
import dupr_backend
from dupr_backend.models.draft_league_request import DraftLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DraftLeagueRequest() # DraftLeagueRequest | request

    try:
        # draft
        api_response = api_instance.draft_using_post1(authorization, version, request)
        print("The response of EventsApi->draft_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->draft_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DraftLeagueRequest**](DraftLeagueRequest.md)| request | 

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

# **edit_league_using_put**
> SingleWrapperOfLeagueResponse edit_league_using_put(authorization, version, request)

editLeague

### Example


```python
import dupr_backend
from dupr_backend.models.edit_league_request import EditLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EditLeagueRequest() # EditLeagueRequest | request

    try:
        # editLeague
        api_response = api_instance.edit_league_using_put(authorization, version, request)
        print("The response of EventsApi->edit_league_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->edit_league_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EditLeagueRequest**](EditLeagueRequest.md)| request | 

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

# **end_league_using_get1**
> Wrapper end_league_using_get1(authorization, league_id, version)

endLeague

### Example


```python
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # endLeague
        api_response = api_instance.end_league_using_get1(authorization, league_id, version)
        print("The response of EventsApi->end_league_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->end_league_using_get1: %s\n" % e)
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
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_event_participants_using_get**
> SingleWrapperOfDownloadS3Response export_event_participants_using_get(authorization, league_id, version)

exportEventParticipants

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_download_s3_response import SingleWrapperOfDownloadS3Response
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # exportEventParticipants
        api_response = api_instance.export_event_participants_using_get(authorization, league_id, version)
        print("The response of EventsApi->export_event_participants_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->export_event_participants_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

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

# **export_event_payments_using_post**
> SingleWrapperOfDownloadS3Response export_event_payments_using_post(authorization, version, request)

exportEventPayments

### Example


```python
import dupr_backend
from dupr_backend.models.export_event_payment_request import ExportEventPaymentRequest
from dupr_backend.models.single_wrapper_of_download_s3_response import SingleWrapperOfDownloadS3Response
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ExportEventPaymentRequest() # ExportEventPaymentRequest | request

    try:
        # exportEventPayments
        api_response = api_instance.export_event_payments_using_post(authorization, version, request)
        print("The response of EventsApi->export_event_payments_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->export_event_payments_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ExportEventPaymentRequest**](ExportEventPaymentRequest.md)| request | 

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

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

# **get_all_event_players_using_post1**
> SingleWrapperOfPageOfPlayerPaymentResponse get_all_event_players_using_post1(authorization, limit, offset, version, search_league_player_request)

getAllEventPlayers

### Example


```python
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_of_page_of_player_payment_response import SingleWrapperOfPageOfPlayerPaymentResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest

    try:
        # getAllEventPlayers
        api_response = api_instance.get_all_event_players_using_post1(authorization, limit, offset, version, search_league_player_request)
        print("The response of EventsApi->get_all_event_players_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_all_event_players_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 

### Return type

[**SingleWrapperOfPageOfPlayerPaymentResponse**](SingleWrapperOfPageOfPlayerPaymentResponse.md)

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

# **get_city_autocomplete_using_get**
> ArrayWrapperOfstring get_city_autocomplete_using_get(authorization, version, search=search)

getCityAutocomplete

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_ofstring import ArrayWrapperOfstring
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    search = 'search_example' # str | search (optional)

    try:
        # getCityAutocomplete
        api_response = api_instance.get_city_autocomplete_using_get(authorization, version, search=search)
        print("The response of EventsApi->get_city_autocomplete_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_city_autocomplete_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **search** | **str**| search | [optional] 

### Return type

[**ArrayWrapperOfstring**](ArrayWrapperOfstring.md)

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

# **get_club_leagues_using_get**
> SingleWrapperOfPageOfLeagueResponse get_club_leagues_using_get(authorization, club_id, limit, offset, version, include_draft_events=include_draft_events)

getClubLeagues

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_response import SingleWrapperOfPageOfLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    include_draft_events = True # bool | includeDraftEvents (optional)

    try:
        # getClubLeagues
        api_response = api_instance.get_club_leagues_using_get(authorization, club_id, limit, offset, version, include_draft_events=include_draft_events)
        print("The response of EventsApi->get_club_leagues_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_club_leagues_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **include_draft_events** | **bool**| includeDraftEvents | [optional] 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

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

# **get_league_policy_using_get**
> SingleWrapperOfPolicyDetailsResponse get_league_policy_using_get(league_id, version)

getLeaguePolicy

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_policy_details_response import SingleWrapperOfPolicyDetailsResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getLeaguePolicy
        api_response = api_instance.get_league_policy_using_get(league_id, version)
        print("The response of EventsApi->get_league_policy_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_league_policy_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPolicyDetailsResponse**](SingleWrapperOfPolicyDetailsResponse.md)

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

# **get_league_using_get**
> SingleWrapperOfLeagueResponse get_league_using_get(league_id, version, authorization=authorization)

getLeague

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.EventsApi(api_client)
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')
    authorization = 'Bearer ' # str |  (optional) (default to 'Bearer ')

    try:
        # getLeague
        api_response = api_instance.get_league_using_get(league_id, version, authorization=authorization)
        print("The response of EventsApi->get_league_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_league_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **authorization** | **str**|  | [optional] [default to &#39;Bearer &#39;]

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

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

# **get_leagues_by_user_id_using_post**
> SingleWrapperOfPageOfLeagueResponse get_leagues_by_user_id_using_post(authorization, id, version, request)

getLeaguesByUserId

### Example


```python
import dupr_backend
from dupr_backend.models.my_league_request import MyLeagueRequest
from dupr_backend.models.single_wrapper_of_page_of_league_response import SingleWrapperOfPageOfLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MyLeagueRequest() # MyLeagueRequest | request

    try:
        # getLeaguesByUserId
        api_response = api_instance.get_leagues_by_user_id_using_post(authorization, id, version, request)
        print("The response of EventsApi->get_leagues_by_user_id_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_leagues_by_user_id_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MyLeagueRequest**](MyLeagueRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

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

# **get_my_leagues_using_post**
> SingleWrapperOfPageOfLeagueResponse get_my_leagues_using_post(authorization, version, request)

getMyLeagues

### Example


```python
import dupr_backend
from dupr_backend.models.my_league_request import MyLeagueRequest
from dupr_backend.models.single_wrapper_of_page_of_league_response import SingleWrapperOfPageOfLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MyLeagueRequest() # MyLeagueRequest | request

    try:
        # getMyLeagues
        api_response = api_instance.get_my_leagues_using_post(authorization, version, request)
        print("The response of EventsApi->get_my_leagues_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->get_my_leagues_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MyLeagueRequest**](MyLeagueRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

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

# **join_event_using_post**
> SingleWrapperOfJoinLeagueResponse join_event_using_post(authorization, league_id, version, request)

joinEvent

### Example


```python
import dupr_backend
from dupr_backend.models.join_league_request import JoinLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.1' # str | version (default to 'v1.1')
    request = [dupr_backend.JoinLeagueRequest()] # List[JoinLeagueRequest] | request

    try:
        # joinEvent
        api_response = api_instance.join_event_using_post(authorization, league_id, version, request)
        print("The response of EventsApi->join_event_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->join_event_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.1&#39;]
 **request** | [**List[JoinLeagueRequest]**](JoinLeagueRequest.md)| request | 

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

# **register_event_using_post**
> SingleWrapperOfSessionResponse register_event_using_post(authorization, league_id, version, requests, x_forwarded_for=x_forwarded_for)

registerEvent

### Example


```python
import dupr_backend
from dupr_backend.models.join_league_request import JoinLeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')
    requests = [dupr_backend.JoinLeagueRequest()] # List[JoinLeagueRequest] | requests
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # registerEvent
        api_response = api_instance.register_event_using_post(authorization, league_id, version, requests, x_forwarded_for=x_forwarded_for)
        print("The response of EventsApi->register_event_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->register_event_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **requests** | [**List[JoinLeagueRequest]**](JoinLeagueRequest.md)| requests | 
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

# **save_using_post1**
> Wrapper save_using_post1(authorization, version, request)

save

### Example


```python
import dupr_backend
from dupr_backend.models.league_request import LeagueRequest
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
    api_instance = dupr_backend.EventsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueRequest() # LeagueRequest | request

    try:
        # save
        api_response = api_instance.save_using_post1(authorization, version, request)
        print("The response of EventsApi->save_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->save_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueRequest**](LeagueRequest.md)| request | 

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

# **search_leagues_using_post**
> SingleWrapperOfPageOfLeagueResponse search_leagues_using_post(version, request, authorization=authorization)

searchLeagues

### Example


```python
import dupr_backend
from dupr_backend.models.search_leagues_request import SearchLeaguesRequest
from dupr_backend.models.single_wrapper_of_page_of_league_response import SingleWrapperOfPageOfLeagueResponse
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
    api_instance = dupr_backend.EventsApi(api_client)
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SearchLeaguesRequest() # SearchLeaguesRequest | request
    authorization = 'Bearer ' # str |  (optional) (default to 'Bearer ')

    try:
        # searchLeagues
        api_response = api_instance.search_leagues_using_post(version, request, authorization=authorization)
        print("The response of EventsApi->search_leagues_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->search_leagues_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SearchLeaguesRequest**](SearchLeaguesRequest.md)| request | 
 **authorization** | **str**|  | [optional] [default to &#39;Bearer &#39;]

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

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

