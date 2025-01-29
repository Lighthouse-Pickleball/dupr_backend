# dupr_backend.ClubApi

All URIs are relative to *https://backend.mydupr.com/*

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
> Wrapper add_club_using_put(body, authorization, version)

addClub

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubRequest() # ClubRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # addClub
    api_response = api_instance.add_club_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->add_club_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubRequest**](ClubRequest.md)| request | 
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

# **add_member_admin_using_put**
> Wrapper add_member_admin_using_put(body, authorization, club_id, version)

addMemberAdmin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.UserListRequest() # UserListRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # addMemberAdmin
    api_response = api_instance.add_member_admin_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->add_member_admin_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserListRequest**](UserListRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_multiple_admin_using_put**
> SingleWrapperOfClubMemberManyResponse add_member_multiple_admin_using_put(body, authorization, club_id, version)

addMemberMultipleAdmin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubMemberAddRequest() # ClubMemberAddRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # addMemberMultipleAdmin
    api_response = api_instance.add_member_multiple_admin_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->add_member_multiple_admin_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubMemberAddRequest**](ClubMemberAddRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfClubMemberManyResponse**](SingleWrapperOfClubMemberManyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_multiple_csv_admin_using_put**
> object add_member_multiple_csv_admin_using_put(authorization, club_id, version, request=request)

addMemberMultipleCsvAdmin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version
request = 'request_example' # str |  (optional)

try:
    # addMemberMultipleCsvAdmin
    api_response = api_instance.add_member_multiple_csv_admin_using_put(authorization, club_id, version, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->add_member_multiple_csv_admin_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 
 **request** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_member_request_using_put**
> object add_member_request_using_put(authorization, club_id, version)

addMemberRequest

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # addMemberRequest
    api_response = api_instance.add_member_request_using_put(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->add_member_request_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_roles_using_post**
> Wrapper approve_roles_using_post(body, authorization, club_id, version)

approveRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.IdsListRequest() # IdsListRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # approveRoles
    api_response = api_instance.approve_roles_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->approve_roles_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**IdsListRequest**](IdsListRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assign_roles_using_post**
> Wrapper assign_roles_using_post(body, authorization, club_id, version)

assignRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.AssignRoleRequest() # AssignRoleRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # assignRoles
    api_response = api_instance.assign_roles_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->assign_roles_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRoleRequest**](AssignRoleRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_match_history_by_filters_using_post**
> SingleWrapperOfPageOfMatchResponse club_match_history_by_filters_using_post(body, authorization, version)

clubMatchHistoryByFilters

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubMatchHistoryRequest() # ClubMatchHistoryRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # clubMatchHistoryByFilters
    api_response = api_instance.club_match_history_by_filters_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->club_match_history_by_filters_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubMatchHistoryRequest**](ClubMatchHistoryRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse club_match_history_using_get(authorization, club_id, limit, offset, version)

clubMatchHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # clubMatchHistory
    api_response = api_instance.club_match_history_using_get(authorization, club_id, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->club_match_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfMatchResponse**](SingleWrapperOfPageOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_save_match_using_put**
> object club_save_match_using_put(body, authorization, club_id, version)

clubSaveMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.MatchRequest() # MatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # clubSaveMatch
    api_response = api_instance.club_save_match_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->club_save_match_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchRequest**](MatchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_club_match_using_post**
> object delete_club_match_using_post(body, authorization, club_id, version)

deleteClubMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # deleteClubMatch
    api_response = api_instance.delete_club_match_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->delete_club_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_admin_using_delete**
> Wrapper delete_member_admin_using_delete(authorization, club_id, user_ids, version)

deleteMemberAdmin

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
user_ids = [56] # list[int] | userIds
version = 'version_example' # str | version

try:
    # deleteMemberAdmin
    api_response = api_instance.delete_member_admin_using_delete(authorization, club_id, user_ids, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->delete_member_admin_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **user_ids** | [**list[int]**](int.md)| userIds | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_request_using_delete**
> object delete_member_request_using_delete(authorization, club_id, version)

deleteMemberRequest

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # deleteMemberRequest
    api_response = api_instance.delete_member_request_using_delete(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->delete_member_request_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_club_match_using_put**
> SingleWrapperOfMatchResponse edit_club_match_using_put(body, authorization, club_id, version)

editClubMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | matchUpdateRequest
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # editClubMatch
    api_response = api_instance.edit_club_match_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->edit_club_match_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchUpdateRequest**](MatchUpdateRequest.md)| matchUpdateRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_club_roles_using_get**
> ArrayWrapperOfClubListingResponse get_all_club_roles_using_get(authorization, version)

getAllClubRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAllClubRoles
    api_response = api_instance.get_all_club_roles_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_club_roles_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfClubListingResponse**](ArrayWrapperOfClubListingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_currency_details_using_get**
> ArrayWrapperOfCurrencyDetailsResponse get_all_currency_details_using_get(authorization, version)

getAllCurrencyDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAllCurrencyDetails
    api_response = api_instance.get_all_currency_details_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_currency_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfCurrencyDetailsResponse**](ArrayWrapperOfCurrencyDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_members_download_using_post**
> SingleWrapperOfDownloadS3Response get_all_members_download_using_post(authorization, club_id, version)

getAllMembersDownload

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getAllMembersDownload
    api_response = api_instance.get_all_members_download_using_post(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_members_download_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_members_using_post**
> SingleWrapperOfPageOfClubMemberResponse get_all_members_using_post(body, authorization, club_id, version)

getAllMembers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getAllMembers
    api_response = api_instance.get_all_members_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_members_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfClubMemberResponse**](SingleWrapperOfPageOfClubMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_using_get1**
> ArrayWrapperOfRoleResponse get_all_roles_using_get1(authorization, version)

getAllRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAllRoles
    api_response = api_instance.get_all_roles_using_get1(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_roles_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfRoleResponse**](ArrayWrapperOfRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_staff_members_using_get**
> SingleWrapperOfStaffClubMemberResponse get_all_staff_members_using_get(authorization, club_id, version)

getAllStaffMembers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getAllStaffMembers
    api_response = api_instance.get_all_staff_members_using_get(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_all_staff_members_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfStaffClubMemberResponse**](SingleWrapperOfStaffClubMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_pending_invites_using_post**
> SingleWrapperOfPageOfClubMemberResponse get_club_pending_invites_using_post(body, authorization, club_id, version)

getClubPendingInvites

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getClubPendingInvites
    api_response = api_instance.get_club_pending_invites_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_pending_invites_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfClubMemberResponse**](SingleWrapperOfPageOfClubMemberResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_restrictions_using_post1**
> object get_club_restrictions_using_post1(authorization, club_id, version)

getClubRestrictions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getClubRestrictions
    api_response = api_instance.get_club_restrictions_using_post1(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_restrictions_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_roles_player_using_post**
> SingleWrapperOfRoleResponse get_club_roles_player_using_post(body, authorization, club_id, version)

getClubRolesPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.UserRequest() # UserRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getClubRolesPlayer
    api_response = api_instance.get_club_roles_player_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_roles_player_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRequest**](UserRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfRoleResponse**](SingleWrapperOfRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_roles_staff_using_get**
> SingleWrapperOfMapOfstringAndobject get_club_roles_staff_using_get(authorization, version)

getClubRolesStaff

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getClubRolesStaff
    api_response = api_instance.get_club_roles_staff_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_roles_staff_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMapOfstringAndobject**](SingleWrapperOfMapOfstringAndobject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_roles_using_post**
> SingleWrapperOfRoleResponse get_club_roles_using_post(body, authorization, club_id, version)

getClubRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.UserRequest() # UserRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getClubRoles
    api_response = api_instance.get_club_roles_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_roles_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRequest**](UserRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfRoleResponse**](SingleWrapperOfRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_using_get**
> SingleWrapperOfClubResponse get_club_using_get(authorization, club_id, version)

getClub

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getClub
    api_response = api_instance.get_club_using_get(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_club_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfClubResponse**](SingleWrapperOfClubResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs_using_get**
> SingleWrapperOfPageOfClubResponse get_clubs_using_get(authorization, limit, offset, own, q, version)

getClubs

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
own = true # bool | own
q = 'q_example' # str | q
version = 'version_example' # str | version

try:
    # getClubs
    api_response = api_instance.get_clubs_using_get(authorization, limit, offset, own, q, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_clubs_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **own** | **bool**| own | 
 **q** | **str**| q | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfClubResponse**](SingleWrapperOfPageOfClubResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs_using_post**
> SingleWrapperOfPageOfClubResponse get_clubs_using_post(body, authorization, version)

getClubs

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubSearch() # ClubSearch | clubSearch
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getClubs
    api_response = api_instance.get_clubs_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_clubs_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubSearch**](ClubSearch.md)| clubSearch | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfClubResponse**](SingleWrapperOfPageOfClubResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_currency_details_using_get**
> SingleWrapperOfCurrencyDetailsResponse get_currency_details_using_get(authorization, currency_code, version)

getCurrencyDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
currency_code = 'currency_code_example' # str | currencyCode
version = 'version_example' # str | version

try:
    # getCurrencyDetails
    api_response = api_instance.get_currency_details_using_get(authorization, currency_code, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_currency_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **currency_code** | **str**| currencyCode | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfCurrencyDetailsResponse**](SingleWrapperOfCurrencyDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_using_get1**
> SingleWrapperOfMatchResponse get_match_using_get1(authorization, club_id, id, version)

getMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
id = 789 # int | id
version = 'version_example' # str | version

try:
    # getMatch
    api_response = api_instance.get_match_using_get1(authorization, club_id, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_match_using_get1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_ranking_using_post**
> SingleWrapperOfClubMemberRankingResponse get_members_ranking_using_post(body, authorization, club_id, version)

getMembersRanking

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # getMembersRanking
    api_response = api_instance.get_members_ranking_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->get_members_ranking_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfClubMemberRankingResponse**](SingleWrapperOfClubMemberRankingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_single_member_using_put**
> SingleWrapperOfstring invite_single_member_using_put(body, authorization, club_id, version)

inviteSingleMember

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.InviteRequest() # InviteRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # inviteSingleMember
    api_response = api_instance.invite_single_member_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->invite_single_member_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**InviteRequest**](InviteRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_roles_using_post**
> Wrapper remove_roles_using_post(body, authorization, club_id, version)

removeRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.AssignRoleRequest() # AssignRoleRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # removeRoles
    api_response = api_instance.remove_roles_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->remove_roles_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssignRoleRequest**](AssignRoleRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_club_match_csv_using_put**
> object save_verified_club_match_csv_using_put(authorization, id, version, request=request)

saveVerifiedClubMatchCSV

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version
request = 'request_example' # str |  (optional)

try:
    # saveVerifiedClubMatchCSV
    api_response = api_instance.save_verified_club_match_csv_using_put(authorization, id, version, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->save_verified_club_match_csv_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 
 **request** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_approval_status_using_post**
> Wrapper update_approval_status_using_post(body, authorization, club_id, version)

updateApprovalStatus

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.StatusRequest() # StatusRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # updateApprovalStatus
    api_response = api_instance.update_approval_status_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->update_approval_status_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StatusRequest**](StatusRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_using_post**
> Wrapper update_club_using_post(body, authorization, version)

updateClub

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.ClubRequest() # ClubRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateClub
    api_response = api_instance.update_club_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->update_club_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubRequest**](ClubRequest.md)| request | 
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

# **update_staff_members_using_put**
> Wrapper update_staff_members_using_put(body, authorization, version)

updateStaffMembers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.ClubApi()
body = dupr_backend.StaffClubMemberRequest() # StaffClubMemberRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateStaffMembers
    api_response = api_instance.update_staff_members_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClubApi->update_staff_members_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**StaffClubMemberRequest**](StaffClubMemberRequest.md)| request | 
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

