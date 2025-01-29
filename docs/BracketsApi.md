# dupr_backend.BracketsApi

All URIs are relative to *https://backend.mydupr.com/*

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
> Wrapper add_match_score_by_director_using_post(body, authorization, version)

addMatchScoreByDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # addMatchScoreByDirector
    api_response = api_instance.add_match_score_by_director_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->add_match_score_by_director_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueMatchRequest**](LeagueMatchRequest.md)| request | 
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

# **add_match_score_using_post**
> Wrapper add_match_score_using_post(body, authorization, version)

addMatchScore

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.LeagueMatchRequest() # LeagueMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # addMatchScore
    api_response = api_instance.add_match_score_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->add_match_score_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueMatchRequest**](LeagueMatchRequest.md)| request | 
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

# **confirm_match_director_using_post**
> Wrapper confirm_match_director_using_post(body, authorization, version)

confirmMatchDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # confirmMatchDirector
    api_response = api_instance.confirm_match_director_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->confirm_match_director_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)| request | 
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

# **confirm_match_using_post**
> Wrapper confirm_match_using_post(body, authorization, version)

confirmMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.LeagueMatchConfirmRequest() # LeagueMatchConfirmRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # confirmMatch
    api_response = api_instance.confirm_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->confirm_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LeagueMatchConfirmRequest**](LeagueMatchConfirmRequest.md)| request | 
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

# **confirm_team_by_director_using_post**
> Wrapper confirm_team_by_director_using_post(body, authorization, version)

confirmTeamByDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.ConfirmTeamRequest() # ConfirmTeamRequest | confirmTeamRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # confirmTeamByDirector
    api_response = api_instance.confirm_team_by_director_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->confirm_team_by_director_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConfirmTeamRequest**](ConfirmTeamRequest.md)| confirmTeamRequest | 
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

# **delete_league_using_delete**
> Wrapper delete_league_using_delete(authorization, bracket_id, league_id, version)

deleteLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # deleteLeague
    api_response = api_instance.delete_league_using_delete(authorization, bracket_id, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->delete_league_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bracket_status_using_put**
> SingleWrapperOfUnit edit_bracket_status_using_put(authorization, bracket_id, club_id, league_id, status, version)

editBracketStatus

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
club_id = 789 # int | clubId
league_id = 789 # int | leagueId
status = 'status_example' # str | status
version = 'version_example' # str | version

try:
    # editBracketStatus
    api_response = api_instance.edit_bracket_status_using_put(authorization, bracket_id, club_id, league_id, status, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_bracket_status_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **club_id** | **int**| clubId | 
 **league_id** | **int**| leagueId | 
 **status** | **str**| status | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfUnit**](SingleWrapperOfUnit.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_bracket_using_put**
> SingleWrapperOfLeagueResponse edit_bracket_using_put(body, authorization, version)

editBracket

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditBracketRequest() # EditBracketRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editBracket
    api_response = api_instance.edit_bracket_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_bracket_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditBracketRequest**](EditBracketRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **edit_confirmed_matches_using_post**
> Wrapper edit_confirmed_matches_using_post(body, authorization, version)

editConfirmedMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditMatchRequest() # EditMatchRequest | editMatchRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editConfirmedMatches
    api_response = api_instance.edit_confirmed_matches_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_confirmed_matches_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditMatchRequest**](EditMatchRequest.md)| editMatchRequest | 
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

# **edit_match_score_by_director_using_post**
> Wrapper edit_match_score_by_director_using_post(body, authorization, version)

editMatchScoreByDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditMatchRequest() # EditMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editMatchScoreByDirector
    api_response = api_instance.edit_match_score_by_director_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_match_score_by_director_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditMatchRequest**](EditMatchRequest.md)| request | 
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

# **edit_match_score_using_post**
> Wrapper edit_match_score_using_post(body, authorization, version)

editMatchScore

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditMatchRequest() # EditMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editMatchScore
    api_response = api_instance.edit_match_score_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_match_score_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditMatchRequest**](EditMatchRequest.md)| request | 
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

# **edit_partner_using_post**
> Wrapper edit_partner_using_post(body, authorization, version)

