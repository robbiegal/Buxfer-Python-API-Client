# swagger_client.GetDataApi

All URIs are relative to *https://www.buxfer.com/api/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_get**](GetDataApi.md#accounts_get) | **GET** /accounts | Get Accounts information
[**budgets_get**](GetDataApi.md#budgets_get) | **GET** /budgets | Get Budgets information
[**contacts_get**](GetDataApi.md#contacts_get) | **GET** /contacts | Get Contacts information
[**groups_get**](GetDataApi.md#groups_get) | **GET** /groups | Get Groups information
[**loans_get**](GetDataApi.md#loans_get) | **GET** /loans | Get Loans information
[**reminders_get**](GetDataApi.md#reminders_get) | **GET** /reminders | Get Reminders information
[**tags_get**](GetDataApi.md#tags_get) | **GET** /tags | Get Tags information
[**transactions_get**](GetDataApi.md#transactions_get) | **GET** /transactions | Get Transactions information

# **accounts_get**
> Accounts accounts_get(token=token)

Get Accounts information

Get Accounts information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Accounts information
    api_response = api_instance.accounts_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Accounts**](Accounts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **budgets_get**
> Budgets budgets_get(token=token)

Get Budgets information

Get Budgets information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Budgets information
    api_response = api_instance.budgets_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->budgets_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Budgets**](Budgets.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **contacts_get**
> Contacts contacts_get(token=token)

Get Contacts information

Get Contacts information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Contacts information
    api_response = api_instance.contacts_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->contacts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Contacts**](Contacts.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get**
> Groups groups_get(token=token)

Get Groups information

Get Groups information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Groups information
    api_response = api_instance.groups_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->groups_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Groups**](Groups.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **loans_get**
> Loans loans_get(token=token)

Get Loans information

Get Loans information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Loans information
    api_response = api_instance.loans_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->loans_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Loans**](Loans.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reminders_get**
> Reminders reminders_get(token=token)

Get Reminders information

Get Reminders information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Reminders information
    api_response = api_instance.reminders_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->reminders_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Reminders**](Reminders.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tags_get**
> Tags tags_get(token=token)

Get Tags information

Get Tags information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Tags information
    api_response = api_instance.tags_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->tags_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Tags**](Tags.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transactions_get**
> Transactions transactions_get(token=token)

Get Transactions information

Get Transactions information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.GetDataApi()
token = 'token_example' # str | token for getting data (optional)

try:
    # Get Transactions information
    api_response = api_instance.transactions_get(token=token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GetDataApi->transactions_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| token for getting data | [optional] 

### Return type

[**Transactions**](Transactions.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

