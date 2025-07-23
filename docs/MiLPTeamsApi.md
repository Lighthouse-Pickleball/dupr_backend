# dupr_backend.MiLPTeamsApi

All URIs are relative to *https://api.dupr.gg*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save**](MiLPTeamsApi.md#save) | **POST** /milp/teams/{version}/save | 


# **save**
> SingleWrapperMiLPTeam save(version, mi_lp_team_request)

### Example


```python
import dupr_backend
from dupr_backend.models.mi_lp_team_request import MiLPTeamRequest
from dupr_backend.models.single_wrapper_mi_lp_team import SingleWrapperMiLPTeam
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
    api_instance = dupr_backend.MiLPTeamsApi(api_client)
    version = 'version_example' # str | 
    mi_lp_team_request = dupr_backend.MiLPTeamRequest() # MiLPTeamRequest | 

    try:
        api_response = api_instance.save(version, mi_lp_team_request)
        print("The response of MiLPTeamsApi->save:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPTeamsApi->save: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  | 
 **mi_lp_team_request** | [**MiLPTeamRequest**](MiLPTeamRequest.md)|  | 

### Return type

[**SingleWrapperMiLPTeam**](SingleWrapperMiLPTeam.md)

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

