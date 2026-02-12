# rentri_formulari.DefaultApi

All URIs are relative to *https://api.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](DefaultApi.md#status_get) | **GET** /status | Stato API
[**transazione_id_result_get**](DefaultApi.md#transazione_id_result_get) | **GET** /{transazione_id}/result | Esito transazione
[**transazione_id_status_get**](DefaultApi.md#transazione_id_status_get) | **GET** /{transazione_id}/status | Stato transazione


# **status_get**
> StatusResponse status_get()

Stato API

Verifica dello stato dell'API.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.status_response import StatusResponse
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://api.rentri.gov.it/formulari/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_formulari.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_formulari.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_formulari.DefaultApi(api_client)

    try:
        # Stato API
        api_response = api_instance.status_get()
        print("The response of DefaultApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->status_get: %s\n" % e)
```



### Parameters
This endpoint does not need any parameter.

### Return type

[**StatusResponse**](StatusResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |
**503** | Service Unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transazione_id_result_get**
> EsitoFormularioModel transazione_id_result_get(transazione_id)

Esito transazione

Ottiene l'esito dell'elaborazione di una richiesta di elaborazione per un formulario.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.esito_formulario_model import EsitoFormularioModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://api.rentri.gov.it/formulari/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_formulari.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_formulari.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_formulari.DefaultApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta

    try:
        # Esito transazione
        api_response = api_instance.transazione_id_result_get(transazione_id)
        print("The response of DefaultApi->transazione_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->transazione_id_result_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transazione_id** | **str**| Id della richiesta | 

### Return type

[**EsitoFormularioModel**](EsitoFormularioModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esito dell&#39;elaborazione con eventuali errori |  -  |
**400** | Richiesta non ancora elaborata |  -  |
**403** | Operazione non consentita |  -  |
**404** | Richiesta non trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **transazione_id_status_get**
> transazione_id_status_get(transazione_id)

Stato transazione

Ottiene lo stato di elaborazione di una richiesta di elaborazione per un formulario.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://api.rentri.gov.it/formulari/v1.0"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = rentri_formulari.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with rentri_formulari.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = rentri_formulari.DefaultApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta.

    try:
        # Stato transazione
        api_instance.transazione_id_status_get(transazione_id)
    except Exception as e:
        print("Exception when calling DefaultApi->transazione_id_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transazione_id** | **str**| Id della richiesta. | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Richiesta non ancora elaborata |  -  |
**303** | La richiesta è stata elaborata e l&#39;URL per il recupero dell&#39;esito si trova nell&#39;header Location |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Bad Request |  -  |
**403** | Operazione non consentita |  -  |
**404** | L&#39;Id della transazione specificata non è stata trovato |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

