# rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi

All URIs are relative to *https://api.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**trasmissioni_soggetto_delegato_num_iscr_sito_get**](TrasmissioneDatiSoggettoDelegatoApi.md#trasmissioni_soggetto_delegato_num_iscr_sito_get) | **GET** /trasmissioni/soggetto-delegato/{num_iscr_sito} | Trasmissioni effettuate
[**trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete**](TrasmissioneDatiSoggettoDelegatoApi.md#trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete) | **DELETE** /trasmissioni/soggetto-delegato/{num_iscr_sito}/{identificativo}/annulla | Annulla trasmissione di dati del FIR digitale
[**trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get**](TrasmissioneDatiSoggettoDelegatoApi.md#trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get) | **GET** /trasmissioni/soggetto-delegato/{num_iscr_sito}/{identificativo} | Dettaglio trasmissione
[**trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post**](TrasmissioneDatiSoggettoDelegatoApi.md#trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post) | **POST** /trasmissioni/soggetto-delegato/{num_iscr_sito}/{numero_fir}/estrai | 🔁[ASYNC] Estrazione dati per FIR digitale
[**trasmissioni_soggetto_delegato_num_iscr_sito_post**](TrasmissioneDatiSoggettoDelegatoApi.md#trasmissioni_soggetto_delegato_num_iscr_sito_post) | **POST** /trasmissioni/soggetto-delegato/{num_iscr_sito} | Trasmette i dati del FIR digitale


# **trasmissioni_soggetto_delegato_num_iscr_sito_get**
> List[TrasmissioneDatiItemResult] trasmissioni_soggetto_delegato_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, data_trasmissione_da=data_trasmissione_da, data_trasmissione_a=data_trasmissione_a, codice_eer=codice_eer, tipo=tipo, stato=stato, paging_page=paging_page, paging_page_size=paging_page_size)

Trasmissioni effettuate

Ottiene la lista delle trasmissioni di dati di FIR digitali effettuate per l'unità locale specificata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.trasmissione_dati_item_result import TrasmissioneDatiItemResult
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
    api_instance = rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione dell'unità locale per cui si vogliono recuperare le trasmissioni
    numero_fir = 'numero_fir_example' # str |  (optional)
    data_trasmissione_da = '2013-10-20T19:20:30+01:00' # datetime | Formato ISO 8601 UTC (optional)
    data_trasmissione_a = '2013-10-20T19:20:30+01:00' # datetime | Formato ISO 8601 UTC (optional)
    codice_eer = 'codice_eer_example' # str |  (optional)
    tipo = rentri_formulari.TipoTrasmissione() # TipoTrasmissione |  (optional)
    stato = rentri_formulari.StatiTrasmissioneDati() # StatiTrasmissioneDati |  (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)

    try:
        # Trasmissioni effettuate
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, data_trasmissione_da=data_trasmissione_da, data_trasmissione_a=data_trasmissione_a, codice_eer=codice_eer, tipo=tipo, stato=stato, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione dell&#39;unità locale per cui si vogliono recuperare le trasmissioni | 
 **numero_fir** | **str**|  | [optional] 
 **data_trasmissione_da** | **datetime**| Formato ISO 8601 UTC | [optional] 
 **data_trasmissione_a** | **datetime**| Formato ISO 8601 UTC | [optional] 
 **codice_eer** | **str**|  | [optional] 
 **tipo** | [**TipoTrasmissione**](.md)|  | [optional] 
 **stato** | [**StatiTrasmissioneDati**](.md)|  | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize | [optional] [default to 100]

### Return type

[**List[TrasmissioneDatiItemResult]**](TrasmissioneDatiItemResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete**
> trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete(num_iscr_sito, identificativo)

Annulla trasmissione di dati del FIR digitale

Pone in stato \"annullata\" la trasmissione di dati del FIR digitale specificata.  L'operazione non è reversibile.

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
    api_instance = rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | 
    identificativo = 'identificativo_example' # str | 

    try:
        # Annulla trasmissione di dati del FIR digitale
        api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete(num_iscr_sito, identificativo)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_annulla_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**|  | 
 **identificativo** | **str**|  | 

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
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get**
> TrasmissioneDatiResult trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)

Dettaglio trasmissione

Recupera le informazioni di dettaglio della trasmissione di dati di FIR digitale corrispondente all'identificativo specificato

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.trasmissione_dati_result import TrasmissioneDatiResult
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
    api_instance = rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione dell'unità locale per cui si vogliono recuperare le trasmissioni
    identificativo = 'identificativo_example' # str | Identificativo della trasmissione

    try:
        # Dettaglio trasmissione
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione dell&#39;unità locale per cui si vogliono recuperare le trasmissioni | 
 **identificativo** | **str**| Identificativo della trasmissione | 

### Return type

[**TrasmissioneDatiResult**](TrasmissioneDatiResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post**
> TransazioneModel trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post(num_iscr_sito, numero_fir, estrai_dati_xfir_model, x_reply_to=x_reply_to)

🔁[ASYNC] Estrazione dati per FIR digitale

Effettua l'estrazione dei dati che devono essere trasmessi dal file del FIR digitale che viene specificato tra i dati della richiesta.  Il file del FIR digitale inviato deve essere firmato digitalmente e deve essere valido secondo le regole definite dalle specifiche xFIR e verificabile dalla specifica funzione di validazione definita dall'endpoint dell'API<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.estrai_dati_xfir_model import EstraiDatiXfirModel
from rentri_formulari.models.transazione_model import TransazioneModel
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
    api_instance = rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | 
    numero_fir = 'numero_fir_example' # str | 
    estrai_dati_xfir_model = rentri_formulari.EstraiDatiXfirModel() # EstraiDatiXfirModel | 
    x_reply_to = 'x_reply_to_example' # str |  (optional)

    try:
        # 🔁[ASYNC] Estrazione dati per FIR digitale
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post(num_iscr_sito, numero_fir, estrai_dati_xfir_model, x_reply_to=x_reply_to)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**|  | 
 **numero_fir** | **str**|  | 
 **estrai_dati_xfir_model** | [**EstraiDatiXfirModel**](EstraiDatiXfirModel.md)|  | 
 **x_reply_to** | **str**|  | [optional] 

### Return type

[**TransazioneModel**](TransazioneModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_post**
> TrasmissioneFormularioResponse trasmissioni_soggetto_delegato_num_iscr_sito_post(num_iscr_sito, dati_trasmissione_formulario_model)

Trasmette i dati del FIR digitale

Effettua la trasmissione dei dati estratti da un FIR digitale riferibili all'unità locale specificata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_trasmissione_formulario_model import DatiTrasmissioneFormularioModel
from rentri_formulari.models.trasmissione_formulario_response import TrasmissioneFormularioResponse
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
    api_instance = rentri_formulari.TrasmissioneDatiSoggettoDelegatoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | 
    dati_trasmissione_formulario_model = rentri_formulari.DatiTrasmissioneFormularioModel() # DatiTrasmissioneFormularioModel | 

    try:
        # Trasmette i dati del FIR digitale
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_post(num_iscr_sito, dati_trasmissione_formulario_model)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**|  | 
 **dati_trasmissione_formulario_model** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md)|  | 

### Return type

[**TrasmissioneFormularioResponse**](TrasmissioneFormularioResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Created |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

