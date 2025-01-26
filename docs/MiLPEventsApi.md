# dupr_backend.MiLPEventsApi

All URIs are relative to *//https://backend.mydupr.com/*

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
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPEventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getEventInfo
    api_response = api_instance.get_event_info_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPEventsApi->get_event_info_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMiLPEvent**](SingleWrapperOfMiLPEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_teams_using_get**
> ArrayWrapperOfMiLPTeamDivision get_teams_using_get(authorization, id, version)

getTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPEventsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getTeams
    api_response = api_instance.get_teams_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPEventsApi->get_teams_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfMiLPTeamDivision**](ArrayWrapperOfMiLPTeamDivision.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_team_using_post**
> SingleWrapperOfSessionResponse register_team_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

registerTeam

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPEventsApi()
body = dupr_backend.MiLPRegisterTeamRequest() # MiLPRegisterTeamRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # registerTeam
    api_response = api_instance.register_team_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPEventsApi->register_team_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MiLPRegisterTeamRequest**](MiLPRegisterTeamRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
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

# **save_using_post2**
> SingleWrapperOflong save_using_post2(body, authorization, version)

save

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPEventsApi()
body = dupr_backend.MiLPEventRequest() # MiLPEventRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # save
    api_response = api_instance.save_using_post2(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPEventsApi->save_using_post2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MiLPEventRequest**](MiLPEventRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOflong**](SingleWrapperOflong.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_event_using_post**
> SingleWrapperOfPageOfMiLPEvent search_event_using_post(body, authorization, version)

searchEvent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.MiLPEventsApi()
body = dupr_backend.MiLPEventSearchRequest() # MiLPEventSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # searchEvent
    api_response = api_instance.search_event_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MiLPEventsApi->search_event_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MiLPEventSearchRequest**](MiLPEventSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMiLPEvent**](SingleWrapperOfPageOfMiLPEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

