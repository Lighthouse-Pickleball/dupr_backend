# dupr_backend.BracketsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_match_score_by_director_using_post**](BracketsApi.md#add_match_score_by_director_using_post) | **POST** /brackets/director/match/{version}/save | addMatchScoreByDirector
[**add_match_score_using_post**](BracketsApi.md#add_match_score_using_post) | **POST** /brackets/match/{version}/save | addMatchScore
[**confirm_match_director_using_post**](BracketsApi.md#confirm_match_director_using_post) | **POST** /brackets/director/match/{version}/confirm | confirmMatchDirector
[**confirm_match_using_post**](BracketsApi.md#confirm_match_using_post) | **POST** /brackets/match/{version}/confirm | confirmMatch
[**confirm_team_by_director_using_post**](BracketsApi.md#confirm_team_by_director_using_post) | **POST** /brackets/director/teams/{version}/confirm | confirmTeamByDirector
[**delete_league_using_delete**](BracketsApi.md#delete_league_using_delete) | **DELETE** /brackets/{version}/{leagueId}/{bracketId} | deleteLeague
[**edit_bracket_status_using_put**](BracketsApi.md#edit_bracket_status_using_put) | **PUT** /brackets/director/{version}/edit/bracket_status | editBracketStatus
[**edit_bracket_using_put**](BracketsApi.md#edit_bracket_using_put) | **PUT** /brackets/{version}/edit | editBracket
[**edit_confirmed_matches_using_post**](BracketsApi.md#edit_confirmed_matches_using_post) | **POST** /brackets/director/confirm/match/{version}/edit | editConfirmedMatches
[**edit_match_score_by_director_using_post**](BracketsApi.md#edit_match_score_by_director_using_post) | **POST** /brackets/director/match/{version}/edit | editMatchScoreByDirector
[**edit_match_score_using_post**](BracketsApi.md#edit_match_score_using_post) | **POST** /brackets/match/{version}/edit | editMatchScore
[**edit_partner_using_post**](BracketsApi.md#edit_partner_using_post) | **POST** /brackets/partner/{version}/edit | editPartner
[**edit_player_wait_list_using_post**](BracketsApi.md#edit_player_wait_list_using_post) | **POST** /brackets/director/waitlist/{version}/edit | editPlayerWaitList
[**edit_teams_using_post**](BracketsApi.md#edit_teams_using_post) | **POST** /brackets/director/{bracketId}/teams/{version}/edit | editTeams
[**end_league_using_get**](BracketsApi.md#end_league_using_get) | **GET** /brackets/{leagueId}/{bracketId}/{version}/end | endLeague
[**export_bracket_participants_using_get**](BracketsApi.md#export_bracket_participants_using_get) | **GET** /brackets/director/{bracketId}/participant/{version}/export | exportBracketParticipants
[**forfeit_match_using_post**](BracketsApi.md#forfeit_match_using_post) | **POST** /brackets/director/match/{version}/forfeit | forfeitMatch
[**get_all_bracket_matches_using_get**](BracketsApi.md#get_all_bracket_matches_using_get) | **GET** /brackets/{bracketId}/match/{version}/all | getAllBracketMatches
[**get_all_event_players_using_post**](BracketsApi.md#get_all_event_players_using_post) | **POST** /brackets/director/participant/{version}/all | getAllEventPlayers
[**get_bracket_by_id_using_get**](BracketsApi.md#get_bracket_by_id_using_get) | **GET** /brackets/{version}/{bracketId} | getBracketById
[**get_bracket_details_teams_using_get**](BracketsApi.md#get_bracket_details_teams_using_get) | **GET** /brackets/{bracketId}/{version}/read | getBracketDetailsTeams
[**get_bracket_match_queue_using_get**](BracketsApi.md#get_bracket_match_queue_using_get) | **GET** /brackets/{bracketId}/queue/{version}/all | getBracketMatchQueue
[**get_bracket_matches_post_using_post**](BracketsApi.md#get_bracket_matches_post_using_post) | **POST** /brackets/match/{version}/history | getBracketMatchesPost
[**get_bracket_matches_using_get**](BracketsApi.md#get_bracket_matches_using_get) | **GET** /brackets/match/{version}/history | getBracketMatches
[**get_bracket_players_using_get**](BracketsApi.md#get_bracket_players_using_get) | **GET** /brackets/{bracketId}/participant/{version}/all | getBracketPlayers
[**get_bracket_players_using_post**](BracketsApi.md#get_bracket_players_using_post) | **POST** /brackets/participant/{version}/all | getBracketPlayers
[**get_bracket_standing_using_get**](BracketsApi.md#get_bracket_standing_using_get) | **GET** /brackets/{version}/standing | getBracketStanding
[**get_bracket_teams_using_get**](BracketsApi.md#get_bracket_teams_using_get) | **GET** /brackets/{bracketId}/{version}/teams | getBracketTeams
[**get_bracket_teams_using_post**](BracketsApi.md#get_bracket_teams_using_post) | **POST** /brackets/{version}/teams | getBracketTeams
[**get_bracket_waitlisted_teams_using_post**](BracketsApi.md#get_bracket_waitlisted_teams_using_post) | **POST** /brackets/{version}/waitlist/teams | getBracketWaitlistedTeams
[**get_director_bracket_teams_using_get**](BracketsApi.md#get_director_bracket_teams_using_get) | **GET** /brackets/director/{bracketId}/{version}/teams | getDirectorBracketTeams
[**get_pending_confirmation_using_get**](BracketsApi.md#get_pending_confirmation_using_get) | **GET** /brackets/teams/{version}/pending | getPendingConfirmation
[**get_pending_teams_to_replace_using_get**](BracketsApi.md#get_pending_teams_to_replace_using_get) | **GET** /brackets/{bracketId}/director/teams/pending/{version}/all | getPendingTeamsToReplace
[**get_registration_details_using_get**](BracketsApi.md#get_registration_details_using_get) | **GET** /brackets/{bracketId}/participant/{version}/details | getRegistrationDetails
[**get_unmatched_players_using_get**](BracketsApi.md#get_unmatched_players_using_get) | **GET** /brackets/{bracketId}/participant/unmatched/{version}/all | getUnmatchedPlayers
[**get_unmatched_players_using_post**](BracketsApi.md#get_unmatched_players_using_post) | **POST** /brackets/participant/unmatched/{version}/all | getUnmatchedPlayers
[**get_user_brackets_using_get**](BracketsApi.md#get_user_brackets_using_get) | **GET** /brackets/{version}/all | getUserBrackets
[**get_user_club_role_using_post**](BracketsApi.md#get_user_club_role_using_post) | **POST** /brackets/club/roles/{version}/details | getUserClubRole
[**get_user_event_brackets_using_get**](BracketsApi.md#get_user_event_brackets_using_get) | **GET** /brackets/director/{leagueId}/{userId}/{version}/all | getUserEventBrackets
[**get_user_matches_using_post**](BracketsApi.md#get_user_matches_using_post) | **POST** /brackets/match/participant/{version}/history | getUserMatches
[**get_valid_user_bracket_id_using_get**](BracketsApi.md#get_valid_user_bracket_id_using_get) | **GET** /brackets/valid/{version}/{leagueId} | getValidUserBracketId
[**get_waterfall_matches_using_get**](BracketsApi.md#get_waterfall_matches_using_get) | **GET** /brackets/match/{bracketId}/{version}/structure | getWaterfallMatches
[**player_withdraw_by_director_using_post**](BracketsApi.md#player_withdraw_by_director_using_post) | **POST** /brackets/director/{version}/withdraw | playerWithdrawByDirector
[**player_withdraw_using_post**](BracketsApi.md#player_withdraw_using_post) | **POST** /brackets/player/{version}/withdraw | playerWithdraw
[**process_refunds_using_post**](BracketsApi.md#process_refunds_using_post) | **POST** /brackets/director/{version}/refund | processRefunds
[**register_users_to_bracket_using_post**](BracketsApi.md#register_users_to_bracket_using_post) | **POST** /brackets/director/user/{version}/add | registerUsersToBracket
[**remove_match_from_queue_using_get**](BracketsApi.md#remove_match_from_queue_using_get) | **GET** /brackets/match/{leagueMatchId}/queue/{version}/remove | removeMatchFromQueue
[**save_bracket_using_put**](BracketsApi.md#save_bracket_using_put) | **PUT** /brackets/{version}/save | saveBracket
[**save_match_seeding_using_post**](BracketsApi.md#save_match_seeding_using_post) | **POST** /brackets/{version}/seed | saveMatchSeeding
[**save_teams_using_post**](BracketsApi.md#save_teams_using_post) | **POST** /brackets/director/{bracketId}/teams/{version}/save | saveTeams
[**seed_matches_using_get**](BracketsApi.md#seed_matches_using_get) | **GET** /brackets/{version}/seed | seedMatches
[**substitute_players_using_post**](BracketsApi.md#substitute_players_using_post) | **POST** /brackets/director/participant/{version}/substitute | substitutePlayers
[**switch_player_using_post**](BracketsApi.md#switch_player_using_post) | **POST** /brackets/director/player/{version}/switch | switchPlayer
[**switch_teams_using_post**](BracketsApi.md#switch_teams_using_post) | **POST** /brackets/director/team/{version}/switch | switchTeams
[**switch_wait_listed_teams_using_post**](BracketsApi.md#switch_wait_listed_teams_using_post) | **POST** /brackets/director/teams/waitlist/{version}/update | switchWaitListedTeams
[**switch_wait_listed_using_post**](BracketsApi.md#switch_wait_listed_using_post) | **POST** /brackets/director/team/{version}/switchWaitlisted | switchWaitListed
[**update_bracket_approval_using_get**](BracketsApi.md#update_bracket_approval_using_get) | **GET** /brackets/approval/{version}/update | updateBracketApproval


# **add_match_score_by_director_using_post**
> Wrapper add_match_score_by_director_using_post(authorization, version, request)

addMatchScoreByDirector

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.league_match_request import LeagueMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | request

    try:
        # addMatchScoreByDirector
        api_response = api_instance.add_match_score_by_director_using_post(authorization, version, request)
        print("The response of BracketsApi->add_match_score_by_director_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->add_match_score_by_director_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueMatchRequest**](LeagueMatchRequest.md)| request | 

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

# **add_match_score_using_post**
> Wrapper add_match_score_using_post(authorization, version, request)

addMatchScore

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.league_match_request import LeagueMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | request

    try:
        # addMatchScore
        api_response = api_instance.add_match_score_using_post(authorization, version, request)
        print("The response of BracketsApi->add_match_score_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->add_match_score_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueMatchRequest**](LeagueMatchRequest.md)| request | 

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

# **confirm_match_director_using_post**
> Wrapper confirm_match_director_using_post(authorization, version, request)

confirmMatchDirector

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | request

    try:
        # confirmMatchDirector
        api_response = api_instance.confirm_match_director_using_post(authorization, version, request)
        print("The response of BracketsApi->confirm_match_director_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_match_director_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)| request | 

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

# **confirm_match_using_post**
> Wrapper confirm_match_using_post(authorization, version, request)

confirmMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.league_match_confirm_request import LeagueMatchConfirmRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | request

    try:
        # confirmMatch
        api_response = api_instance.confirm_match_using_post(authorization, version, request)
        print("The response of BracketsApi->confirm_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_match_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)| request | 

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

# **confirm_team_by_director_using_post**
> Wrapper confirm_team_by_director_using_post(authorization, version, confirm_team_request)

confirmTeamByDirector

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.confirm_team_request import ConfirmTeamRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    confirm_team_request = dupr_backend.ConfirmTeamRequest() # ConfirmTeamRequest | confirmTeamRequest

    try:
        # confirmTeamByDirector
        api_response = api_instance.confirm_team_by_director_using_post(authorization, version, confirm_team_request)
        print("The response of BracketsApi->confirm_team_by_director_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->confirm_team_by_director_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **confirm_team_request** | [**ConfirmTeamRequest**](ConfirmTeamRequest.md)| confirmTeamRequest | 

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

# **delete_league_using_delete**
> Wrapper delete_league_using_delete(authorization, bracket_id, league_id, version)

deleteLeague

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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # deleteLeague
        api_response = api_instance.delete_league_using_delete(authorization, bracket_id, league_id, version)
        print("The response of BracketsApi->delete_league_using_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->delete_league_using_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **league_id** | **int**| leagueId | 
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

# **edit_bracket_status_using_put**
> SingleWrapperOfUnit edit_bracket_status_using_put(authorization, bracket_id, club_id, league_id, status, version)

editBracketStatus

### Example

```python
import time
import os
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    club_id = 56 # int | clubId
    league_id = 56 # int | leagueId
    status = 'status_example' # str | status
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # editBracketStatus
        api_response = api_instance.edit_bracket_status_using_put(authorization, bracket_id, club_id, league_id, status, version)
        print("The response of BracketsApi->edit_bracket_status_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_bracket_status_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **club_id** | **int**| clubId | 
 **league_id** | **int**| leagueId | 
 **status** | **str**| status | 
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

# **edit_bracket_using_put**
> SingleWrapperOfLeagueResponse edit_bracket_using_put(authorization, version, request)

editBracket

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_bracket_request import EditBracketRequest
from dupr_backend.models.single_wrapper_of_league_response import SingleWrapperOfLeagueResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EditBracketRequest() # EditBracketRequest | request

    try:
        # editBracket
        api_response = api_instance.edit_bracket_using_put(authorization, version, request)
        print("The response of BracketsApi->edit_bracket_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_bracket_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EditBracketRequest**](EditBracketRequest.md)| request | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

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

# **edit_confirmed_matches_using_post**
> Wrapper edit_confirmed_matches_using_post(authorization, version, edit_match_request)

editConfirmedMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    edit_match_request = dupr_backend.EditMatchRequest() # EditMatchRequest | editMatchRequest

    try:
        # editConfirmedMatches
        api_response = api_instance.edit_confirmed_matches_using_post(authorization, version, edit_match_request)
        print("The response of BracketsApi->edit_confirmed_matches_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_confirmed_matches_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **edit_match_request** | [**EditMatchRequest**](EditMatchRequest.md)| editMatchRequest | 

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

# **edit_match_score_by_director_using_post**
> Wrapper edit_match_score_by_director_using_post(authorization, version, request)

editMatchScoreByDirector

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EditMatchRequest() # EditMatchRequest | request

    try:
        # editMatchScoreByDirector
        api_response = api_instance.edit_match_score_by_director_using_post(authorization, version, request)
        print("The response of BracketsApi->edit_match_score_by_director_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_match_score_by_director_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EditMatchRequest**](EditMatchRequest.md)| request | 

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

# **edit_match_score_using_post**
> Wrapper edit_match_score_using_post(authorization, version, request)

editMatchScore

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_match_request import EditMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EditMatchRequest() # EditMatchRequest | request

    try:
        # editMatchScore
        api_response = api_instance.edit_match_score_using_post(authorization, version, request)
        print("The response of BracketsApi->edit_match_score_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_match_score_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EditMatchRequest**](EditMatchRequest.md)| request | 

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

# **edit_partner_using_post**
> Wrapper edit_partner_using_post(authorization, version, request)

editPartner

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_partner_request import EditPartnerRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EditPartnerRequest() # EditPartnerRequest | request

    try:
        # editPartner
        api_response = api_instance.edit_partner_using_post(authorization, version, request)
        print("The response of BracketsApi->edit_partner_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_partner_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EditPartnerRequest**](EditPartnerRequest.md)| request | 

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

# **edit_player_wait_list_using_post**
> Wrapper edit_player_wait_list_using_post(authorization, version, edit_wait_list_request)

editPlayerWaitList

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_wait_list_request import EditWaitListRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    edit_wait_list_request = [dupr_backend.EditWaitListRequest()] # List[EditWaitListRequest] | editWaitListRequest

    try:
        # editPlayerWaitList
        api_response = api_instance.edit_player_wait_list_using_post(authorization, version, edit_wait_list_request)
        print("The response of BracketsApi->edit_player_wait_list_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_player_wait_list_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **edit_wait_list_request** | [**List[EditWaitListRequest]**](EditWaitListRequest.md)| editWaitListRequest | 

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

# **edit_teams_using_post**
> Wrapper edit_teams_using_post(authorization, version, edit_event_team_request)

editTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.edit_event_team_request import EditEventTeamRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    edit_event_team_request = dupr_backend.EditEventTeamRequest() # EditEventTeamRequest | editEventTeamRequest

    try:
        # editTeams
        api_response = api_instance.edit_teams_using_post(authorization, version, edit_event_team_request)
        print("The response of BracketsApi->edit_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->edit_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **edit_event_team_request** | [**EditEventTeamRequest**](EditEventTeamRequest.md)| editEventTeamRequest | 

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

# **end_league_using_get**
> Wrapper end_league_using_get(authorization, bracket_id, league_id, version)

endLeague

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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # endLeague
        api_response = api_instance.end_league_using_get(authorization, bracket_id, league_id, version)
        print("The response of BracketsApi->end_league_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->end_league_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **league_id** | **int**| leagueId | 
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

# **export_bracket_participants_using_get**
> SingleWrapperOfDownloadS3Response export_bracket_participants_using_get(authorization, bracket_id, version)

exportBracketParticipants

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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # exportBracketParticipants
        api_response = api_instance.export_bracket_participants_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->export_bracket_participants_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->export_bracket_participants_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
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

# **forfeit_match_using_post**
> Wrapper forfeit_match_using_post(authorization, version, request)

forfeitMatch

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.forfeit_match_request import ForfeitMatchRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.ForfeitMatchRequest() # ForfeitMatchRequest | request

    try:
        # forfeitMatch
        api_response = api_instance.forfeit_match_using_post(authorization, version, request)
        print("The response of BracketsApi->forfeit_match_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->forfeit_match_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**ForfeitMatchRequest**](ForfeitMatchRequest.md)| request | 

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

# **get_all_bracket_matches_using_get**
> ArrayWrapperOfLeagueMatchResponse get_all_bracket_matches_using_get(authorization, bracket_id, version)

getAllBracketMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_league_match_response import ArrayWrapperOfLeagueMatchResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getAllBracketMatches
        api_response = api_instance.get_all_bracket_matches_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_all_bracket_matches_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_all_bracket_matches_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfLeagueMatchResponse**](ArrayWrapperOfLeagueMatchResponse.md)

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

# **get_all_event_players_using_post**
> SingleWrapperOfPageOfPlayerPaymentResponse get_all_event_players_using_post(authorization, limit, offset, version, search_league_player_request)

getAllEventPlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_of_page_of_player_payment_response import SingleWrapperOfPageOfPlayerPaymentResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest

    try:
        # getAllEventPlayers
        api_response = api_instance.get_all_event_players_using_post(authorization, limit, offset, version, search_league_player_request)
        print("The response of BracketsApi->get_all_event_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_all_event_players_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 

### Return type

[**SingleWrapperOfPageOfPlayerPaymentResponse**](SingleWrapperOfPageOfPlayerPaymentResponse.md)

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

# **get_bracket_by_id_using_get**
> SingleWrapperOfBracketResponse get_bracket_by_id_using_get(bracket_id, version, authorization=authorization)

getBracketById

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_bracket_response import SingleWrapperOfBracketResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    authorization = 'Bearer ' # str |  (optional) (default to 'Bearer ')

    try:
        # getBracketById
        api_response = api_instance.get_bracket_by_id_using_get(bracket_id, version, authorization=authorization)
        print("The response of BracketsApi->get_bracket_by_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_by_id_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **authorization** | **str**|  | [optional] [default to &#39;Bearer &#39;]

### Return type

[**SingleWrapperOfBracketResponse**](SingleWrapperOfBracketResponse.md)

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

# **get_bracket_details_teams_using_get**
> SingleWrapperOfBracketDetailsResponse get_bracket_details_teams_using_get(authorization, bracket_id, version)

getBracketDetailsTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_bracket_details_response import SingleWrapperOfBracketDetailsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getBracketDetailsTeams
        api_response = api_instance.get_bracket_details_teams_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_bracket_details_teams_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_details_teams_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfBracketDetailsResponse**](SingleWrapperOfBracketDetailsResponse.md)

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

# **get_bracket_match_queue_using_get**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_match_queue_using_get(authorization, bracket_id, version, limit=limit, offset=offset)

getBracketMatchQueue

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_match_response import SingleWrapperOfPageOfLeagueMatchResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)

    try:
        # getBracketMatchQueue
        api_response = api_instance.get_bracket_match_queue_using_get(authorization, bracket_id, version, limit=limit, offset=offset)
        print("The response of BracketsApi->get_bracket_match_queue_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_match_queue_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

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

# **get_bracket_matches_post_using_post**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_matches_post_using_post(authorization, bracket_id, version, bracket_match_request, limit=limit, offset=offset, round=round)

getBracketMatchesPost

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_match_request import BracketMatchRequest
from dupr_backend.models.single_wrapper_of_page_of_league_match_response import SingleWrapperOfPageOfLeagueMatchResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    bracket_match_request = dupr_backend.BracketMatchRequest() # BracketMatchRequest | bracketMatchRequest
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)
    round = 0 # int | round (optional) (default to 0)

    try:
        # getBracketMatchesPost
        api_response = api_instance.get_bracket_matches_post_using_post(authorization, bracket_id, version, bracket_match_request, limit=limit, offset=offset, round=round)
        print("The response of BracketsApi->get_bracket_matches_post_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_matches_post_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **bracket_match_request** | [**BracketMatchRequest**](BracketMatchRequest.md)| bracketMatchRequest | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]
 **round** | **int**| round | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

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

# **get_bracket_matches_using_get**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_matches_using_get(authorization, bracket_id, version, limit=limit, offset=offset, round=round, tags=tags)

getBracketMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_match_response import SingleWrapperOfPageOfLeagueMatchResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    limit = 10 # int | limit (optional) (default to 10)
    offset = 0 # int | offset (optional) (default to 0)
    round = 0 # int | round (optional) (default to 0)
    tags = '10' # str | tags (optional) (default to '10')

    try:
        # getBracketMatches
        api_response = api_instance.get_bracket_matches_using_get(authorization, bracket_id, version, limit=limit, offset=offset, round=round, tags=tags)
        print("The response of BracketsApi->get_bracket_matches_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_matches_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]
 **round** | **int**| round | [optional] [default to 0]
 **tags** | **str**| tags | [optional] [default to &#39;10&#39;]

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

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

# **get_bracket_players_using_get**
> SingleWrapperOfPageOfPlayerResponse get_bracket_players_using_get(authorization, bracket_id, limit, offset, version, query=query)

getBracketPlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    query = 'query_example' # str | query (optional)

    try:
        # getBracketPlayers
        api_response = api_instance.get_bracket_players_using_get(authorization, bracket_id, limit, offset, version, query=query)
        print("The response of BracketsApi->get_bracket_players_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_players_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **query** | **str**| query | [optional] 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

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

# **get_bracket_players_using_post**
> SingleWrapperOfPageOfPlayerResponse get_bracket_players_using_post(authorization, limit, offset, version, search_league_player_request)

getBracketPlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.search_league_player_request import SearchLeaguePlayerRequest
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    search_league_player_request = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest

    try:
        # getBracketPlayers
        api_response = api_instance.get_bracket_players_using_post(authorization, limit, offset, version, search_league_player_request)
        print("The response of BracketsApi->get_bracket_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_players_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **search_league_player_request** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

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

# **get_bracket_standing_using_get**
> SingleWrapperOfPageOfLeagueStandingResponse get_bracket_standing_using_get(authorization, bracket_id, limit, version, offset=offset, round=round)

getBracketStanding

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_standing_response import SingleWrapperOfPageOfLeagueStandingResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    limit = 56 # int | limit
    version = 'v1.0' # str | version (default to 'v1.0')
    offset = 0 # int | offset (optional) (default to 0)
    round = 0 # int | round (optional) (default to 0)

    try:
        # getBracketStanding
        api_response = api_instance.get_bracket_standing_using_get(authorization, bracket_id, limit, version, offset=offset, round=round)
        print("The response of BracketsApi->get_bracket_standing_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_standing_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **offset** | **int**| offset | [optional] [default to 0]
 **round** | **int**| round | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfLeagueStandingResponse**](SingleWrapperOfPageOfLeagueStandingResponse.md)

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

# **get_bracket_teams_using_get**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)

getBracketTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_teams_response import SingleWrapperOfPageOfLeagueTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    format = 'format_example' # str | format
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getBracketTeams
        api_response = api_instance.get_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)
        print("The response of BracketsApi->get_bracket_teams_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_teams_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **format** | **str**| format | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

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

# **get_bracket_teams_using_post**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_teams_using_post(authorization, format, version, bracket_search_teams_request)

getBracketTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_search_teams_request import BracketSearchTeamsRequest
from dupr_backend.models.single_wrapper_of_page_of_league_teams_response import SingleWrapperOfPageOfLeagueTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    format = 'format_example' # str | format
    version = 'v1.0' # str | version (default to 'v1.0')
    bracket_search_teams_request = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | bracketSearchTeamsRequest

    try:
        # getBracketTeams
        api_response = api_instance.get_bracket_teams_using_post(authorization, format, version, bracket_search_teams_request)
        print("The response of BracketsApi->get_bracket_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **format** | **str**| format | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **bracket_search_teams_request** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)| bracketSearchTeamsRequest | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

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

# **get_bracket_waitlisted_teams_using_post**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_waitlisted_teams_using_post(authorization, format, version, bracket_search_teams_request)

getBracketWaitlistedTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_search_teams_request import BracketSearchTeamsRequest
from dupr_backend.models.single_wrapper_of_page_of_league_teams_response import SingleWrapperOfPageOfLeagueTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    format = 'format_example' # str | format
    version = 'v1.0' # str | version (default to 'v1.0')
    bracket_search_teams_request = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | bracketSearchTeamsRequest

    try:
        # getBracketWaitlistedTeams
        api_response = api_instance.get_bracket_waitlisted_teams_using_post(authorization, format, version, bracket_search_teams_request)
        print("The response of BracketsApi->get_bracket_waitlisted_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_bracket_waitlisted_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **format** | **str**| format | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **bracket_search_teams_request** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)| bracketSearchTeamsRequest | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

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

# **get_director_bracket_teams_using_get**
> SingleWrapperOfPageOfLeagueTeamsResponse get_director_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)

getDirectorBracketTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_teams_response import SingleWrapperOfPageOfLeagueTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    format = 'format_example' # str | format
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getDirectorBracketTeams
        api_response = api_instance.get_director_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)
        print("The response of BracketsApi->get_director_bracket_teams_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_director_bracket_teams_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **format** | **str**| format | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

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

# **get_pending_confirmation_using_get**
> ArrayWrapperOfLeagueTeamsResponse get_pending_confirmation_using_get(authorization, bracket_id, version)

getPendingConfirmation

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_league_teams_response import ArrayWrapperOfLeagueTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getPendingConfirmation
        api_response = api_instance.get_pending_confirmation_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_pending_confirmation_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_pending_confirmation_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfLeagueTeamsResponse**](ArrayWrapperOfLeagueTeamsResponse.md)

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

# **get_pending_teams_to_replace_using_get**
> ArrayWrapperOfPendingTeamsResponse get_pending_teams_to_replace_using_get(authorization, bracket_id, version)

getPendingTeamsToReplace

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_pending_teams_response import ArrayWrapperOfPendingTeamsResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getPendingTeamsToReplace
        api_response = api_instance.get_pending_teams_to_replace_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_pending_teams_to_replace_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_pending_teams_to_replace_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfPendingTeamsResponse**](ArrayWrapperOfPendingTeamsResponse.md)

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

# **get_registration_details_using_get**
> SingleWrapperOfRegistrationResponse get_registration_details_using_get(authorization, bracket_id, version)

getRegistrationDetails

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_registration_response import SingleWrapperOfRegistrationResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getRegistrationDetails
        api_response = api_instance.get_registration_details_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_registration_details_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_registration_details_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**SingleWrapperOfRegistrationResponse**](SingleWrapperOfRegistrationResponse.md)

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

# **get_unmatched_players_using_get**
> SingleWrapperOfPageOfPlayerResponse get_unmatched_players_using_get(authorization, bracket_id, limit, offset, version, query=query)

getUnmatchedPlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    query = 'query_example' # str | query (optional)

    try:
        # getUnmatchedPlayers
        api_response = api_instance.get_unmatched_players_using_get(authorization, bracket_id, limit, offset, version, query=query)
        print("The response of BracketsApi->get_unmatched_players_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_unmatched_players_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **query** | **str**| query | [optional] 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

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

# **get_unmatched_players_using_post**
> SingleWrapperOfPageOfPlayerResponse get_unmatched_players_using_post(authorization, version, search_unmatched_players_request)

getUnmatchedPlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.search_unmatched_players_request import SearchUnmatchedPlayersRequest
from dupr_backend.models.single_wrapper_of_page_of_player_response import SingleWrapperOfPageOfPlayerResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    search_unmatched_players_request = dupr_backend.SearchUnmatchedPlayersRequest() # SearchUnmatchedPlayersRequest | searchUnmatchedPlayersRequest

    try:
        # getUnmatchedPlayers
        api_response = api_instance.get_unmatched_players_using_post(authorization, version, search_unmatched_players_request)
        print("The response of BracketsApi->get_unmatched_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_unmatched_players_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **search_unmatched_players_request** | [**SearchUnmatchedPlayersRequest**](SearchUnmatchedPlayersRequest.md)| searchUnmatchedPlayersRequest | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

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

# **get_user_brackets_using_get**
> SingleWrapperOfPageOfBracketResponse get_user_brackets_using_get(authorization, limit, offset, version, status=status)

getUserBrackets

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_bracket_response import SingleWrapperOfPageOfBracketResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    limit = 56 # int | limit
    offset = 56 # int | offset
    version = 'v1.0' # str | version (default to 'v1.0')
    status = 'status_example' # str | status (optional)

    try:
        # getUserBrackets
        api_response = api_instance.get_user_brackets_using_get(authorization, limit, offset, version, status=status)
        print("The response of BracketsApi->get_user_brackets_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_brackets_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **status** | **str**| status | [optional] 

### Return type

[**SingleWrapperOfPageOfBracketResponse**](SingleWrapperOfPageOfBracketResponse.md)

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

# **get_user_club_role_using_post**
> SingleWrapperOfBracketClubRoleResponse get_user_club_role_using_post(authorization, version, request)

getUserClubRole

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_bracket_club_role_response import SingleWrapperOfBracketClubRoleResponse
from dupr_backend.models.user_club_role_request import UserClubRoleRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.UserClubRoleRequest() # UserClubRoleRequest | request

    try:
        # getUserClubRole
        api_response = api_instance.get_user_club_role_using_post(authorization, version, request)
        print("The response of BracketsApi->get_user_club_role_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_club_role_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**UserClubRoleRequest**](UserClubRoleRequest.md)| request | 

### Return type

[**SingleWrapperOfBracketClubRoleResponse**](SingleWrapperOfBracketClubRoleResponse.md)

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

# **get_user_event_brackets_using_get**
> ArrayWrapperOfBracketResponse get_user_event_brackets_using_get(authorization, league_id, user_id, version)

getUserEventBrackets

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_bracket_response import ArrayWrapperOfBracketResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    user_id = 56 # int | userId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getUserEventBrackets
        api_response = api_instance.get_user_event_brackets_using_get(authorization, league_id, user_id, version)
        print("The response of BracketsApi->get_user_event_brackets_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_event_brackets_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **user_id** | **int**| userId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfBracketResponse**](ArrayWrapperOfBracketResponse.md)

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

# **get_user_matches_using_post**
> SingleWrapperOfPageOfLeagueMatchResponse get_user_matches_using_post(authorization, version, user_matches_request)

getUserMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_page_of_league_match_response import SingleWrapperOfPageOfLeagueMatchResponse
from dupr_backend.models.user_matches_request import UserMatchesRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    user_matches_request = dupr_backend.UserMatchesRequest() # UserMatchesRequest | userMatchesRequest

    try:
        # getUserMatches
        api_response = api_instance.get_user_matches_using_post(authorization, version, user_matches_request)
        print("The response of BracketsApi->get_user_matches_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_user_matches_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **user_matches_request** | [**UserMatchesRequest**](UserMatchesRequest.md)| userMatchesRequest | 

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

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

# **get_valid_user_bracket_id_using_get**
> ArrayWrapperOfBracketResponse get_valid_user_bracket_id_using_get(authorization, league_id, version)

getValidUserBracketId

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_bracket_response import ArrayWrapperOfBracketResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_id = 56 # int | leagueId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getValidUserBracketId
        api_response = api_instance.get_valid_user_bracket_id_using_get(authorization, league_id, version)
        print("The response of BracketsApi->get_valid_user_bracket_id_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_valid_user_bracket_id_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfBracketResponse**](ArrayWrapperOfBracketResponse.md)

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

# **get_waterfall_matches_using_get**
> ArrayWrapperOfLeagueMatchResponse get_waterfall_matches_using_get(authorization, bracket_id, version)

getWaterfallMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_league_match_response import ArrayWrapperOfLeagueMatchResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # getWaterfallMatches
        api_response = api_instance.get_waterfall_matches_using_get(authorization, bracket_id, version)
        print("The response of BracketsApi->get_waterfall_matches_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->get_waterfall_matches_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]

### Return type

[**ArrayWrapperOfLeagueMatchResponse**](ArrayWrapperOfLeagueMatchResponse.md)

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

# **player_withdraw_by_director_using_post**
> Wrapper player_withdraw_by_director_using_post(authorization, version, withdraw_player_request)

playerWithdrawByDirector

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.withdraw_player_request import WithdrawPlayerRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    withdraw_player_request = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | withdrawPlayerRequest

    try:
        # playerWithdrawByDirector
        api_response = api_instance.player_withdraw_by_director_using_post(authorization, version, withdraw_player_request)
        print("The response of BracketsApi->player_withdraw_by_director_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->player_withdraw_by_director_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **withdraw_player_request** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)| withdrawPlayerRequest | 

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

# **player_withdraw_using_post**
> Wrapper player_withdraw_using_post(authorization, version, withdraw_player_request)

playerWithdraw

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.withdraw_player_request import WithdrawPlayerRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    withdraw_player_request = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | withdrawPlayerRequest

    try:
        # playerWithdraw
        api_response = api_instance.player_withdraw_using_post(authorization, version, withdraw_player_request)
        print("The response of BracketsApi->player_withdraw_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->player_withdraw_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **withdraw_player_request** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)| withdrawPlayerRequest | 

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

# **process_refunds_using_post**
> Wrapper process_refunds_using_post(authorization, version, request)

processRefunds

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.event_refund_request import EventRefundRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.EventRefundRequest() # EventRefundRequest | request

    try:
        # processRefunds
        api_response = api_instance.process_refunds_using_post(authorization, version, request)
        print("The response of BracketsApi->process_refunds_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->process_refunds_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**EventRefundRequest**](EventRefundRequest.md)| request | 

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

# **register_users_to_bracket_using_post**
> SingleWrapperOfJoinLeagueResponse register_users_to_bracket_using_post(authorization, version, request)

registerUsersToBracket

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.register_to_bracket_request import RegisterToBracketRequest
from dupr_backend.models.single_wrapper_of_join_league_response import SingleWrapperOfJoinLeagueResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.RegisterToBracketRequest() # RegisterToBracketRequest | request

    try:
        # registerUsersToBracket
        api_response = api_instance.register_users_to_bracket_using_post(authorization, version, request)
        print("The response of BracketsApi->register_users_to_bracket_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->register_users_to_bracket_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**RegisterToBracketRequest**](RegisterToBracketRequest.md)| request | 

### Return type

[**SingleWrapperOfJoinLeagueResponse**](SingleWrapperOfJoinLeagueResponse.md)

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

# **remove_match_from_queue_using_get**
> Wrapper remove_match_from_queue_using_get(authorization, league_match_id, version)

removeMatchFromQueue

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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    league_match_id = 56 # int | leagueMatchId
    version = 'v1.0' # str | version (default to 'v1.0')

    try:
        # removeMatchFromQueue
        api_response = api_instance.remove_match_from_queue_using_get(authorization, league_match_id, version)
        print("The response of BracketsApi->remove_match_from_queue_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->remove_match_from_queue_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **league_match_id** | **int**| leagueMatchId | 
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

# **save_bracket_using_put**
> SingleWrapperOfLeagueResponse save_bracket_using_put(authorization, version, request)

saveBracket

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_request import BracketRequest
from dupr_backend.models.single_wrapper_of_league_response import SingleWrapperOfLeagueResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BracketRequest() # BracketRequest | request

    try:
        # saveBracket
        api_response = api_instance.save_bracket_using_put(authorization, version, request)
        print("The response of BracketsApi->save_bracket_using_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_bracket_using_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BracketRequest**](BracketRequest.md)| request | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

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

# **save_match_seeding_using_post**
> Wrapper save_match_seeding_using_post(authorization, bracket_id, version, request)

saveMatchSeeding

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.match_round_req import MatchRoundReq
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.MatchRoundReq()] # List[MatchRoundReq] | request

    try:
        # saveMatchSeeding
        api_response = api_instance.save_match_seeding_using_post(authorization, bracket_id, version, request)
        print("The response of BracketsApi->save_match_seeding_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_match_seeding_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[MatchRoundReq]**](MatchRoundReq.md)| request | 

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

# **save_teams_using_post**
> Wrapper save_teams_using_post(authorization, version, create_new_team_request)

saveTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.create_new_team_request import CreateNewTeamRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    create_new_team_request = dupr_backend.CreateNewTeamRequest() # CreateNewTeamRequest | createNewTeamRequest

    try:
        # saveTeams
        api_response = api_instance.save_teams_using_post(authorization, version, create_new_team_request)
        print("The response of BracketsApi->save_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->save_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **create_new_team_request** | [**CreateNewTeamRequest**](CreateNewTeamRequest.md)| createNewTeamRequest | 

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

# **seed_matches_using_get**
> ArrayWrapperOfMatchRound seed_matches_using_get(authorization, bracket_id, version, type=type)

seedMatches

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_match_round import ArrayWrapperOfMatchRound
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    version = 'v1.0' # str | version (default to 'v1.0')
    type = 'ROUND_ROBIN' # str | type (optional) (default to 'ROUND_ROBIN')

    try:
        # seedMatches
        api_response = api_instance.seed_matches_using_get(authorization, bracket_id, version, type=type)
        print("The response of BracketsApi->seed_matches_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->seed_matches_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **type** | **str**| type | [optional] [default to &#39;ROUND_ROBIN&#39;]

### Return type

[**ArrayWrapperOfMatchRound**](ArrayWrapperOfMatchRound.md)

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

# **substitute_players_using_post**
> SingleWrapperOfUnit substitute_players_using_post(authorization, version, request)

substitutePlayers

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_unit import SingleWrapperOfUnit
from dupr_backend.models.substitute_player_request import SubstitutePlayerRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.SubstitutePlayerRequest()] # List[SubstitutePlayerRequest] | request

    try:
        # substitutePlayers
        api_response = api_instance.substitute_players_using_post(authorization, version, request)
        print("The response of BracketsApi->substitute_players_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->substitute_players_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[SubstitutePlayerRequest]**](SubstitutePlayerRequest.md)| request | 

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

# **switch_player_using_post**
> ArrayWrapperOfSwitchBracketResponse switch_player_using_post(authorization, version, request)

switchPlayer

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_switch_bracket_response import ArrayWrapperOfSwitchBracketResponse
from dupr_backend.models.switch_bracket_request import SwitchBracketRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.SwitchBracketRequest()] # List[SwitchBracketRequest] | request

    try:
        # switchPlayer
        api_response = api_instance.switch_player_using_post(authorization, version, request)
        print("The response of BracketsApi->switch_player_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_player_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[SwitchBracketRequest]**](SwitchBracketRequest.md)| request | 

### Return type

[**ArrayWrapperOfSwitchBracketResponse**](ArrayWrapperOfSwitchBracketResponse.md)

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

# **switch_teams_using_post**
> ArrayWrapperOfSwitchBracketResponse switch_teams_using_post(authorization, version, request)

switchTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.array_wrapper_of_switch_bracket_response import ArrayWrapperOfSwitchBracketResponse
from dupr_backend.models.switch_team_request import SwitchTeamRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.SwitchTeamRequest()] # List[SwitchTeamRequest] | request

    try:
        # switchTeams
        api_response = api_instance.switch_teams_using_post(authorization, version, request)
        print("The response of BracketsApi->switch_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[SwitchTeamRequest]**](SwitchTeamRequest.md)| request | 

### Return type

[**ArrayWrapperOfSwitchBracketResponse**](ArrayWrapperOfSwitchBracketResponse.md)

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

# **switch_wait_listed_teams_using_post**
> SingleWrapperOfUnit switch_wait_listed_teams_using_post(authorization, version, request)

switchWaitListedTeams

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_player_switch_wait_listed_request import BracketPlayerSwitchWaitListedRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = [dupr_backend.BracketPlayerSwitchWaitListedRequest()] # List[BracketPlayerSwitchWaitListedRequest] | request

    try:
        # switchWaitListedTeams
        api_response = api_instance.switch_wait_listed_teams_using_post(authorization, version, request)
        print("The response of BracketsApi->switch_wait_listed_teams_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_wait_listed_teams_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**List[BracketPlayerSwitchWaitListedRequest]**](BracketPlayerSwitchWaitListedRequest.md)| request | 

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

# **switch_wait_listed_using_post**
> SingleWrapperOfUnit switch_wait_listed_using_post(authorization, version, request)

switchWaitListed

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.bracket_player_switch_wait_listed_request import BracketPlayerSwitchWaitListedRequest
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.BracketPlayerSwitchWaitListedRequest() # BracketPlayerSwitchWaitListedRequest | request

    try:
        # switchWaitListed
        api_response = api_instance.switch_wait_listed_using_post(authorization, version, request)
        print("The response of BracketsApi->switch_wait_listed_using_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->switch_wait_listed_using_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**BracketPlayerSwitchWaitListedRequest**](BracketPlayerSwitchWaitListedRequest.md)| request | 

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

# **update_bracket_approval_using_get**
> SingleWrapperOfSessionResponse update_bracket_approval_using_get(authorization, bracket_id, is_club_member, registration_id, status, version, x_forwarded_for=x_forwarded_for)

updateBracketApproval

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.single_wrapper_of_session_response import SingleWrapperOfSessionResponse
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
    api_instance = dupr_backend.BracketsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    bracket_id = 56 # int | bracketId
    is_club_member = True # bool | isClubMember
    registration_id = 56 # int | registrationId
    status = 'status_example' # str | status
    version = 'v1.0' # str | version (default to 'v1.0')
    x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

    try:
        # updateBracketApproval
        api_response = api_instance.update_bracket_approval_using_get(authorization, bracket_id, is_club_member, registration_id, status, version, x_forwarded_for=x_forwarded_for)
        print("The response of BracketsApi->update_bracket_approval_using_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BracketsApi->update_bracket_approval_using_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **bracket_id** | **int**| bracketId | 
 **is_club_member** | **bool**| isClubMember | 
 **registration_id** | **int**| registrationId | 
 **status** | **str**| status | 
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

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