editPartner

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditPartnerRequest() # EditPartnerRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editPartner
    api_response = api_instance.edit_partner_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_partner_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditPartnerRequest**](EditPartnerRequest.md)| request | 
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

# **edit_player_wait_list_using_post**
> Wrapper edit_player_wait_list_using_post(body, authorization, version)

editPlayerWaitList

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.EditWaitListRequest()] # list[EditWaitListRequest] | editWaitListRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editPlayerWaitList
    api_response = api_instance.edit_player_wait_list_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_player_wait_list_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[EditWaitListRequest]**](EditWaitListRequest.md)| editWaitListRequest | 
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

# **edit_teams_using_post**
> Wrapper edit_teams_using_post(body, authorization, version)

editTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EditEventTeamRequest() # EditEventTeamRequest | editEventTeamRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # editTeams
    api_response = api_instance.edit_teams_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->edit_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EditEventTeamRequest**](EditEventTeamRequest.md)| editEventTeamRequest | 
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

# **end_league_using_get**
> Wrapper end_league_using_get(authorization, bracket_id, league_id, version)

endLeague

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # endLeague
    api_response = api_instance.end_league_using_get(authorization, bracket_id, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->end_league_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **export_bracket_participants_using_get**
> SingleWrapperOfDownloadS3Response export_bracket_participants_using_get(authorization, bracket_id, version)

exportBracketParticipants

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # exportBracketParticipants
    api_response = api_instance.export_bracket_participants_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->export_bracket_participants_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfDownloadS3Response**](SingleWrapperOfDownloadS3Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forfeit_match_using_post**
> Wrapper forfeit_match_using_post(body, authorization, version)

forfeitMatch

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.ForfeitMatchRequest() # ForfeitMatchRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # forfeitMatch
    api_response = api_instance.forfeit_match_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->forfeit_match_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForfeitMatchRequest**](ForfeitMatchRequest.md)| request | 
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

# **get_all_bracket_matches_using_get**
> ArrayWrapperOfLeagueMatchResponse get_all_bracket_matches_using_get(authorization, bracket_id, version)

getAllBracketMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getAllBracketMatches
    api_response = api_instance.get_all_bracket_matches_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_all_bracket_matches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfLeagueMatchResponse**](ArrayWrapperOfLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_event_players_using_post**
> SingleWrapperOfPageOfPlayerPaymentResponse get_all_event_players_using_post(body, authorization, limit, offset, version)

getAllEventPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getAllEventPlayers
    api_response = api_instance.get_all_event_players_using_post(body, authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_all_event_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerPaymentResponse**](SingleWrapperOfPageOfPlayerPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_by_id_using_get**
> SingleWrapperOfBracketResponse get_bracket_by_id_using_get(bracket_id, version, authorization=authorization)

getBracketById

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version
authorization = 'Bearer ' # str |  (optional) (default to Bearer )

try:
    # getBracketById
    api_response = api_instance.get_bracket_by_id_using_get(bracket_id, version, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_by_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 
 **authorization** | **str**|  | [optional] [default to Bearer ]

### Return type

[**SingleWrapperOfBracketResponse**](SingleWrapperOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_details_teams_using_get**
> SingleWrapperOfBracketDetailsResponse get_bracket_details_teams_using_get(authorization, bracket_id, version)

getBracketDetailsTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getBracketDetailsTeams
    api_response = api_instance.get_bracket_details_teams_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_details_teams_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfBracketDetailsResponse**](SingleWrapperOfBracketDetailsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_match_queue_using_get**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_match_queue_using_get(authorization, bracket_id, version, limit=limit, offset=offset)

getBracketMatchQueue

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)

try:
    # getBracketMatchQueue
    api_response = api_instance.get_bracket_match_queue_using_get(authorization, bracket_id, version, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_match_queue_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_matches_post_using_post**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_matches_post_using_post(body, authorization, bracket_id, version, limit=limit, offset=offset, round=round)

getBracketMatchesPost

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.BracketMatchRequest() # BracketMatchRequest | bracketMatchRequest
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)
round = 0 # int | round (optional) (default to 0)

try:
    # getBracketMatchesPost
    api_response = api_instance.get_bracket_matches_post_using_post(body, authorization, bracket_id, version, limit=limit, offset=offset, round=round)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_matches_post_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BracketMatchRequest**](BracketMatchRequest.md)| bracketMatchRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 
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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_matches_using_get**
> SingleWrapperOfPageOfLeagueMatchResponse get_bracket_matches_using_get(authorization, bracket_id, version, limit=limit, offset=offset, round=round, tags=tags)

getBracketMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)
round = 0 # int | round (optional) (default to 0)
tags = '10' # str | tags (optional) (default to 10)

try:
    # getBracketMatches
    api_response = api_instance.get_bracket_matches_using_get(authorization, bracket_id, version, limit=limit, offset=offset, round=round, tags=tags)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_matches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]
 **round** | **int**| round | [optional] [default to 0]
 **tags** | **str**| tags | [optional] [default to 10]

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_players_using_get**
> SingleWrapperOfPageOfPlayerResponse get_bracket_players_using_get(authorization, bracket_id, limit, offset, version, query=query)

getBracketPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
query = 'query_example' # str | query (optional)

try:
    # getBracketPlayers
    api_response = api_instance.get_bracket_players_using_get(authorization, bracket_id, limit, offset, version, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_players_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **query** | **str**| query | [optional] 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_players_using_post**
> SingleWrapperOfPageOfPlayerResponse get_bracket_players_using_post(body, authorization, limit, offset, version)

getBracketPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.SearchLeaguePlayerRequest() # SearchLeaguePlayerRequest | searchLeaguePlayerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getBracketPlayers
    api_response = api_instance.get_bracket_players_using_post(body, authorization, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchLeaguePlayerRequest**](SearchLeaguePlayerRequest.md)| searchLeaguePlayerRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_standing_using_get**
> SingleWrapperOfPageOfLeagueStandingResponse get_bracket_standing_using_get(authorization, bracket_id, limit, version, offset=offset, round=round)

getBracketStanding

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
limit = 56 # int | limit
version = 'version_example' # str | version
offset = 0 # int | offset (optional) (default to 0)
round = 0 # int | round (optional) (default to 0)

try:
    # getBracketStanding
    api_response = api_instance.get_bracket_standing_using_get(authorization, bracket_id, limit, version, offset=offset, round=round)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_standing_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **version** | **str**| version | 
 **offset** | **int**| offset | [optional] [default to 0]
 **round** | **int**| round | [optional] [default to 0]

### Return type

[**SingleWrapperOfPageOfLeagueStandingResponse**](SingleWrapperOfPageOfLeagueStandingResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_teams_using_get**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)

getBracketTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
format = 'format_example' # str | format
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getBracketTeams
    api_response = api_instance.get_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_teams_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **format** | **str**| format | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_teams_using_post**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_teams_using_post(body, authorization, format, version)

getBracketTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | bracketSearchTeamsRequest
authorization = 'Bearer ' # str |  (default to Bearer )
format = 'format_example' # str | format
version = 'version_example' # str | version

try:
    # getBracketTeams
    api_response = api_instance.get_bracket_teams_using_post(body, authorization, format, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)| bracketSearchTeamsRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **format** | **str**| format | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bracket_waitlisted_teams_using_post**
> SingleWrapperOfPageOfLeagueTeamsResponse get_bracket_waitlisted_teams_using_post(body, authorization, format, version)

getBracketWaitlistedTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.BracketSearchTeamsRequest() # BracketSearchTeamsRequest | bracketSearchTeamsRequest
authorization = 'Bearer ' # str |  (default to Bearer )
format = 'format_example' # str | format
version = 'version_example' # str | version

try:
    # getBracketWaitlistedTeams
    api_response = api_instance.get_bracket_waitlisted_teams_using_post(body, authorization, format, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_bracket_waitlisted_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BracketSearchTeamsRequest**](BracketSearchTeamsRequest.md)| bracketSearchTeamsRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **format** | **str**| format | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_director_bracket_teams_using_get**
> SingleWrapperOfPageOfLeagueTeamsResponse get_director_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)

getDirectorBracketTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
format = 'format_example' # str | format
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version

