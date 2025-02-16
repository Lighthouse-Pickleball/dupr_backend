# dupr_backend.ClubApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_club_using_put**](ClubApi.md#add_club_using_put) | **PUT** /club/{version}/add | addClub
[**add_member_admin_using_put**](ClubApi.md#add_member_admin_using_put) | **PUT** /club/{clubId}/members/{version}/add | addMemberAdmin
[**add_member_multiple_admin_using_put**](ClubApi.md#add_member_multiple_admin_using_put) | **PUT** /club/{clubId}/members/{version}/multiple/add | addMemberMultipleAdmin
[**add_member_multiple_csv_admin_using_put**](ClubApi.md#add_member_multiple_csv_admin_using_put) | **PUT** /club/{clubId}/members/{version}/csv/add | addMemberMultipleCsvAdmin
[**add_member_request_using_put**](ClubApi.md#add_member_request_using_put) | **PUT** /club/{clubId}/members/{version}/join | addMemberRequest
[**approve_roles_using_post**](ClubApi.md#approve_roles_using_post) | **POST** /club/{clubId}/{version}/approve | approveRoles
[**assign_roles_using_post**](ClubApi.md#assign_roles_using_post) | **POST** /club/{clubId}/roles/{version}/assign | assignRoles
[**club_match_history_by_filters_using_post**](ClubApi.md#club_match_history_by_filters_using_post) | **POST** /club/match/{version}/history | clubMatchHistoryByFilters
[**club_match_history_using_get**](ClubApi.md#club_match_history_using_get) | **GET** /club/{clubId}/{version}/history | clubMatchHistory
[**club_save_match_using_put**](ClubApi.md#club_save_match_using_put) | **PUT** /club/{clubId}/match/{version}/save | clubSaveMatch
[**delete_club_match_using_post**](ClubApi.md#delete_club_match_using_post) | **POST** /club/{clubId}/match/{id}/{version}/delete | deleteClubMatch
[**delete_member_admin_using_delete**](ClubApi.md#delete_member_admin_using_delete) | **DELETE** /club/{clubId}/members/{version}/remove | deleteMemberAdmin
[**delete_member_request_using_delete**](ClubApi.md#delete_member_request_using_delete) | **DELETE** /club/{clubId}/members/{version}/leave | deleteMemberRequest
[**edit_club_match_using_put**](ClubApi.md#edit_club_match_using_put) | **PUT** /club/{clubId}/match/{id}/{version}/edit | editClubMatch
[**get_all_club_roles_using_get**](ClubApi.md#get_all_club_roles_using_get) | **GET** /club/roles/{version}/all | getAllClubRoles
[**get_all_currency_details_using_get**](ClubApi.md#get_all_currency_details_using_get) | **GET** /club/currency/{version}/all | getAllCurrencyDetails
[**get_all_members_download_using_post**](ClubApi.md#get_all_members_download_using_post) | **POST** /club/{clubId}/members/{version}/all/download | getAllMembersDownload
[**get_all_members_using_post**](ClubApi.md#get_all_members_using_post) | **POST** /club/{clubId}/members/{version}/all | getAllMembers
[**get_all_roles_using_get1**](ClubApi.md#get_all_roles_using_get1) | **GET** /club/{clubId}/roles/{version}/all | getAllRoles
[**get_all_staff_members_using_get**](ClubApi.md#get_all_staff_members_using_get) | **GET** /club/{clubId}/members/{version}/staff | getAllStaffMembers
[**get_club_pending_invites_using_post**](ClubApi.md#get_club_pending_invites_using_post) | **POST** /club/{clubId}/members/{version}/pending/invites | getClubPendingInvites
[**get_club_restrictions_using_post1**](ClubApi.md#get_club_restrictions_using_post1) | **POST** /club/{clubId}/{version}/restrictions | getClubRestrictions
[**get_club_roles_player_using_post**](ClubApi.md#get_club_roles_player_using_post) | **POST** /club/{clubId}/roles/{version}/permission | getClubRolesPlayer
[**get_club_roles_staff_using_get**](ClubApi.md#get_club_roles_staff_using_get) | **GET** /club/roles/{version}/staff | getClubRolesStaff
[**get_club_roles_using_post**](ClubApi.md#get_club_roles_using_post) | **POST** /club/{clubId}/roles/{version}/user | getClubRoles
[**get_club_using_get**](ClubApi.md#get_club_using_get) | **GET** /club/{version}/{clubId} | getClub
[**get_clubs_using_get**](ClubApi.md#get_clubs_using_get) | **GET** /club/{version}/all | getClubs
[**get_clubs_using_post**](ClubApi.md#get_clubs_using_post) | **POST** /club/{version}/all | getClubs
[**get_currency_details_using_get**](ClubApi.md#get_currency_details_using_get) | **GET** /club/currency/{version}/{currencyCode} | getCurrencyDetails
[**get_match_using_get1**](ClubApi.md#get_match_using_get1) | **GET** /club/{clubId}/match/{id}/{version}/get | getMatch
[**get_members_ranking_using_post**](ClubApi.md#get_members_ranking_using_post) | **POST** /club/{clubId}/{version}/ranking | getMembersRanking
[**invite_single_member_using_put**](ClubApi.md#invite_single_member_using_put) | **PUT** /club/{clubId}/members/{version}/invite | inviteSingleMember
[**remove_roles_using_post**](ClubApi.md#remove_roles_using_post) | **POST** /club/{clubId}/roles/{version}/remove | removeRoles
[**save_verified_club_match_csv_using_put**](ClubApi.md#save_verified_club_match_csv_using_put) | **PUT** /club/{id}/match/verified/{version}/save/csv/add | saveVerifiedClubMatchCSV
[**update_approval_status_using_post**](ClubApi.md#update_approval_status_using_post) | **POST** /club/{clubId}/{version}/approval | updateApprovalStatus
[**update_club_using_post**](ClubApi.md#update_club_using_post) | **POST** /club/{version}/update | updateClub
[**update_staff_members_using_put**](ClubApi.md#update_staff_members_using_put) | **PUT** /club/{clubId}/members/{version}/staff | updateStaffMembers


# **add_club_using_put**
> Wrapper add_club_using_put(authorization, version, request)

addClub

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_request import ClubRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubRequest() # ClubRequest | request

    try:
        # addClub
        api_response = api_instance.add_club_using_put(authorization, version, request)
        print("The response of ClubApi->add_club_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_club_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubRequest**](ClubRequest.md)| request | 

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

# **add_member_admin_using_put**
> Wrapper add_member_admin_using_put(authorization, club_id, version, request)

addMemberAdmin

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.user_list_request import UserListRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserListRequest() # UserListRequest | request

    try:
        # addMemberAdmin
        api_response = api_instance.add_member_admin_using_put(authorization, club_id, version, request)
        print("The response of ClubApi->add_member_admin_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_admin_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserListRequest**](UserListRequest.md)| request | 

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

# **add_member_multiple_admin_using_put**
> SingleWrapperOfClubMemberManyResponse add_member_multiple_admin_using_put(authorization, club_id, version, request)

addMemberMultipleAdmin

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_member_add_request import ClubMemberAddRequest
from dupr_backend.models.single_wrapper_of_club_member_many_response import SingleWrapperOfClubMemberManyResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubMemberAddRequest() # ClubMemberAddRequest | request

    try:
        # addMemberMultipleAdmin
        api_response = api_instance.add_member_multiple_admin_using_put(authorization, club_id, version, request)
        print("The response of ClubApi->add_member_multiple_admin_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_multiple_admin_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubMemberAddRequest**](ClubMemberAddRequest.md)| request | 

### Return type

[**SingleWrapperOfClubMemberManyResponse**](SingleWrapperOfClubMemberManyResponse.md)

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

# **add_member_multiple_csv_admin_using_put**
> object add_member_multiple_csv_admin_using_put(authorization, club_id, version, request=request)

addMemberMultipleCsvAdmin

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = None # bytearray |  (optional)

    try:
        # addMemberMultipleCsvAdmin
        api_response = api_instance.add_member_multiple_csv_admin_using_put(authorization, club_id, version, request=request)
        print("The response of ClubApi->add_member_multiple_csv_admin_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_multiple_csv_admin_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_request_using_put**
> object add_member_request_using_put(authorization, club_id, version)

addMemberRequest

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # addMemberRequest
        api_response = api_instance.add_member_request_using_put(authorization, club_id, version)
        print("The response of ClubApi->add_member_request_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_request_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

**object**

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

# **approve_roles_using_post**
> Wrapper approve_roles_using_post(authorization, club_id, version, request)

approveRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.ids_list_request import IdsListRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.IdsListRequest() # IdsListRequest | request

    try:
        # approveRoles
        api_response = api_instance.approve_roles_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->approve_roles_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->approve_roles_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**IdsListRequest**](IdsListRequest.md)| request | 

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

# **assign_roles_using_post**
> Wrapper assign_roles_using_post(authorization, club_id, version, request)

assignRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.assign_role_request import AssignRoleRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AssignRoleRequest() # AssignRoleRequest | request

    try:
        # assignRoles
        api_response = api_instance.assign_roles_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->assign_roles_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->assign_roles_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AssignRoleRequest**](AssignRoleRequest.md)| request | 

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

# **club_match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse club_match_history_by_filters_using_post(authorization, version, request)

clubMatchHistoryByFilters

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_match_history_request import ClubMatchHistoryRequest
from dupr_backend.models.single_wrapper_of_page_of_match_response import SingleWrapperOfPageOfMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubMatchHistoryRequest() # ClubMatchHistoryRequest | request

    try:
        # clubMatchHistoryByFilters
        api_response = api_instance.club_match_history_by_filters_using_post(authorization, version, request)
        print("The response of ClubApi->club_match_history_by_filters_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_match_history_by_filters_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubMatchHistoryRequest**](ClubMatchHistoryRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

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

# **club_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse club_match_history_using_get(authorization, club_id, limit, offset, version)

clubMatchHistory

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_match_response import SingleWrapperOfPageOfMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # clubMatchHistory
        api_response = api_instance.club_match_history_using_get(authorization, club_id, limit, offset, version)
        print("The response of ClubApi->club_match_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_match_history_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

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

# **club_save_match_using_put**
> object club_save_match_using_put(authorization, club_id, version, request)

clubSaveMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchRequest() # MatchRequest | request

    try:
        # clubSaveMatch
        api_response = api_instance.club_save_match_using_put(authorization, club_id, version, request)
        print("The response of ClubApi->club_save_match_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_save_match_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MatchRequest**](MatchRequest.md)| request | 

### Return type

**object**

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

# **delete_club_match_using_post**
> object delete_club_match_using_post(authorization, club_id, version, request)

deleteClubMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request

    try:
        # deleteClubMatch
        api_response = api_instance.delete_club_match_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->delete_club_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_club_match_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 

### Return type

**object**

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

# **delete_member_admin_using_delete**
> Wrapper delete_member_admin_using_delete(authorization, club_id, user_ids, version)

deleteMemberAdmin

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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    user_ids = [56] # List[int] | userIds
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteMemberAdmin
        api_response = api_instance.delete_member_admin_using_delete(authorization, club_id, user_ids, version)
        print("The response of ClubApi->delete_member_admin_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_member_admin_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **user_ids** | [**List[int]**](int.md)| userIds | 
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

# **delete_member_request_using_delete**
> object delete_member_request_using_delete(authorization, club_id, version)

deleteMemberRequest

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteMemberRequest
        api_response = api_instance.delete_member_request_using_delete(authorization, club_id, version)
        print("The response of ClubApi->delete_member_request_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_member_request_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

**object**

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

# **edit_club_match_using_put**
> SingleWrapperOfMatchResponse edit_club_match_using_put(authorization, club_id, version, match_update_request)

editClubMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.match_update_request import MatchUpdateRequest
from dupr_backend.models.single_wrapper_of_match_response import SingleWrapperOfMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    match_update_request = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | matchUpdateRequest

    try:
        # editClubMatch
        api_response = api_instance.edit_club_match_using_put(authorization, club_id, version, match_update_request)
        print("The response of ClubApi->edit_club_match_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->edit_club_match_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **match_update_request** | [**MatchUpdateRequest**](MatchUpdateRequest.md)| matchUpdateRequest | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

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

# **get_all_club_roles_using_get**
> ArrayWrapperOfClubListingResponse get_all_club_roles_using_get(authorization, version)

getAllClubRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_club_listing_response import ArrayWrapperOfClubListingResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllClubRoles
        api_response = api_instance.get_all_club_roles_using_get(authorization, version)
        print("The response of ClubApi->get_all_club_roles_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_club_roles_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfClubListingResponse**](ArrayWrapperOfClubListingResponse.md)

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

# **get_all_currency_details_using_get**
> ArrayWrapperOfCurrencyDetailsResponse get_all_currency_details_using_get(authorization, version)

getAllCurrencyDetails

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_currency_details_response import ArrayWrapperOfCurrencyDetailsResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllCurrencyDetails
        api_response = api_instance.get_all_currency_details_using_get(authorization, version)
        print("The response of ClubApi->get_all_currency_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_currency_details_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfCurrencyDetailsResponse**](ArrayWrapperOfCurrencyDetailsResponse.md)

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

# **get_all_members_download_using_post**
> SingleWrapperOfDownloadS3Response get_all_members_download_using_post(authorization, club_id, version)

getAllMembersDownload

### Example

```python
import time
import os
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllMembersDownload
        api_response = api_instance.get_all_members_download_using_post(authorization, club_id, version)
        print("The response of ClubApi->get_all_members_download_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_members_download_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
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

# **get_all_members_using_post**
> SingleWrapperOfPageOfClubMemberResponse get_all_members_using_post(authorization, club_id, version, request)

getAllMembers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_of_page_of_club_member_response import SingleWrapperOfPageOfClubMemberResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request

    try:
        # getAllMembers
        api_response = api_instance.get_all_members_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->get_all_members_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_members_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfClubMemberResponse**](SingleWrapperOfPageOfClubMemberResponse.md)

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

# **get_all_roles_using_get1**
> ArrayWrapperOfRoleResponse get_all_roles_using_get1(authorization, version)

getAllRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_role_response import ArrayWrapperOfRoleResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllRoles
        api_response = api_instance.get_all_roles_using_get1(authorization, version)
        print("The response of ClubApi->get_all_roles_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_roles_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfRoleResponse**](ArrayWrapperOfRoleResponse.md)

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

# **get_all_staff_members_using_get**
> SingleWrapperOfStaffClubMemberResponse get_all_staff_members_using_get(authorization, club_id, version)

getAllStaffMembers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_staff_club_member_response import SingleWrapperOfStaffClubMemberResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllStaffMembers
        api_response = api_instance.get_all_staff_members_using_get(authorization, club_id, version)
        print("The response of ClubApi->get_all_staff_members_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_staff_members_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfStaffClubMemberResponse**](SingleWrapperOfStaffClubMemberResponse.md)

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

# **get_club_pending_invites_using_post**
> SingleWrapperOfPageOfClubMemberResponse get_club_pending_invites_using_post(authorization, club_id, version, request)

getClubPendingInvites

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_of_page_of_club_member_response import SingleWrapperOfPageOfClubMemberResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request

    try:
        # getClubPendingInvites
        api_response = api_instance.get_club_pending_invites_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->get_club_pending_invites_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_pending_invites_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfPageOfClubMemberResponse**](SingleWrapperOfPageOfClubMemberResponse.md)

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

# **get_club_restrictions_using_post1**
> object get_club_restrictions_using_post1(authorization, club_id, version)

getClubRestrictions

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getClubRestrictions
        api_response = api_instance.get_club_restrictions_using_post1(authorization, club_id, version)
        print("The response of ClubApi->get_club_restrictions_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_restrictions_using_post1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

**object**

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

# **get_club_roles_player_using_post**
> SingleWrapperOfRoleResponse get_club_roles_player_using_post(authorization, club_id, version, request)

getClubRolesPlayer

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_role_response import SingleWrapperOfRoleResponse
from dupr_backend.models.user_request import UserRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserRequest() # UserRequest | request

    try:
        # getClubRolesPlayer
        api_response = api_instance.get_club_roles_player_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->get_club_roles_player_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles_player_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserRequest**](UserRequest.md)| request | 

### Return type

[**SingleWrapperOfRoleResponse**](SingleWrapperOfRoleResponse.md)

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

# **get_club_roles_staff_using_get**
> SingleWrapperOfMapOfstringAndobject get_club_roles_staff_using_get(authorization, version)

getClubRolesStaff

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_map_ofstring_andobject import SingleWrapperOfMapOfstringAndobject
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getClubRolesStaff
        api_response = api_instance.get_club_roles_staff_using_get(authorization, version)
        print("The response of ClubApi->get_club_roles_staff_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles_staff_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMapOfstringAndobject**](SingleWrapperOfMapOfstringAndobject.md)

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

# **get_club_roles_using_post**
> SingleWrapperOfRoleResponse get_club_roles_using_post(authorization, club_id, version, request)

getClubRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_role_response import SingleWrapperOfRoleResponse
from dupr_backend.models.user_request import UserRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserRequest() # UserRequest | request

    try:
        # getClubRoles
        api_response = api_instance.get_club_roles_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->get_club_roles_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserRequest**](UserRequest.md)| request | 

### Return type

[**SingleWrapperOfRoleResponse**](SingleWrapperOfRoleResponse.md)

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

# **get_club_using_get**
> SingleWrapperOfClubResponse get_club_using_get(authorization, club_id, version)

getClub

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_club_response import SingleWrapperOfClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getClub
        api_response = api_instance.get_club_using_get(authorization, club_id, version)
        print("The response of ClubApi->get_club_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfClubResponse**](SingleWrapperOfClubResponse.md)

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

# **get_clubs_using_get**
> SingleWrapperOfPageOfClubResponse get_clubs_using_get(authorization, limit, offset, own, q, version)

getClubs

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_club_response import SingleWrapperOfPageOfClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    own = True # bool | own
    q = 'q_example' # str | q
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getClubs
        api_response = api_instance.get_clubs_using_get(authorization, limit, offset, own, q, version)
        print("The response of ClubApi->get_clubs_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_clubs_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **own** | **bool**| own | 
 **q** | **str**| q | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfClubResponse**](SingleWrapperOfPageOfClubResponse.md)

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

# **get_clubs_using_post**
> SingleWrapperOfPageOfClubResponse get_clubs_using_post(authorization, version, club_search)

getClubs

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_search import ClubSearch
from dupr_backend.models.single_wrapper_of_page_of_club_response import SingleWrapperOfPageOfClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    club_search = dupr_backend.ClubSearch() # ClubSearch | clubSearch

    try:
        # getClubs
        api_response = api_instance.get_clubs_using_post(authorization, version, club_search)
        print("The response of ClubApi->get_clubs_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_clubs_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **club_search** | [**ClubSearch**](ClubSearch.md)| clubSearch | 

### Return type

[**SingleWrapperOfPageOfClubResponse**](SingleWrapperOfPageOfClubResponse.md)

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

# **get_currency_details_using_get**
> SingleWrapperOfCurrencyDetailsResponse get_currency_details_using_get(authorization, currency_code, version)

getCurrencyDetails

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_currency_details_response import SingleWrapperOfCurrencyDetailsResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    currency_code = 'currency_code_example' # str | currencyCode
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getCurrencyDetails
        api_response = api_instance.get_currency_details_using_get(authorization, currency_code, version)
        print("The response of ClubApi->get_currency_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_currency_details_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **currency_code** | **str**| currencyCode | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfCurrencyDetailsResponse**](SingleWrapperOfCurrencyDetailsResponse.md)

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

# **get_match_using_get1**
> SingleWrapperOfMatchResponse get_match_using_get1(authorization, club_id, id, version)

getMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_match_response import SingleWrapperOfMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getMatch
        api_response = api_instance.get_match_using_get1(authorization, club_id, id, version)
        print("The response of ClubApi->get_match_using_get1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_match_using_get1: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

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

# **get_members_ranking_using_post**
> SingleWrapperOfClubMemberRankingResponse get_members_ranking_using_post(authorization, club_id, version, request)

getMembersRanking

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_of_club_member_ranking_response import SingleWrapperOfClubMemberRankingResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request

    try:
        # getMembersRanking
        api_response = api_instance.get_members_ranking_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->get_members_ranking_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_members_ranking_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 

### Return type

[**SingleWrapperOfClubMemberRankingResponse**](SingleWrapperOfClubMemberRankingResponse.md)

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

# **invite_single_member_using_put**
> SingleWrapperOfstring invite_single_member_using_put(authorization, club_id, version, request)

inviteSingleMember

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.invite_request import InviteRequest
from dupr_backend.models.single_wrapper_ofstring import SingleWrapperOfstring
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.InviteRequest() # InviteRequest | request

    try:
        # inviteSingleMember
        api_response = api_instance.invite_single_member_using_put(authorization, club_id, version, request)
        print("The response of ClubApi->invite_single_member_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->invite_single_member_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**InviteRequest**](InviteRequest.md)| request | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

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

# **remove_roles_using_post**
> Wrapper remove_roles_using_post(authorization, club_id, version, request)

removeRoles

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.assign_role_request import AssignRoleRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AssignRoleRequest() # AssignRoleRequest | request

    try:
        # removeRoles
        api_response = api_instance.remove_roles_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->remove_roles_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->remove_roles_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AssignRoleRequest**](AssignRoleRequest.md)| request | 

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

# **save_verified_club_match_csv_using_put**
> object save_verified_club_match_csv_using_put(authorization, id, version, request=request)

saveVerifiedClubMatchCSV

### Example

```python
import time
import os
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = None # bytearray |  (optional)

    try:
        # saveVerifiedClubMatchCSV
        api_response = api_instance.save_verified_club_match_csv_using_put(authorization, id, version, request=request)
        print("The response of ClubApi->save_verified_club_match_csv_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->save_verified_club_match_csv_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_approval_status_using_post**
> Wrapper update_approval_status_using_post(authorization, club_id, version, request)

updateApprovalStatus

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.status_request import StatusRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.StatusRequest() # StatusRequest | request

    try:
        # updateApprovalStatus
        api_response = api_instance.update_approval_status_using_post(authorization, club_id, version, request)
        print("The response of ClubApi->update_approval_status_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->update_approval_status_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**StatusRequest**](StatusRequest.md)| request | 

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

# **update_club_using_post**
> Wrapper update_club_using_post(authorization, version, request)

updateClub

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.club_request import ClubRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubRequest() # ClubRequest | request

    try:
        # updateClub
        api_response = api_instance.update_club_using_post(authorization, version, request)
        print("The response of ClubApi->update_club_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->update_club_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubRequest**](ClubRequest.md)| request | 

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

# **update_staff_members_using_put**
> Wrapper update_staff_members_using_put(authorization, version, request)

updateStaffMembers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.staff_club_member_request import StaffClubMemberRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.StaffClubMemberRequest() # StaffClubMemberRequest | request

    try:
        # updateStaffMembers
        api_response = api_instance.update_staff_members_using_put(authorization, version, request)
        print("The response of ClubApi->update_staff_members_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->update_staff_members_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**StaffClubMemberRequest**](StaffClubMemberRequest.md)| request | 

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

