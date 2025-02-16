# dupr_backend.MiLPTeamsApi

All URIs are relative to *http://https://backend.mydupr.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**save_using_post3**](MiLPTeamsApi.md#save_using_post3) | **POST** /milp/teams/{version}/save | save


# **save_using_post3**
> SingleWrapperOfMiLPTeam save_using_post3(authorization, version, request)

save

### Example

```python
import time
import os
import dupr_backend
from dupr_backend.models.mi_lp_team_request import MiLPTeamRequest
from dupr_backend.models.single_wrapper_of_mi_lp_team import SingleWrapperOfMiLPTeam
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
    api_instance = dupr_backend.MiLPTeamsApi(api_client)
    authorization = 'Bearer ' # str |  (default to 'Bearer ')
    version = 'v1.0' # str | version (default to 'v1.0')
    request = dupr_backend.MiLPTeamRequest() # MiLPTeamRequest | request

    try:
        # save
        api_response = api_instance.save_using_post3(authorization, version, request)
        print("The response of MiLPTeamsApi->save_using_post3:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MiLPTeamsApi->save_using_post3: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to &#39;Bearer &#39;]
 **version** | **str**| version | [default to &#39;v1.0&#39;]
 **request** | [**MiLPTeamRequest**](MiLPTeamRequest.md)| request | 

### Return type

[**SingleWrapperOfMiLPTeam**](SingleWrapperOfMiLPTeam.md)

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