try:
    # getDirectorBracketTeams
    api_response = api_instance.get_director_bracket_teams_using_get(authorization, bracket_id, format, limit, offset, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_director_bracket_teams_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **format** | **str**| format | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueTeamsResponse**](SingleWrapperOfPageOfLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_confirmation_using_get**
> ArrayWrapperOfLeagueTeamsResponse get_pending_confirmation_using_get(authorization, bracket_id, version)

getPendingConfirmation

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getPendingConfirmation
    api_response = api_instance.get_pending_confirmation_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_pending_confirmation_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfLeagueTeamsResponse**](ArrayWrapperOfLeagueTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_pending_teams_to_replace_using_get**
> ArrayWrapperOfPendingTeamsResponse get_pending_teams_to_replace_using_get(authorization, bracket_id, version)

getPendingTeamsToReplace

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getPendingTeamsToReplace
    api_response = api_instance.get_pending_teams_to_replace_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_pending_teams_to_replace_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfPendingTeamsResponse**](ArrayWrapperOfPendingTeamsResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_registration_details_using_get**
> SingleWrapperOfRegistrationResponse get_registration_details_using_get(authorization, bracket_id, version)

getRegistrationDetails

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getRegistrationDetails
    api_response = api_instance.get_registration_details_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_registration_details_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfRegistrationResponse**](SingleWrapperOfRegistrationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmatched_players_using_get**
> SingleWrapperOfPageOfPlayerResponse get_unmatched_players_using_get(authorization, bracket_id, limit, offset, version, query=query)

getUnmatchedPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
query = 'query_example' # str | query (optional)

try:
    # getUnmatchedPlayers
    api_response = api_instance.get_unmatched_players_using_get(authorization, bracket_id, limit, offset, version, query=query)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_unmatched_players_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **query** | **str**| query | [optional] 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_unmatched_players_using_post**
> SingleWrapperOfPageOfPlayerResponse get_unmatched_players_using_post(body, authorization, version)

getUnmatchedPlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.SearchUnmatchedPlayersRequest() # SearchUnmatchedPlayersRequest | searchUnmatchedPlayersRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getUnmatchedPlayers
    api_response = api_instance.get_unmatched_players_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_unmatched_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchUnmatchedPlayersRequest**](SearchUnmatchedPlayersRequest.md)| searchUnmatchedPlayersRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfPlayerResponse**](SingleWrapperOfPageOfPlayerResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_brackets_using_get**
> SingleWrapperOfPageOfBracketResponse get_user_brackets_using_get(authorization, limit, offset, version, status=status)

getUserBrackets

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
limit = 56 # int | limit
offset = 56 # int | offset
version = 'version_example' # str | version
status = 'status_example' # str | status (optional)

try:
    # getUserBrackets
    api_response = api_instance.get_user_brackets_using_get(authorization, limit, offset, version, status=status)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_user_brackets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **limit** | **int**| limit | 
 **offset** | **int**| offset | 
 **version** | **str**| version | 
 **status** | **str**| status | [optional] 

### Return type

[**SingleWrapperOfPageOfBracketResponse**](SingleWrapperOfPageOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_club_role_using_post**
> SingleWrapperOfBracketClubRoleResponse get_user_club_role_using_post(body, authorization, version)

getUserClubRole

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.UserClubRoleRequest() # UserClubRoleRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getUserClubRole
    api_response = api_instance.get_user_club_role_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_user_club_role_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserClubRoleRequest**](UserClubRoleRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfBracketClubRoleResponse**](SingleWrapperOfBracketClubRoleResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_event_brackets_using_get**
> ArrayWrapperOfBracketResponse get_user_event_brackets_using_get(authorization, league_id, user_id, version)

getUserEventBrackets

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
user_id = 789 # int | userId
version = 'version_example' # str | version

try:
    # getUserEventBrackets
    api_response = api_instance.get_user_event_brackets_using_get(authorization, league_id, user_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_user_event_brackets_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **user_id** | **int**| userId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfBracketResponse**](ArrayWrapperOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_matches_using_post**
> SingleWrapperOfPageOfLeagueMatchResponse get_user_matches_using_post(body, authorization, version)

getUserMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.UserMatchesRequest() # UserMatchesRequest | userMatchesRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # getUserMatches
    api_response = api_instance.get_user_matches_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_user_matches_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserMatchesRequest**](UserMatchesRequest.md)| userMatchesRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPageOfLeagueMatchResponse**](SingleWrapperOfPageOfLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_valid_user_bracket_id_using_get**
> ArrayWrapperOfBracketResponse get_valid_user_bracket_id_using_get(authorization, league_id, version)

getValidUserBracketId

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_id = 789 # int | leagueId
version = 'version_example' # str | version

try:
    # getValidUserBracketId
    api_response = api_instance.get_valid_user_bracket_id_using_get(authorization, league_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_valid_user_bracket_id_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_id** | **int**| leagueId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfBracketResponse**](ArrayWrapperOfBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_waterfall_matches_using_get**
> ArrayWrapperOfLeagueMatchResponse get_waterfall_matches_using_get(authorization, bracket_id, version)

getWaterfallMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # getWaterfallMatches
    api_response = api_instance.get_waterfall_matches_using_get(authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->get_waterfall_matches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfLeagueMatchResponse**](ArrayWrapperOfLeagueMatchResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **player_withdraw_by_director_using_post**
> Wrapper player_withdraw_by_director_using_post(body, authorization, version)

playerWithdrawByDirector

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | withdrawPlayerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # playerWithdrawByDirector
    api_response = api_instance.player_withdraw_by_director_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->player_withdraw_by_director_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)| withdrawPlayerRequest | 
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

# **player_withdraw_using_post**
> Wrapper player_withdraw_using_post(body, authorization, version)

playerWithdraw

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.WithdrawPlayerRequest() # WithdrawPlayerRequest | withdrawPlayerRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # playerWithdraw
    api_response = api_instance.player_withdraw_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->player_withdraw_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**WithdrawPlayerRequest**](WithdrawPlayerRequest.md)| withdrawPlayerRequest | 
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

# **process_refunds_using_post**
> Wrapper process_refunds_using_post(body, authorization, version)

processRefunds

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.EventRefundRequest() # EventRefundRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # processRefunds
    api_response = api_instance.process_refunds_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->process_refunds_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EventRefundRequest**](EventRefundRequest.md)| request | 
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

# **register_users_to_bracket_using_post**
> SingleWrapperOfJoinLeagueResponse register_users_to_bracket_using_post(body, authorization, version)

registerUsersToBracket

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.RegisterToBracketRequest() # RegisterToBracketRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # registerUsersToBracket
    api_response = api_instance.register_users_to_bracket_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->register_users_to_bracket_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RegisterToBracketRequest**](RegisterToBracketRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfJoinLeagueResponse**](SingleWrapperOfJoinLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_match_from_queue_using_get**
> Wrapper remove_match_from_queue_using_get(authorization, league_match_id, version)

removeMatchFromQueue

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
league_match_id = 789 # int | leagueMatchId
version = 'version_example' # str | version

try:
    # removeMatchFromQueue
    api_response = api_instance.remove_match_from_queue_using_get(authorization, league_match_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->remove_match_from_queue_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **league_match_id** | **int**| leagueMatchId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_bracket_using_put**
> SingleWrapperOfLeagueResponse save_bracket_using_put(body, authorization, version)

saveBracket

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.BracketRequest() # BracketRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveBracket
    api_response = api_instance.save_bracket_using_put(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->save_bracket_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BracketRequest**](BracketRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfLeagueResponse**](SingleWrapperOfLeagueResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_match_seeding_using_post**
> Wrapper save_match_seeding_using_post(body, authorization, bracket_id, version)

saveMatchSeeding

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.MatchRoundReq()] # list[MatchRoundReq] | request
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version

try:
    # saveMatchSeeding
    api_response = api_instance.save_match_seeding_using_post(body, authorization, bracket_id, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->save_match_seeding_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[MatchRoundReq]**](MatchRoundReq.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_teams_using_post**
> Wrapper save_teams_using_post(body, authorization, version)

saveTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.CreateNewTeamRequest() # CreateNewTeamRequest | createNewTeamRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # saveTeams
    api_response = api_instance.save_teams_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->save_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateNewTeamRequest**](CreateNewTeamRequest.md)| createNewTeamRequest | 
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

# **seed_matches_using_get**
> ArrayWrapperOfMatchRound seed_matches_using_get(authorization, bracket_id, version, type=type)

seedMatches

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
version = 'version_example' # str | version
type = 'ROUND_ROBIN' # str | type (optional) (default to ROUND_ROBIN)

try:
    # seedMatches
    api_response = api_instance.seed_matches_using_get(authorization, bracket_id, version, type=type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->seed_matches_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **version** | **str**| version | 
 **type** | **str**| type | [optional] [default to ROUND_ROBIN]

### Return type

[**ArrayWrapperOfMatchRound**](ArrayWrapperOfMatchRound.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **substitute_players_using_post**
> SingleWrapperOfUnit substitute_players_using_post(body, authorization, version)

substitutePlayers

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.SubstitutePlayerRequest()] # list[SubstitutePlayerRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # substitutePlayers
    api_response = api_instance.substitute_players_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->substitute_players_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SubstitutePlayerRequest]**](SubstitutePlayerRequest.md)| request | 
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

# **switch_player_using_post**
> ArrayWrapperOfSwitchBracketResponse switch_player_using_post(body, authorization, version)

switchPlayer

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.SwitchBracketRequest()] # list[SwitchBracketRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # switchPlayer
    api_response = api_instance.switch_player_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->switch_player_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SwitchBracketRequest]**](SwitchBracketRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfSwitchBracketResponse**](ArrayWrapperOfSwitchBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_teams_using_post**
> ArrayWrapperOfSwitchBracketResponse switch_teams_using_post(body, authorization, version)

switchTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.SwitchTeamRequest()] # list[SwitchTeamRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # switchTeams
    api_response = api_instance.switch_teams_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->switch_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[SwitchTeamRequest]**](SwitchTeamRequest.md)| request | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**ArrayWrapperOfSwitchBracketResponse**](ArrayWrapperOfSwitchBracketResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_wait_listed_teams_using_post**
> SingleWrapperOfUnit switch_wait_listed_teams_using_post(body, authorization, version)

switchWaitListedTeams

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = [dupr_backend.BracketPlayerSwitchWaitListedRequest()] # list[BracketPlayerSwitchWaitListedRequest] | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # switchWaitListedTeams
    api_response = api_instance.switch_wait_listed_teams_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->switch_wait_listed_teams_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[BracketPlayerSwitchWaitListedRequest]**](BracketPlayerSwitchWaitListedRequest.md)| request | 
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

