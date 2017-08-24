# swagger_client.AccessApi

All URIs are relative to *http://localhost/nifi-api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token**](AccessApi.md#create_access_token) | **POST** /access/token | Creates a token for accessing the REST API via username/password
[**create_access_token_from_ticket**](AccessApi.md#create_access_token_from_ticket) | **POST** /access/kerberos | Creates a token for accessing the REST API via Kerberos ticket exchange / SPNEGO negotiation
[**create_download_token**](AccessApi.md#create_download_token) | **POST** /access/download-token | Creates a single use access token for downloading FlowFile content.
[**create_ui_extension_token**](AccessApi.md#create_ui_extension_token) | **POST** /access/ui-extension-token | Creates a single use access token for accessing a NiFi UI extension.
[**get_access_status**](AccessApi.md#get_access_status) | **GET** /access | Gets the status the client&#39;s access
[**get_login_config**](AccessApi.md#get_login_config) | **GET** /access/config | Retrieves the access configuration for this NiFi


# **create_access_token**
> str create_access_token(username=username, password=password)

Creates a token for accessing the REST API via username/password

The token returned is formatted as a JSON Web Token (JWT). The token is base64 encoded and comprised of three parts. The header, the body, and the signature. The expiration of the token is a contained within the body. The token can be used in the Authorization header in the format 'Authorization: Bearer <token>'.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()
username = 'username_example' # str |  (optional)
password = 'password_example' # str |  (optional)

try: 
    # Creates a token for accessing the REST API via username/password
    api_response = api_instance.create_access_token(username=username, password=password)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_access_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | [optional] 
 **password** | **str**|  | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_access_token_from_ticket**
> str create_access_token_from_ticket()

Creates a token for accessing the REST API via Kerberos ticket exchange / SPNEGO negotiation

The token returned is formatted as a JSON Web Token (JWT). The token is base64 encoded and comprised of three parts. The header, the body, and the signature. The expiration of the token is a contained within the body. The token can be used in the Authorization header in the format 'Authorization: Bearer <token>'.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()

try: 
    # Creates a token for accessing the REST API via Kerberos ticket exchange / SPNEGO negotiation
    api_response = api_instance.create_access_token_from_ticket()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_access_token_from_ticket: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: text/plain
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_download_token**
> str create_download_token()

Creates a single use access token for downloading FlowFile content.

The token returned is a base64 encoded string. It is valid for a single request up to five minutes from being issued. It is used as a query parameter name 'access_token'.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()

try: 
    # Creates a single use access token for downloading FlowFile content.
    api_response = api_instance.create_download_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_download_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_ui_extension_token**
> str create_ui_extension_token()

Creates a single use access token for accessing a NiFi UI extension.

The token returned is a base64 encoded string. It is valid for a single request up to five minutes from being issued. It is used as a query parameter name 'access_token'.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()

try: 
    # Creates a single use access token for accessing a NiFi UI extension.
    api_response = api_instance.create_ui_extension_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->create_ui_extension_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_status**
> AccessStatusEntity get_access_status()

Gets the status the client's access

Note: This endpoint is subject to change as NiFi and it's REST API evolve.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()

try: 
    # Gets the status the client's access
    api_response = api_instance.get_access_status()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_access_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessStatusEntity**](AccessStatusEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_login_config**
> AccessConfigurationEntity get_login_config()

Retrieves the access configuration for this NiFi



### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccessApi()

try: 
    # Retrieves the access configuration for this NiFi
    api_response = api_instance.get_login_config()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessApi->get_login_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessConfigurationEntity**](AccessConfigurationEntity.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: */*
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

