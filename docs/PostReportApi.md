# dupr_backend.PostReportApi

All URIs are relative to *https://backend.mydupr.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_reports_using_get**](PostReportApi.md#get_reports_using_get) | **GET** /report/{version}/{status} | getReports
[**report_activity_using_post**](PostReportApi.md#report_activity_using_post) | **POST** /report/{version} | reportActivity
[**report_process_using_post**](PostReportApi.md#report_process_using_post) | **POST** /report/{version}/process/{reportId}/{status} | reportProcess

# **get_reports_using_get**
> SingleWrapperOfPageOfPostReport get_reports_using_get(authorization, status, version, from_date=from_date, limit=limit, offset=offset, reason=reason, sort_by=sort_by, sort_direction=sort_direction, to_date=to_date)

getReports

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PostReportApi()
authorization = 'Bearer ' # str |  (default to Bearer )
status = 'status_example' # str | PostReport status
version = 'version_example' # str | version
from_date = 'from_date_example' # str | fromDate (optional)
limit = 10 # int | limit (optional) (default to 10)
offset = 0 # int | offset (optional) (default to 0)
reason = 'reason_example' # str | reason (optional)
sort_by = 'created_at' # str | sortBy (optional) (default to created_at)
sort_direction = 'DESC' # str | sortDirection (optional) (default to DESC)
to_date = 'to_date_example' # str | toDate (optional)

try:
    # getReports
    api_response = api_instance.get_reports_using_get(authorization, status, version, from_date=from_date, limit=limit, offset=offset, reason=reason, sort_by=sort_by, sort_direction=sort_direction, to_date=to_date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReportApi->get_reports_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **status** | **str**| PostReport status | 
 **version** | **str**| version | 
 **from_date** | **str**| fromDate | [optional] 
 **limit** | **int**| limit | [optional] [default to 10]
 **offset** | **int**| offset | [optional] [default to 0]
 **reason** | **str**| reason | [optional] 
 **sort_by** | **str**| sortBy | [optional] [default to created_at]
 **sort_direction** | **str**| sortDirection | [optional] [default to DESC]
 **to_date** | **str**| toDate | [optional] 

### Return type

[**SingleWrapperOfPageOfPostReport**](SingleWrapperOfPageOfPostReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_activity_using_post**
> SingleWrapperOfPostReport report_activity_using_post(body, authorization, version)

reportActivity

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PostReportApi()
body = dupr_backend.ReportRequest() # ReportRequest | reportRequest
authorization = 'Bearer ' # str |  (default to Bearer )
version = 'version_example' # str | version

try:
    # reportActivity
    api_response = api_instance.report_activity_using_post(body, authorization, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReportApi->report_activity_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ReportRequest**](ReportRequest.md)| reportRequest | 
 **authorization** | **str**|  | [default to Bearer ]
 **version** | **str**| version | 

### Return type

[**SingleWrapperOfPostReport**](SingleWrapperOfPostReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **report_process_using_post**
> Wrapper report_process_using_post(authorization, report_id, status, version)

reportProcess

### Example
```python
from __future__ import print_function
import time
import dupr_backend
from dupr_backend.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = dupr_backend.PostReportApi()
authorization = 'Bearer ' # str |  (default to Bearer )
report_id = 'report_id_example' # str | The report's Id
status = 'status_example' # str | APPROVE/REJECT
version = 'version_example' # str | version

try:
    # reportProcess
    api_response = api_instance.report_process_using_post(authorization, report_id, status, version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PostReportApi->report_process_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [default to Bearer ]
 **report_id** | **str**| The report&#x27;s Id | 
 **status** | **str**| APPROVE/REJECT | 
 **version** | **str**| version | 

### Return type

[**Wrapper**](Wrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

