# dupr_backend.AdminApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_match**](AdminApi.md#activate_match) | **POST** /admin/{version}/panel/match/active | 
[**add_key_to_external_client**](AdminApi.md#add_key_to_external_client) | **POST** /admin/{version}/client/keys/add | 
[**adjust_rating**](AdminApi.md#adjust_rating) | **PUT** /admin/rating/{version}/edit | 
[**admin_verified_match_history**](AdminApi.md#admin_verified_match_history) | **GET** /admin/match/{version}/history | 
[**batch_calculated_statistics**](AdminApi.md#batch_calculated_statistics) | **PUT** /admin/calculated/{version}/stats | 
[**batch_club_matches**](AdminApi.md#batch_club_matches) | **POST** /admin/{version}/club/{clubId}/match/batch | 
[**batch_manual_club_matches**](AdminApi.md#batch_manual_club_matches) | **POST** /admin/{version}/match/club-batch | 
[**batch_manual_matches**](AdminApi.md#batch_manual_matches) | **POST** /admin/{version}/match/batch | 
[**batch_player_rating**](AdminApi.md#batch_player_rating) | **PUT** /admin/{version}/rating/batch | 
[**batch_player_rating_provisional**](AdminApi.md#batch_player_rating_provisional) | **PUT** /admin/{version}/ratings-provisional/batch | 
[**batch_set_reliability_scores**](AdminApi.md#batch_set_reliability_scores) | **POST** /admin/{version}/player/batch-reliability-score | 
[**block_admin_apis**](AdminApi.md#block_admin_apis) | **PUT** /admin/{version}/panel/block | 
[**bulk_delete_matches**](AdminApi.md#bulk_delete_matches) | **PUT** /admin/{version}/match/delete | 
[**bulk_grant_entitlements_by_user_id**](AdminApi.md#bulk_grant_entitlements_by_user_id) | **POST** /admin/revenuecat/entitlements/grant/bulk | 
[**bulk_reliability_score**](AdminApi.md#bulk_reliability_score) | **PUT** /admin/{version}/player/bulk-reliability-score | 
[**bulk_send_coppa_email**](AdminApi.md#bulk_send_coppa_email) | **POST** /admin/{version}/bulkcoppaemail | 
[**bulk_send_wrapped_email**](AdminApi.md#bulk_send_wrapped_email) | **POST** /admin/{version}/bulkwrappedemail | 
[**bulk_set_club_restrictions**](AdminApi.md#bulk_set_club_restrictions) | **PUT** /admin/{version}/clubs/restrictions/bulk | 
[**bulk_upload_pb_com_events**](AdminApi.md#bulk_upload_pb_com_events) | **POST** /admin/{version}/bulkuploadpbcomevents | 
[**change_email**](AdminApi.md#change_email) | **PUT** /admin/{version}/panel/email/change | 
[**change_role**](AdminApi.md#change_role) | **POST** /admin/{version}/panel/role/change | 
[**club_create**](AdminApi.md#club_create) | **PUT** /admin/{version}/clubs/create | 
[**create_banner**](AdminApi.md#create_banner) | **POST** /admin/{version}/panel/create/banner | 
[**create_clubs_batch**](AdminApi.md#create_clubs_batch) | **PUT** /admin/{version}/clubs/create/batch | 
[**create_external_client**](AdminApi.md#create_external_client) | **POST** /admin/{version}/client | 
[**decode**](AdminApi.md#decode) | **GET** /admin/decode | 
[**delete_club**](AdminApi.md#delete_club) | **DELETE** /admin/{version}/club/{clubId} | 
[**delete_match**](AdminApi.md#delete_match) | **POST** /admin/{version}/panel/match/delete | 
[**delete_user**](AdminApi.md#delete_user) | **PUT** /admin/{version}/panel/user/delete | 
[**delete_wix_user**](AdminApi.md#delete_wix_user) | **DELETE** /admin/wix/{version}/{version}/delete | 
[**dupr_id**](AdminApi.md#dupr_id) | **GET** /admin/{version}/panel/user | 
[**edit_club_staff**](AdminApi.md#edit_club_staff) | **POST** /admin/club/staff/{version}/edit | 
[**encode**](AdminApi.md#encode) | **GET** /admin/encode | 
[**export_matches_missing_team_player**](AdminApi.md#export_matches_missing_team_player) | **GET** /admin/{version}/team-players/missing/export | 
[**export_provisional_ratings**](AdminApi.md#export_provisional_ratings) | **GET** /admin/datascience/provisional_ratings/export | 
[**export_users_via_mail**](AdminApi.md#export_users_via_mail) | **POST** /admin/{version}/panel/user/export | 
[**find_duplicated_account_for_players**](AdminApi.md#find_duplicated_account_for_players) | **POST** /admin/{version}/duplicated | 
[**get_active_banner**](AdminApi.md#get_active_banner) | **GET** /admin/{version}/panel/get/banner | 
[**get_all_banner**](AdminApi.md#get_all_banner) | **GET** /admin/{version}/panel/get/banners | 
[**get_all_roles1**](AdminApi.md#get_all_roles1) | **GET** /admin/{version}/roles | 
[**get_club_restrictions**](AdminApi.md#get_club_restrictions) | **POST** /admin/{version}/clubs/restrictions | 
[**get_club_settings**](AdminApi.md#get_club_settings) | **POST** /admin/{version}/clubs/settings | 
[**get_external_client_permissions**](AdminApi.md#get_external_client_permissions) | **POST** /admin/{version}/client/keys | 
[**get_external_clients**](AdminApi.md#get_external_clients) | **POST** /admin/{version}/client/batch | 
[**get_match1**](AdminApi.md#get_match1) | **GET** /admin/{version}/panel/match/{id} | 
[**get_rating_leaderboard**](AdminApi.md#get_rating_leaderboard) | **GET** /admin/{version}/leaderboard/search | 
[**get_user_bracket**](AdminApi.md#get_user_bracket) | **POST** /admin/{version}/panel/brackets/user/all | 
[**get_user_profile**](AdminApi.md#get_user_profile) | **GET** /admin/{version}/panel/user/profile | 
[**grant_entitlements_by_user_id**](AdminApi.md#grant_entitlements_by_user_id) | **POST** /admin/revenuecat/entitlements/grant | 
[**index_club_members**](AdminApi.md#index_club_members) | **POST** /admin/{version}/members/index | 
[**index_clubs**](AdminApi.md#index_clubs) | **PUT** /admin/{version}/clubs/index | 
[**index_player**](AdminApi.md#index_player) | **PATCH** /admin/{version}/index/{id} | 
[**index_players**](AdminApi.md#index_players) | **PATCH** /admin/{version}/index | 
[**map_csv_to_braze_segment**](AdminApi.md#map_csv_to_braze_segment) | **PUT** /admin/marketing/mapCsvToBrazeSegment | 
[**match_codes_export**](AdminApi.md#match_codes_export) | **GET** /admin/{version}/match/export/codes | 
[**match_reassign**](AdminApi.md#match_reassign) | **POST** /admin/{version}/match/reassign | 
[**match_reassign_batch**](AdminApi.md#match_reassign_batch) | **POST** /admin/{version}/match/reassign/batch | 
[**matches_export**](AdminApi.md#matches_export) | **GET** /admin/{version}/match/export | 
[**merge_users**](AdminApi.md#merge_users) | **POST** /admin/{version}/panel/merge | 
[**merge_users_batch**](AdminApi.md#merge_users_batch) | **POST** /admin/{version}/panel/merge/batch | 
[**obfuscate**](AdminApi.md#obfuscate) | **GET** /admin/obfuscate | 
[**obfuscate_match_id**](AdminApi.md#obfuscate_match_id) | **GET** /admin/obfuscate-matchid | 
[**populate_unknown_player_pre_ratings**](AdminApi.md#populate_unknown_player_pre_ratings) | **POST** /admin/{version}/unknown/players/populate-pre-rating | 
[**re_create_es_index**](AdminApi.md#re_create_es_index) | **POST** /admin/{version}/panel/es/{id}/mapping | 
[**recalculate_match_elo_ratings_bulk**](AdminApi.md#recalculate_match_elo_ratings_bulk) | **POST** /admin/{version}/match/elo-rating-recalculation | 
[**recalculate_pre_match_ratings**](AdminApi.md#recalculate_pre_match_ratings) | **POST** /admin/{version}/match/pre-rating-impact | 
[**recalculate_pre_match_ratings1**](AdminApi.md#recalculate_pre_match_ratings1) | **POST** /admin/{version}/match/bulk-pre-rating-impact | 
[**remove_all_club_restrictions**](AdminApi.md#remove_all_club_restrictions) | **DELETE** /admin/{version}/clubs/restrictions/all | 
[**remove_club_restrictions**](AdminApi.md#remove_club_restrictions) | **DELETE** /admin/{version}/clubs/restrictions | 
[**remove_tag_from_shopify_customers**](AdminApi.md#remove_tag_from_shopify_customers) | **DELETE** /admin/subscriptions/shopify/users/tag | 
[**reset_client_secret**](AdminApi.md#reset_client_secret) | **GET** /admin/client/{version}/secret/reset | 
[**restrict**](AdminApi.md#restrict) | **POST** /admin/{version}/panel/user/{id}/restrict | 
[**save_topic**](AdminApi.md#save_topic) | **POST** /admin/{version}/topic | 
[**save_verified_match1**](AdminApi.md#save_verified_match1) | **PUT** /admin/match/{version}/save | 
[**set_club_restrictions**](AdminApi.md#set_club_restrictions) | **PUT** /admin/{version}/clubs/restrictions | 
[**set_club_settings**](AdminApi.md#set_club_settings) | **PUT** /admin/{version}/clubs/settings | 
[**set_users_active_by_dupr_id**](AdminApi.md#set_users_active_by_dupr_id) | **POST** /admin/users/enable | 
[**set_users_inactive_by_dupr_id**](AdminApi.md#set_users_inactive_by_dupr_id) | **POST** /admin/users/disable | 
[**signup**](AdminApi.md#signup) | **PUT** /admin/{version}/panel/user/signup | 
[**signup_batch**](AdminApi.md#signup_batch) | **PUT** /admin/{version}/panel/user/signup/batch | 
[**trigger_missing_elo_rating_for_players**](AdminApi.md#trigger_missing_elo_rating_for_players) | **POST** /admin/{version}/player-rating-history | 
[**unclaim_user**](AdminApi.md#unclaim_user) | **PUT** /admin/{version}/panel/user/unclaim | 
[**unobfuscate**](AdminApi.md#unobfuscate) | **GET** /admin/unobfuscate | 
[**unobfuscate_match_code**](AdminApi.md#unobfuscate_match_code) | **GET** /admin/unobfuscate-matchcode | 
[**update_banner**](AdminApi.md#update_banner) | **PUT** /admin/{version}/panel/update/banner | 
[**update_club_currency**](AdminApi.md#update_club_currency) | **PUT** /admin/{version}/club/{clubId}/currency | 
[**update_club_revenue_model**](AdminApi.md#update_club_revenue_model) | **PUT** /admin/{version}/club/{clubId}/revenue | 
[**update_currency_rates**](AdminApi.md#update_currency_rates) | **GET** /admin/club/currency/{version}/update | 
[**update_es_index**](AdminApi.md#update_es_index) | **PUT** /admin/{version}/panel/es/{id}/mapping | 
[**update_external_client_permissions**](AdminApi.md#update_external_client_permissions) | **POST** /admin/{version}/client/permissions | 
[**update_external_id_cron**](AdminApi.md#update_external_id_cron) | **PUT** /admin/{version}/external-id/bulk | 
[**update_lucra_connection1**](AdminApi.md#update_lucra_connection1) | **PUT** /admin/{version}/panel/user/{id}/lucra-connect | 
[**update_match**](AdminApi.md#update_match) | **PUT** /admin/{version}/panel/match/{version}/update | 
[**update_payment_status**](AdminApi.md#update_payment_status) | **POST** /admin/{version}/panel/brackets/registration/update | 
[**update_player_rating**](AdminApi.md#update_player_rating) | **PUT** /admin/{version}/rating/{id} | 
[**update_player_statistics**](AdminApi.md#update_player_statistics) | **PUT** /admin/calculated/{version}/stats/update | 
[**update_ratings_cron**](AdminApi.md#update_ratings_cron) | **PUT** /admin/{version}/ratings/bulk | 
[**update_referral_code**](AdminApi.md#update_referral_code) | **PATCH** /admin/referral-code/{version}/update | 
[**update_status**](AdminApi.md#update_status) | **POST** /admin/{version}/panel/user/status | 
[**update_user_profile**](AdminApi.md#update_user_profile) | **PUT** /admin/{version}/panel/user/profile | 
[**upload_dupr_performance_chart_data**](AdminApi.md#upload_dupr_performance_chart_data) | **PUT** /admin/{version}/panel/performance | 
[**upsert_and_tag_shopify_customers**](AdminApi.md#upsert_and_tag_shopify_customers) | **PUT** /admin/subscriptions/shopify/users/tag | 
[**user_lookup**](AdminApi.md#user_lookup) | **POST** /admin/{version}/panel/user/lookup | 
[**verify_email**](AdminApi.md#verify_email) | **POST** /admin/{version}/panel/email/verify | 


# **activate_match**
> Wrapper activate_match(version, delete_match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    delete_match_request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | 

    try:
        api_response = api_instance.activate_match(version, delete_match_request)
        print("The response of AdminApi->activate_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->activate_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **delete_match_request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)|  | 

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

# **add_key_to_external_client**
> object add_key_to_external_client(version, add_client_key_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.add_client_key_request import AddClientKeyRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    add_client_key_request = dupr_backend.AddClientKeyRequest() # AddClientKeyRequest | 

    try:
        api_response = api_instance.add_key_to_external_client(version, add_client_key_request)
        print("The response of AdminApi->add_key_to_external_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_key_to_external_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **add_client_key_request** | [**AddClientKeyRequest**](AddClientKeyRequest.md)|  | 

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

# **adjust_rating**
> Wrapper adjust_rating(version, adjust_rating_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.adjust_rating_request import AdjustRatingRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    adjust_rating_request = dupr_backend.AdjustRatingRequest() # AdjustRatingRequest | 

    try:
        api_response = api_instance.adjust_rating(version, adjust_rating_request)
        print("The response of AdminApi->adjust_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->adjust_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **adjust_rating_request** | [**AdjustRatingRequest**](AdjustRatingRequest.md)|  | 

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

# **admin_verified_match_history**
> SingleWrapperPageMatchResponse admin_verified_match_history(version, offset, limit)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    offset = 56 # int | 
    limit = 56 # int | 

    try:
        api_response = api_instance.admin_verified_match_history(version, offset, limit)
        print("The response of AdminApi->admin_verified_match_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_verified_match_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **offset** | **int**|  | 
 **limit** | **int**|  | 

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

# **batch_calculated_statistics**
> batch_calculated_statistics(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_instance.batch_calculated_statistics(version, s3_object)
    except Exception as e:
        print("Exception when calling AdminApi->batch_calculated_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_club_matches**
> SingleWrapperUnit batch_club_matches(version, club_id, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.batch_club_matches(version, club_id, s3_object)
        print("The response of AdminApi->batch_club_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_club_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 
 **s3_object** | [**S3Object**](S3Object.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

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

# **batch_manual_club_matches**
> SingleWrapperUnit batch_manual_club_matches(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.batch_manual_club_matches(version, s3_object)
        print("The response of AdminApi->batch_manual_club_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_manual_club_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

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

# **batch_manual_matches**
> SingleWrapperUnit batch_manual_matches(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.batch_manual_matches(version, s3_object)
        print("The response of AdminApi->batch_manual_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_manual_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

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

# **batch_player_rating**
> SingleWrapperUnit batch_player_rating(version, batch_player_rating_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.batch_player_rating_request import BatchPlayerRatingRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    batch_player_rating_request = dupr_backend.BatchPlayerRatingRequest() # BatchPlayerRatingRequest | 

    try:
        api_response = api_instance.batch_player_rating(version, batch_player_rating_request)
        print("The response of AdminApi->batch_player_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_player_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **batch_player_rating_request** | [**BatchPlayerRatingRequest**](BatchPlayerRatingRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_player_rating_provisional**
> SingleWrapperUnit batch_player_rating_provisional(version, batch_player_rating_provisional_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.batch_player_rating_provisional_request import BatchPlayerRatingProvisionalRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    batch_player_rating_provisional_request = dupr_backend.BatchPlayerRatingProvisionalRequest() # BatchPlayerRatingProvisionalRequest | 

    try:
        api_response = api_instance.batch_player_rating_provisional(version, batch_player_rating_provisional_request)
        print("The response of AdminApi->batch_player_rating_provisional:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_player_rating_provisional: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **batch_player_rating_provisional_request** | [**BatchPlayerRatingProvisionalRequest**](BatchPlayerRatingProvisionalRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_set_reliability_scores**
> batch_set_reliability_scores(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_instance.batch_set_reliability_scores(version, s3_object)
    except Exception as e:
        print("Exception when calling AdminApi->batch_set_reliability_scores: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

### Return type

void (empty response body)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_admin_apis**
> bool block_admin_apis(version, flag)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    flag = True # bool | 

    try:
        api_response = api_instance.block_admin_apis(version, flag)
        print("The response of AdminApi->block_admin_apis:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->block_admin_apis: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **flag** | **bool**|  | 

### Return type

**bool**

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

# **bulk_delete_matches**
> Wrapper bulk_delete_matches(version, type, document)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    type = 'type_example' # str | 
    document = None # bytearray | 

    try:
        api_response = api_instance.bulk_delete_matches(version, type, document)
        print("The response of AdminApi->bulk_delete_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_delete_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **type** | **str**|  | 
 **document** | **bytearray**|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **bulk_grant_entitlements_by_user_id**
> ResultUnit bulk_grant_entitlements_by_user_id(entitlements, expiration_time, file)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_unit import ResultUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    entitlements = ['entitlements_example'] # List[str] | 
    expiration_time = 56 # int | 
    file = None # bytearray | 

    try:
        api_response = api_instance.bulk_grant_entitlements_by_user_id(entitlements, expiration_time, file)
        print("The response of AdminApi->bulk_grant_entitlements_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_grant_entitlements_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entitlements** | [**List[str]**](str.md)|  | 
 **expiration_time** | **int**|  | 
 **file** | **bytearray**|  | 

### Return type

[**ResultUnit**](ResultUnit.md)

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

# **bulk_reliability_score**
> Wrapper bulk_reliability_score(version, request)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    request = None # bytearray | 

    try:
        api_response = api_instance.bulk_reliability_score(version, request)
        print("The response of AdminApi->bulk_reliability_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_reliability_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | 

### Return type

[**Wrapper**](Wrapper.md)

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

# **bulk_send_coppa_email**
> object bulk_send_coppa_email(version, bulk_coppa_email_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.bulk_coppa_email_request import BulkCoppaEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    bulk_coppa_email_request = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | 

    try:
        api_response = api_instance.bulk_send_coppa_email(version, bulk_coppa_email_request)
        print("The response of AdminApi->bulk_send_coppa_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_send_coppa_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **bulk_coppa_email_request** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_send_wrapped_email**
> object bulk_send_wrapped_email(version, bulk_coppa_email_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.bulk_coppa_email_request import BulkCoppaEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    bulk_coppa_email_request = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | 

    try:
        api_response = api_instance.bulk_send_wrapped_email(version, bulk_coppa_email_request)
        print("The response of AdminApi->bulk_send_wrapped_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_send_wrapped_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **bulk_coppa_email_request** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_set_club_restrictions**
> object bulk_set_club_restrictions(version, bulk_set_club_restrictions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.bulk_set_club_restrictions_request import BulkSetClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    bulk_set_club_restrictions_request = dupr_backend.BulkSetClubRestrictionsRequest() # BulkSetClubRestrictionsRequest | 

    try:
        api_response = api_instance.bulk_set_club_restrictions(version, bulk_set_club_restrictions_request)
        print("The response of AdminApi->bulk_set_club_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_set_club_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **bulk_set_club_restrictions_request** | [**BulkSetClubRestrictionsRequest**](BulkSetClubRestrictionsRequest.md)|  | 

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

# **bulk_upload_pb_com_events**
> object bulk_upload_pb_com_events(version, page_size=page_size, delay=delay, current_page=current_page, total_events=total_events)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    page_size = 56 # int |  (optional)
    delay = 56 # int |  (optional)
    current_page = 56 # int |  (optional)
    total_events = 56 # int |  (optional)

    try:
        api_response = api_instance.bulk_upload_pb_com_events(version, page_size=page_size, delay=delay, current_page=current_page, total_events=total_events)
        print("The response of AdminApi->bulk_upload_pb_com_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_upload_pb_com_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **page_size** | **int**|  | [optional] 
 **delay** | **int**|  | [optional] 
 **current_page** | **int**|  | [optional] 
 **total_events** | **int**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_email**
> Wrapper change_email(version, change_email_admin_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.change_email_admin_request import ChangeEmailAdminRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    change_email_admin_request = dupr_backend.ChangeEmailAdminRequest() # ChangeEmailAdminRequest | 

    try:
        api_response = api_instance.change_email(version, change_email_admin_request)
        print("The response of AdminApi->change_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->change_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **change_email_admin_request** | [**ChangeEmailAdminRequest**](ChangeEmailAdminRequest.md)|  | 

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

# **change_role**
> Wrapper change_role(version, change_role_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.change_role_request import ChangeRoleRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    change_role_request = dupr_backend.ChangeRoleRequest() # ChangeRoleRequest | 

    try:
        api_response = api_instance.change_role(version, change_role_request)
        print("The response of AdminApi->change_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->change_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **change_role_request** | [**ChangeRoleRequest**](ChangeRoleRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_create**
> Wrapper club_create(version, create_clubs_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.create_clubs_request import CreateClubsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    create_clubs_request = dupr_backend.CreateClubsRequest() # CreateClubsRequest | 

    try:
        api_response = api_instance.club_create(version, create_clubs_request)
        print("The response of AdminApi->club_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->club_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **create_clubs_request** | [**CreateClubsRequest**](CreateClubsRequest.md)|  | 

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

# **create_banner**
> SingleWrapperUnit create_banner(version, create_banner_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.create_banner_request import CreateBannerRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    create_banner_request = dupr_backend.CreateBannerRequest() # CreateBannerRequest | 

    try:
        api_response = api_instance.create_banner(version, create_banner_request)
        print("The response of AdminApi->create_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **create_banner_request** | [**CreateBannerRequest**](CreateBannerRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clubs_batch**
> SingleWrapperString create_clubs_batch(version, document)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    document = None # bytearray | 

    try:
        api_response = api_instance.create_clubs_batch(version, document)
        print("The response of AdminApi->create_clubs_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_clubs_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | 

### Return type

[**SingleWrapperString**](SingleWrapperString.md)

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

# **create_external_client**
> SingleWrapperCreateClientResponse create_external_client(version, create_client_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.create_client_request import CreateClientRequest
from dupr_backend.models.single_wrapper_create_client_response import SingleWrapperCreateClientResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    create_client_request = dupr_backend.CreateClientRequest() # CreateClientRequest | 

    try:
        api_response = api_instance.create_external_client(version, create_client_request)
        print("The response of AdminApi->create_external_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_external_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **create_client_request** | [**CreateClientRequest**](CreateClientRequest.md)|  | 

### Return type

[**SingleWrapperCreateClientResponse**](SingleWrapperCreateClientResponse.md)

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

# **decode**
> object decode(id=id, ids=ids)

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
    api_instance = dupr_backend.AdminApi(api_client)
    id = 'id_example' # str |  (optional)
    ids = 'ids_example' # str |  (optional)

    try:
        api_response = api_instance.decode(id=id, ids=ids)
        print("The response of AdminApi->decode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->decode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **ids** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_club**
> Wrapper delete_club(version, club_id)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 

    try:
        api_response = api_instance.delete_club(version, club_id)
        print("The response of AdminApi->delete_club:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_club: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 

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

# **delete_match**
> Wrapper delete_match(version, delete_match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    delete_match_request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | 

    try:
        api_response = api_instance.delete_match(version, delete_match_request)
        print("The response of AdminApi->delete_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **delete_match_request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)|  | 

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

# **delete_user**
> Wrapper delete_user(version, request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.dynamic_user_identity_type import DynamicUserIdentityType
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    request = dupr_backend.DynamicUserIdentityType() # DynamicUserIdentityType | 

    try:
        api_response = api_instance.delete_user(version, request)
        print("The response of AdminApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **request** | [**DynamicUserIdentityType**](.md)|  | 

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

# **delete_wix_user**
> Wrapper delete_wix_user(version, user_id)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_id = 56 # int | 

    try:
        api_response = api_instance.delete_wix_user(version, user_id)
        print("The response of AdminApi->delete_wix_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_wix_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_id** | **int**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dupr_id**
> SingleWrapperAdminUserProfile dupr_id(version, dupr_id=dupr_id, user_id=user_id, external_id=external_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_admin_user_profile import SingleWrapperAdminUserProfile
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    dupr_id = 'dupr_id_example' # str |  (optional)
    user_id = 56 # int |  (optional)
    external_id = 'external_id_example' # str |  (optional)

    try:
        api_response = api_instance.dupr_id(version, dupr_id=dupr_id, user_id=user_id, external_id=external_id)
        print("The response of AdminApi->dupr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->dupr_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **dupr_id** | **str**|  | [optional] 
 **user_id** | **int**|  | [optional] 
 **external_id** | **str**|  | [optional] 

### Return type

[**SingleWrapperAdminUserProfile**](SingleWrapperAdminUserProfile.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_club_staff**
> Wrapper edit_club_staff(version, edit_club_staff_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.edit_club_staff_request import EditClubStaffRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    edit_club_staff_request = dupr_backend.EditClubStaffRequest() # EditClubStaffRequest | 

    try:
        api_response = api_instance.edit_club_staff(version, edit_club_staff_request)
        print("The response of AdminApi->edit_club_staff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->edit_club_staff: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **edit_club_staff_request** | [**EditClubStaffRequest**](EditClubStaffRequest.md)|  | 

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

# **encode**
> object encode(id=id, ids=ids)

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
    api_instance = dupr_backend.AdminApi(api_client)
    id = 56 # int |  (optional)
    ids = 'ids_example' # str |  (optional)

    try:
        api_response = api_instance.encode(id=id, ids=ids)
        print("The response of AdminApi->encode:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->encode: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | [optional] 
 **ids** | **str**|  | [optional] 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_matches_missing_team_player**
> Wrapper export_matches_missing_team_player(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.export_matches_missing_team_player(version)
        print("The response of AdminApi->export_matches_missing_team_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->export_matches_missing_team_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

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

# **export_provisional_ratings**
> object export_provisional_ratings()

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
    api_instance = dupr_backend.AdminApi(api_client)

    try:
        api_response = api_instance.export_provisional_ratings()
        print("The response of AdminApi->export_provisional_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->export_provisional_ratings: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_users_via_mail**
> Wrapper export_users_via_mail(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.export_users_via_mail(version)
        print("The response of AdminApi->export_users_via_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->export_users_via_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

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

# **find_duplicated_account_for_players**
> ArrayWrapperDuplicatedAccountResponse find_duplicated_account_for_players(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_duplicated_account_response import ArrayWrapperDuplicatedAccountResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.find_duplicated_account_for_players(version)
        print("The response of AdminApi->find_duplicated_account_for_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->find_duplicated_account_for_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperDuplicatedAccountResponse**](ArrayWrapperDuplicatedAccountResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_banner**
> ArrayWrapperInformativeBannerResponce get_active_banner(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_informative_banner_responce import ArrayWrapperInformativeBannerResponce
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.get_active_banner(version)
        print("The response of AdminApi->get_active_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_active_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperInformativeBannerResponce**](ArrayWrapperInformativeBannerResponce.md)

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

# **get_all_banner**
> ArrayWrapperInformativeBannerResponce get_all_banner(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.array_wrapper_informative_banner_responce import ArrayWrapperInformativeBannerResponce
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.get_all_banner(version)
        print("The response of AdminApi->get_all_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_all_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperInformativeBannerResponce**](ArrayWrapperInformativeBannerResponce.md)

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

# **get_all_roles1**
> ArrayWrapperRoleResponse get_all_roles1(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.get_all_roles1(version)
        print("The response of AdminApi->get_all_roles1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_all_roles1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

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

# **get_club_restrictions**
> object get_club_restrictions(version, get_club_restrictions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.get_club_restrictions_request import GetClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    get_club_restrictions_request = dupr_backend.GetClubRestrictionsRequest() # GetClubRestrictionsRequest | 

    try:
        api_response = api_instance.get_club_restrictions(version, get_club_restrictions_request)
        print("The response of AdminApi->get_club_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_club_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **get_club_restrictions_request** | [**GetClubRestrictionsRequest**](GetClubRestrictionsRequest.md)|  | 

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

# **get_club_settings**
> object get_club_settings(version, get_club_settings_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.get_club_settings_request import GetClubSettingsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    get_club_settings_request = dupr_backend.GetClubSettingsRequest() # GetClubSettingsRequest | 

    try:
        api_response = api_instance.get_club_settings(version, get_club_settings_request)
        print("The response of AdminApi->get_club_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_club_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **get_club_settings_request** | [**GetClubSettingsRequest**](GetClubSettingsRequest.md)|  | 

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

# **get_external_client_permissions**
> object get_external_client_permissions(version, get_client_permissions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.get_client_permissions_request import GetClientPermissionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    get_client_permissions_request = dupr_backend.GetClientPermissionsRequest() # GetClientPermissionsRequest | 

    try:
        api_response = api_instance.get_external_client_permissions(version, get_client_permissions_request)
        print("The response of AdminApi->get_external_client_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_external_client_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **get_client_permissions_request** | [**GetClientPermissionsRequest**](GetClientPermissionsRequest.md)|  | 

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

# **get_external_clients**
> object get_external_clients(version, batch_get_clients_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.batch_get_clients_request import BatchGetClientsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    batch_get_clients_request = dupr_backend.BatchGetClientsRequest() # BatchGetClientsRequest | 

    try:
        api_response = api_instance.get_external_clients(version, batch_get_clients_request)
        print("The response of AdminApi->get_external_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_external_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **batch_get_clients_request** | [**BatchGetClientsRequest**](BatchGetClientsRequest.md)|  | 

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

# **get_match1**
> SingleWrapperMatchResponse get_match1(version, id)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 'id_example' # str | 

    try:
        api_response = api_instance.get_match1(version, id)
        print("The response of AdminApi->get_match1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_match1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **str**|  | 

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

# **get_rating_leaderboard**
> object get_rating_leaderboard(version, request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.rating_leaderboard_request import RatingLeaderboardRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    request = dupr_backend.RatingLeaderboardRequest() # RatingLeaderboardRequest | 

    try:
        api_response = api_instance.get_rating_leaderboard(version, request)
        print("The response of AdminApi->get_rating_leaderboard:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_rating_leaderboard: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **request** | [**RatingLeaderboardRequest**](.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_bracket**
> SingleWrapperPageBracketResponse get_user_bracket(version, user_bracket_admin_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_bracket_response import SingleWrapperPageBracketResponse
from dupr_backend.models.user_bracket_admin_request import UserBracketAdminRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_bracket_admin_request = dupr_backend.UserBracketAdminRequest() # UserBracketAdminRequest | 

    try:
        api_response = api_instance.get_user_bracket(version, user_bracket_admin_request)
        print("The response of AdminApi->get_user_bracket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_bracket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_bracket_admin_request** | [**UserBracketAdminRequest**](UserBracketAdminRequest.md)|  | 

### Return type

[**SingleWrapperPageBracketResponse**](SingleWrapperPageBracketResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile**
> SingleWrapperUserResponse get_user_profile(version, user_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_user_response import SingleWrapperUserResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_id = 56 # int | 

    try:
        api_response = api_instance.get_user_profile(version, user_id)
        print("The response of AdminApi->get_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_id** | **int**|  | 

### Return type

[**SingleWrapperUserResponse**](SingleWrapperUserResponse.md)

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

# **grant_entitlements_by_user_id**
> ResultUnit grant_entitlements_by_user_id(admin_grant_entitlement_by_dupr_id_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.admin_grant_entitlement_by_dupr_id_request import AdminGrantEntitlementByDuprIdRequest
from dupr_backend.models.result_unit import ResultUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    admin_grant_entitlement_by_dupr_id_request = dupr_backend.AdminGrantEntitlementByDuprIdRequest() # AdminGrantEntitlementByDuprIdRequest | 

    try:
        api_response = api_instance.grant_entitlements_by_user_id(admin_grant_entitlement_by_dupr_id_request)
        print("The response of AdminApi->grant_entitlements_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->grant_entitlements_by_user_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_grant_entitlement_by_dupr_id_request** | [**AdminGrantEntitlementByDuprIdRequest**](AdminGrantEntitlementByDuprIdRequest.md)|  | 

### Return type

[**ResultUnit**](ResultUnit.md)

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

# **index_club_members**
> Wrapper index_club_members(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.index_club_members(version)
        print("The response of AdminApi->index_club_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_club_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_clubs**
> Wrapper index_clubs(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.index_clubs(version)
        print("The response of AdminApi->index_clubs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_clubs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_player**
> object index_player(version, id)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 'id_example' # str | 

    try:
        api_response = api_instance.index_player(version, id)
        print("The response of AdminApi->index_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **str**|  | 

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

# **index_players**
> Wrapper index_players(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.index_players(version)
        print("The response of AdminApi->index_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

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

# **map_csv_to_braze_segment**
> object map_csv_to_braze_segment(document)

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
    api_instance = dupr_backend.AdminApi(api_client)
    document = None # bytearray | 

    try:
        api_response = api_instance.map_csv_to_braze_segment(document)
        print("The response of AdminApi->map_csv_to_braze_segment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->map_csv_to_braze_segment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **bytearray**|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/octet-stream

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_codes_export**
> Wrapper match_codes_export(version, sources=sources)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.match_codes_export(version, sources=sources)
        print("The response of AdminApi->match_codes_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_codes_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **sources** | [**List[str]**](str.md)|  | [optional] 

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

# **match_reassign**
> SingleWrapperUnit match_reassign(version, matches_reassign_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.matches_reassign_request import MatchesReassignRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    matches_reassign_request = dupr_backend.MatchesReassignRequest() # MatchesReassignRequest | 

    try:
        api_response = api_instance.match_reassign(version, matches_reassign_request)
        print("The response of AdminApi->match_reassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_reassign: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **matches_reassign_request** | [**MatchesReassignRequest**](MatchesReassignRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_reassign_batch**
> SingleWrapperString match_reassign_batch(version, notify=notify, signup_batch_request=signup_batch_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.signup_batch_request import SignupBatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    notify = True # bool |  (optional)
    signup_batch_request = dupr_backend.SignupBatchRequest() # SignupBatchRequest |  (optional)

    try:
        api_response = api_instance.match_reassign_batch(version, notify=notify, signup_batch_request=signup_batch_request)
        print("The response of AdminApi->match_reassign_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_reassign_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **notify** | **bool**|  | [optional] 
 **signup_batch_request** | [**SignupBatchRequest**](SignupBatchRequest.md)|  | [optional] 

### Return type

[**SingleWrapperString**](SingleWrapperString.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_export**
> Wrapper matches_export(version, all, sources=sources)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    all = True # bool | 
    sources = ['sources_example'] # List[str] |  (optional)

    try:
        api_response = api_instance.matches_export(version, all, sources=sources)
        print("The response of AdminApi->matches_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->matches_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **all** | **bool**|  | 
 **sources** | [**List[str]**](str.md)|  | [optional] 

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

# **merge_users**
> SingleWrapperMergeUsersResponse merge_users(version, merge_users_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.merge_users_request import MergeUsersRequest
from dupr_backend.models.single_wrapper_merge_users_response import SingleWrapperMergeUsersResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    merge_users_request = dupr_backend.MergeUsersRequest() # MergeUsersRequest | 

    try:
        api_response = api_instance.merge_users(version, merge_users_request)
        print("The response of AdminApi->merge_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->merge_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **merge_users_request** | [**MergeUsersRequest**](MergeUsersRequest.md)|  | 

### Return type

[**SingleWrapperMergeUsersResponse**](SingleWrapperMergeUsersResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_users_batch**
> SingleWrapperString merge_users_batch(version, document)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    document = None # bytearray | 

    try:
        api_response = api_instance.merge_users_batch(version, document)
        print("The response of AdminApi->merge_users_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->merge_users_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | 

### Return type

[**SingleWrapperString**](SingleWrapperString.md)

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

# **obfuscate**
> object obfuscate(type, id=id, ids=ids)

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
    api_instance = dupr_backend.AdminApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int |  (optional)
    ids = 'ids_example' # str |  (optional)

    try:
        api_response = api_instance.obfuscate(type, id=id, ids=ids)
        print("The response of AdminApi->obfuscate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->obfuscate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | [optional] 
 **ids** | **str**|  | [optional] 

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

# **obfuscate_match_id**
> str obfuscate_match_id(to_type, ids=ids)

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
    api_instance = dupr_backend.AdminApi(api_client)
    to_type = 'to_type_example' # str | 
    ids = 'ids_example' # str |  (optional)

    try:
        api_response = api_instance.obfuscate_match_id(to_type, ids=ids)
        print("The response of AdminApi->obfuscate_match_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->obfuscate_match_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **to_type** | **str**|  | 
 **ids** | **str**|  | [optional] 

### Return type

**str**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **populate_unknown_player_pre_ratings**
> Wrapper populate_unknown_player_pre_ratings(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.populate_unknown_player_pre_ratings(version)
        print("The response of AdminApi->populate_unknown_player_pre_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->populate_unknown_player_pre_ratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_create_es_index**
> Wrapper re_create_es_index(version, id)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 'id_example' # str | 

    try:
        api_response = api_instance.re_create_es_index(version, id)
        print("The response of AdminApi->re_create_es_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->re_create_es_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **str**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_match_elo_ratings_bulk**
> Wrapper recalculate_match_elo_ratings_bulk(version, type, signup_batch_request=signup_batch_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.signup_batch_request import SignupBatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    type = 'type_example' # str | 
    signup_batch_request = dupr_backend.SignupBatchRequest() # SignupBatchRequest |  (optional)

    try:
        api_response = api_instance.recalculate_match_elo_ratings_bulk(version, type, signup_batch_request=signup_batch_request)
        print("The response of AdminApi->recalculate_match_elo_ratings_bulk:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_match_elo_ratings_bulk: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **type** | **str**|  | 
 **signup_batch_request** | [**SignupBatchRequest**](SignupBatchRequest.md)|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings**
> Wrapper recalculate_pre_match_ratings(version, calculate_matches_range)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.calculate_matches_range import CalculateMatchesRange
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    calculate_matches_range = dupr_backend.CalculateMatchesRange() # CalculateMatchesRange | 

    try:
        api_response = api_instance.recalculate_pre_match_ratings(version, calculate_matches_range)
        print("The response of AdminApi->recalculate_pre_match_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_pre_match_ratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **calculate_matches_range** | [**CalculateMatchesRange**](CalculateMatchesRange.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings1**
> Wrapper recalculate_pre_match_ratings1(version, type, signup_batch_request=signup_batch_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.signup_batch_request import SignupBatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    type = 'type_example' # str | 
    signup_batch_request = dupr_backend.SignupBatchRequest() # SignupBatchRequest |  (optional)

    try:
        api_response = api_instance.recalculate_pre_match_ratings1(version, type, signup_batch_request=signup_batch_request)
        print("The response of AdminApi->recalculate_pre_match_ratings1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_pre_match_ratings1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **type** | **str**|  | 
 **signup_batch_request** | [**SignupBatchRequest**](SignupBatchRequest.md)|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_club_restrictions**
> object remove_all_club_restrictions(version, remove_all_club_restrictions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.remove_all_club_restrictions_request import RemoveAllClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    remove_all_club_restrictions_request = dupr_backend.RemoveAllClubRestrictionsRequest() # RemoveAllClubRestrictionsRequest | 

    try:
        api_response = api_instance.remove_all_club_restrictions(version, remove_all_club_restrictions_request)
        print("The response of AdminApi->remove_all_club_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_all_club_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **remove_all_club_restrictions_request** | [**RemoveAllClubRestrictionsRequest**](RemoveAllClubRestrictionsRequest.md)|  | 

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

# **remove_club_restrictions**
> object remove_club_restrictions(version, remove_club_restrictions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.remove_club_restrictions_request import RemoveClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    remove_club_restrictions_request = dupr_backend.RemoveClubRestrictionsRequest() # RemoveClubRestrictionsRequest | 

    try:
        api_response = api_instance.remove_club_restrictions(version, remove_club_restrictions_request)
        print("The response of AdminApi->remove_club_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_club_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **remove_club_restrictions_request** | [**RemoveClubRestrictionsRequest**](RemoveClubRestrictionsRequest.md)|  | 

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

# **remove_tag_from_shopify_customers**
> object remove_tag_from_shopify_customers(document)

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
    api_instance = dupr_backend.AdminApi(api_client)
    document = None # bytearray | 

    try:
        api_response = api_instance.remove_tag_from_shopify_customers(document)
        print("The response of AdminApi->remove_tag_from_shopify_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_tag_from_shopify_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **bytearray**|  | 

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

# **reset_client_secret**
> SingleWrapperCreateClientResponse reset_client_secret(version, client_id)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_create_client_response import SingleWrapperCreateClientResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    client_id = 56 # int | 

    try:
        api_response = api_instance.reset_client_secret(version, client_id)
        print("The response of AdminApi->reset_client_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->reset_client_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **client_id** | **int**|  | 

### Return type

[**SingleWrapperCreateClientResponse**](SingleWrapperCreateClientResponse.md)

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

# **restrict**
> Wrapper restrict(version, id, user_restrict_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.user_restrict_request import UserRestrictRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    user_restrict_request = dupr_backend.UserRestrictRequest() # UserRestrictRequest | 

    try:
        api_response = api_instance.restrict(version, id, user_restrict_request)
        print("The response of AdminApi->restrict:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->restrict: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **user_restrict_request** | [**UserRestrictRequest**](UserRestrictRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_topic**
> SingleWrapperTopicResponse save_topic(version, topic_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_topic_response import SingleWrapperTopicResponse
from dupr_backend.models.topic_request import TopicRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    topic_request = dupr_backend.TopicRequest() # TopicRequest | 

    try:
        api_response = api_instance.save_topic(version, topic_request)
        print("The response of AdminApi->save_topic:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->save_topic: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **topic_request** | [**TopicRequest**](TopicRequest.md)|  | 

### Return type

[**SingleWrapperTopicResponse**](SingleWrapperTopicResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match1**
> Wrapper save_verified_match1(version, match_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_request = dupr_backend.MatchRequest() # MatchRequest | 

    try:
        api_response = api_instance.save_verified_match1(version, match_request)
        print("The response of AdminApi->save_verified_match1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->save_verified_match1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **match_request** | [**MatchRequest**](MatchRequest.md)|  | 

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

# **set_club_restrictions**
> object set_club_restrictions(version, set_club_restrictions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.set_club_restrictions_request import SetClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    set_club_restrictions_request = dupr_backend.SetClubRestrictionsRequest() # SetClubRestrictionsRequest | 

    try:
        api_response = api_instance.set_club_restrictions(version, set_club_restrictions_request)
        print("The response of AdminApi->set_club_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_club_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **set_club_restrictions_request** | [**SetClubRestrictionsRequest**](SetClubRestrictionsRequest.md)|  | 

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

# **set_club_settings**
> object set_club_settings(version, set_club_settings_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.set_club_settings_request import SetClubSettingsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    set_club_settings_request = dupr_backend.SetClubSettingsRequest() # SetClubSettingsRequest | 

    try:
        api_response = api_instance.set_club_settings(version, set_club_settings_request)
        print("The response of AdminApi->set_club_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_club_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **set_club_settings_request** | [**SetClubSettingsRequest**](SetClubSettingsRequest.md)|  | 

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

# **set_users_active_by_dupr_id**
> ResultString set_users_active_by_dupr_id(set_dupr_ids_inactive_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_string import ResultString
from dupr_backend.models.set_dupr_ids_inactive_request import SetDuprIdsInactiveRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    set_dupr_ids_inactive_request = dupr_backend.SetDuprIdsInactiveRequest() # SetDuprIdsInactiveRequest | 

    try:
        api_response = api_instance.set_users_active_by_dupr_id(set_dupr_ids_inactive_request)
        print("The response of AdminApi->set_users_active_by_dupr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_users_active_by_dupr_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_dupr_ids_inactive_request** | [**SetDuprIdsInactiveRequest**](SetDuprIdsInactiveRequest.md)|  | 

### Return type

[**ResultString**](ResultString.md)

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

# **set_users_inactive_by_dupr_id**
> ResultString set_users_inactive_by_dupr_id(set_dupr_ids_inactive_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.result_string import ResultString
from dupr_backend.models.set_dupr_ids_inactive_request import SetDuprIdsInactiveRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    set_dupr_ids_inactive_request = dupr_backend.SetDuprIdsInactiveRequest() # SetDuprIdsInactiveRequest | 

    try:
        api_response = api_instance.set_users_inactive_by_dupr_id(set_dupr_ids_inactive_request)
        print("The response of AdminApi->set_users_inactive_by_dupr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_users_inactive_by_dupr_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_dupr_ids_inactive_request** | [**SetDuprIdsInactiveRequest**](SetDuprIdsInactiveRequest.md)|  | 

### Return type

[**ResultString**](ResultString.md)

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

# **signup**
> SingleWrapperString signup(version, sign_up_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.sign_up_request import SignUpRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    sign_up_request = dupr_backend.SignUpRequest() # SignUpRequest | 

    try:
        api_response = api_instance.signup(version, sign_up_request)
        print("The response of AdminApi->signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **sign_up_request** | [**SignUpRequest**](SignUpRequest.md)|  | 

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

# **signup_batch**
> SingleWrapperMapStringString signup_batch(version, document)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_map_string_string import SingleWrapperMapStringString
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    document = None # bytearray | 

    try:
        api_response = api_instance.signup_batch(version, document)
        print("The response of AdminApi->signup_batch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->signup_batch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | 

### Return type

[**SingleWrapperMapStringString**](SingleWrapperMapStringString.md)

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

# **trigger_missing_elo_rating_for_players**
> SingleWrapperUnit trigger_missing_elo_rating_for_players(version)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.trigger_missing_elo_rating_for_players(version)
        print("The response of AdminApi->trigger_missing_elo_rating_for_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->trigger_missing_elo_rating_for_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaim_user**
> Wrapper unclaim_user(version, request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.dynamic_user_identity_type import DynamicUserIdentityType
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    request = dupr_backend.DynamicUserIdentityType() # DynamicUserIdentityType | 

    try:
        api_response = api_instance.unclaim_user(version, request)
        print("The response of AdminApi->unclaim_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unclaim_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **request** | [**DynamicUserIdentityType**](.md)|  | 

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

# **unobfuscate**
> object unobfuscate(type, id=id, ids=ids)

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
    api_instance = dupr_backend.AdminApi(api_client)
    type = 'type_example' # str | 
    id = 56 # int |  (optional)
    ids = 'ids_example' # str |  (optional)

    try:
        api_response = api_instance.unobfuscate(type, id=id, ids=ids)
        print("The response of AdminApi->unobfuscate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unobfuscate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | 
 **id** | **int**|  | [optional] 
 **ids** | **str**|  | [optional] 

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

# **unobfuscate_match_code**
> object unobfuscate_match_code(matches=matches)

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
    api_instance = dupr_backend.AdminApi(api_client)
    matches = 'matches_example' # str |  (optional)

    try:
        api_response = api_instance.unobfuscate_match_code(matches=matches)
        print("The response of AdminApi->unobfuscate_match_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unobfuscate_match_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matches** | **str**|  | [optional] 

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

# **update_banner**
> SingleWrapperUnit update_banner(version, create_banner_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.create_banner_request import CreateBannerRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    create_banner_request = dupr_backend.CreateBannerRequest() # CreateBannerRequest | 

    try:
        api_response = api_instance.update_banner(version, create_banner_request)
        print("The response of AdminApi->update_banner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_banner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **create_banner_request** | [**CreateBannerRequest**](CreateBannerRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_currency**
> SingleWrapperUnit update_club_currency(version, club_id, club_currency_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_currency_request import ClubCurrencyRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 
    club_currency_request = dupr_backend.ClubCurrencyRequest() # ClubCurrencyRequest | 

    try:
        api_response = api_instance.update_club_currency(version, club_id, club_currency_request)
        print("The response of AdminApi->update_club_currency:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_club_currency: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 
 **club_currency_request** | [**ClubCurrencyRequest**](ClubCurrencyRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_revenue_model**
> SingleWrapperRevenueModel update_club_revenue_model(version, club_id, club_revenue_model_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.club_revenue_model_request import ClubRevenueModelRequest
from dupr_backend.models.single_wrapper_revenue_model import SingleWrapperRevenueModel
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    club_id = 56 # int | 
    club_revenue_model_request = dupr_backend.ClubRevenueModelRequest() # ClubRevenueModelRequest | 

    try:
        api_response = api_instance.update_club_revenue_model(version, club_id, club_revenue_model_request)
        print("The response of AdminApi->update_club_revenue_model:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_club_revenue_model: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **club_id** | **int**|  | 
 **club_revenue_model_request** | [**ClubRevenueModelRequest**](ClubRevenueModelRequest.md)|  | 

### Return type

[**SingleWrapperRevenueModel**](SingleWrapperRevenueModel.md)

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

# **update_currency_rates**
> Wrapper update_currency_rates(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.update_currency_rates(version)
        print("The response of AdminApi->update_currency_rates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_currency_rates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_es_index**
> Wrapper update_es_index(version, id, body)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 'id_example' # str | 
    body = 'body_example' # str | 

    try:
        api_response = api_instance.update_es_index(version, id, body)
        print("The response of AdminApi->update_es_index:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_es_index: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **str**|  | 
 **body** | **str**|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_client_permissions**
> SingleWrapperUpdateClientPermissionsResponse update_external_client_permissions(version, update_client_permissions_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_update_client_permissions_response import SingleWrapperUpdateClientPermissionsResponse
from dupr_backend.models.update_client_permissions_request import UpdateClientPermissionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    update_client_permissions_request = dupr_backend.UpdateClientPermissionsRequest() # UpdateClientPermissionsRequest | 

    try:
        api_response = api_instance.update_external_client_permissions(version, update_client_permissions_request)
        print("The response of AdminApi->update_external_client_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_external_client_permissions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **update_client_permissions_request** | [**UpdateClientPermissionsRequest**](UpdateClientPermissionsRequest.md)|  | 

### Return type

[**SingleWrapperUpdateClientPermissionsResponse**](SingleWrapperUpdateClientPermissionsResponse.md)

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

# **update_external_id_cron**
> object update_external_id_cron(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.update_external_id_cron(version, s3_object)
        print("The response of AdminApi->update_external_id_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_external_id_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

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

# **update_lucra_connection1**
> Wrapper update_lucra_connection1(version, id, user_lucra_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.user_lucra_request import UserLucraRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    user_lucra_request = dupr_backend.UserLucraRequest() # UserLucraRequest | 

    try:
        api_response = api_instance.update_lucra_connection1(version, id, user_lucra_request)
        print("The response of AdminApi->update_lucra_connection1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_lucra_connection1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **user_lucra_request** | [**UserLucraRequest**](UserLucraRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_match**
> SingleWrapperMatchResponse update_match(version, match_update_request)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    match_update_request = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | 

    try:
        api_response = api_instance.update_match(version, match_update_request)
        print("The response of AdminApi->update_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
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

# **update_payment_status**
> Wrapper update_payment_status(version, update_registration_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.update_registration_request import UpdateRegistrationRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    update_registration_request = [dupr_backend.UpdateRegistrationRequest()] # List[UpdateRegistrationRequest] | 

    try:
        api_response = api_instance.update_payment_status(version, update_registration_request)
        print("The response of AdminApi->update_payment_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_payment_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **update_registration_request** | [**List[UpdateRegistrationRequest]**](UpdateRegistrationRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_rating**
> SingleWrapperUnit update_player_rating(version, id, player_rating_update_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.player_rating_update_request import PlayerRatingUpdateRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    id = 56 # int | 
    player_rating_update_request = dupr_backend.PlayerRatingUpdateRequest() # PlayerRatingUpdateRequest | 

    try:
        api_response = api_instance.update_player_rating(version, id, player_rating_update_request)
        print("The response of AdminApi->update_player_rating:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_player_rating: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **id** | **int**|  | 
 **player_rating_update_request** | [**PlayerRatingUpdateRequest**](PlayerRatingUpdateRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_statistics**
> SingleWrapperBoolean update_player_statistics(version, player_statistics_update_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.player_statistics_update_request import PlayerStatisticsUpdateRequest
from dupr_backend.models.single_wrapper_boolean import SingleWrapperBoolean
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    player_statistics_update_request = dupr_backend.PlayerStatisticsUpdateRequest() # PlayerStatisticsUpdateRequest | 

    try:
        api_response = api_instance.update_player_statistics(version, player_statistics_update_request)
        print("The response of AdminApi->update_player_statistics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_player_statistics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **player_statistics_update_request** | [**PlayerStatisticsUpdateRequest**](PlayerStatisticsUpdateRequest.md)|  | 

### Return type

[**SingleWrapperBoolean**](SingleWrapperBoolean.md)

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

# **update_ratings_cron**
> Wrapper update_ratings_cron(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.update_ratings_cron(version, s3_object)
        print("The response of AdminApi->update_ratings_cron:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_ratings_cron: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

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

# **update_referral_code**
> Wrapper update_referral_code(version)

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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')

    try:
        api_response = api_instance.update_referral_code(version)
        print("The response of AdminApi->update_referral_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_referral_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]

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

# **update_status**
> object update_status(version, user_status_update_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.user_status_update_request import UserStatusUpdateRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_status_update_request = dupr_backend.UserStatusUpdateRequest() # UserStatusUpdateRequest | 

    try:
        api_response = api_instance.update_status(version, user_status_update_request)
        print("The response of AdminApi->update_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_status_update_request** | [**UserStatusUpdateRequest**](UserStatusUpdateRequest.md)|  | 

### Return type

**object**

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile**
> SingleWrapperUserResponse update_user_profile(version, user_id, player_profile_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.player_profile_request import PlayerProfileRequest
from dupr_backend.models.single_wrapper_user_response import SingleWrapperUserResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_id = 56 # int | 
    player_profile_request = dupr_backend.PlayerProfileRequest() # PlayerProfileRequest | 

    try:
        api_response = api_instance.update_user_profile(version, user_id, player_profile_request)
        print("The response of AdminApi->update_user_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_user_profile: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_id** | **int**|  | 
 **player_profile_request** | [**PlayerProfileRequest**](PlayerProfileRequest.md)|  | 

### Return type

[**SingleWrapperUserResponse**](SingleWrapperUserResponse.md)

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

# **upload_dupr_performance_chart_data**
> Wrapper upload_dupr_performance_chart_data(version, s3_object)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | 

    try:
        api_response = api_instance.upload_dupr_performance_chart_data(version, s3_object)
        print("The response of AdminApi->upload_dupr_performance_chart_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->upload_dupr_performance_chart_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)|  | 

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

# **upsert_and_tag_shopify_customers**
> object upsert_and_tag_shopify_customers(document)

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
    api_instance = dupr_backend.AdminApi(api_client)
    document = None # bytearray | 

    try:
        api_response = api_instance.upsert_and_tag_shopify_customers(document)
        print("The response of AdminApi->upsert_and_tag_shopify_customers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->upsert_and_tag_shopify_customers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **bytearray**|  | 

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

# **user_lookup**
> SingleWrapperPageUserLookupResponse user_lookup(version, user_search_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_user_lookup_response import SingleWrapperPageUserLookupResponse
from dupr_backend.models.user_search_request import UserSearchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    user_search_request = dupr_backend.UserSearchRequest() # UserSearchRequest | 

    try:
        api_response = api_instance.user_lookup(version, user_search_request)
        print("The response of AdminApi->user_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->user_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **user_search_request** | [**UserSearchRequest**](UserSearchRequest.md)|  | 

### Return type

[**SingleWrapperPageUserLookupResponse**](SingleWrapperPageUserLookupResponse.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email**
> Wrapper verify_email(version, verify_email_request)

### Example

* Bearer (JWT) Authentication (bearerAuth):

```python
import dupr_backend
from dupr_backend.models.verify_email_request import VerifyEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    version = 'v1.0' # str |  (default to 'v1.0')
    verify_email_request = dupr_backend.VerifyEmailRequest() # VerifyEmailRequest | 

    try:
        api_response = api_instance.verify_email(version, verify_email_request)
        print("The response of AdminApi->verify_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->verify_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | [default to &#39;v1.0&#39;]
 **verify_email_request** | [**VerifyEmailRequest**](VerifyEmailRequest.md)|  | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

[bearerAuth](../README.md#bearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

