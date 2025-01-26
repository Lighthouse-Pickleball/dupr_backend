# dupr_backend.OpenPlayApi

All URIs are relative to *//https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_invitation_using_post**](OpenPlayApi.md#accept_invitation_using_post) | **POST** /event/{version}/open-play/{id}/invitation/accept | acceptInvitation
[**create_using_post**](OpenPlayApi.md#create_using_post) | **POST** /event/{version}/open-play/create | create
[**get_event_detail_using_get**](OpenPlayApi.md#get_event_detail_using_get) | **GET** /event/{version}/open-play/{id} | getEventDetail
[**get_events_members_using_get**](OpenPlayApi.md#get_events_members_using_get) | **GET** /event/{version}/open-play/{id}/participants | getEventsMembers
[**get_events_near_by_using_get**](OpenPlayApi.md#get_events_near_by_using_get) | **GET** /event/{version}/open-play/near-by | getEventsNearBy
[**get_invitation_by_player_using_get**](OpenPlayApi.md#get_invitation_by_player_using_get) | **GET** /event/{version}/open-play/invitation/player | getInvitationByPlayer
[**get_waitlist_by_player_using_get**](OpenPlayApi.md#get_waitlist_by_player_using_get) | **GET** /event/{version}/open-play/waitlist/player | getWaitlistByPlayer
[**join_waitlist_using_post**](OpenPlayApi.md#join_waitlist_using_post) | **POST** /event/{version}/open-play/{id}/join-waitlist | joinWaitlist
[**register_event_using_post1**](OpenPlayApi.md#register_event_using_post1) | **POST** /event/{version}/open-play/{id}/register | registerEvent
[**reject_invitation_using_post**](OpenPlayApi.md#reject_invitation_using_post) | **POST** /event/{version}/open-play/{id}/invitation/reject | rejectInvitation
[**update_using_put**](OpenPlayApi.md#update_using_put) | **PUT** /event/{version}/open-play/{id}/{version}/update | update
[**withdraw_event_using_delete**](OpenPlayApi.md#withdraw_event_using_delete) | **DELETE** /event/{version}/open-play/{id}/withdraw | withdrawEvent

# **accept_invitation_using_post**
> SingleWrapperOfUnit accept_invitation_using_post(authorization, id, version)

acceptInvitation

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # acceptInvitation
    api_response = api_instance.accept_invitation_using_post(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->accept_invitation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_using_post**
> SingleWrapperOfUnit create_using_post(body, authorization, version)

create

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
body = dupr_backend.OpenPlayCreateRequest() # OpenPlayCreateRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # create
    api_response = api_instance.create_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->create_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenPlayCreateRequest**](OpenPlayCreateRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_detail_using_get**
> SingleWrapperOfOpenPlayEvent get_event_detail_using_get(authorization, id, version)

getEventDetail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getEventDetail
    api_response = api_instance.get_event_detail_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->get_event_detail_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfOpenPlayEvent**](SingleWrapperOfOpenPlayEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_members_using_get**
> SingleWrapperOfPageOfOpenPlayMember get_events_members_using_get(authorization, id, limit, offset, version)

getEventsMembers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getEventsMembers
    api_response = api_instance.get_events_members_using_get(authorization, id, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->get_events_members_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfOpenPlayMember**](SingleWrapperOfPageOfOpenPlayMember.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events_near_by_using_get**
> SingleWrapperOfPageOfOpenPlayEvent get_events_near_by_using_get(authorization, limit, offset, version, latitude=latitude, longitude=longitude, query=query, radius=radius)

getEventsNearBy

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
latitude = 1.2 # float | latitude (optional)
longitude = 1.2 # float | longitude (optional)
query = 'query_example' # str | query (optional)
radius = 1.2 # float | radius (optional)

try:
    # getEventsNearBy
    api_response = api_instance.get_events_near_by_using_get(authorization, limit, offset, version, latitude=latitude, longitude=longitude, query=query, radius=radius)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->get_events_near_by_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **latitude** | **float**| latitude | [optional] 
 **longitude** | **float**| longitude | [optional] 
 **query** | **str**| query | [optional] 
 **radius** | **float**| radius | [optional] 

### Return type

[**SingleWrapperOfPageOfOpenPlayEvent**](SingleWrapperOfPageOfOpenPlayEvent.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_invitation_by_player_using_get**
> SingleWrapperOfPageOfPlayerQueue get_invitation_by_player_using_get(authorization, limit, offset, version)

getInvitationByPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getInvitationByPlayer
    api_response = api_instance.get_invitation_by_player_using_get(authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->get_invitation_by_player_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerQueue**](SingleWrapperOfPageOfPlayerQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waitlist_by_player_using_get**
> SingleWrapperOfPageOfPlayerQueue get_waitlist_by_player_using_get(authorization, limit, offset, version)

getWaitlistByPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getWaitlistByPlayer
    api_response = api_instance.get_waitlist_by_player_using_get(authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->get_waitlist_by_player_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerQueue**](SingleWrapperOfPageOfPlayerQueue.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **join_waitlist_using_post**
> SingleWrapperOfOpenPlayEventWaitlist join_waitlist_using_post(authorization, id, version)

joinWaitlist

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # joinWaitlist
    api_response = api_instance.join_waitlist_using_post(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->join_waitlist_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfOpenPlayEventWaitlist**](SingleWrapperOfOpenPlayEventWaitlist.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_event_using_post1**
> SingleWrapperOfUnit register_event_using_post1(authorization, id, version)

registerEvent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # registerEvent
    api_response = api_instance.register_event_using_post1(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->register_event_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reject_invitation_using_post**
> SingleWrapperOfUnit reject_invitation_using_post(authorization, id, version)

rejectInvitation

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # rejectInvitation
    api_response = api_instance.reject_invitation_using_post(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->reject_invitation_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put**
> SingleWrapperOfUnit update_using_put(body, authorization, id, version)

update

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
body = dupr_backend.OpenPlayUpdateRequest() # OpenPlayUpdateRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # update
    api_response = api_instance.update_using_put(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->update_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OpenPlayUpdateRequest**](OpenPlayUpdateRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **withdraw_event_using_delete**
> SingleWrapperOfUnit withdraw_event_using_delete(authorization, id, version)

withdrawEvent

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.OpenPlayApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # withdrawEvent
    api_response = api_instance.withdraw_event_using_delete(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OpenPlayApi->withdraw_event_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