# **switch_wait_listed_using_post**
> SingleWrapperOfUnit switch_wait_listed_using_post(body, authorization, version)

switchWaitListed

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
body = dupr_backend.BracketPlayerSwitchWaitListedRequest() # BracketPlayerSwitchWaitListedRequest | request
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # switchWaitListed
    api_response = api_instance.switch_wait_listed_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->switch_wait_listed_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BracketPlayerSwitchWaitListedRequest**](BracketPlayerSwitchWaitListedRequest.md)| request | 
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

# **update_bracket_approval_using_get**
> SingleWrapperOfSessionResponse update_bracket_approval_using_get(authorization, bracket_id, is_club_member, registration_id, status, version, x_forwarded_for=x_forwarded_for)

updateBracketApproval

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.BracketsApi()
authorization = 'Bearer ' # str |  (default to Bearer )
bracket_id = 789 # int | bracketId
is_club_member = true # bool | isClubMember
registration_id = 789 # int | registrationId
status = 'status_example' # str | status
version = 'version_example' # str | version
x_forwarded_for = 'x_forwarded_for_example' # str | x-forwarded-for (optional)

try:
    # updateBracketApproval
    api_response = api_instance.update_bracket_approval_using_get(authorization, bracket_id, is_club_member, registration_id, status, version, x_forwarded_for=x_forwarded_for)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BracketsApi->update_bracket_approval_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **bracket_id** | **int**| bracketId | 
 **is_club_member** | **bool**| isClubMember | 
 **registration_id** | **int**| registrationId | 
 **status** | **str**| status | 
 **version** | **str**| version | 
 **x_forwarded_for** | **str**| x-forwarded-for | [optional] 

### Return type

[**SingleWrapperOfSessionResponse**](SingleWrapperOfSessionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

