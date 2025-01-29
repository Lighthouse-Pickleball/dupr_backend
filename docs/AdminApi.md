# dupr_backend.AdminApi

All URIs are relative to *https://backend.mydupr.com/*

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
> Wrapper activate_match_using_post(body, authorization, version)

activateMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # activateMatch
    api_response = api_instance.activate_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->activate_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 
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

# **add_key_to_external_client_using_post**
> object add_key_to_external_client_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

addKeyToExternalClient

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.AddClientKeyRequest() # AddClientKeyRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # addKeyToExternalClient
    api_response = api_instance.add_key_to_external_client_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->add_key_to_external_client_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AddClientKeyRequest**](AddClientKeyRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **adjust_rating_using_put**
> Wrapper adjust_rating_using_put(body, authorization, version)

adjustRating

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.AdjustRatingRequest() # AdjustRatingRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # adjustRating
    api_response = api_instance.adjust_rating_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->adjust_rating_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AdjustRatingRequest**](AdjustRatingRequest.md)| request | 
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

# **admin_verified_match_history_using_get**
> SingleWrapperOfPageOfMatchResponse admin_verified_match_history_using_get(authorization, limit, offset, version)

adminVerifiedMatchHistory

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # adminVerifiedMatchHistory
    api_response = api_instance.admin_verified_match_history_using_get(authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->admin_verified_match_history_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
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

# **batch_calculated_statistics_using_put**
> batch_calculated_statistics_using_put(body, authorization, version)

batchCalculatedStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | s3Object
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchCalculatedStatistics
    api_instance.batch_calculated_statistics_using_put(body, authorization, version)
except ApiException as e:
    print("Exception when calling AdminApi->batch_calculated_statistics_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| s3Object | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_club_matches_using_post**
> SingleWrapperOfUnit batch_club_matches_using_post(body, authorization, club_id, version)

batchClubMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # batchClubMatches
    api_response = api_instance.batch_club_matches_using_post(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->batch_club_matches_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_manual_club_matches_using_post**
> SingleWrapperOfUnit batch_manual_club_matches_using_post(body, authorization, version)

batchManualClubMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchManualClubMatches
    api_response = api_instance.batch_manual_club_matches_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->batch_manual_club_matches_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| request | 
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

# **batch_manual_matches_using_post**
> SingleWrapperOfUnit batch_manual_matches_using_post(body, authorization, version)

batchManualMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchManualMatches
    api_response = api_instance.batch_manual_matches_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->batch_manual_matches_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| request | 
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

# **batch_player_rating_provisional_using_put**
> SingleWrapperOfUnit batch_player_rating_provisional_using_put(body, authorization, version)

batchPlayerRatingProvisional

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.BatchPlayerRatingProvisionalRequest() # BatchPlayerRatingProvisionalRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchPlayerRatingProvisional
    api_response = api_instance.batch_player_rating_provisional_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->batch_player_rating_provisional_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchPlayerRatingProvisionalRequest**](BatchPlayerRatingProvisionalRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_player_rating_using_put**
> SingleWrapperOfUnit batch_player_rating_using_put(body, authorization, version)

batchPlayerRating

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.BatchPlayerRatingRequest() # BatchPlayerRatingRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchPlayerRating
    api_response = api_instance.batch_player_rating_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->batch_player_rating_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BatchPlayerRatingRequest**](BatchPlayerRatingRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **batch_set_reliability_scores_using_post**
> batch_set_reliability_scores_using_post(body, authorization, version)

batchSetReliabilityScores

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | s3Object
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # batchSetReliabilityScores
    api_instance.batch_set_reliability_scores_using_post(body, authorization, version)
except ApiException as e:
    print("Exception when calling AdminApi->batch_set_reliability_scores_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| s3Object | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **block_admin_apis_using_put**
> bool block_admin_apis_using_put(authorization, flag, version)

blockAdminApis

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
flag = true # bool | flag
version = 'version_example' # str | version

try:
    # blockAdminApis
    api_response = api_instance.block_admin_apis_using_put(authorization, flag, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->block_admin_apis_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **flag** | **bool**| flag | 
 **version** | **str**| version | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_delete_matches_using_put**
> Wrapper bulk_delete_matches_using_put(authorization, type, version, document=document)

bulkDeleteMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
type = 'type_example' # str | type
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # bulkDeleteMatches
    api_response = api_instance.bulk_delete_matches_using_put(authorization, type, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->bulk_delete_matches_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **type** | **str**| type | 
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_reliability_score_using_put**
> Wrapper bulk_reliability_score_using_put(authorization, version, request=request)

bulkReliabilityScore

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
request = 'request_example' # str |  (optional)

try:
    # bulkReliabilityScore
    api_response = api_instance.bulk_reliability_score_using_put(authorization, version, request=request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->bulk_reliability_score_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **request** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_send_coppa_email_using_post**
> object bulk_send_coppa_email_using_post(body, authorization, version)

bulkSendCoppaEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # bulkSendCoppaEmail
    api_response = api_instance.bulk_send_coppa_email_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->bulk_send_coppa_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bulk_send_wrapped_email_using_post**
> object bulk_send_wrapped_email_using_post(body, authorization, version)

bulkSendWrappedEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.BulkCoppaEmailRequest() # BulkCoppaEmailRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # bulkSendWrappedEmail
    api_response = api_instance.bulk_send_wrapped_email_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->bulk_send_wrapped_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BulkCoppaEmailRequest**](BulkCoppaEmailRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_email_using_put**
> Wrapper change_email_using_put(body, authorization, version)

changeEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.ChangeEmailAdminRequest() # ChangeEmailAdminRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # changeEmail
    api_response = api_instance.change_email_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->change_email_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeEmailAdminRequest**](ChangeEmailAdminRequest.md)| request | 
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

# **change_role_using_post**
> Wrapper change_role_using_post(body, authorization, version)

changeRole

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.ChangeRoleRequest() # ChangeRoleRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # changeRole
    api_response = api_instance.change_role_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->change_role_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChangeRoleRequest**](ChangeRoleRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **club_create_using_put**
> Wrapper club_create_using_put(body, authorization, version)

clubCreate

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.CreateClubsRequest() # CreateClubsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # clubCreate
    api_response = api_instance.club_create_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->club_create_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClubsRequest**](CreateClubsRequest.md)| request | 
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

# **create_banner_using_post**
> SingleWrapperOfUnit create_banner_using_post(body, authorization, version)

createBanner

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.CreateBannerRequest() # CreateBannerRequest | createBannerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # createBanner
    api_response = api_instance.create_banner_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_banner_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBannerRequest**](CreateBannerRequest.md)| createBannerRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_clubs_batch_using_put**
> SingleWrapperOfstring create_clubs_batch_using_put(authorization, version, document=document)

createClubsBatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # createClubsBatch
    api_response = api_instance.create_clubs_batch_using_put(authorization, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_clubs_batch_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_external_client_using_post**
> SingleWrapperOfCreateClientResponse create_external_client_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

createExternalClient

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.CreateClientRequest() # CreateClientRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # createExternalClient
    api_response = api_instance.create_external_client_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->create_external_client_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateClientRequest**](CreateClientRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfCreateClientResponse**](SingleWrapperOfCreateClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **decode_using_get**
> object decode_using_get(authorization, id=id, ids=ids)

decode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id (optional)
ids = 'ids_example' # str | ids (optional)

try:
    # decode
    api_response = api_instance.decode_using_get(authorization, id=id, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->decode_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | [optional] 
 **ids** | **str**| ids | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_club_using_delete**
> Wrapper delete_club_using_delete(authorization, club_id, version)

deleteClub

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # deleteClub
    api_response = api_instance.delete_club_using_delete(authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_club_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_match_using_post**
> Wrapper delete_match_using_post(body, authorization, version)

deleteMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.DeleteMatchRequest() # DeleteMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # deleteMatch
    api_response = api_instance.delete_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DeleteMatchRequest**](DeleteMatchRequest.md)| request | 
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

# **delete_user_using_put**
> Wrapper delete_user_using_put(authorization, version, input=input, type=type)

deleteUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
input = 'input_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    # deleteUser
    api_response = api_instance.delete_user_using_put(authorization, version, input=input, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **input** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wix_user_using_delete**
> Wrapper delete_wix_user_using_delete(authorization, user_id, version)

deleteWixUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
user_id = 789 # int | userId
version = 'version_example' # str | version

try:
    # deleteWixUser
    api_response = api_instance.delete_wix_user_using_delete(authorization, user_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->delete_wix_user_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **user_id** | **int**| userId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dupr_id_using_get**
> SingleWrapperOfAdminUserProfile dupr_id_using_get(authorization, version, dupr_id=dupr_id, external_id=external_id, user_id=user_id)

duprId

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
dupr_id = 'dupr_id_example' # str | duprId (optional)
external_id = 'external_id_example' # str | externalId (optional)
user_id = 789 # int | userId (optional)

try:
    # duprId
    api_response = api_instance.dupr_id_using_get(authorization, version, dupr_id=dupr_id, external_id=external_id, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->dupr_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_club_staff_using_post**
> Wrapper edit_club_staff_using_post(body, authorization, version)

editClubStaff

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.EditClubStaffRequest() # EditClubStaffRequest | editClubStaffRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editClubStaff
    api_response = api_instance.edit_club_staff_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->edit_club_staff_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditClubStaffRequest**](EditClubStaffRequest.md)| editClubStaffRequest | 
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

# **encode_using_get**
> object encode_using_get(authorization, id=id, ids=ids)

encode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id (optional)
ids = 'ids_example' # str | ids (optional)

try:
    # encode
    api_response = api_instance.encode_using_get(authorization, id=id, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->encode_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | [optional] 
 **ids** | **str**| ids | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_matches_missing_team_player_using_get**
> Wrapper export_matches_missing_team_player_using_get(authorization, version)

exportMatchesMissingTeamPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # exportMatchesMissingTeamPlayer
    api_response = api_instance.export_matches_missing_team_player_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->export_matches_missing_team_player_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_users_via_mail_using_post**
> Wrapper export_users_via_mail_using_post(authorization, version)

exportUsersViaMail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # exportUsersViaMail
    api_response = api_instance.export_users_via_mail_using_post(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->export_users_via_mail_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **find_duplicated_account_for_players_using_post**
> ArrayWrapperOfDuplicatedAccountResponse find_duplicated_account_for_players_using_post(authorization, version)

findDuplicatedAccountForPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # findDuplicatedAccountForPlayers
    api_response = api_instance.find_duplicated_account_for_players_using_post(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->find_duplicated_account_for_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfDuplicatedAccountResponse**](ArrayWrapperOfDuplicatedAccountResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_banner_using_get**
> ArrayWrapperOfInformativeBannerResponce get_active_banner_using_get(authorization, version)

getActiveBanner

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getActiveBanner
    api_response = api_instance.get_active_banner_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_active_banner_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfInformativeBannerResponce**](ArrayWrapperOfInformativeBannerResponce.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_banner_using_get**
> ArrayWrapperOfInformativeBannerResponce get_all_banner_using_get(authorization, version)

getAllBanner

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAllBanner
    api_response = api_instance.get_all_banner_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_all_banner_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfInformativeBannerResponce**](ArrayWrapperOfInformativeBannerResponce.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_roles_using_get**
> ArrayWrapperOfRoleResponse get_all_roles_using_get(authorization, version)

getAllRoles

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getAllRoles
    api_response = api_instance.get_all_roles_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_all_roles_using_get: %s\n" % e)
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

# **get_club_restrictions_using_post**
> object get_club_restrictions_using_post(body, authorization, version)

getClubRestrictions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.GetClubRestrictionsRequest() # GetClubRestrictionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getClubRestrictions
    api_response = api_instance.get_club_restrictions_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_club_restrictions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClubRestrictionsRequest**](GetClubRestrictionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_club_settings_using_post**
> object get_club_settings_using_post(body, authorization, version)

getClubSettings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.GetClubSettingsRequest() # GetClubSettingsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getClubSettings
    api_response = api_instance.get_club_settings_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_club_settings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClubSettingsRequest**](GetClubSettingsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_client_permissions_using_post**
> object get_external_client_permissions_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

getExternalClientPermissions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.GetClientPermissionsRequest() # GetClientPermissionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # getExternalClientPermissions
    api_response = api_instance.get_external_client_permissions_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_external_client_permissions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GetClientPermissionsRequest**](GetClientPermissionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_using_get**
> SingleWrapperOfMatchResponse get_match_using_get(authorization, id, version)

getMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # getMatch
    api_response = api_instance.get_match_using_get(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_match_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_bracket_using_post**
> SingleWrapperOfPageOfBracketResponse get_user_bracket_using_post(body, authorization, version)

getUserBracket

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UserBracketAdminRequest() # UserBracketAdminRequest | userBracketAdminRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getUserBracket
    api_response = api_instance.get_user_bracket_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_user_bracket_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserBracketAdminRequest**](UserBracketAdminRequest.md)| userBracketAdminRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfBracketResponse**](SingleWrapperOfPageOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_profile_using_get**
> SingleWrapperOfUserResponse get_user_profile_using_get(authorization, user_id, version)

getUserProfile

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
user_id = 789 # int | userId
version = 'version_example' # str | version

try:
    # getUserProfile
    api_response = api_instance.get_user_profile_using_get(authorization, user_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->get_user_profile_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **user_id** | **int**| userId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_club_members_using_post**
> Wrapper index_club_members_using_post(authorization, version)

indexClubMembers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # indexClubMembers
    api_response = api_instance.index_club_members_using_post(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->index_club_members_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_clubs_using_put**
> Wrapper index_clubs_using_put(authorization, version)

indexClubs

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # indexClubs
    api_response = api_instance.index_clubs_using_put(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->index_clubs_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_player_using_patch**
> object index_player_using_patch(authorization, id, version)

indexPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # indexPlayer
    api_response = api_instance.index_player_using_patch(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->index_player_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **index_players_using_patch**
> Wrapper index_players_using_patch(authorization, version)

indexPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # indexPlayers
    api_response = api_instance.index_players_using_patch(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->index_players_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_codes_export_using_get**
> Wrapper match_codes_export_using_get(authorization, version, sources=sources)

matchCodesExport

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
sources = ['sources_example'] # list[str] | sources (optional)

try:
    # matchCodesExport
    api_response = api_instance.match_codes_export_using_get(authorization, version, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->match_codes_export_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **sources** | [**list[str]**](str.md)| sources | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_reassign_batch_using_post**
> SingleWrapperOfstring match_reassign_batch_using_post(authorization, version, document=document, notify=notify)

matchReassignBatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)
notify = true # bool | notify (optional)

try:
    # matchReassignBatch
    api_response = api_instance.match_reassign_batch_using_post(authorization, version, document=document, notify=notify)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->match_reassign_batch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 
 **notify** | **bool**| notify | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **match_reassign_using_post**
> SingleWrapperOfUnit match_reassign_using_post(body, authorization, version)

matchReassign

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.MatchesReassignRequest() # MatchesReassignRequest | matchesReassignRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # matchReassign
    api_response = api_instance.match_reassign_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->match_reassign_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchesReassignRequest**](MatchesReassignRequest.md)| matchesReassignRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **matches_export_using_get**
> Wrapper matches_export_using_get(all, authorization, version, sources=sources)

matchesExport

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
all = true # bool | all
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
sources = ['sources_example'] # list[str] | sources (optional)

try:
    # matchesExport
    api_response = api_instance.matches_export_using_get(all, authorization, version, sources=sources)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->matches_export_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **all** | **bool**| all | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **sources** | [**list[str]**](str.md)| sources | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_users_batch_using_post**
> SingleWrapperOfstring merge_users_batch_using_post(authorization, version, document=document)

mergeUsersBatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # mergeUsersBatch
    api_response = api_instance.merge_users_batch_using_post(authorization, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->merge_users_batch_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge_users_using_post**
> SingleWrapperOfMergeUsersResponse merge_users_using_post(body, authorization, version)

mergeUsers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.MergeUsersRequest() # MergeUsersRequest | mergeUsersRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # mergeUsers
    api_response = api_instance.merge_users_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->merge_users_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MergeUsersRequest**](MergeUsersRequest.md)| mergeUsersRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMergeUsersResponse**](SingleWrapperOfMergeUsersResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obfuscate_match_id_using_get**
> str obfuscate_match_id_using_get(authorization, to_type, ids=ids)

obfuscateMatchId

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
to_type = 'to_type_example' # str | toType
ids = 'ids_example' # str | ids (optional)

try:
    # obfuscateMatchId
    api_response = api_instance.obfuscate_match_id_using_get(authorization, to_type, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->obfuscate_match_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **to_type** | **str**| toType | 
 **ids** | **str**| ids | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **obfuscate_using_get**
> object obfuscate_using_get(authorization, type, id=id, ids=ids)

obfuscate

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
type = 'type_example' # str | type
id = 789 # int | id (optional)
ids = 'ids_example' # str | ids (optional)

try:
    # obfuscate
    api_response = api_instance.obfuscate_using_get(authorization, type, id=id, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->obfuscate_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **populate_unknown_player_pre_ratings_using_post**
> Wrapper populate_unknown_player_pre_ratings_using_post(authorization)

populateUnknownPlayerPreRatings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )

try:
    # populateUnknownPlayerPreRatings
    api_response = api_instance.populate_unknown_player_pre_ratings_using_post(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->populate_unknown_player_pre_ratings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **re_create_es_index_using_post**
> Wrapper re_create_es_index_using_post(authorization, id, version)

reCreateESIndex

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # reCreateESIndex
    api_response = api_instance.re_create_es_index_using_post(authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->re_create_es_index_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_match_elo_ratings_bulk_using_post**
> Wrapper recalculate_match_elo_ratings_bulk_using_post(authorization, type, version, document=document)

recalculateMatchELORatingsBulk

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
type = 'type_example' # str | type
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # recalculateMatchELORatingsBulk
    api_response = api_instance.recalculate_match_elo_ratings_bulk_using_post(authorization, type, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->recalculate_match_elo_ratings_bulk_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **type** | **str**| type | 
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings_using_post**
> Wrapper recalculate_pre_match_ratings_using_post(body, authorization, version)

recalculatePreMatchRatings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.CalculateMatchesRange() # CalculateMatchesRange | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # recalculatePreMatchRatings
    api_response = api_instance.recalculate_pre_match_ratings_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->recalculate_pre_match_ratings_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CalculateMatchesRange**](CalculateMatchesRange.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **recalculate_pre_match_ratings_using_post1**
> Wrapper recalculate_pre_match_ratings_using_post1(authorization, type, version, document=document)

recalculatePreMatchRatings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
type = 'type_example' # str | type
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # recalculatePreMatchRatings
    api_response = api_instance.recalculate_pre_match_ratings_using_post1(authorization, type, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->recalculate_pre_match_ratings_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **type** | **str**| type | 
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_all_club_restrictions_using_delete**
> object remove_all_club_restrictions_using_delete(body, authorization, version)

removeAllClubRestrictions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.RemoveAllClubRestrictionsRequest() # RemoveAllClubRestrictionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # removeAllClubRestrictions
    api_response = api_instance.remove_all_club_restrictions_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->remove_all_club_restrictions_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveAllClubRestrictionsRequest**](RemoveAllClubRestrictionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_club_restrictions_using_delete**
> object remove_club_restrictions_using_delete(body, authorization, version)

removeClubRestrictions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.RemoveClubRestrictionsRequest() # RemoveClubRestrictionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # removeClubRestrictions
    api_response = api_instance.remove_club_restrictions_using_delete(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->remove_club_restrictions_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RemoveClubRestrictionsRequest**](RemoveClubRestrictionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_client_secret_using_get**
> SingleWrapperOfCreateClientResponse reset_client_secret_using_get(authorization, client_id, version, x_forwarded_for=x_forwarded_for)

resetClientSecret

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
client_id = 789 # int | clientId
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # resetClientSecret
    api_response = api_instance.reset_client_secret_using_get(authorization, client_id, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->reset_client_secret_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **client_id** | **int**| clientId | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfCreateClientResponse**](SingleWrapperOfCreateClientResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restrict_using_post**
> Wrapper restrict_using_post(body, authorization, id, version)

restrict

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UserRestrictRequest() # UserRestrictRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # restrict
    api_response = api_instance.restrict_using_post(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->restrict_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRestrictRequest**](UserRestrictRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_topic_using_post**
> SingleWrapperOfTopicResponse save_topic_using_post(body, authorization, version)

saveTopic

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.TopicRequest() # TopicRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveTopic
    api_response = api_instance.save_topic_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->save_topic_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TopicRequest**](TopicRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfTopicResponse**](SingleWrapperOfTopicResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_verified_match_using_put**
> Wrapper save_verified_match_using_put(body, authorization, version)

saveVerifiedMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.MatchRequest() # MatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveVerifiedMatch
    api_response = api_instance.save_verified_match_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->save_verified_match_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchRequest**](MatchRequest.md)| request | 
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

# **set_club_restrictions_using_put**
> object set_club_restrictions_using_put(body, authorization, version)

setClubRestrictions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.SetClubRestrictionsRequest() # SetClubRestrictionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # setClubRestrictions
    api_response = api_instance.set_club_restrictions_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->set_club_restrictions_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetClubRestrictionsRequest**](SetClubRestrictionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_club_settings_using_put**
> object set_club_settings_using_put(body, authorization, version)

setClubSettings

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.SetClubSettingsRequest() # SetClubSettingsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # setClubSettings
    api_response = api_instance.set_club_settings_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->set_club_settings_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SetClubSettingsRequest**](SetClubSettingsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_batch_using_put**
> SingleWrapperOfMapOfstringAndstring signup_batch_using_put(authorization, version, document=document)

signupBatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
document = 'document_example' # str |  (optional)

try:
    # signupBatch
    api_response = api_instance.signup_batch_using_put(authorization, version, document=document)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->signup_batch_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **document** | **str**|  | [optional] 

### Return type

[**SingleWrapperOfMapOfstringAndstring**](SingleWrapperOfMapOfstringAndstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_using_put**
> SingleWrapperOfstring signup_using_put(body, authorization, version)

signup

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.SignUpRequest() # SignUpRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # signup
    api_response = api_instance.signup_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->signup_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SignUpRequest**](SignUpRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfstring**](SingleWrapperOfstring.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trigger_missing_elo_rating_for_players_using_post**
> SingleWrapperOfUnit trigger_missing_elo_rating_for_players_using_post(authorization, version)

triggerMissingEloRatingForPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # triggerMissingEloRatingForPlayers
    api_response = api_instance.trigger_missing_elo_rating_for_players_using_post(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->trigger_missing_elo_rating_for_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unclaim_user_using_put**
> Wrapper unclaim_user_using_put(authorization, version, input=input, type=type)

unclaimUser

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
input = 'input_example' # str |  (optional)
type = 'type_example' # str |  (optional)

try:
    # unclaimUser
    api_response = api_instance.unclaim_user_using_put(authorization, version, input=input, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->unclaim_user_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **input** | **str**|  | [optional] 
 **type** | **str**|  | [optional] 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unobfuscate_match_code_using_get**
> object unobfuscate_match_code_using_get(authorization, matches=matches)

unobfuscateMatchCode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
matches = 'matches_example' # str | matches (optional)

try:
    # unobfuscateMatchCode
    api_response = api_instance.unobfuscate_match_code_using_get(authorization, matches=matches)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->unobfuscate_match_code_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **matches** | **str**| matches | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unobfuscate_using_get**
> object unobfuscate_using_get(authorization, type, id=id, ids=ids)

unobfuscate

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
type = 'type_example' # str | type
id = 789 # int | id (optional)
ids = 'ids_example' # str | ids (optional)

try:
    # unobfuscate
    api_response = api_instance.unobfuscate_using_get(authorization, type, id=id, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->unobfuscate_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_banner_using_put**
> SingleWrapperOfUnit update_banner_using_put(body, authorization, version)

updateBanner

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.CreateBannerRequest() # CreateBannerRequest | createBannerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateBanner
    api_response = api_instance.update_banner_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_banner_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateBannerRequest**](CreateBannerRequest.md)| createBannerRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_currency_using_put**
> SingleWrapperOfUnit update_club_currency_using_put(body, authorization, club_id, version)

updateClubCurrency

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.ClubCurrencyRequest() # ClubCurrencyRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # updateClubCurrency
    api_response = api_instance.update_club_currency_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_club_currency_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubCurrencyRequest**](ClubCurrencyRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_club_revenue_model_using_put**
> SingleWrapperOfRevenueModel update_club_revenue_model_using_put(body, authorization, club_id, version)

updateClubRevenueModel

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.ClubRevenueModelRequest() # ClubRevenueModelRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
club_id = 789 # int | clubId
version = 'version_example' # str | version

try:
    # updateClubRevenueModel
    api_response = api_instance.update_club_revenue_model_using_put(body, authorization, club_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_club_revenue_model_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClubRevenueModelRequest**](ClubRevenueModelRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **club_id** | **int**| clubId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfRevenueModel**](SingleWrapperOfRevenueModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_currency_rates_using_get**
> Wrapper update_currency_rates_using_get(authorization, version)

updateCurrencyRates

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateCurrencyRates
    api_response = api_instance.update_currency_rates_using_get(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_currency_rates_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_es_index_using_put**
> Wrapper update_es_index_using_put(body, authorization, id, version)

updateESIndex

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = 'body_example' # str | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 'id_example' # str | id
version = 'version_example' # str | version

try:
    # updateESIndex
    api_response = api_instance.update_es_index_using_put(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_es_index_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**str**](str.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **str**| id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_client_permissions_using_post**
> SingleWrapperOfUpdateClientPermissionsResponse update_external_client_permissions_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)

updateExternalClientPermissions

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UpdateClientPermissionsRequest() # UpdateClientPermissionsRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # updateExternalClientPermissions
    api_response = api_instance.update_external_client_permissions_using_post(body, authorization, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_external_client_permissions_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateClientPermissionsRequest**](UpdateClientPermissionsRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfUpdateClientPermissionsResponse**](SingleWrapperOfUpdateClientPermissionsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_external_id_cron_using_put**
> object update_external_id_cron_using_put(body, authorization, version)

updateExternalIdCron

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateExternalIdCron
    api_response = api_instance.update_external_id_cron_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_external_id_cron_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lucra_connection_using_put**
> Wrapper update_lucra_connection_using_put(body, authorization, id, version)

updateLucraConnection

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UserLucraRequest() # UserLucraRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # updateLucraConnection
    api_response = api_instance.update_lucra_connection_using_put(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_lucra_connection_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLucraRequest**](UserLucraRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_match_using_put**
> SingleWrapperOfMatchResponse update_match_using_put(body, authorization, version)

updateMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.MatchUpdateRequest() # MatchUpdateRequest | matchUpdateRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateMatch
    api_response = api_instance.update_match_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_match_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MatchUpdateRequest**](MatchUpdateRequest.md)| matchUpdateRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfMatchResponse**](SingleWrapperOfMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment_status_using_post**
> Wrapper update_payment_status_using_post(body, authorization, version)

updatePaymentStatus

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = [dupr_backend.UpdateRegistrationRequest()] # list[UpdateRegistrationRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updatePaymentStatus
    api_response = api_instance.update_payment_status_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_payment_status_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[UpdateRegistrationRequest]**](UpdateRegistrationRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_rating_using_put**
> SingleWrapperOfUnit update_player_rating_using_put(body, authorization, id, version)

updatePlayerRating

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.PlayerRatingUpdateRequest() # PlayerRatingUpdateRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
id = 789 # int | id
version = 'version_example' # str | version

try:
    # updatePlayerRating
    api_response = api_instance.update_player_rating_using_put(body, authorization, id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_player_rating_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerRatingUpdateRequest**](PlayerRatingUpdateRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **id** | **int**| id | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_player_statistics_using_put**
> SingleWrapperOfboolean update_player_statistics_using_put(body, authorization, version)

updatePlayerStatistics

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.PlayerStatisticsUpdateRequest() # PlayerStatisticsUpdateRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updatePlayerStatistics
    api_response = api_instance.update_player_statistics_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_player_statistics_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerStatisticsUpdateRequest**](PlayerStatisticsUpdateRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfboolean**](SingleWrapperOfboolean.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ratings_cron_using_put**
> Wrapper update_ratings_cron_using_put(body, authorization, version)

updateRatingsCron

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | s3
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateRatingsCron
    api_response = api_instance.update_ratings_cron_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_ratings_cron_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| s3 | 
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

# **update_referral_code_using_patch**
> Wrapper update_referral_code_using_patch(authorization, version)

updateReferralCode

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateReferralCode
    api_response = api_instance.update_referral_code_using_patch(authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_referral_code_using_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_status_using_post**
> object update_status_using_post(body, authorization, version)

updateStatus

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UserStatusUpdateRequest() # UserStatusUpdateRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # updateStatus
    api_response = api_instance.update_status_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_status_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserStatusUpdateRequest**](UserStatusUpdateRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_profile_using_put**
> SingleWrapperOfUserResponse update_user_profile_using_put(body, authorization, user_id, version)

updateUserProfile

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.PlayerProfileRequest() # PlayerProfileRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
user_id = 789 # int | userId
version = 'version_example' # str | version

try:
    # updateUserProfile
    api_response = api_instance.update_user_profile_using_put(body, authorization, user_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->update_user_profile_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**PlayerProfileRequest**](PlayerProfileRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **user_id** | **int**| userId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUserResponse**](SingleWrapperOfUserResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_dupr_performance_chart_data_using_put**
> Wrapper upload_dupr_performance_chart_data_using_put(body, authorization, version)

uploadDuprPerformanceChartData

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.S3Object() # S3Object | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # uploadDuprPerformanceChartData
    api_response = api_instance.upload_dupr_performance_chart_data_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->upload_dupr_performance_chart_data_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**S3Object**](S3Object.md)| request | 
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

# **user_lookup_using_post**
> SingleWrapperOfPageOfUserLookupResponse user_lookup_using_post(body, authorization, version)

userLookup

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.UserSearchRequest() # UserSearchRequest | userLookupRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # userLookup
    api_response = api_instance.user_lookup_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->user_lookup_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSearchRequest**](UserSearchRequest.md)| userLookupRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfUserLookupResponse**](SingleWrapperOfPageOfUserLookupResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_email_using_post**
> Wrapper verify_email_using_post(body, authorization, version)

verifyEmail

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.AdminApi()
body = dupr_backend.VerifyEmailRequest() # VerifyEmailRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # verifyEmail
    api_response = api_instance.verify_email_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AdminApi->verify_email_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**VerifyEmailRequest**](VerifyEmailRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

