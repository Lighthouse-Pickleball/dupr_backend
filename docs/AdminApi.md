# dupr_backend.AdminApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_match_using_post**](AdminApi.md#activate_match_using_post) | **POST** /admin/{version}/panel/match/active | activateMatch
[**add_key_to_external_client_using_post**](AdminApi.md#add_key_to_external_client_using_post) | **POST** /admin/{version}/client/keys/add | addKeyToExternalClient
[**adjust_rating_using_put**](AdminApi.md#adjust_rating_using_put) | **PUT** /admin/rating/{version}/edit | adjustRating
[**admin_verified_match_history_using_get**](AdminApi.md#admin_verified_match_history_using_get) | **GET** /admin/match/{version}/history | adminVerifiedMatchHistory
[**batch_calculated_statistics_using_put**](AdminApi.md#batch_calculated_statistics_using_put) | **PUT** /admin/calculated/{version}/stats | batchCalculatedStatistics
[**batch_club_matches_using_post**](AdminApi.md#batch_club_matches_using_post) | **POST** /admin/{version}/club/{clubId}/match/batch | batchClubMatches
[**batch_manual_club_matches_using_post**](AdminApi.md#batch_manual_club_matches_using_post) | **POST** /admin/{version}/match/club-batch | batchManualClubMatches
[**batch_manual_matches_using_post**](AdminApi.md#batch_manual_matches_using_post) | **POST** /admin/{version}/match/batch | batchManualMatches
[**batch_player_rating_provisional_using_put**](AdminApi.md#batch_player_rating_provisional_using_put) | **PUT** /admin/{version}/ratings-provisional/batch | batchPlayerRatingProvisional
[**batch_player_rating_using_put**](AdminApi.md#batch_player_rating_using_put) | **PUT** /admin/{version}/rating/batch | batchPlayerRating
[**batch_set_reliability_scores_using_post**](AdminApi.md#batch_set_reliability_scores_using_post) | **POST** /admin/{version}/player/batch-reliability-score | batchSetReliabilityScores
[**block_admin_apis_using_put**](AdminApi.md#block_admin_apis_using_put) | **PUT** /admin/{version}/panel/block | blockAdminApis
[**bulk_delete_matches_using_put**](AdminApi.md#bulk_delete_matches_using_put) | **PUT** /admin/{version}/match/delete | bulkDeleteMatches
[**bulk_reliability_score_using_put**](AdminApi.md#bulk_reliability_score_using_put) | **PUT** /admin/{version}/player/bulk-reliability-score | bulkReliabilityScore
[**bulk_send_coppa_email_using_post**](AdminApi.md#bulk_send_coppa_email_using_post) | **POST** /admin/{version}/bulkcoppaemail | bulkSendCoppaEmail
[**bulk_send_wrapped_email_using_post**](AdminApi.md#bulk_send_wrapped_email_using_post) | **POST** /admin/{version}/bulkwrappedemail | bulkSendWrappedEmail
[**change_email_using_put**](AdminApi.md#change_email_using_put) | **PUT** /admin/{version}/panel/email/change | changeEmail
[**change_role_using_post**](AdminApi.md#change_role_using_post) | **POST** /admin/{version}/panel/role/change | changeRole
[**club_create_using_put**](AdminApi.md#club_create_using_put) | **PUT** /admin/{version}/clubs/create | clubCreate
[**create_banner_using_post**](AdminApi.md#create_banner_using_post) | **POST** /admin/{version}/panel/create/banner | createBanner
[**create_clubs_batch_using_put**](AdminApi.md#create_clubs_batch_using_put) | **PUT** /admin/{version}/clubs/create/batch | createClubsBatch
[**create_external_client_using_post**](AdminApi.md#create_external_client_using_post) | **POST** /admin/{version}/client | createExternalClient
[**decode_using_get**](AdminApi.md#decode_using_get) | **GET** /admin/decode | decode
[**delete_club_using_delete**](AdminApi.md#delete_club_using_delete) | **DELETE** /admin/{version}/club/{clubId} | deleteClub
[**delete_match_using_post**](AdminApi.md#delete_match_using_post) | **POST** /admin/{version}/panel/match/delete | deleteMatch
[**delete_user_using_put**](AdminApi.md#delete_user_using_put) | **PUT** /admin/{version}/panel/user/delete | deleteUser
[**delete_wix_user_using_delete**](AdminApi.md#delete_wix_user_using_delete) | **DELETE** /admin/wix/{version}/{version}/delete | deleteWixUser
[**dupr_id_using_get**](AdminApi.md#dupr_id_using_get) | **GET** /admin/{version}/panel/user | duprId
[**edit_club_staff_using_post**](AdminApi.md#edit_club_staff_using_post) | **POST** /admin/club/staff/{version}/edit | editClubStaff
[**encode_using_get**](AdminApi.md#encode_using_get) | **GET** /admin/encode | encode
[**export_matches_missing_team_player_using_get**](AdminApi.md#export_matches_missing_team_player_using_get) | **GET** /admin/{version}/team-players/missing/export | exportMatchesMissingTeamPlayer
[**export_users_via_mail_using_post**](AdminApi.md#export_users_via_mail_using_post) | **POST** /admin/{version}/panel/user/export | exportUsersViaMail
[**find_duplicated_account_for_players_using_post**](AdminApi.md#find_duplicated_account_for_players_using_post) | **POST** /admin/{version}/duplicated | findDuplicatedAccountForPlayers
[**get_active_banner_using_get**](AdminApi.md#get_active_banner_using_get) | **GET** /admin/{version}/panel/get/banner | getActiveBanner
[**get_all_banner_using_get**](AdminApi.md#get_all_banner_using_get) | **GET** /admin/{version}/panel/get/banners | getAllBanner
[**get_all_roles_using_get**](AdminApi.md#get_all_roles_using_get) | **GET** /admin/{version}/roles | getAllRoles
[**get_club_restrictions_using_post**](AdminApi.md#get_club_restrictions_using_post) | **POST** /admin/{version}/clubs/restrictions | getClubRestrictions
[**get_club_settings_using_post**](AdminApi.md#get_club_settings_using_post) | **POST** /admin/{version}/clubs/settings | getClubSettings
[**get_external_client_permissions_using_post**](AdminApi.md#get_external_client_permissions_using_post) | **POST** /admin/{version}/client/keys | getExternalClientPermissions
[**get_match_using_get**](AdminApi.md#get_match_using_get) | **GET** /admin/{version}/panel/match/{id} | getMatch
[**get_user_bracket_using_post**](AdminApi.md#get_user_bracket_using_post) | **POST** /admin/{version}/panel/brackets/user/all | getUserBracket
[**get_user_profile_using_get**](AdminApi.md#get_user_profile_using_get) | **GET** /admin/{version}/panel/user/profile | getUserProfile
[**index_club_members_using_post**](AdminApi.md#index_club_members_using_post) | **POST** /admin/{version}/members/index | indexClubMembers
[**index_clubs_using_put**](AdminApi.md#index_clubs_using_put) | **PUT** /admin/{version}/clubs/index | indexClubs
[**index_player_using_patch**](AdminApi.md#index_player_using_patch) | **PATCH** /admin/{version}/index/{id} | indexPlayer
[**index_players_using_patch**](AdminApi.md#index_players_using_patch) | **PATCH** /admin/{version}/index | indexPlayers
[**match_codes_export_using_get**](AdminApi.md#match_codes_export_using_get) | **GET** /admin/{version}/match/export/codes | matchCodesExport
[**match_reassign_batch_using_post**](AdminApi.md#match_reassign_batch_using_post) | **POST** /admin/{version}/match/reassign/batch | matchReassignBatch
[**match_reassign_using_post**](AdminApi.md#match_reassign_using_post) | **POST** /admin/{version}/match/reassign | matchReassign
[**matches_export_using_get**](AdminApi.md#matches_export_using_get) | **GET** /admin/{version}/match/export | matchesExport
[**merge_users_batch_using_post**](AdminApi.md#merge_users_batch_using_post) | **POST** /admin/{version}/panel/merge/batch | mergeUsersBatch
[**merge_users_using_post**](AdminApi.md#merge_users_using_post) | **POST** /admin/{version}/panel/merge | mergeUsers
[**obfuscate_match_id_using_get**](AdminApi.md#obfuscate_match_id_using_get) | **GET** /admin/obfuscate-matchid | obfuscateMatchId
[**obfuscate_using_get**](AdminApi.md#obfuscate_using_get) | **GET** /admin/obfuscate | obfuscate
[**populate_unknown_player_pre_ratings_using_post**](AdminApi.md#populate_unknown_player_pre_ratings_using_post) | **POST** /admin/{version}/unknown/players/populate-pre-rating | populateUnknownPlayerPreRatings
[**re_create_es_index_using_post**](AdminApi.md#re_create_es_index_using_post) | **POST** /admin/{version}/panel/es/{id}/mapping | reCreateESIndex
[**recalculate_match_elo_ratings_bulk_using_post**](AdminApi.md#recalculate_match_elo_ratings_bulk_using_post) | **POST** /admin/{version}/match/elo-rating-recalculation | recalculateMatchELORatingsBulk
[**recalculate_pre_match_ratings_using_post**](AdminApi.md#recalculate_pre_match_ratings_using_post) | **POST** /admin/{version}/match/pre-rating-impact | recalculatePreMatchRatings
[**recalculate_pre_match_ratings_using_post1**](AdminApi.md#recalculate_pre_match_ratings_using_post1) | **POST** /admin/{version}/match/bulk-pre-rating-impact | recalculatePreMatchRatings
[**remove_all_club_restrictions_using_delete**](AdminApi.md#remove_all_club_restrictions_using_delete) | **DELETE** /admin/{version}/clubs/restrictions/all | removeAllClubRestrictions
[**remove_club_restrictions_using_delete**](AdminApi.md#remove_club_restrictions_using_delete) | **DELETE** /admin/{version}/clubs/restrictions | removeClubRestrictions
[**reset_client_secret_using_get**](AdminApi.md#reset_client_secret_using_get) | **GET** /admin/client/{version}/secret/reset | resetClientSecret
[**restrict_using_post**](AdminApi.md#restrict_using_post) | **POST** /admin/{version}/panel/user/{id}/restrict | restrict
[**save_topic_using_post**](AdminApi.md#save_topic_using_post) | **POST** /admin/{version}/topic | saveTopic
[**save_verified_match_using_put**](AdminApi.md#save_verified_match_using_put) | **PUT** /admin/match/{version}/save | saveVerifiedMatch
[**set_club_restrictions_using_put**](AdminApi.md#set_club_restrictions_using_put) | **PUT** /admin/{version}/clubs/restrictions | setClubRestrictions
[**set_club_settings_using_put**](AdminApi.md#set_club_settings_using_put) | **PUT** /admin/{version}/clubs/settings | setClubSettings
[**signup_batch_using_put**](AdminApi.md#signup_batch_using_put) | **PUT** /admin/{version}/panel/user/signup/batch | signupBatch
[**signup_using_put**](AdminApi.md#signup_using_put) | **PUT** /admin/{version}/panel/user/signup | signup
[**trigger_missing_elo_rating_for_players_using_post**](AdminApi.md#trigger_missing_elo_rating_for_players_using_post) | **POST** /admin/{version}/player-rating-history | triggerMissingEloRatingForPlayers
[**unclaim_user_using_put**](AdminApi.md#unclaim_user_using_put) | **PUT** /admin/{version}/panel/user/unclaim | unclaimUser
[**unobfuscate_match_code_using_get**](AdminApi.md#unobfuscate_match_code_using_get) | **GET** /admin/unobfuscate-matchcode | unobfuscateMatchCode
[**unobfuscate_using_get**](AdminApi.md#unobfuscate_using_get) | **GET** /admin/unobfuscate | unobfuscate
[**update_banner_using_put**](AdminApi.md#update_banner_using_put) | **PUT** /admin/{version}/panel/update/banner | updateBanner
[**update_club_currency_using_put**](AdminApi.md#update_club_currency_using_put) | **PUT** /admin/{version}/club/{clubId}/currency | updateClubCurrency
[**update_club_revenue_model_using_put**](AdminApi.md#update_club_revenue_model_using_put) | **PUT** /admin/{version}/club/{clubId}/revenue | updateClubRevenueModel
[**update_currency_rates_using_get**](AdminApi.md#update_currency_rates_using_get) | **GET** /admin/club/currency/{version}/update | updateCurrencyRates
[**update_es_index_using_put**](AdminApi.md#update_es_index_using_put) | **PUT** /admin/{version}/panel/es/{id}/mapping | updateESIndex
[**update_external_client_permissions_using_post**](AdminApi.md#update_external_client_permissions_using_post) | **POST** /admin/{version}/client/permissions | updateExternalClientPermissions
[**update_external_id_cron_using_put**](AdminApi.md#update_external_id_cron_using_put) | **PUT** /admin/{version}/external-id/bulk | updateExternalIdCron
[**update_lucra_connection_using_put**](AdminApi.md#update_lucra_connection_using_put) | **PUT** /admin/{version}/panel/user/{id}/lucra-connect | updateLucraConnection
[**update_match_using_put**](AdminApi.md#update_match_using_put) | **PUT** /admin/{version}/panel/match/{version}/update | updateMatch
[**update_payment_status_using_post**](AdminApi.md#update_payment_status_using_post) | **POST** /admin/{version}/panel/brackets/registration/update | updatePaymentStatus
[**update_player_rating_using_put**](AdminApi.md#update_player_rating_using_put) | **PUT** /admin/{version}/rating/{id} | updatePlayerRating
[**update_player_statistics_using_put**](AdminApi.md#update_player_statistics_using_put) | **PUT** /admin/calculated/{version}/stats/update | updatePlayerStatistics
[**update_ratings_cron_using_put**](AdminApi.md#update_ratings_cron_using_put) | **PUT** /admin/{version}/ratings/bulk | updateRatingsCron
[**update_referral_code_using_patch**](AdminApi.md#update_referral_code_using_patch) | **PATCH** /admin/referral-code/{version}/update | updateReferralCode
[**update_status_using_post**](AdminApi.md#update_status_using_post) | **POST** /admin/{version}/panel/user/status | updateStatus
[**update_user_profile_using_put**](AdminApi.md#update_user_profile_using_put) | **PUT** /admin/{version}/panel/user/profile | updateUserProfile
[**upload_dupr_performance_chart_data_using_put**](AdminApi.md#upload_dupr_performance_chart_data_using_put) | **PUT** /admin/{version}/panel/performance | uploadDuprPerformanceChartData
[**user_lookup_using_post**](AdminApi.md#user_lookup_using_post) | **POST** /admin/{version}/panel/user/lookup | userLookup
[**verify_email_using_post**](AdminApi.md#verify_email_using_post) | **POST** /admin/{version}/panel/email/verify | verifyEmail


# **activate_match_using_post**
> Wrapper activate_match_using_post(authorization, version, request)

activateMatch

### Example


```python
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request

    try:
        # activateMatch
        api_response = api_instance.activate_match_using_post(authorization, version, request)
        print("The response of AdminApi->activate_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->activate_match_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 

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

# **add_key_to_external_client_using_post**
> object add_key_to_external_client_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)

addKeyToExternalClient

### Example


```python
import dupr_backend
from dupr_backend.models.add_client_key_request import AddClientKeyRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AddClientKeyRequest() # AddClientKeyRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # addKeyToExternalClient
        api_response = api_instance.add_key_to_external_client_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AdminApi->add_key_to_external_client_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->add_key_to_external_client_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AddClientKeyRequest**](AddClientKeyRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

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

# **adjust_rating_using_put**
> Wrapper adjust_rating_using_put(authorization, version, request)

adjustRating

### Example


```python
import dupr_backend
from dupr_backend.models.adjust_rating_request import AdjustRatingRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.AdjustRatingRequest() # AdjustRatingRequest | request

    try:
        # adjustRating
        api_response = api_instance.adjust_rating_using_put(authorization, version, request)
        print("The response of AdminApi->adjust_rating_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->adjust_rating_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**AdjustRatingRequest**](AdjustRatingRequest.md)| request | 

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

# **admin_verified_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse admin_verified_match_history_using_get(authorization, limit, offset, version)

adminVerifiedMatchHistory

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # adminVerifiedMatchHistory
        api_response = api_instance.admin_verified_match_history_using_get(authorization, limit, offset, version)
        print("The response of AdminApi->admin_verified_match_history_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_verified_match_history_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **batch_calculated_statistics_using_put**
> batch_calculated_statistics_using_put(authorization, version, s3_object)

batchCalculatedStatistics

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | s3Object

    try:
        # batchCalculatedStatistics
        api_instance.batch_calculated_statistics_using_put(authorization, version, s3_object)
    except Exception as e:
        print("Exception when calling AdminApi->batch_calculated_statistics_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)| s3Object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_club_matches_using_post**
> SingleWrapperOfUnit batch_club_matches_using_post(authorization, club_id, version, request)

batchClubMatches

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.S3Object() # S3Object | request

    try:
        # batchClubMatches
        api_response = api_instance.batch_club_matches_using_post(authorization, club_id, version, request)
        print("The response of AdminApi->batch_club_matches_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_club_matches_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**S3Object**](S3Object.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **batch_manual_club_matches_using_post**
> SingleWrapperOfUnit batch_manual_club_matches_using_post(authorization, version, request)

batchManualClubMatches

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.S3Object() # S3Object | request

    try:
        # batchManualClubMatches
        api_response = api_instance.batch_manual_club_matches_using_post(authorization, version, request)
        print("The response of AdminApi->batch_manual_club_matches_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_manual_club_matches_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**S3Object**](S3Object.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **batch_manual_matches_using_post**
> SingleWrapperOfUnit batch_manual_matches_using_post(authorization, version, request)

batchManualMatches

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.S3Object() # S3Object | request

    try:
        # batchManualMatches
        api_response = api_instance.batch_manual_matches_using_post(authorization, version, request)
        print("The response of AdminApi->batch_manual_matches_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_manual_matches_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**S3Object**](S3Object.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **batch_player_rating_provisional_using_put**
> SingleWrapperOfUnit batch_player_rating_provisional_using_put(authorization, version, request)

batchPlayerRatingProvisional

### Example


```python
import dupr_backend
from dupr_backend.models.batch_player_rating_provisional_request import BatchPlayerRatingProvisionalRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BatchPlayerRatingProvisionalRequest() # BatchPlayerRatingProvisionalRequest | request

    try:
        # batchPlayerRatingProvisional
        api_response = api_instance.batch_player_rating_provisional_using_put(authorization, version, request)
        print("The response of AdminApi->batch_player_rating_provisional_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_player_rating_provisional_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BatchPlayerRatingProvisionalRequest**](BatchPlayerRatingProvisionalRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_player_rating_using_put**
> SingleWrapperOfUnit batch_player_rating_using_put(authorization, version, request)

batchPlayerRating

### Example


```python
import dupr_backend
from dupr_backend.models.batch_player_rating_request import BatchPlayerRatingRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BatchPlayerRatingRequest() # BatchPlayerRatingRequest | request

    try:
        # batchPlayerRating
        api_response = api_instance.batch_player_rating_using_put(authorization, version, request)
        print("The response of AdminApi->batch_player_rating_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->batch_player_rating_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BatchPlayerRatingRequest**](BatchPlayerRatingRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_set_reliability_scores_using_post**
> batch_set_reliability_scores_using_post(authorization, version, s3_object)

batchSetReliabilityScores

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    s3_object = dupr_backend.S3Object() # S3Object | s3Object

    try:
        # batchSetReliabilityScores
        api_instance.batch_set_reliability_scores_using_post(authorization, version, s3_object)
    except Exception as e:
        print("Exception when calling AdminApi->batch_set_reliability_scores_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **s3_object** | [**S3Object**](S3Object.md)| s3Object | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_admin_apis_using_put**
> bool block_admin_apis_using_put(authorization, flag, version)

blockAdminApis

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    flag = True # bool | flag
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # blockAdminApis
        api_response = api_instance.block_admin_apis_using_put(authorization, flag, version)
        print("The response of AdminApi->block_admin_apis_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->block_admin_apis_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **flag** | **bool**| flag | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

**bool**

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

# **bulk_delete_matches_using_put**
> Wrapper bulk_delete_matches_using_put(authorization, type, version, document=document)

bulkDeleteMatches

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    type = 'type_example' # str | type
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # bulkDeleteMatches
        api_response = api_instance.bulk_delete_matches_using_put(authorization, type, version, document=document)
        print("The response of AdminApi->bulk_delete_matches_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_delete_matches_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **type** | **str**| type | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

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

# **bulk_reliability_score_using_put**
> Wrapper bulk_reliability_score_using_put(authorization, version, request=request)

bulkReliabilityScore

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = None # bytearray |  (optional)

    try:
        # bulkReliabilityScore
        api_response = api_instance.bulk_reliability_score_using_put(authorization, version, request=request)
        print("The response of AdminApi->bulk_reliability_score_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_reliability_score_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **bytearray**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

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

# **bulk_send_coppa_email_using_post**
> object bulk_send_coppa_email_using_post(authorization, version, request)

bulkSendCoppaEmail

### Example


```python
import dupr_backend
from dupr_backend.models.bulk_coppa_email_request import BulkCoppaEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | request

    try:
        # bulkSendCoppaEmail
        api_response = api_instance.bulk_send_coppa_email_using_post(authorization, version, request)
        print("The response of AdminApi->bulk_send_coppa_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_send_coppa_email_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)| request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_send_wrapped_email_using_post**
> object bulk_send_wrapped_email_using_post(authorization, version, request)

bulkSendWrappedEmail

### Example


```python
import dupr_backend
from dupr_backend.models.bulk_coppa_email_request import BulkCoppaEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | request

    try:
        # bulkSendWrappedEmail
        api_response = api_instance.bulk_send_wrapped_email_using_post(authorization, version, request)
        print("The response of AdminApi->bulk_send_wrapped_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->bulk_send_wrapped_email_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)| request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_email_using_put**
> Wrapper change_email_using_put(authorization, version, request)

changeEmail

### Example


```python
import dupr_backend
from dupr_backend.models.change_email_admin_request import ChangeEmailAdminRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ChangeEmailAdminRequest() # ChangeEmailAdminRequest | request

    try:
        # changeEmail
        api_response = api_instance.change_email_using_put(authorization, version, request)
        print("The response of AdminApi->change_email_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->change_email_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ChangeEmailAdminRequest**](ChangeEmailAdminRequest.md)| request | 

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

# **change_role_using_post**
> Wrapper change_role_using_post(authorization, version, request)

changeRole

### Example


```python
import dupr_backend
from dupr_backend.models.change_role_request import ChangeRoleRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ChangeRoleRequest() # ChangeRoleRequest | request

    try:
        # changeRole
        api_response = api_instance.change_role_using_post(authorization, version, request)
        print("The response of AdminApi->change_role_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->change_role_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ChangeRoleRequest**](ChangeRoleRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_create_using_put**
> Wrapper club_create_using_put(authorization, version, request)

clubCreate

### Example


```python
import dupr_backend
from dupr_backend.models.create_clubs_request import CreateClubsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.CreateClubsRequest() # CreateClubsRequest | request

    try:
        # clubCreate
        api_response = api_instance.club_create_using_put(authorization, version, request)
        print("The response of AdminApi->club_create_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->club_create_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**CreateClubsRequest**](CreateClubsRequest.md)| request | 

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

# **create_banner_using_post**
> SingleWrapperOfUnit create_banner_using_post(authorization, version, create_banner_request)

createBanner

### Example


```python
import dupr_backend
from dupr_backend.models.create_banner_request import CreateBannerRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    create_banner_request = dupr_backend.CreateBannerRequest() # CreateBannerRequest | createBannerRequest

    try:
        # createBanner
        api_response = api_instance.create_banner_using_post(authorization, version, create_banner_request)
        print("The response of AdminApi->create_banner_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_banner_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **create_banner_request** | [**CreateBannerRequest**](CreateBannerRequest.md)| createBannerRequest | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clubs_batch_using_put**
> SingleWrapperOfstring create_clubs_batch_using_put(authorization, version, document=document)

createClubsBatch

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # createClubsBatch
        api_response = api_instance.create_clubs_batch_using_put(authorization, version, document=document)
        print("The response of AdminApi->create_clubs_batch_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_clubs_batch_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

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

# **create_external_client_using_post**
> SingleWrapperOfCreateClientResponse create_external_client_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)

createExternalClient

### Example


```python
import dupr_backend
from dupr_backend.models.create_client_request import CreateClientRequest
from dupr_backend.models.single_wrapper_of_create_client_response import SingleWrapperOfCreateClientResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.CreateClientRequest() # CreateClientRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # createExternalClient
        api_response = api_instance.create_external_client_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AdminApi->create_external_client_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->create_external_client_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**CreateClientRequest**](CreateClientRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfCreateClientResponse**](SingleWrapperOfCreateClientResponse.md)

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

# **decode_using_get**
> object decode_using_get(authorization, id=id, ids=ids)

decode

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id (optional)
    ids = 'ids_example' # str | ids (optional)

    try:
        # decode
        api_response = api_instance.decode_using_get(authorization, id=id, ids=ids)
        print("The response of AdminApi->decode_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->decode_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | [optional] 
 **ids** | **str**| ids | [optional] 

### Return type

**object**

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

# **delete_club_using_delete**
> Wrapper delete_club_using_delete(authorization, club_id, version)

deleteClub

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteClub
        api_response = api_instance.delete_club_using_delete(authorization, club_id, version)
        print("The response of AdminApi->delete_club_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_club_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
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

# **delete_match_using_post**
> Wrapper delete_match_using_post(authorization, version, request)

deleteMatch

### Example


```python
import dupr_backend
from dupr_backend.models.delete_match_request import DeleteMatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request

    try:
        # deleteMatch
        api_response = api_instance.delete_match_using_post(authorization, version, request)
        print("The response of AdminApi->delete_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_match_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 

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

# **delete_user_using_put**
> Wrapper delete_user_using_put(authorization, version, input=input, type=type)

deleteUser

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    input = 'input_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # deleteUser
        api_response = api_instance.delete_user_using_put(authorization, version, input=input, type=type)
        print("The response of AdminApi->delete_user_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_user_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **input** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

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

# **delete_wix_user_using_delete**
> Wrapper delete_wix_user_using_delete(authorization, user_id, version)

deleteWixUser

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    user_id = 56 # int | userId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteWixUser
        api_response = api_instance.delete_wix_user_using_delete(authorization, user_id, version)
        print("The response of AdminApi->delete_wix_user_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->delete_wix_user_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **user_id** | **int**| userId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **dupr_id_using_get**
> SingleWrapperOfAdminUserProfile dupr_id_using_get(authorization, version, dupr_id=dupr_id, external_id=external_id, user_id=user_id)

duprId

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_admin_user_profile import SingleWrapperOfAdminUserProfile
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    dupr_id = 'dupr_id_example' # str | duprId (optional)
    external_id = 'external_id_example' # str | externalId (optional)
    user_id = 56 # int | userId (optional)

    try:
        # duprId
        api_response = api_instance.dupr_id_using_get(authorization, version, dupr_id=dupr_id, external_id=external_id, user_id=user_id)
        print("The response of AdminApi->dupr_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->dupr_id_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **dupr_id** | **str**| duprId | [optional] 
 **external_id** | **str**| externalId | [optional] 
 **user_id** | **int**| userId | [optional] 

### Return type

[**SingleWrapperOfAdminUserProfile**](SingleWrapperOfAdminUserProfile.md)

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

# **edit_club_staff_using_post**
> Wrapper edit_club_staff_using_post(authorization, version, edit_club_staff_request)

editClubStaff

### Example


```python
import dupr_backend
from dupr_backend.models.edit_club_staff_request import EditClubStaffRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    edit_club_staff_request = dupr_backend.EditClubStaffRequest() # EditClubStaffRequest | editClubStaffRequest

    try:
        # editClubStaff
        api_response = api_instance.edit_club_staff_using_post(authorization, version, edit_club_staff_request)
        print("The response of AdminApi->edit_club_staff_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->edit_club_staff_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **edit_club_staff_request** | [**EditClubStaffRequest**](EditClubStaffRequest.md)| editClubStaffRequest | 

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

# **encode_using_get**
> object encode_using_get(authorization, id=id, ids=ids)

encode

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id (optional)
    ids = 'ids_example' # str | ids (optional)

    try:
        # encode
        api_response = api_instance.encode_using_get(authorization, id=id, ids=ids)
        print("The response of AdminApi->encode_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->encode_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | [optional] 
 **ids** | **str**| ids | [optional] 

### Return type

**object**

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

# **export_matches_missing_team_player_using_get**
> Wrapper export_matches_missing_team_player_using_get(authorization, version)

exportMatchesMissingTeamPlayer

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # exportMatchesMissingTeamPlayer
        api_response = api_instance.export_matches_missing_team_player_using_get(authorization, version)
        print("The response of AdminApi->export_matches_missing_team_player_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->export_matches_missing_team_player_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **export_users_via_mail_using_post**
> Wrapper export_users_via_mail_using_post(authorization, version)

exportUsersViaMail

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # exportUsersViaMail
        api_response = api_instance.export_users_via_mail_using_post(authorization, version)
        print("The response of AdminApi->export_users_via_mail_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->export_users_via_mail_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **find_duplicated_account_for_players_using_post**
> ArrayWrapperOfDuplicatedAccountResponse find_duplicated_account_for_players_using_post(authorization, version)

findDuplicatedAccountForPlayers

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_duplicated_account_response import ArrayWrapperOfDuplicatedAccountResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # findDuplicatedAccountForPlayers
        api_response = api_instance.find_duplicated_account_for_players_using_post(authorization, version)
        print("The response of AdminApi->find_duplicated_account_for_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->find_duplicated_account_for_players_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfDuplicatedAccountResponse**](ArrayWrapperOfDuplicatedAccountResponse.md)

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

# **get_active_banner_using_get**
> ArrayWrapperOfInformativeBannerResponce get_active_banner_using_get(authorization, version)

getActiveBanner

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_informative_banner_responce import ArrayWrapperOfInformativeBannerResponce
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getActiveBanner
        api_response = api_instance.get_active_banner_using_get(authorization, version)
        print("The response of AdminApi->get_active_banner_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_active_banner_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfInformativeBannerResponce**](ArrayWrapperOfInformativeBannerResponce.md)

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

# **get_all_banner_using_get**
> ArrayWrapperOfInformativeBannerResponce get_all_banner_using_get(authorization, version)

getAllBanner

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_of_informative_banner_responce import ArrayWrapperOfInformativeBannerResponce
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllBanner
        api_response = api_instance.get_all_banner_using_get(authorization, version)
        print("The response of AdminApi->get_all_banner_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_all_banner_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfInformativeBannerResponce**](ArrayWrapperOfInformativeBannerResponce.md)

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

# **get_all_roles_using_get**
> ArrayWrapperOfRoleResponse get_all_roles_using_get(authorization, version)

getAllRoles

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllRoles
        api_response = api_instance.get_all_roles_using_get(authorization, version)
        print("The response of AdminApi->get_all_roles_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_all_roles_using_get: %s\n" % e)
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

# **get_club_restrictions_using_post**
> object get_club_restrictions_using_post(authorization, version, request)

getClubRestrictions

### Example


```python
import dupr_backend
from dupr_backend.models.get_club_restrictions_request import GetClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.GetClubRestrictionsRequest() # GetClubRestrictionsRequest | request

    try:
        # getClubRestrictions
        api_response = api_instance.get_club_restrictions_using_post(authorization, version, request)
        print("The response of AdminApi->get_club_restrictions_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_club_restrictions_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**GetClubRestrictionsRequest**](GetClubRestrictionsRequest.md)| request | 

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

# **get_club_settings_using_post**
> object get_club_settings_using_post(authorization, version, request)

getClubSettings

### Example


```python
import dupr_backend
from dupr_backend.models.get_club_settings_request import GetClubSettingsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.GetClubSettingsRequest() # GetClubSettingsRequest | request

    try:
        # getClubSettings
        api_response = api_instance.get_club_settings_using_post(authorization, version, request)
        print("The response of AdminApi->get_club_settings_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_club_settings_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**GetClubSettingsRequest**](GetClubSettingsRequest.md)| request | 

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

# **get_external_client_permissions_using_post**
> object get_external_client_permissions_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)

getExternalClientPermissions

### Example


```python
import dupr_backend
from dupr_backend.models.get_client_permissions_request import GetClientPermissionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.GetClientPermissionsRequest() # GetClientPermissionsRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # getExternalClientPermissions
        api_response = api_instance.get_external_client_permissions_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AdminApi->get_external_client_permissions_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_external_client_permissions_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**GetClientPermissionsRequest**](GetClientPermissionsRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

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

# **get_match_using_get**
> SingleWrapperOfMatchResponse get_match_using_get(authorization, id, version)

getMatch

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getMatch
        api_response = api_instance.get_match_using_get(authorization, id, version)
        print("The response of AdminApi->get_match_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_match_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
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

# **get_user_bracket_using_post**
> SingleWrapperOfPageOfBracketResponse get_user_bracket_using_post(authorization, version, user_bracket_admin_request)

getUserBracket

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_bracket_response import SingleWrapperOfPageOfBracketResponse
from dupr_backend.models.user_bracket_admin_request import UserBracketAdminRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    user_bracket_admin_request = dupr_backend.UserBracketAdminRequest() # UserBracketAdminRequest | userBracketAdminRequest

    try:
        # getUserBracket
        api_response = api_instance.get_user_bracket_using_post(authorization, version, user_bracket_admin_request)
        print("The response of AdminApi->get_user_bracket_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_bracket_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **user_bracket_admin_request** | [**UserBracketAdminRequest**](UserBracketAdminRequest.md)| userBracketAdminRequest | 

### Return type

[**SingleWrapperOfPageOfBracketResponse**](SingleWrapperOfPageOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile_using_get**
> SingleWrapperOfUserResponse get_user_profile_using_get(authorization, user_id, version)

getUserProfile

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_user_response import SingleWrapperOfUserResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    user_id = 56 # int | userId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getUserProfile
        api_response = api_instance.get_user_profile_using_get(authorization, user_id, version)
        print("The response of AdminApi->get_user_profile_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_user_profile_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **user_id** | **int**| userId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

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

# **index_club_members_using_post**
> Wrapper index_club_members_using_post(authorization, version)

indexClubMembers

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexClubMembers
        api_response = api_instance.index_club_members_using_post(authorization, version)
        print("The response of AdminApi->index_club_members_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_club_members_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **index_clubs_using_put**
> Wrapper index_clubs_using_put(authorization, version)

indexClubs

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexClubs
        api_response = api_instance.index_clubs_using_put(authorization, version)
        print("The response of AdminApi->index_clubs_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_clubs_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **index_player_using_patch**
> object index_player_using_patch(authorization, id, version)

indexPlayer

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexPlayer
        api_response = api_instance.index_player_using_patch(authorization, id, version)
        print("The response of AdminApi->index_player_using_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_player_using_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_players_using_patch**
> Wrapper index_players_using_patch(authorization, version)

indexPlayers

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # indexPlayers
        api_response = api_instance.index_players_using_patch(authorization, version)
        print("The response of AdminApi->index_players_using_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->index_players_using_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_codes_export_using_get**
> Wrapper match_codes_export_using_get(authorization, version, sources=sources)

matchCodesExport

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    sources = ['sources_example'] # List[str] | sources (optional)

    try:
        # matchCodesExport
        api_response = api_instance.match_codes_export_using_get(authorization, version, sources=sources)
        print("The response of AdminApi->match_codes_export_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_codes_export_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **sources** | [**List[str]**](str.md)| sources | [optional] 

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

# **match_reassign_batch_using_post**
> SingleWrapperOfstring match_reassign_batch_using_post(authorization, version, notify=notify, document=document)

matchReassignBatch

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    notify = True # bool | notify (optional)
    document = None # bytearray |  (optional)

    try:
        # matchReassignBatch
        api_response = api_instance.match_reassign_batch_using_post(authorization, version, notify=notify, document=document)
        print("The response of AdminApi->match_reassign_batch_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_reassign_batch_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **notify** | **bool**| notify | [optional] 
 **document** | **bytearray**|  | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_reassign_using_post**
> SingleWrapperOfUnit match_reassign_using_post(authorization, version, matches_reassign_request)

matchReassign

### Example


```python
import dupr_backend
from dupr_backend.models.matches_reassign_request import MatchesReassignRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    matches_reassign_request = dupr_backend.MatchesReassignRequest() # MatchesReassignRequest | matchesReassignRequest

    try:
        # matchReassign
        api_response = api_instance.match_reassign_using_post(authorization, version, matches_reassign_request)
        print("The response of AdminApi->match_reassign_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->match_reassign_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **matches_reassign_request** | [**MatchesReassignRequest**](MatchesReassignRequest.md)| matchesReassignRequest | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_export_using_get**
> Wrapper matches_export_using_get(all, authorization, version, sources=sources)

matchesExport

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
    api_instance = dupr_backend.AdminApi(api_client)
    all = True # bool | all
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    sources = ['sources_example'] # List[str] | sources (optional)

    try:
        # matchesExport
        api_response = api_instance.matches_export_using_get(all, authorization, version, sources=sources)
        print("The response of AdminApi->matches_export_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->matches_export_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| all | 
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **sources** | [**List[str]**](str.md)| sources | [optional] 

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

# **merge_users_batch_using_post**
> SingleWrapperOfstring merge_users_batch_using_post(authorization, version, document=document)

mergeUsersBatch

### Example


```python
import dupr_backend
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # mergeUsersBatch
        api_response = api_instance.merge_users_batch_using_post(authorization, version, document=document)
        print("The response of AdminApi->merge_users_batch_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->merge_users_batch_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

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

# **merge_users_using_post**
> SingleWrapperOfMergeUsersResponse merge_users_using_post(authorization, version, merge_users_request)

mergeUsers

### Example


```python
import dupr_backend
from dupr_backend.models.merge_users_request import MergeUsersRequest
from dupr_backend.models.single_wrapper_of_merge_users_response import SingleWrapperOfMergeUsersResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    merge_users_request = dupr_backend.MergeUsersRequest() # MergeUsersRequest | mergeUsersRequest

    try:
        # mergeUsers
        api_response = api_instance.merge_users_using_post(authorization, version, merge_users_request)
        print("The response of AdminApi->merge_users_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->merge_users_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **merge_users_request** | [**MergeUsersRequest**](MergeUsersRequest.md)| mergeUsersRequest | 

### Return type

[**SingleWrapperOfMergeUsersResponse**](SingleWrapperOfMergeUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obfuscate_match_id_using_get**
> str obfuscate_match_id_using_get(authorization, to_type, ids=ids)

obfuscateMatchId

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    to_type = 'to_type_example' # str | toType
    ids = 'ids_example' # str | ids (optional)

    try:
        # obfuscateMatchId
        api_response = api_instance.obfuscate_match_id_using_get(authorization, to_type, ids=ids)
        print("The response of AdminApi->obfuscate_match_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->obfuscate_match_id_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **to_type** | **str**| toType | 
 **ids** | **str**| ids | [optional] 

### Return type

**str**

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

# **obfuscate_using_get**
> object obfuscate_using_get(authorization, type, id=id, ids=ids)

obfuscate

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    type = 'type_example' # str | type
    id = 56 # int | id (optional)
    ids = 'ids_example' # str | ids (optional)

    try:
        # obfuscate
        api_response = api_instance.obfuscate_using_get(authorization, type, id=id, ids=ids)
        print("The response of AdminApi->obfuscate_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->obfuscate_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **type** | **str**| type | 
 **id** | **int**| id | [optional] 
 **ids** | **str**| ids | [optional] 

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

# **populate_unknown_player_pre_ratings_using_post**
> Wrapper populate_unknown_player_pre_ratings_using_post(authorization)

populateUnknownPlayerPreRatings

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')

    try:
        # populateUnknownPlayerPreRatings
        api_response = api_instance.populate_unknown_player_pre_ratings_using_post(authorization)
        print("The response of AdminApi->populate_unknown_player_pre_ratings_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->populate_unknown_player_pre_ratings_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **re_create_es_index_using_post**
> Wrapper re_create_es_index_using_post(authorization, id, version)

reCreateESIndex

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # reCreateESIndex
        api_response = api_instance.re_create_es_index_using_post(authorization, id, version)
        print("The response of AdminApi->re_create_es_index_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->re_create_es_index_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **recalculate_match_elo_ratings_bulk_using_post**
> Wrapper recalculate_match_elo_ratings_bulk_using_post(authorization, type, version, document=document)

recalculateMatchELORatingsBulk

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    type = 'type_example' # str | type
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # recalculateMatchELORatingsBulk
        api_response = api_instance.recalculate_match_elo_ratings_bulk_using_post(authorization, type, version, document=document)
        print("The response of AdminApi->recalculate_match_elo_ratings_bulk_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_match_elo_ratings_bulk_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **type** | **str**| type | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings_using_post**
> Wrapper recalculate_pre_match_ratings_using_post(authorization, version, request)

recalculatePreMatchRatings

### Example


```python
import dupr_backend
from dupr_backend.models.calculate_matches_range import CalculateMatchesRange
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.CalculateMatchesRange() # CalculateMatchesRange | request

    try:
        # recalculatePreMatchRatings
        api_response = api_instance.recalculate_pre_match_ratings_using_post(authorization, version, request)
        print("The response of AdminApi->recalculate_pre_match_ratings_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_pre_match_ratings_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**CalculateMatchesRange**](CalculateMatchesRange.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings_using_post1**
> Wrapper recalculate_pre_match_ratings_using_post1(authorization, type, version, document=document)

recalculatePreMatchRatings

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    type = 'type_example' # str | type
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # recalculatePreMatchRatings
        api_response = api_instance.recalculate_pre_match_ratings_using_post1(authorization, type, version, document=document)
        print("The response of AdminApi->recalculate_pre_match_ratings_using_post1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->recalculate_pre_match_ratings_using_post1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **type** | **str**| type | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_club_restrictions_using_delete**
> object remove_all_club_restrictions_using_delete(authorization, version, request)

removeAllClubRestrictions

### Example


```python
import dupr_backend
from dupr_backend.models.remove_all_club_restrictions_request import RemoveAllClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.RemoveAllClubRestrictionsRequest() # RemoveAllClubRestrictionsRequest | request

    try:
        # removeAllClubRestrictions
        api_response = api_instance.remove_all_club_restrictions_using_delete(authorization, version, request)
        print("The response of AdminApi->remove_all_club_restrictions_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_all_club_restrictions_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**RemoveAllClubRestrictionsRequest**](RemoveAllClubRestrictionsRequest.md)| request | 

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

# **remove_club_restrictions_using_delete**
> object remove_club_restrictions_using_delete(authorization, version, request)

removeClubRestrictions

### Example


```python
import dupr_backend
from dupr_backend.models.remove_club_restrictions_request import RemoveClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.RemoveClubRestrictionsRequest() # RemoveClubRestrictionsRequest | request

    try:
        # removeClubRestrictions
        api_response = api_instance.remove_club_restrictions_using_delete(authorization, version, request)
        print("The response of AdminApi->remove_club_restrictions_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->remove_club_restrictions_using_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**RemoveClubRestrictionsRequest**](RemoveClubRestrictionsRequest.md)| request | 

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

# **reset_client_secret_using_get**
> SingleWrapperOfCreateClientResponse reset_client_secret_using_get(authorization, client_id, version, x_forwarded_for=x_forwarded_for)

resetClientSecret

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_create_client_response import SingleWrapperOfCreateClientResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    client_id = 56 # int | clientId
    version = 'v1.0' # str | version (default to 'v1.0')
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # resetClientSecret
        api_response = api_instance.reset_client_secret_using_get(authorization, client_id, version, x_forwarded_for=x_forwarded_for)
        print("The response of AdminApi->reset_client_secret_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->reset_client_secret_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **client_id** | **int**| clientId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfCreateClientResponse**](SingleWrapperOfCreateClientResponse.md)

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

# **restrict_using_post**
> Wrapper restrict_using_post(authorization, id, version, request)

restrict

### Example


```python
import dupr_backend
from dupr_backend.models.user_restrict_request import UserRestrictRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserRestrictRequest() # UserRestrictRequest | request

    try:
        # restrict
        api_response = api_instance.restrict_using_post(authorization, id, version, request)
        print("The response of AdminApi->restrict_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->restrict_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserRestrictRequest**](UserRestrictRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_topic_using_post**
> SingleWrapperOfTopicResponse save_topic_using_post(authorization, version, request)

saveTopic

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_topic_response import SingleWrapperOfTopicResponse
from dupr_backend.models.topic_request import TopicRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.TopicRequest() # TopicRequest | request

    try:
        # saveTopic
        api_response = api_instance.save_topic_using_post(authorization, version, request)
        print("The response of AdminApi->save_topic_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->save_topic_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**TopicRequest**](TopicRequest.md)| request | 

### Return type

[**SingleWrapperOfTopicResponse**](SingleWrapperOfTopicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match_using_put**
> Wrapper save_verified_match_using_put(authorization, version, request)

saveVerifiedMatch

### Example


```python
import dupr_backend
from dupr_backend.models.match_request import MatchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MatchRequest() # MatchRequest | request

    try:
        # saveVerifiedMatch
        api_response = api_instance.save_verified_match_using_put(authorization, version, request)
        print("The response of AdminApi->save_verified_match_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->save_verified_match_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MatchRequest**](MatchRequest.md)| request | 

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

# **set_club_restrictions_using_put**
> object set_club_restrictions_using_put(authorization, version, request)

setClubRestrictions

### Example


```python
import dupr_backend
from dupr_backend.models.set_club_restrictions_request import SetClubRestrictionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SetClubRestrictionsRequest() # SetClubRestrictionsRequest | request

    try:
        # setClubRestrictions
        api_response = api_instance.set_club_restrictions_using_put(authorization, version, request)
        print("The response of AdminApi->set_club_restrictions_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_club_restrictions_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SetClubRestrictionsRequest**](SetClubRestrictionsRequest.md)| request | 

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

# **set_club_settings_using_put**
> object set_club_settings_using_put(authorization, version, request)

setClubSettings

### Example


```python
import dupr_backend
from dupr_backend.models.set_club_settings_request import SetClubSettingsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SetClubSettingsRequest() # SetClubSettingsRequest | request

    try:
        # setClubSettings
        api_response = api_instance.set_club_settings_using_put(authorization, version, request)
        print("The response of AdminApi->set_club_settings_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->set_club_settings_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SetClubSettingsRequest**](SetClubSettingsRequest.md)| request | 

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

# **signup_batch_using_put**
> SingleWrapperOfMapOfstringAndstring signup_batch_using_put(authorization, version, document=document)

signupBatch

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_map_ofstring_andstring import SingleWrapperOfMapOfstringAndstring
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    document = None # bytearray |  (optional)

    try:
        # signupBatch
        api_response = api_instance.signup_batch_using_put(authorization, version, document=document)
        print("The response of AdminApi->signup_batch_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->signup_batch_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **document** | **bytearray**|  | [optional] 

### Return type

[**SingleWrapperOfMapOfstringAndstring**](SingleWrapperOfMapOfstringAndstring.md)

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

# **signup_using_put**
> SingleWrapperOfstring signup_using_put(authorization, version, request)

signup

### Example


```python
import dupr_backend
from dupr_backend.models.sign_up_request import SignUpRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.SignUpRequest() # SignUpRequest | request

    try:
        # signup
        api_response = api_instance.signup_using_put(authorization, version, request)
        print("The response of AdminApi->signup_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->signup_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**SignUpRequest**](SignUpRequest.md)| request | 

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

# **trigger_missing_elo_rating_for_players_using_post**
> SingleWrapperOfUnit trigger_missing_elo_rating_for_players_using_post(authorization, version)

triggerMissingEloRatingForPlayers

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # triggerMissingEloRatingForPlayers
        api_response = api_instance.trigger_missing_elo_rating_for_players_using_post(authorization, version)
        print("The response of AdminApi->trigger_missing_elo_rating_for_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->trigger_missing_elo_rating_for_players_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

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

# **unclaim_user_using_put**
> Wrapper unclaim_user_using_put(authorization, version, input=input, type=type)

unclaimUser

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    input = 'input_example' # str |  (optional)
    type = 'type_example' # str |  (optional)

    try:
        # unclaimUser
        api_response = api_instance.unclaim_user_using_put(authorization, version, input=input, type=type)
        print("The response of AdminApi->unclaim_user_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unclaim_user_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **input** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

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

# **unobfuscate_match_code_using_get**
> object unobfuscate_match_code_using_get(authorization, matches=matches)

unobfuscateMatchCode

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    matches = 'matches_example' # str | matches (optional)

    try:
        # unobfuscateMatchCode
        api_response = api_instance.unobfuscate_match_code_using_get(authorization, matches=matches)
        print("The response of AdminApi->unobfuscate_match_code_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unobfuscate_match_code_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **matches** | **str**| matches | [optional] 

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

# **unobfuscate_using_get**
> object unobfuscate_using_get(authorization, type, id=id, ids=ids)

unobfuscate

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    type = 'type_example' # str | type
    id = 56 # int | id (optional)
    ids = 'ids_example' # str | ids (optional)

    try:
        # unobfuscate
        api_response = api_instance.unobfuscate_using_get(authorization, type, id=id, ids=ids)
        print("The response of AdminApi->unobfuscate_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->unobfuscate_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **type** | **str**| type | 
 **id** | **int**| id | [optional] 
 **ids** | **str**| ids | [optional] 

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

# **update_banner_using_put**
> SingleWrapperOfUnit update_banner_using_put(authorization, version, create_banner_request)

updateBanner

### Example


```python
import dupr_backend
from dupr_backend.models.create_banner_request import CreateBannerRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    create_banner_request = dupr_backend.CreateBannerRequest() # CreateBannerRequest | createBannerRequest

    try:
        # updateBanner
        api_response = api_instance.update_banner_using_put(authorization, version, create_banner_request)
        print("The response of AdminApi->update_banner_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_banner_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **create_banner_request** | [**CreateBannerRequest**](CreateBannerRequest.md)| createBannerRequest | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_currency_using_put**
> SingleWrapperOfUnit update_club_currency_using_put(authorization, club_id, version, request)

updateClubCurrency

### Example


```python
import dupr_backend
from dupr_backend.models.club_currency_request import ClubCurrencyRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubCurrencyRequest() # ClubCurrencyRequest | request

    try:
        # updateClubCurrency
        api_response = api_instance.update_club_currency_using_put(authorization, club_id, version, request)
        print("The response of AdminApi->update_club_currency_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_club_currency_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubCurrencyRequest**](ClubCurrencyRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_revenue_model_using_put**
> SingleWrapperOfRevenueModel update_club_revenue_model_using_put(authorization, club_id, version, request)

updateClubRevenueModel

### Example


```python
import dupr_backend
from dupr_backend.models.club_revenue_model_request import ClubRevenueModelRequest
from dupr_backend.models.single_wrapper_of_revenue_model import SingleWrapperOfRevenueModel
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    club_id = 56 # int | clubId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ClubRevenueModelRequest() # ClubRevenueModelRequest | request

    try:
        # updateClubRevenueModel
        api_response = api_instance.update_club_revenue_model_using_put(authorization, club_id, version, request)
        print("The response of AdminApi->update_club_revenue_model_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_club_revenue_model_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ClubRevenueModelRequest**](ClubRevenueModelRequest.md)| request | 

### Return type

[**SingleWrapperOfRevenueModel**](SingleWrapperOfRevenueModel.md)

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

# **update_currency_rates_using_get**
> Wrapper update_currency_rates_using_get(authorization, version)

updateCurrencyRates

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # updateCurrencyRates
        api_response = api_instance.update_currency_rates_using_get(authorization, version)
        print("The response of AdminApi->update_currency_rates_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_currency_rates_using_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**Wrapper**](Wrapper.md)

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

# **update_es_index_using_put**
> Wrapper update_es_index_using_put(authorization, id, version, request)

updateESIndex

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 'id_example' # str | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = 'request_example' # str | request

    try:
        # updateESIndex
        api_response = api_instance.update_es_index_using_put(authorization, id, version, request)
        print("The response of AdminApi->update_es_index_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_es_index_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **str**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | **str**| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_client_permissions_using_post**
> SingleWrapperOfUpdateClientPermissionsResponse update_external_client_permissions_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)

updateExternalClientPermissions

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_update_client_permissions_response import SingleWrapperOfUpdateClientPermissionsResponse
from dupr_backend.models.update_client_permissions_request import UpdateClientPermissionsRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UpdateClientPermissionsRequest() # UpdateClientPermissionsRequest | request
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # updateExternalClientPermissions
        api_response = api_instance.update_external_client_permissions_using_post(authorization, version, request, x_forwarded_for=x_forwarded_for)
        print("The response of AdminApi->update_external_client_permissions_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_external_client_permissions_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UpdateClientPermissionsRequest**](UpdateClientPermissionsRequest.md)| request | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfUpdateClientPermissionsResponse**](SingleWrapperOfUpdateClientPermissionsResponse.md)

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

# **update_external_id_cron_using_put**
> object update_external_id_cron_using_put(authorization, version, request)

updateExternalIdCron

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.S3Object() # S3Object | request

    try:
        # updateExternalIdCron
        api_response = api_instance.update_external_id_cron_using_put(authorization, version, request)
        print("The response of AdminApi->update_external_id_cron_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_external_id_cron_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**S3Object**](S3Object.md)| request | 

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

# **update_lucra_connection_using_put**
> Wrapper update_lucra_connection_using_put(authorization, id, version, request)

updateLucraConnection

### Example


```python
import dupr_backend
from dupr_backend.models.user_lucra_request import UserLucraRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserLucraRequest() # UserLucraRequest | request

    try:
        # updateLucraConnection
        api_response = api_instance.update_lucra_connection_using_put(authorization, id, version, request)
        print("The response of AdminApi->update_lucra_connection_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_lucra_connection_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserLucraRequest**](UserLucraRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_match_using_put**
> SingleWrapperOfMatchResponse update_match_using_put(authorization, version, match_update_request)

updateMatch

### Example


```python
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    match_update_request = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | matchUpdateRequest

    try:
        # updateMatch
        api_response = api_instance.update_match_using_put(authorization, version, match_update_request)
        print("The response of AdminApi->update_match_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_match_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

# **update_payment_status_using_post**
> Wrapper update_payment_status_using_post(authorization, version, request)

updatePaymentStatus

### Example


```python
import dupr_backend
from dupr_backend.models.update_registration_request import UpdateRegistrationRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.UpdateRegistrationRequest()] # List[UpdateRegistrationRequest] | request

    try:
        # updatePaymentStatus
        api_response = api_instance.update_payment_status_using_post(authorization, version, request)
        print("The response of AdminApi->update_payment_status_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_payment_status_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[UpdateRegistrationRequest]**](UpdateRegistrationRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_rating_using_put**
> SingleWrapperOfUnit update_player_rating_using_put(authorization, id, version, request)

updatePlayerRating

### Example


```python
import dupr_backend
from dupr_backend.models.player_rating_update_request import PlayerRatingUpdateRequest
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    id = 56 # int | id
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerRatingUpdateRequest() # PlayerRatingUpdateRequest | request

    try:
        # updatePlayerRating
        api_response = api_instance.update_player_rating_using_put(authorization, id, version, request)
        print("The response of AdminApi->update_player_rating_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_player_rating_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **id** | **int**| id | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerRatingUpdateRequest**](PlayerRatingUpdateRequest.md)| request | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_statistics_using_put**
> SingleWrapperOfboolean update_player_statistics_using_put(authorization, version, request)

updatePlayerStatistics

### Example


```python
import dupr_backend
from dupr_backend.models.player_statistics_update_request import PlayerStatisticsUpdateRequest
from dupr_backend.models.single_wrapper_ofboolean import SingleWrapperOfboolean
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerStatisticsUpdateRequest() # PlayerStatisticsUpdateRequest | request

    try:
        # updatePlayerStatistics
        api_response = api_instance.update_player_statistics_using_put(authorization, version, request)
        print("The response of AdminApi->update_player_statistics_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_player_statistics_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerStatisticsUpdateRequest**](PlayerStatisticsUpdateRequest.md)| request | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

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

# **update_ratings_cron_using_put**
> Wrapper update_ratings_cron_using_put(authorization, version, s3)

updateRatingsCron

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    s3 = dupr_backend.S3Object() # S3Object | s3

    try:
        # updateRatingsCron
        api_response = api_instance.update_ratings_cron_using_put(authorization, version, s3)
        print("The response of AdminApi->update_ratings_cron_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_ratings_cron_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **s3** | [**S3Object**](S3Object.md)| s3 | 

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

# **update_referral_code_using_patch**
> Wrapper update_referral_code_using_patch(authorization, version)

updateReferralCode

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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # updateReferralCode
        api_response = api_instance.update_referral_code_using_patch(authorization, version)
        print("The response of AdminApi->update_referral_code_using_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_referral_code_using_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_using_post**
> object update_status_using_post(authorization, version, request)

updateStatus

### Example


```python
import dupr_backend
from dupr_backend.models.user_status_update_request import UserStatusUpdateRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserStatusUpdateRequest() # UserStatusUpdateRequest | request

    try:
        # updateStatus
        api_response = api_instance.update_status_using_post(authorization, version, request)
        print("The response of AdminApi->update_status_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_status_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserStatusUpdateRequest**](UserStatusUpdateRequest.md)| request | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile_using_put**
> SingleWrapperOfUserResponse update_user_profile_using_put(authorization, user_id, version, request)

updateUserProfile

### Example


```python
import dupr_backend
from dupr_backend.models.player_profile_request import PlayerProfileRequest
from dupr_backend.models.single_wrapper_of_user_response import SingleWrapperOfUserResponse
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    user_id = 56 # int | userId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.PlayerProfileRequest() # PlayerProfileRequest | request

    try:
        # updateUserProfile
        api_response = api_instance.update_user_profile_using_put(authorization, user_id, version, request)
        print("The response of AdminApi->update_user_profile_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->update_user_profile_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **user_id** | **int**| userId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**PlayerProfileRequest**](PlayerProfileRequest.md)| request | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

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

# **upload_dupr_performance_chart_data_using_put**
> Wrapper upload_dupr_performance_chart_data_using_put(authorization, version, request)

uploadDuprPerformanceChartData

### Example


```python
import dupr_backend
from dupr_backend.models.s3_object import S3Object
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.S3Object() # S3Object | request

    try:
        # uploadDuprPerformanceChartData
        api_response = api_instance.upload_dupr_performance_chart_data_using_put(authorization, version, request)
        print("The response of AdminApi->upload_dupr_performance_chart_data_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->upload_dupr_performance_chart_data_using_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**S3Object**](S3Object.md)| request | 

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

# **user_lookup_using_post**
> SingleWrapperOfPageOfUserLookupResponse user_lookup_using_post(authorization, version, user_lookup_request)

userLookup

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_user_lookup_response import SingleWrapperOfPageOfUserLookupResponse
from dupr_backend.models.user_search_request import UserSearchRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    user_lookup_request = dupr_backend.UserSearchRequest() # UserSearchRequest | userLookupRequest

    try:
        # userLookup
        api_response = api_instance.user_lookup_using_post(authorization, version, user_lookup_request)
        print("The response of AdminApi->user_lookup_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->user_lookup_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **user_lookup_request** | [**UserSearchRequest**](UserSearchRequest.md)| userLookupRequest | 

### Return type

[**SingleWrapperOfPageOfUserLookupResponse**](SingleWrapperOfPageOfUserLookupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_using_post**
> Wrapper verify_email_using_post(authorization, version, request)

verifyEmail

### Example


```python
import dupr_backend
from dupr_backend.models.verify_email_request import VerifyEmailRequest
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
    api_instance = dupr_backend.AdminApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.VerifyEmailRequest() # VerifyEmailRequest | request

    try:
        # verifyEmail
        api_response = api_instance.verify_email_using_post(authorization, version, request)
        print("The response of AdminApi->verify_email_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->verify_email_using_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**VerifyEmailRequest**](VerifyEmailRequest.md)| request | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

