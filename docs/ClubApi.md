# dupr_backend.ClubApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_club**](ClubApi.md#add_club) | **PUT** /club/{version}/add | 
[**add_member_admin**](ClubApi.md#add_member_admin) | **PUT** /club/{clubId}/members/{version}/add | 
[**add_member_multiple_admin**](ClubApi.md#add_member_multiple_admin) | **PUT** /club/{clubId}/members/{version}/multiple/add | 
[**add_member_multiple_csv_admin**](ClubApi.md#add_member_multiple_csv_admin) | **PUT** /club/{clubId}/members/{version}/csv/add | 
[**add_member_request**](ClubApi.md#add_member_request) | **PUT** /club/{clubId}/members/{version}/join | 
[**approve_roles**](ClubApi.md#approve_roles) | **POST** /club/{clubId}/{version}/approve | 
[**assign_roles**](ClubApi.md#assign_roles) | **POST** /club/{clubId}/roles/{version}/assign | 
[**club_match_history**](ClubApi.md#club_match_history) | **GET** /club/{clubId}/{version}/history | 
[**club_match_history_by_filters**](ClubApi.md#club_match_history_by_filters) | **POST** /club/match/{version}/history | 
[**club_save_match**](ClubApi.md#club_save_match) | **PUT** /club/{clubId}/match/{version}/save | 
[**delete_club_match**](ClubApi.md#delete_club_match) | **POST** /club/{clubId}/match/{id}/{version}/delete | 
[**delete_member_admin**](ClubApi.md#delete_member_admin) | **DELETE** /club/{clubId}/members/{version}/remove | 
[**delete_member_request**](ClubApi.md#delete_member_request) | **DELETE** /club/{clubId}/members/{version}/leave | 
[**edit_club_match**](ClubApi.md#edit_club_match) | **PUT** /club/{clubId}/match/{id}/{version}/edit | 
[**get_all_club_roles**](ClubApi.md#get_all_club_roles) | **GET** /club/roles/{version}/all | 
[**get_all_currency_details**](ClubApi.md#get_all_currency_details) | **GET** /club/currency/{version}/all | 
[**get_all_members**](ClubApi.md#get_all_members) | **POST** /club/{clubId}/members/{version}/all | 
[**get_all_members_download**](ClubApi.md#get_all_members_download) | **POST** /club/{clubId}/members/{version}/all/download | 
[**get_all_roles**](ClubApi.md#get_all_roles) | **GET** /club/{clubId}/roles/{version}/all | 
[**get_club**](ClubApi.md#get_club) | **GET** /club/{version}/{clubId} | 
[**get_club_pending_invites**](ClubApi.md#get_club_pending_invites) | **POST** /club/{clubId}/members/{version}/pending/invites | 
[**get_club_restrictions1**](ClubApi.md#get_club_restrictions1) | **POST** /club/{clubId}/{version}/restrictions | 
[**get_club_roles**](ClubApi.md#get_club_roles) | **POST** /club/{clubId}/roles/{version}/user | 
[**get_club_roles_player**](ClubApi.md#get_club_roles_player) | **POST** /club/{clubId}/roles/{version}/permission | 
[**get_club_roles_staff**](ClubApi.md#get_club_roles_staff) | **GET** /club/roles/{version}/staff | 
[**get_clubs**](ClubApi.md#get_clubs) | **GET** /club/{version}/all | 
[**get_clubs1**](ClubApi.md#get_clubs1) | **POST** /club/{version}/all | 
[**get_currency_details**](ClubApi.md#get_currency_details) | **GET** /club/currency/{version}/{currencyCode} | 
[**get_match**](ClubApi.md#get_match) | **GET** /club/{clubId}/match/{id}/{version}/get | 
[**get_members_ranking**](ClubApi.md#get_members_ranking) | **POST** /club/{clubId}/{version}/ranking | 
[**invite_single_member**](ClubApi.md#invite_single_member) | **PUT** /club/{clubId}/members/{version}/invite | 
[**remove_roles**](ClubApi.md#remove_roles) | **POST** /club/{clubId}/roles/{version}/remove | 
[**save_verified_club_match_csv**](ClubApi.md#save_verified_club_match_csv) | **PUT** /club/{id}/match/verified/{version}/save/csv/add | 
[**save_verified_multi_club_match_csv**](ClubApi.md#save_verified_multi_club_match_csv) | **PUT** /club/match/bulk | 
[**update_approval_status**](ClubApi.md#update_approval_status) | **POST** /club/{clubId}/{version}/approval | 
[**update_club**](ClubApi.md#update_club) | **POST** /club/{version}/update | 


# **add_club**
> Wrapper add_club(version, club_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_request import ClubRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_request = dupr_backend.ClubRequest() # ClubRequest | 

    try:
        api_response = api_instance.add_club(version, club_request)
        print("The response of ClubApi->add_club:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_club: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_request** | [**ClubRequest**](ClubRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **add_member_admin**
> Wrapper add_member_admin(version, club_id, user_list_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.user_list_request import UserListRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    user_list_request = dupr_backend.UserListRequest() # UserListRequest | 

    try:
        api_response = api_instance.add_member_admin(version, club_id, user_list_request)
        print("The response of ClubApi->add_member_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **user_list_request** | [**UserListRequest**](UserListRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **add_member_multiple_admin**
> SingleWrapperClubMemberManyResponse add_member_multiple_admin(version, club_id, club_member_add_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_member_add_request import ClubMemberAddRequest
from dupr_backend.models.single_wrapper_club_member_many_response import SingleWrapperClubMemberManyResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    club_member_add_request = dupr_backend.ClubMemberAddRequest() # ClubMemberAddRequest | 

    try:
        api_response = api_instance.add_member_multiple_admin(version, club_id, club_member_add_request)
        print("The response of ClubApi->add_member_multiple_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_multiple_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **club_member_add_request** | [**ClubMemberAddRequest**](ClubMemberAddRequest.md)|  | 

### Return type

[**SingleWrapperClubMemberManyResponse**](SingleWrapperClubMemberManyResponse.md)

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

# **add_member_multiple_csv_admin**
> object add_member_multiple_csv_admin(version, club_id, save_verified_match_cvs_request=save_verified_match_cvs_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.save_verified_match_cvs_request import SaveVerifiedMatchCVSRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    save_verified_match_cvs_request = dupr_backend.SaveVerifiedMatchCVSRequest() # SaveVerifiedMatchCVSRequest |  (optional)

    try:
        api_response = api_instance.add_member_multiple_csv_admin(version, club_id, save_verified_match_cvs_request=save_verified_match_cvs_request)
        print("The response of ClubApi->add_member_multiple_csv_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_multiple_csv_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **save_verified_match_cvs_request** | [**SaveVerifiedMatchCVSRequest**](SaveVerifiedMatchCVSRequest.md)|  | [optional] 

### Return type

**object**

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

# **add_member_request**
> object add_member_request(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.add_member_request(version, club_id)
        print("The response of ClubApi->add_member_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->add_member_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **approve_roles**
> Wrapper approve_roles(version, club_id, ids_list_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.ids_list_request import IdsListRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    ids_list_request = dupr_backend.IdsListRequest() # IdsListRequest | 

    try:
        api_response = api_instance.approve_roles(version, club_id, ids_list_request)
        print("The response of ClubApi->approve_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->approve_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **ids_list_request** | [**IdsListRequest**](IdsListRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **assign_roles**
> Wrapper assign_roles(version, club_id, assign_role_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.assign_role_request import AssignRoleRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    assign_role_request = dupr_backend.AssignRoleRequest() # AssignRoleRequest | 

    try:
        api_response = api_instance.assign_roles(version, club_id, assign_role_request)
        print("The response of ClubApi->assign_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->assign_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **assign_role_request** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **club_match_history**
> SingleWrapperPageMatchResponse club_match_history(version, offset, limit, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_match_response import SingleWrapperPageMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.club_match_history(version, offset, limit, club_id)
        print("The response of ClubApi->club_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperPageMatchResponse**](SingleWrapperPageMatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_match_history_by_filters**
> SingleWrapperPageMatchResponse club_match_history_by_filters(version, club_match_history_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_match_history_request import ClubMatchHistoryRequest
from dupr_backend.models.single_wrapper_page_match_response import SingleWrapperPageMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_match_history_request = dupr_backend.ClubMatchHistoryRequest() # ClubMatchHistoryRequest | 

    try:
        api_response = api_instance.club_match_history_by_filters(version, club_match_history_request)
        print("The response of ClubApi->club_match_history_by_filters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_match_history_by_filters: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_match_history_request** | [**ClubMatchHistoryRequest**](ClubMatchHistoryRequest.md)|  | 

### Return type

[**SingleWrapperPageMatchResponse**](SingleWrapperPageMatchResponse.md)

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

# **club_save_match**
> object club_save_match(version, club_id, match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    match_request = dupr_backend.MatchRequest() # MatchRequest | 

    try:
        api_response = api_instance.club_save_match(version, club_id, match_request)
        print("The response of ClubApi->club_save_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->club_save_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **match_request** | [**MatchRequest**](MatchRequest.md)|  | 

### Return type

**object**

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

# **delete_club_match**
> object delete_club_match(version, club_id, id, delete_match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    id = 56 # int | 
    delete_match_request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | 

    try:
        api_response = api_instance.delete_club_match(version, club_id, id, delete_match_request)
        print("The response of ClubApi->delete_club_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_club_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **id** | **int**|  | 
 **delete_match_request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)|  | 

### Return type

**object**

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

# **delete_member_admin**
> Wrapper delete_member_admin(version, club_id, user_ids)

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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    user_ids = [56] # List[int] | 

    try:
        api_response = api_instance.delete_member_admin(version, club_id, user_ids)
        print("The response of ClubApi->delete_member_admin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_member_admin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **user_ids** | [**List[int]**](int.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_request**
> object delete_member_request(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.delete_member_request(version, club_id)
        print("The response of ClubApi->delete_member_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->delete_member_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_club_match**
> SingleWrapperMatchResponse edit_club_match(version, club_id, id, match_update_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_update_request import MatchUpdateRequest
from dupr_backend.models.single_wrapper_match_response import SingleWrapperMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    id = 56 # int | 
    match_update_request = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | 

    try:
        api_response = api_instance.edit_club_match(version, club_id, id, match_update_request)
        print("The response of ClubApi->edit_club_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->edit_club_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **id** | **int**|  | 
 **match_update_request** | [**MatchUpdateRequest**](MatchUpdateRequest.md)|  | 

### Return type

[**SingleWrapperMatchResponse**](SingleWrapperMatchResponse.md)

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

# **get_all_club_roles**
> ArrayWrapperClubListingResponse get_all_club_roles(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_club_listing_response import ArrayWrapperClubListingResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_all_club_roles(version)
        print("The response of ClubApi->get_all_club_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_club_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

[**ArrayWrapperClubListingResponse**](ArrayWrapperClubListingResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_currency_details**
> ArrayWrapperCurrencyDetailsResponse get_all_currency_details(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_currency_details_response import ArrayWrapperCurrencyDetailsResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_all_currency_details(version)
        print("The response of ClubApi->get_all_currency_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_currency_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

[**ArrayWrapperCurrencyDetailsResponse**](ArrayWrapperCurrencyDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_members**
> SingleWrapperPageClubMemberResponse get_all_members(version, club_id, club_members_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_page_club_member_response import SingleWrapperPageClubMemberResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    club_members_search_request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | 

    try:
        api_response = api_instance.get_all_members(version, club_id, club_members_search_request)
        print("The response of ClubApi->get_all_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **club_members_search_request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageClubMemberResponse**](SingleWrapperPageClubMemberResponse.md)

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

# **get_all_members_download**
> SingleWrapperDownloadS3Response get_all_members_download(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.get_all_members_download(version, club_id)
        print("The response of ClubApi->get_all_members_download:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_members_download: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperDownloadS3Response**](SingleWrapperDownloadS3Response.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles**
> ArrayWrapperRoleResponse get_all_roles(club_id, version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_role_response import ArrayWrapperRoleResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    club_id = 56 # int | 
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_all_roles(club_id, version)
        print("The response of ClubApi->get_all_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_all_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **club_id** | **int**|  | 
 **version** | **str**|  | 

### Return type

[**ArrayWrapperRoleResponse**](ArrayWrapperRoleResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club**
> SingleWrapperClubResponse get_club(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_club_response import SingleWrapperClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.get_club(version, club_id)
        print("The response of ClubApi->get_club:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperClubResponse**](SingleWrapperClubResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_pending_invites**
> SingleWrapperPageClubMemberResponse get_club_pending_invites(version, club_id, club_members_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_page_club_member_response import SingleWrapperPageClubMemberResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    club_members_search_request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | 

    try:
        api_response = api_instance.get_club_pending_invites(version, club_id, club_members_search_request)
        print("The response of ClubApi->get_club_pending_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_pending_invites: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **club_members_search_request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageClubMemberResponse**](SingleWrapperPageClubMemberResponse.md)

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

# **get_club_restrictions1**
> object get_club_restrictions1(version, club_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.get_club_restrictions1(version, club_id)
        print("The response of ClubApi->get_club_restrictions1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_restrictions1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_roles**
> SingleWrapperRoleResponse get_club_roles(version, club_id, user_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_role_response import SingleWrapperRoleResponse
from dupr_backend.models.user_request import UserRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    user_request = dupr_backend.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.get_club_roles(version, club_id, user_request)
        print("The response of ClubApi->get_club_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **user_request** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**SingleWrapperRoleResponse**](SingleWrapperRoleResponse.md)

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

# **get_club_roles_player**
> SingleWrapperRoleResponse get_club_roles_player(version, club_id, user_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_role_response import SingleWrapperRoleResponse
from dupr_backend.models.user_request import UserRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    user_request = dupr_backend.UserRequest() # UserRequest | 

    try:
        api_response = api_instance.get_club_roles_player(version, club_id, user_request)
        print("The response of ClubApi->get_club_roles_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **user_request** | [**UserRequest**](UserRequest.md)|  | 

### Return type

[**SingleWrapperRoleResponse**](SingleWrapperRoleResponse.md)

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

# **get_club_roles_staff**
> SingleWrapperMapStringObject get_club_roles_staff(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_map_string_object import SingleWrapperMapStringObject
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 

    try:
        api_response = api_instance.get_club_roles_staff(version)
        print("The response of ClubApi->get_club_roles_staff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_club_roles_staff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 

### Return type

[**SingleWrapperMapStringObject**](SingleWrapperMapStringObject.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs**
> SingleWrapperPageClubResponse get_clubs(version, q, own, offset, limit)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_club_response import SingleWrapperPageClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    q = 'q_example' # str | 
    own = True # bool | 
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.get_clubs(version, q, own, offset, limit)
        print("The response of ClubApi->get_clubs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_clubs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **q** | **str**|  | 
 **own** | **bool**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 

### Return type

[**SingleWrapperPageClubResponse**](SingleWrapperPageClubResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clubs1**
> SingleWrapperPageClubResponse get_clubs1(version, club_search)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_search import ClubSearch
from dupr_backend.models.single_wrapper_page_club_response import SingleWrapperPageClubResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_search = dupr_backend.ClubSearch() # ClubSearch | 

    try:
        api_response = api_instance.get_clubs1(version, club_search)
        print("The response of ClubApi->get_clubs1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_clubs1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_search** | [**ClubSearch**](ClubSearch.md)|  | 

### Return type

[**SingleWrapperPageClubResponse**](SingleWrapperPageClubResponse.md)

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

# **get_currency_details**
> SingleWrapperCurrencyDetailsResponse get_currency_details(version, currency_code)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_currency_details_response import SingleWrapperCurrencyDetailsResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    currency_code = 'currency_code_example' # str | 

    try:
        api_response = api_instance.get_currency_details(version, currency_code)
        print("The response of ClubApi->get_currency_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_currency_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **currency_code** | **str**|  | 

### Return type

[**SingleWrapperCurrencyDetailsResponse**](SingleWrapperCurrencyDetailsResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match**
> SingleWrapperMatchResponse get_match(version, club_id, id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_match_response import SingleWrapperMatchResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    id = 56 # int | 

    try:
        api_response = api_instance.get_match(version, club_id, id)
        print("The response of ClubApi->get_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **id** | **int**|  | 

### Return type

[**SingleWrapperMatchResponse**](SingleWrapperMatchResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_members_ranking**
> SingleWrapperClubMemberRankingResponse get_members_ranking(version, club_id, club_members_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_members_search_request import ClubMembersSearchRequest
from dupr_backend.models.single_wrapper_club_member_ranking_response import SingleWrapperClubMemberRankingResponse
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    club_members_search_request = dupr_backend.ClubMembersSearchRequest() # ClubMembersSearchRequest | 

    try:
        api_response = api_instance.get_members_ranking(version, club_id, club_members_search_request)
        print("The response of ClubApi->get_members_ranking:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->get_members_ranking: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **club_members_search_request** | [**ClubMembersSearchRequest**](ClubMembersSearchRequest.md)|  | 

### Return type

[**SingleWrapperClubMemberRankingResponse**](SingleWrapperClubMemberRankingResponse.md)

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

# **invite_single_member**
> SingleWrapperString invite_single_member(version, club_id, invite_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.invite_request import InviteRequest
from dupr_backend.models.single_wrapper_string import SingleWrapperString
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    invite_request = dupr_backend.InviteRequest() # InviteRequest | 

    try:
        api_response = api_instance.invite_single_member(version, club_id, invite_request)
        print("The response of ClubApi->invite_single_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->invite_single_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **invite_request** | [**InviteRequest**](InviteRequest.md)|  | 

### Return type

[**SingleWrapperString**](SingleWrapperString.md)

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

# **remove_roles**
> Wrapper remove_roles(version, club_id, assign_role_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.assign_role_request import AssignRoleRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    assign_role_request = dupr_backend.AssignRoleRequest() # AssignRoleRequest | 

    try:
        api_response = api_instance.remove_roles(version, club_id, assign_role_request)
        print("The response of ClubApi->remove_roles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->remove_roles: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **assign_role_request** | [**AssignRoleRequest**](AssignRoleRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **save_verified_club_match_csv**
> object save_verified_club_match_csv(version, id, request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    id = 56 # int | 
    request = None # bytearray | 

    try:
        api_response = api_instance.save_verified_club_match_csv(version, id, request)
        print("The response of ClubApi->save_verified_club_match_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->save_verified_club_match_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **id** | **int**|  | 
 **request** | **bytearray**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_multi_club_match_csv**
> object save_verified_multi_club_match_csv(request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.ClubApi(api_client)
    request = None # bytearray | 

    try:
        api_response = api_instance.save_verified_multi_club_match_csv(request)
        print("The response of ClubApi->save_verified_multi_club_match_csv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->save_verified_multi_club_match_csv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | **bytearray**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_approval_status**
> Wrapper update_approval_status(version, club_id, status_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.status_request import StatusRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_id = 56 # int | 
    status_request = dupr_backend.StatusRequest() # StatusRequest | 

    try:
        api_response = api_instance.update_approval_status(version, club_id, status_request)
        print("The response of ClubApi->update_approval_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->update_approval_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_id** | **int**|  | 
 **status_request** | [**StatusRequest**](StatusRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **update_club**
> Wrapper update_club(version, club_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_request import ClubRequest
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
    api_instance = dupr_backend.ClubApi(api_client)
    version = 'version_example' # str | 
    club_request = dupr_backend.ClubRequest() # ClubRequest | 

    try:
        api_response = api_instance.update_club(version, club_request)
        print("The response of ClubApi->update_club:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClubApi->update_club: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **club_request** | [**ClubRequest**](ClubRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

