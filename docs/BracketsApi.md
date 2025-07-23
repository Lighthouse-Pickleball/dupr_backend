# dupr_backend.BracketsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_match_score**](BracketsApi.md#add_match_score) | **POST** /brackets/match/{version}/save | 
[**add_match_score_by_director**](BracketsApi.md#add_match_score_by_director) | **POST** /brackets/director/match/{version}/save | 
[**confirm_match1**](BracketsApi.md#confirm_match1) | **POST** /brackets/match/{version}/confirm | 
[**confirm_match_director**](BracketsApi.md#confirm_match_director) | **POST** /brackets/director/match/{version}/confirm | 
[**confirm_team_by_director**](BracketsApi.md#confirm_team_by_director) | **POST** /brackets/director/teams/{version}/confirm | 
[**delete_league1**](BracketsApi.md#delete_league1) | **DELETE** /brackets/{version}/{leagueId}/{bracketId} | 
[**edit_bracket**](BracketsApi.md#edit_bracket) | **PUT** /brackets/{version}/edit | 
[**edit_bracket_status**](BracketsApi.md#edit_bracket_status) | **PUT** /brackets/director/{version}/edit/bracket_status | 
[**edit_confirmed_matches**](BracketsApi.md#edit_confirmed_matches) | **POST** /brackets/director/confirm/match/{version}/edit | 
[**edit_match_score**](BracketsApi.md#edit_match_score) | **POST** /brackets/match/{version}/edit | 
[**edit_match_score_by_director**](BracketsApi.md#edit_match_score_by_director) | **POST** /brackets/director/match/{version}/edit | 
[**edit_partner**](BracketsApi.md#edit_partner) | **POST** /brackets/partner/{version}/edit | 
[**edit_player_wait_list**](BracketsApi.md#edit_player_wait_list) | **POST** /brackets/director/waitlist/{version}/edit | 
[**edit_teams**](BracketsApi.md#edit_teams) | **POST** /brackets/director/{bracketId}/teams/{version}/edit | 
[**end_league1**](BracketsApi.md#end_league1) | **GET** /brackets/{leagueId}/{bracketId}/{version}/end | 
[**export_bracket_participants**](BracketsApi.md#export_bracket_participants) | **GET** /brackets/director/{bracketId}/participant/{version}/export | 
[**forfeit_match**](BracketsApi.md#forfeit_match) | **POST** /brackets/director/match/{version}/forfeit | 
[**get_all_bracket_matches**](BracketsApi.md#get_all_bracket_matches) | **GET** /brackets/{bracketId}/match/{version}/all | 
[**get_all_event_players1**](BracketsApi.md#get_all_event_players1) | **POST** /brackets/director/participant/{version}/all | 
[**get_bracket_by_id**](BracketsApi.md#get_bracket_by_id) | **GET** /brackets/{version}/{bracketId} | 
[**get_bracket_details_teams**](BracketsApi.md#get_bracket_details_teams) | **GET** /brackets/{bracketId}/{version}/read | 
[**get_bracket_match_queue**](BracketsApi.md#get_bracket_match_queue) | **GET** /brackets/{bracketId}/queue/{version}/all | 
[**get_bracket_matches**](BracketsApi.md#get_bracket_matches) | **GET** /brackets/match/{version}/history | 
[**get_bracket_matches_post**](BracketsApi.md#get_bracket_matches_post) | **POST** /brackets/match/{version}/history | 
[**get_bracket_players**](BracketsApi.md#get_bracket_players) | **POST** /brackets/participant/{version}/all | 
[**get_bracket_players1**](BracketsApi.md#get_bracket_players1) | **GET** /brackets/{bracketId}/participant/{version}/all | 
[**get_bracket_standing**](BracketsApi.md#get_bracket_standing) | **GET** /brackets/{version}/standing | 
[**get_bracket_teams**](BracketsApi.md#get_bracket_teams) | **POST** /brackets/{version}/teams | 
[**get_bracket_teams1**](BracketsApi.md#get_bracket_teams1) | **GET** /brackets/{bracketId}/{version}/teams | 
[**get_bracket_waitlisted_teams**](BracketsApi.md#get_bracket_waitlisted_teams) | **POST** /brackets/{version}/waitlist/teams | 
[**get_director_bracket_teams**](BracketsApi.md#get_director_bracket_teams) | **GET** /brackets/director/{bracketId}/{version}/teams | 
[**get_pending_confirmation**](BracketsApi.md#get_pending_confirmation) | **GET** /brackets/teams/{version}/pending | 
[**get_pending_teams_to_replace**](BracketsApi.md#get_pending_teams_to_replace) | **GET** /brackets/{bracketId}/director/teams/pending/{version}/all | 
[**get_registration_details**](BracketsApi.md#get_registration_details) | **GET** /brackets/{bracketId}/participant/{version}/details | 
[**get_unmatched_players**](BracketsApi.md#get_unmatched_players) | **POST** /brackets/participant/unmatched/{version}/all | 
[**get_unmatched_players1**](BracketsApi.md#get_unmatched_players1) | **GET** /brackets/{bracketId}/participant/unmatched/{version}/all | 
[**get_user_brackets**](BracketsApi.md#get_user_brackets) | **GET** /brackets/{version}/all | 
[**get_user_club_role**](BracketsApi.md#get_user_club_role) | **POST** /brackets/club/roles/{version}/details | 
[**get_user_event_brackets**](BracketsApi.md#get_user_event_brackets) | **GET** /brackets/director/{leagueId}/{userId}/{version}/all | 
[**get_user_matches**](BracketsApi.md#get_user_matches) | **POST** /brackets/match/participant/{version}/history | 
[**get_valid_user_bracket_id**](BracketsApi.md#get_valid_user_bracket_id) | **GET** /brackets/valid/{version}/{leagueId} | 
[**get_waterfall_matches**](BracketsApi.md#get_waterfall_matches) | **GET** /brackets/match/{bracketId}/{version}/structure | 
[**player_withdraw**](BracketsApi.md#player_withdraw) | **POST** /brackets/player/{version}/withdraw | 
[**player_withdraw_by_director**](BracketsApi.md#player_withdraw_by_director) | **POST** /brackets/director/{version}/withdraw | 
[**process_refunds**](BracketsApi.md#process_refunds) | **POST** /brackets/director/{version}/refund | 
[**register_users_to_bracket**](BracketsApi.md#register_users_to_bracket) | **POST** /brackets/director/user/{version}/add | 
[**remove_match_from_queue**](BracketsApi.md#remove_match_from_queue) | **GET** /brackets/match/{leagueMatchId}/queue/{version}/remove | 
[**save_bracket**](BracketsApi.md#save_bracket) | **PUT** /brackets/{version}/save | 
[**save_match_seeding**](BracketsApi.md#save_match_seeding) | **POST** /brackets/{version}/seed | 
[**save_teams**](BracketsApi.md#save_teams) | **POST** /brackets/director/{bracketId}/teams/{version}/save | 
[**seed_matches**](BracketsApi.md#seed_matches) | **GET** /brackets/{version}/seed | 
[**substitute_players**](BracketsApi.md#substitute_players) | **POST** /brackets/director/participant/{version}/substitute | 
[**switch_player**](BracketsApi.md#switch_player) | **POST** /brackets/director/player/{version}/switch | 
[**switch_teams**](BracketsApi.md#switch_teams) | **POST** /brackets/director/team/{version}/switch | 
[**switch_wait_listed**](BracketsApi.md#switch_wait_listed) | **POST** /brackets/director/team/{version}/switchWaitlisted | 
[**switch_wait_listed_teams**](BracketsApi.md#switch_wait_listed_teams) | **POST** /brackets/director/teams/waitlist/{version}/update | 
[**update_bracket_approval**](BracketsApi.md#update_bracket_approval) | **GET** /brackets/approval/{version}/update | 


# **add_match_score**
> Wrapper add_match_score(version, league_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.league_match_request import LeagueMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_match_request = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | 

    try:
        api_response = api_instance.add_match_score(version, league_match_request)
        print("The response of BracketsApi->add_match_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->add_match_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_match_request** | [**LeagueMatchRequest**](LeagueMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_match_score_by_director**
> Wrapper add_match_score_by_director(version, league_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.league_match_request import LeagueMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_match_request = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | 

    try:
        api_response = api_instance.add_match_score_by_director(version, league_match_request)
        print("The response of BracketsApi->add_match_score_by_director:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->add_match_score_by_director: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_match_request** | [**LeagueMatchRequest**](LeagueMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_match1**
> Wrapper confirm_match1(version, league_match_confirm_request)

### Example


```python
import dupr_backend
from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_match_confirm_request = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | 

    try:
        api_response = api_instance.confirm_match1(version, league_match_confirm_request)
        print("The response of BracketsApi->confirm_match1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_match1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_match_confirm_request** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_match_director**
> Wrapper confirm_match_director(version, league_match_confirm_request)

### Example


```python
import dupr_backend
from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_match_confirm_request = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | 

    try:
        api_response = api_instance.confirm_match_director(version, league_match_confirm_request)
        print("The response of BracketsApi->confirm_match_director:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_match_director: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_match_confirm_request** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **confirm_team_by_director**
> Wrapper confirm_team_by_director(version, confirm_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.confirm_team_request import ConfirmTeamRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    confirm_team_request = dupr_backend.ConfirmTeamRequest() # ConfirmTeamRequest | 

    try:
        api_response = api_instance.confirm_team_by_director(version, confirm_team_request)
        print("The response of BracketsApi->confirm_team_by_director:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_team_by_director: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **confirm_team_request** | [**ConfirmTeamRequest**](ConfirmTeamRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_league1**
> Wrapper delete_league1(version, league_id, bracket_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.delete_league1(version, league_id, bracket_id)
        print("The response of BracketsApi->delete_league1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->delete_league1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 
 **bracket_id** | **int**|  | 

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

# **edit_bracket**
> SingleWrapperLeagueResponse edit_bracket(version, edit_bracket_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_bracket_request import EditBracketRequest
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_bracket_request = dupr_backend.EditBracketRequest() # EditBracketRequest | 

    try:
        api_response = api_instance.edit_bracket(version, edit_bracket_request)
        print("The response of BracketsApi->edit_bracket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_bracket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_bracket_request** | [**EditBracketRequest**](EditBracketRequest.md)|  | 

### Return type

[**SingleWrapperLeagueResponse**](SingleWrapperLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bracket_status**
> SingleWrapperUnit edit_bracket_status(version, league_id, bracket_id, status, club_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 
    bracket_id = 56 # int | 
    status = 'status_example' # str | 
    club_id = 56 # int | 

    try:
        api_response = api_instance.edit_bracket_status(version, league_id, bracket_id, status, club_id)
        print("The response of BracketsApi->edit_bracket_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_bracket_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 
 **bracket_id** | **int**|  | 
 **status** | **str**|  | 
 **club_id** | **int**|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_confirmed_matches**
> Wrapper edit_confirmed_matches(version, edit_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_match_request = dupr_backend.EditMatchRequest() # EditMatchRequest | 

    try:
        api_response = api_instance.edit_confirmed_matches(version, edit_match_request)
        print("The response of BracketsApi->edit_confirmed_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_confirmed_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_match_request** | [**EditMatchRequest**](EditMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_match_score**
> Wrapper edit_match_score(version, edit_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_match_request = dupr_backend.EditMatchRequest() # EditMatchRequest | 

    try:
        api_response = api_instance.edit_match_score(version, edit_match_request)
        print("The response of BracketsApi->edit_match_score:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_match_score: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_match_request** | [**EditMatchRequest**](EditMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_match_score_by_director**
> Wrapper edit_match_score_by_director(version, edit_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_match_request = dupr_backend.EditMatchRequest() # EditMatchRequest | 

    try:
        api_response = api_instance.edit_match_score_by_director(version, edit_match_request)
        print("The response of BracketsApi->edit_match_score_by_director:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_match_score_by_director: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_match_request** | [**EditMatchRequest**](EditMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_partner**
> Wrapper edit_partner(version, edit_partner_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_partner_request import EditPartnerRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_partner_request = dupr_backend.EditPartnerRequest() # EditPartnerRequest | 

    try:
        api_response = api_instance.edit_partner(version, edit_partner_request)
        print("The response of BracketsApi->edit_partner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_partner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_partner_request** | [**EditPartnerRequest**](EditPartnerRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_player_wait_list**
> Wrapper edit_player_wait_list(version, edit_wait_list_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_wait_list_request import EditWaitListRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    edit_wait_list_request = [dupr_backend.EditWaitListRequest()] # List[EditWaitListRequest] | 

    try:
        api_response = api_instance.edit_player_wait_list(version, edit_wait_list_request)
        print("The response of BracketsApi->edit_player_wait_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_player_wait_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **edit_wait_list_request** | [**List[EditWaitListRequest]**](EditWaitListRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_teams**
> Wrapper edit_teams(bracket_id, version, edit_event_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.edit_event_team_request import EditEventTeamRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    bracket_id = 56 # int | 
    version = 'version_example' # str | 
    edit_event_team_request = dupr_backend.EditEventTeamRequest() # EditEventTeamRequest | 

    try:
        api_response = api_instance.edit_teams(bracket_id, version, edit_event_team_request)
        print("The response of BracketsApi->edit_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bracket_id** | **int**|  | 
 **version** | **str**|  | 
 **edit_event_team_request** | [**EditEventTeamRequest**](EditEventTeamRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **end_league1**
> Wrapper end_league1(version, league_id, bracket_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.end_league1(version, league_id, bracket_id)
        print("The response of BracketsApi->end_league1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->end_league1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 
 **bracket_id** | **int**|  | 

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

# **export_bracket_participants**
> SingleWrapperDownloadS3Response export_bracket_participants(version, bracket_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.export_bracket_participants(version, bracket_id)
        print("The response of BracketsApi->export_bracket_participants:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->export_bracket_participants: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**SingleWrapperDownloadS3Response**](SingleWrapperDownloadS3Response.md)

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

# **forfeit_match**
> Wrapper forfeit_match(version, forfeit_match_request)

### Example


```python
import dupr_backend
from dupr_backend.models.forfeit_match_request import ForfeitMatchRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    forfeit_match_request = dupr_backend.ForfeitMatchRequest() # ForfeitMatchRequest | 

    try:
        api_response = api_instance.forfeit_match(version, forfeit_match_request)
        print("The response of BracketsApi->forfeit_match:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->forfeit_match: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **forfeit_match_request** | [**ForfeitMatchRequest**](ForfeitMatchRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_bracket_matches**
> ArrayWrapperLeagueMatchResponse get_all_bracket_matches(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_league_match_response import ArrayWrapperLeagueMatchResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_all_bracket_matches(version, bracket_id)
        print("The response of BracketsApi->get_all_bracket_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_all_bracket_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**ArrayWrapperLeagueMatchResponse**](ArrayWrapperLeagueMatchResponse.md)

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

# **get_all_event_players1**
> SingleWrapperPagePlayerPaymentResponse get_all_event_players1(version, offset, limit, search_league_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_page_player_payment_response import SingleWrapperPagePlayerPaymentResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | 

    try:
        api_response = api_instance.get_all_event_players1(version, offset, limit, search_league_player_request)
        print("The response of BracketsApi->get_all_event_players1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_all_event_players1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerPaymentResponse**](SingleWrapperPagePlayerPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_by_id**
> SingleWrapperBracketResponse get_bracket_by_id(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_bracket_response import SingleWrapperBracketResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_bracket_by_id(version, bracket_id)
        print("The response of BracketsApi->get_bracket_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**SingleWrapperBracketResponse**](SingleWrapperBracketResponse.md)

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

# **get_bracket_details_teams**
> SingleWrapperBracketDetailsResponse get_bracket_details_teams(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_bracket_details_response import SingleWrapperBracketDetailsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_bracket_details_teams(version, bracket_id)
        print("The response of BracketsApi->get_bracket_details_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_details_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**SingleWrapperBracketDetailsResponse**](SingleWrapperBracketDetailsResponse.md)

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

# **get_bracket_match_queue**
> SingleWrapperPageLeagueMatchResponse get_bracket_match_queue(version, bracket_id, offset=offset, limit=limit)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_match_response import SingleWrapperPageLeagueMatchResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        api_response = api_instance.get_bracket_match_queue(version, bracket_id, offset=offset, limit=limit)
        print("The response of BracketsApi->get_bracket_match_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_match_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**SingleWrapperPageLeagueMatchResponse**](SingleWrapperPageLeagueMatchResponse.md)

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

# **get_bracket_matches**
> SingleWrapperPageLeagueMatchResponse get_bracket_matches(version, bracket_id, round=round, offset=offset, limit=limit, tags=tags)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_match_response import SingleWrapperPageLeagueMatchResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    round = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)
    tags = '10' # str |  (optional) (default to '10')

    try:
        api_response = api_instance.get_bracket_matches(version, bracket_id, round=round, offset=offset, limit=limit, tags=tags)
        print("The response of BracketsApi->get_bracket_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **round** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]
 **tags** | **str**|  | [optional] [default to &#39;10&#39;]

### Return type

[**SingleWrapperPageLeagueMatchResponse**](SingleWrapperPageLeagueMatchResponse.md)

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

# **get_bracket_matches_post**
> SingleWrapperPageLeagueMatchResponse get_bracket_matches_post(version, bracket_id, bracket_match_request, round=round, offset=offset, limit=limit)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_match_request import BracketMatchRequest
from dupr_backend.models.single_wrapper_page_league_match_response import SingleWrapperPageLeagueMatchResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    bracket_match_request = dupr_backend.BracketMatchRequest() # BracketMatchRequest | 
    round = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)
    limit = 10 # int |  (optional) (default to 10)

    try:
        api_response = api_instance.get_bracket_matches_post(version, bracket_id, bracket_match_request, round=round, offset=offset, limit=limit)
        print("The response of BracketsApi->get_bracket_matches_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_matches_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **bracket_match_request** | [**BracketMatchRequest**](BracketMatchRequest.md)|  | 
 **round** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**SingleWrapperPageLeagueMatchResponse**](SingleWrapperPageLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_players**
> SingleWrapperPagePlayerResponse get_bracket_players(version, offset, limit, search_league_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | 

    try:
        api_response = api_instance.get_bracket_players(version, offset, limit, search_league_player_request)
        print("The response of BracketsApi->get_bracket_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_players1**
> SingleWrapperPagePlayerResponse get_bracket_players1(version, bracket_id, offset, limit, query=query)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.get_bracket_players1(version, bracket_id, offset, limit, query=query)
        print("The response of BracketsApi->get_bracket_players1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_players1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

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

# **get_bracket_standing**
> SingleWrapperPageLeagueStandingResponse get_bracket_standing(version, bracket_id, limit, round=round, offset=offset)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_standing_response import SingleWrapperPageLeagueStandingResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    limit = 56 # int | 
    round = 0 # int |  (optional) (default to 0)
    offset = 0 # int |  (optional) (default to 0)

    try:
        api_response = api_instance.get_bracket_standing(version, bracket_id, limit, round=round, offset=offset)
        print("The response of BracketsApi->get_bracket_standing:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_standing: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **limit** | **int**|  | 
 **round** | **int**|  | [optional] [default to 0]
 **offset** | **int**|  | [optional] [default to 0]

### Return type

[**SingleWrapperPageLeagueStandingResponse**](SingleWrapperPageLeagueStandingResponse.md)

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

# **get_bracket_teams**
> SingleWrapperPageLeagueTeamsResponse get_bracket_teams(version, format, bracket_search_teams_request)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_search_teams_request import BracketSearchTeamsRequest
from dupr_backend.models.single_wrapper_page_league_teams_response import SingleWrapperPageLeagueTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    format = 'format_example' # str | 
    bracket_search_teams_request = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | 

    try:
        api_response = api_instance.get_bracket_teams(version, format, bracket_search_teams_request)
        print("The response of BracketsApi->get_bracket_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **format** | **str**|  | 
 **bracket_search_teams_request** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueTeamsResponse**](SingleWrapperPageLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_teams1**
> SingleWrapperPageLeagueTeamsResponse get_bracket_teams1(version, bracket_id, offset, limit, format)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_teams_response import SingleWrapperPageLeagueTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 
    format = 'format_example' # str | 

    try:
        api_response = api_instance.get_bracket_teams1(version, bracket_id, offset, limit, format)
        print("The response of BracketsApi->get_bracket_teams1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_teams1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **format** | **str**|  | 

### Return type

[**SingleWrapperPageLeagueTeamsResponse**](SingleWrapperPageLeagueTeamsResponse.md)

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

# **get_bracket_waitlisted_teams**
> SingleWrapperPageLeagueTeamsResponse get_bracket_waitlisted_teams(version, format, bracket_search_teams_request)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_search_teams_request import BracketSearchTeamsRequest
from dupr_backend.models.single_wrapper_page_league_teams_response import SingleWrapperPageLeagueTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    format = 'format_example' # str | 
    bracket_search_teams_request = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | 

    try:
        api_response = api_instance.get_bracket_waitlisted_teams(version, format, bracket_search_teams_request)
        print("The response of BracketsApi->get_bracket_waitlisted_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_waitlisted_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **format** | **str**|  | 
 **bracket_search_teams_request** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueTeamsResponse**](SingleWrapperPageLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_director_bracket_teams**
> SingleWrapperPageLeagueTeamsResponse get_director_bracket_teams(version, bracket_id, offset, limit, format)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_teams_response import SingleWrapperPageLeagueTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 
    format = 'format_example' # str | 

    try:
        api_response = api_instance.get_director_bracket_teams(version, bracket_id, offset, limit, format)
        print("The response of BracketsApi->get_director_bracket_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_director_bracket_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **format** | **str**|  | 

### Return type

[**SingleWrapperPageLeagueTeamsResponse**](SingleWrapperPageLeagueTeamsResponse.md)

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

# **get_pending_confirmation**
> ArrayWrapperLeagueTeamsResponse get_pending_confirmation(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_league_teams_response import ArrayWrapperLeagueTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_pending_confirmation(version, bracket_id)
        print("The response of BracketsApi->get_pending_confirmation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_pending_confirmation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**ArrayWrapperLeagueTeamsResponse**](ArrayWrapperLeagueTeamsResponse.md)

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

# **get_pending_teams_to_replace**
> ArrayWrapperPendingTeamsResponse get_pending_teams_to_replace(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_pending_teams_response import ArrayWrapperPendingTeamsResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_pending_teams_to_replace(version, bracket_id)
        print("The response of BracketsApi->get_pending_teams_to_replace:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_pending_teams_to_replace: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**ArrayWrapperPendingTeamsResponse**](ArrayWrapperPendingTeamsResponse.md)

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

# **get_registration_details**
> SingleWrapperRegistrationResponse get_registration_details(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_registration_response import SingleWrapperRegistrationResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_registration_details(version, bracket_id)
        print("The response of BracketsApi->get_registration_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_registration_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**SingleWrapperRegistrationResponse**](SingleWrapperRegistrationResponse.md)

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

# **get_unmatched_players**
> SingleWrapperPagePlayerResponse get_unmatched_players(version, search_unmatched_players_request)

### Example


```python
import dupr_backend
from dupr_backend.models.search_unmatched_players_request import SearchUnmatchedPlayersRequest
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    search_unmatched_players_request = dupr_backend.SearchUnmatchedPlayersRequest() # SearchUnmatchedPlayersRequest | 

    try:
        api_response = api_instance.get_unmatched_players(version, search_unmatched_players_request)
        print("The response of BracketsApi->get_unmatched_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_unmatched_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **search_unmatched_players_request** | [**SearchUnmatchedPlayersRequest**](SearchUnmatchedPlayersRequest.md)|  | 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmatched_players1**
> SingleWrapperPagePlayerResponse get_unmatched_players1(version, bracket_id, offset, limit, query=query)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_player_response import SingleWrapperPagePlayerResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    offset = 56 # int | 
    limit = 56 # int | 
    query = 'query_example' # str |  (optional)

    try:
        api_response = api_instance.get_unmatched_players1(version, bracket_id, offset, limit, query=query)
        print("The response of BracketsApi->get_unmatched_players1:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_unmatched_players1: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **query** | **str**|  | [optional] 

### Return type

[**SingleWrapperPagePlayerResponse**](SingleWrapperPagePlayerResponse.md)

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

# **get_user_brackets**
> SingleWrapperPageBracketResponse get_user_brackets(version, offset, limit, status=status)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_bracket_response import SingleWrapperPageBracketResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    offset = 56 # int | 
    limit = 56 # int | 
    status = 'status_example' # str |  (optional)

    try:
        api_response = api_instance.get_user_brackets(version, offset, limit, status=status)
        print("The response of BracketsApi->get_user_brackets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_brackets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **offset** | **int**|  | 
 **limit** | **int**|  | 
 **status** | **str**|  | [optional] 

### Return type

[**SingleWrapperPageBracketResponse**](SingleWrapperPageBracketResponse.md)

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

# **get_user_club_role**
> SingleWrapperBracketClubRoleResponse get_user_club_role(version, user_club_role_request)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_bracket_club_role_response import SingleWrapperBracketClubRoleResponse
from dupr_backend.models.user_club_role_request import UserClubRoleRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    user_club_role_request = dupr_backend.UserClubRoleRequest() # UserClubRoleRequest | 

    try:
        api_response = api_instance.get_user_club_role(version, user_club_role_request)
        print("The response of BracketsApi->get_user_club_role:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_club_role: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **user_club_role_request** | [**UserClubRoleRequest**](UserClubRoleRequest.md)|  | 

### Return type

[**SingleWrapperBracketClubRoleResponse**](SingleWrapperBracketClubRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_event_brackets**
> ArrayWrapperBracketResponse get_user_event_brackets(version, league_id, user_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_bracket_response import ArrayWrapperBracketResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 
    user_id = 56 # int | 

    try:
        api_response = api_instance.get_user_event_brackets(version, league_id, user_id)
        print("The response of BracketsApi->get_user_event_brackets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_event_brackets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 
 **user_id** | **int**|  | 

### Return type

[**ArrayWrapperBracketResponse**](ArrayWrapperBracketResponse.md)

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

# **get_user_matches**
> SingleWrapperPageLeagueMatchResponse get_user_matches(version, user_matches_request)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_page_league_match_response import SingleWrapperPageLeagueMatchResponse
from dupr_backend.models.user_matches_request import UserMatchesRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    user_matches_request = dupr_backend.UserMatchesRequest() # UserMatchesRequest | 

    try:
        api_response = api_instance.get_user_matches(version, user_matches_request)
        print("The response of BracketsApi->get_user_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **user_matches_request** | [**UserMatchesRequest**](UserMatchesRequest.md)|  | 

### Return type

[**SingleWrapperPageLeagueMatchResponse**](SingleWrapperPageLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valid_user_bracket_id**
> ArrayWrapperBracketResponse get_valid_user_bracket_id(version, league_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_bracket_response import ArrayWrapperBracketResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_id = 56 # int | 

    try:
        api_response = api_instance.get_valid_user_bracket_id(version, league_id)
        print("The response of BracketsApi->get_valid_user_bracket_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_valid_user_bracket_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_id** | **int**|  | 

### Return type

[**ArrayWrapperBracketResponse**](ArrayWrapperBracketResponse.md)

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

# **get_waterfall_matches**
> ArrayWrapperLeagueMatchResponse get_waterfall_matches(version, bracket_id)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_league_match_response import ArrayWrapperLeagueMatchResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 

    try:
        api_response = api_instance.get_waterfall_matches(version, bracket_id)
        print("The response of BracketsApi->get_waterfall_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_waterfall_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 

### Return type

[**ArrayWrapperLeagueMatchResponse**](ArrayWrapperLeagueMatchResponse.md)

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

# **player_withdraw**
> Wrapper player_withdraw(version, withdraw_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.withdraw_player_request import WithdrawPlayerRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    withdraw_player_request = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | 

    try:
        api_response = api_instance.player_withdraw(version, withdraw_player_request)
        print("The response of BracketsApi->player_withdraw:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->player_withdraw: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **withdraw_player_request** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_withdraw_by_director**
> Wrapper player_withdraw_by_director(version, withdraw_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.withdraw_player_request import WithdrawPlayerRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    withdraw_player_request = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | 

    try:
        api_response = api_instance.player_withdraw_by_director(version, withdraw_player_request)
        print("The response of BracketsApi->player_withdraw_by_director:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->player_withdraw_by_director: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **withdraw_player_request** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_refunds**
> Wrapper process_refunds(version, event_refund_request)

### Example


```python
import dupr_backend
from dupr_backend.models.event_refund_request import EventRefundRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    event_refund_request = dupr_backend.EventRefundRequest() # EventRefundRequest | 

    try:
        api_response = api_instance.process_refunds(version, event_refund_request)
        print("The response of BracketsApi->process_refunds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->process_refunds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **event_refund_request** | [**EventRefundRequest**](EventRefundRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register_users_to_bracket**
> SingleWrapperJoinLeagueResponse register_users_to_bracket(version, register_to_bracket_request)

### Example


```python
import dupr_backend
from dupr_backend.models.register_to_bracket_request import RegisterToBracketRequest
from dupr_backend.models.single_wrapper_join_league_response import SingleWrapperJoinLeagueResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    register_to_bracket_request = dupr_backend.RegisterToBracketRequest() # RegisterToBracketRequest | 

    try:
        api_response = api_instance.register_users_to_bracket(version, register_to_bracket_request)
        print("The response of BracketsApi->register_users_to_bracket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->register_users_to_bracket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **register_to_bracket_request** | [**RegisterToBracketRequest**](RegisterToBracketRequest.md)|  | 

### Return type

[**SingleWrapperJoinLeagueResponse**](SingleWrapperJoinLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_match_from_queue**
> Wrapper remove_match_from_queue(version, league_match_id)

### Example


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


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    league_match_id = 56 # int | 

    try:
        api_response = api_instance.remove_match_from_queue(version, league_match_id)
        print("The response of BracketsApi->remove_match_from_queue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->remove_match_from_queue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **league_match_id** | **int**|  | 

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

# **save_bracket**
> SingleWrapperLeagueResponse save_bracket(version, bracket_request)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_request import BracketRequest
from dupr_backend.models.single_wrapper_league_response import SingleWrapperLeagueResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_request = dupr_backend.BracketRequest() # BracketRequest | 

    try:
        api_response = api_instance.save_bracket(version, bracket_request)
        print("The response of BracketsApi->save_bracket:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_bracket: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_request** | [**BracketRequest**](BracketRequest.md)|  | 

### Return type

[**SingleWrapperLeagueResponse**](SingleWrapperLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_seeding**
> Wrapper save_match_seeding(version, bracket_id, match_round)

### Example


```python
import dupr_backend
from dupr_backend.models.match_round import MatchRound
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    match_round = [dupr_backend.MatchRound()] # List[MatchRound] | 

    try:
        api_response = api_instance.save_match_seeding(version, bracket_id, match_round)
        print("The response of BracketsApi->save_match_seeding:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_match_seeding: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **match_round** | [**List[MatchRound]**](MatchRound.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_teams**
> Wrapper save_teams(bracket_id, version, create_new_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.create_new_team_request import CreateNewTeamRequest
from dupr_backend.models.wrapper import Wrapper
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    bracket_id = 56 # int | 
    version = 'version_example' # str | 
    create_new_team_request = dupr_backend.CreateNewTeamRequest() # CreateNewTeamRequest | 

    try:
        api_response = api_instance.save_teams(bracket_id, version, create_new_team_request)
        print("The response of BracketsApi->save_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bracket_id** | **int**|  | 
 **version** | **str**|  | 
 **create_new_team_request** | [**CreateNewTeamRequest**](CreateNewTeamRequest.md)|  | 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **seed_matches**
> ArrayWrapperMatchRound seed_matches(version, bracket_id, type=type)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_match_round import ArrayWrapperMatchRound
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_id = 56 # int | 
    type = 'ROUND_ROBIN' # str |  (optional) (default to 'ROUND_ROBIN')

    try:
        api_response = api_instance.seed_matches(version, bracket_id, type=type)
        print("The response of BracketsApi->seed_matches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->seed_matches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_id** | **int**|  | 
 **type** | **str**|  | [optional] [default to &#39;ROUND_ROBIN&#39;]

### Return type

[**ArrayWrapperMatchRound**](ArrayWrapperMatchRound.md)

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

# **substitute_players**
> SingleWrapperUnit substitute_players(version, substitute_player_request)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.models.substitute_player_request import SubstitutePlayerRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    substitute_player_request = [dupr_backend.SubstitutePlayerRequest()] # List[SubstitutePlayerRequest] | 

    try:
        api_response = api_instance.substitute_players(version, substitute_player_request)
        print("The response of BracketsApi->substitute_players:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->substitute_players: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **substitute_player_request** | [**List[SubstitutePlayerRequest]**](SubstitutePlayerRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_player**
> ArrayWrapperSwitchBracketResponse switch_player(version, switch_bracket_request)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_switch_bracket_response import ArrayWrapperSwitchBracketResponse
from dupr_backend.models.switch_bracket_request import SwitchBracketRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    switch_bracket_request = [dupr_backend.SwitchBracketRequest()] # List[SwitchBracketRequest] | 

    try:
        api_response = api_instance.switch_player(version, switch_bracket_request)
        print("The response of BracketsApi->switch_player:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_player: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **switch_bracket_request** | [**List[SwitchBracketRequest]**](SwitchBracketRequest.md)|  | 

### Return type

[**ArrayWrapperSwitchBracketResponse**](ArrayWrapperSwitchBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_teams**
> ArrayWrapperSwitchBracketResponse switch_teams(version, switch_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.array_wrapper_switch_bracket_response import ArrayWrapperSwitchBracketResponse
from dupr_backend.models.switch_team_request import SwitchTeamRequest
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    switch_team_request = [dupr_backend.SwitchTeamRequest()] # List[SwitchTeamRequest] | 

    try:
        api_response = api_instance.switch_teams(version, switch_team_request)
        print("The response of BracketsApi->switch_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **switch_team_request** | [**List[SwitchTeamRequest]**](SwitchTeamRequest.md)|  | 

### Return type

[**ArrayWrapperSwitchBracketResponse**](ArrayWrapperSwitchBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_wait_listed**
> SingleWrapperUnit switch_wait_listed(version, bracket_player_switch_wait_listed_request)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_player_switch_wait_listed_request import BracketPlayerSwitchWaitListedRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_player_switch_wait_listed_request = dupr_backend.BracketPlayerSwitchWaitListedRequest() # BracketPlayerSwitchWaitListedRequest | 

    try:
        api_response = api_instance.switch_wait_listed(version, bracket_player_switch_wait_listed_request)
        print("The response of BracketsApi->switch_wait_listed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_wait_listed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_player_switch_wait_listed_request** | [**BracketPlayerSwitchWaitListedRequest**](BracketPlayerSwitchWaitListedRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_wait_listed_teams**
> SingleWrapperUnit switch_wait_listed_teams(version, bracket_player_switch_wait_listed_request)

### Example


```python
import dupr_backend
from dupr_backend.models.bracket_player_switch_wait_listed_request import BracketPlayerSwitchWaitListedRequest
from dupr_backend.models.single_wrapper_unit import SingleWrapperUnit
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    bracket_player_switch_wait_listed_request = [dupr_backend.BracketPlayerSwitchWaitListedRequest()] # List[BracketPlayerSwitchWaitListedRequest] | 

    try:
        api_response = api_instance.switch_wait_listed_teams(version, bracket_player_switch_wait_listed_request)
        print("The response of BracketsApi->switch_wait_listed_teams:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_wait_listed_teams: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **bracket_player_switch_wait_listed_request** | [**List[BracketPlayerSwitchWaitListedRequest]**](BracketPlayerSwitchWaitListedRequest.md)|  | 

### Return type

[**SingleWrapperUnit**](SingleWrapperUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_bracket_approval**
> SingleWrapperSessionResponse update_bracket_approval(version, registration_id, bracket_id, status, is_club_member=is_club_member)

### Example


```python
import dupr_backend
from dupr_backend.models.single_wrapper_session_response import SingleWrapperSessionResponse
from dupr_backend.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.dupr.gg
# See configuration.py for a list of all supported configuration parameters.
configuration = dupr_backend.Configuration(
    host = "https://api.dupr.gg"
)


# Enter a context with an instance of the API client
with dupr_backend.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dupr_backend.BracketsApi(api_client)
    version = 'version_example' # str | 
    registration_id = 56 # int | 
    bracket_id = 56 # int | 
    status = 'status_example' # str | 
    is_club_member = True # bool |  (optional)

    try:
        api_response = api_instance.update_bracket_approval(version, registration_id, bracket_id, status, is_club_member=is_club_member)
        print("The response of BracketsApi->update_bracket_approval:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->update_bracket_approval: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **registration_id** | **int**|  | 
 **bracket_id** | **int**|  | 
 **status** | **str**|  | 
 **is_club_member** | **bool**|  | [optional] 

### Return type

[**SingleWrapperSessionResponse**](SingleWrapperSessionResponse.md)

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

