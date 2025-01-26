# dupr_backend.EventsApi

All URIs are relative to *//https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # checkoutEvent
    api_response = api_instance.checkout_event_using_get(authorization, league_id, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->checkout_event_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_league_using_delete1**
> Wrapper delete_league_using_delete1(authorization, league_id, version)

deleteLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # deleteLeague
    api_response = api_instance.delete_league_using_delete1(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->delete_league_using_delete1: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_text_content_using_delete**
> Wrapper delete_text_content_using_delete(body, authorization, version)

deleteTextContent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.DeleteEventMediaRequest() # DeleteEventMediaRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteTextContent
    api_response = api_instance.delete_text_content_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->delete_text_content_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteEventMediaRequest**](DeleteEventMediaRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **draft_using_post1**
> Wrapper draft_using_post1(body, authorization, version)

draft

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.DraftLeagueRequest() # DraftLeagueRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # draft
    api_response = api_instance.draft_using_post1(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->draft_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DraftLeagueRequest**](DraftLeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_league_using_put**
> SingleWrapperOfLeagueResponse edit_league_using_put(body, authorization, version)

editLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.EditLeagueRequest() # EditLeagueRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editLeague
    api_response = api_instance.edit_league_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->edit_league_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditLeagueRequest**](EditLeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_league_using_get1**
> Wrapper end_league_using_get1(authorization, league_id, version)

endLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # endLeague
    api_response = api_instance.end_league_using_get1(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->end_league_using_get1: %s\n" % e)
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
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_event_participants_using_get**
> SingleWrapperOfDownloadS3Response export_event_participants_using_get(authorization, league_id, version)

exportEventParticipants

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # exportEventParticipants
    api_response = api_instance.export_event_participants_using_get(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->export_event_participants_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_event_payments_using_post**
> SingleWrapperOfDownloadS3Response export_event_payments_using_post(body, authorization, version)

exportEventPayments

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.ExportEventPaymentRequest() # ExportEventPaymentRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # exportEventPayments
    api_response = api_instance.export_event_payments_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->export_event_payments_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExportEventPaymentRequest**](ExportEventPaymentRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_event_players_using_post1**
> SingleWrapperOfPageOfPlayerPaymentResponse get_all_event_players_using_post1(body, authorization, limit, offset, version)

getAllEventPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getAllEventPlayers
    api_response = api_instance.get_all_event_players_using_post1(body, authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_all_event_players_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerPaymentResponse**](SingleWrapperOfPageOfPlayerPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_city_autocomplete_using_get**
> ArrayWrapperOfstring get_city_autocomplete_using_get(authorization, version, search=search)

getCityAutocomplete

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
search = 'search_example' # str | search (optional)

try:
    # getCityAutocomplete
    api_response = api_instance.get_city_autocomplete_using_get(authorization, version, search=search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_city_autocomplete_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **search** | **str**| search | [optional] 

### Return type

[**ArrayWrapperOfstring**](ArrayWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_leagues_using_get**
> SingleWrapperOfPageOfLeagueResponse get_club_leagues_using_get(authorization, club_id, limit, offset, version, include_draft_events=include_draft_events)

getClubLeagues

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
include_draft_events = true # bool | includeDraftEvents (optional)

try:
    # getClubLeagues
    api_response = api_instance.get_club_leagues_using_get(authorization, club_id, limit, offset, version, include_draft_events=include_draft_events)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_club_leagues_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **include_draft_events** | **bool**| includeDraftEvents | [optional] 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league_policy_using_get**
> SingleWrapperOfPolicyDetailsResponse get_league_policy_using_get(league_id, version)

getLeaguePolicy

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # getLeaguePolicy
    api_response = api_instance.get_league_policy_using_get(league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_league_policy_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPolicyDetailsResponse**](SingleWrapperOfPolicyDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league_using_get**
> SingleWrapperOfLeagueResponse get_league_using_get(league_id, version, authorization=authorization)

getLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
league_id = 789 # int | leagueId
version = 'version_example' # str | version
authorization = 'Bearer ' # str |  (optional) (default to Bearer )

try:
    # getLeague
    api_response = api_instance.get_league_using_get(league_id, version, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_league_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 
 **authorization** | **str**|  | [optional] [default to Bearer ]

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leagues_by_user_id_using_post**
> SingleWrapperOfPageOfLeagueResponse get_leagues_by_user_id_using_post(body, authorization, id, version)

getLeaguesByUserId

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.MyLeagueRequest() # MyLeagueRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getLeaguesByUserId
    api_response = api_instance.get_leagues_by_user_id_using_post(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_leagues_by_user_id_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MyLeagueRequest**](MyLeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_my_leagues_using_post**
> SingleWrapperOfPageOfLeagueResponse get_my_leagues_using_post(body, authorization, version)

getMyLeagues

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.MyLeagueRequest() # MyLeagueRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getMyLeagues
    api_response = api_instance.get_my_leagues_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_my_leagues_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MyLeagueRequest**](MyLeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_event_using_post**
> SingleWrapperOfJoinLeagueResponse join_event_using_post(body, authorization, league_id, version)

joinEvent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = [dupr_backend.JoinLeagueRequest()] # list[JoinLeagueRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # joinEvent
    api_response = api_instance.join_event_using_post(body, authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->join_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JoinLeagueRequest]**](JoinLeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfJoinLeagueResponse**](SingleWrapperOfJoinLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_event_using_post**
> SingleWrapperOfSessionResponse register_event_using_post(body, authorization, league_id, version, x_forwarded_for=x_forwarded_for)

registerEvent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = [dupr_backend.JoinLeagueRequest()] # list[JoinLeagueRequest] | requests
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # registerEvent
    api_response = api_instance.register_event_using_post(body, authorization, league_id, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->register_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[JoinLeagueRequest]**](JoinLeagueRequest.md)| requests | 
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_using_post1**
> Wrapper save_using_post1(body, authorization, version)

save

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.LeagueRequest() # LeagueRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # save
    api_response = api_instance.save_using_post1(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->save_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueRequest**](LeagueRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_leagues_using_post**
> SingleWrapperOfPageOfLeagueResponse search_leagues_using_post(body, version, authorization=authorization)

searchLeagues

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.EventsApi()
body = dupr_backend.SearchLeaguesRequest() # SearchLeaguesRequest | request
version = 'version_example' # str | version
authorization = 'Bearer ' # str |  (optional) (default to Bearer )

try:
    # searchLeagues
    api_response = api_instance.search_leagues_using_post(body, version, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->search_leagues_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLeaguesRequest**](SearchLeaguesRequest.md)| request | 
 **version** | **str**| version | 
 **authorization** | **str**|  | [optional] [default to Bearer ]

### Return type

[**SingleWrapperOfPageOfLeagueResponse**](SingleWrapperOfPageOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

