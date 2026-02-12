# rentri_formulari.CopiaFIRCartaceoApi

All URIs are relative to *https://api.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copia_cartacea_caricamento_num_iscr_sito_get**](CopiaFIRCartaceoApi.md#copia_cartacea_caricamento_num_iscr_sito_get) | **GET** /copia-cartacea/caricamento/{num_iscr_sito} | Elenco copie FIR cartaceo caricate
[**copia_cartacea_caricamento_num_iscr_sito_identificativo_delete**](CopiaFIRCartaceoApi.md#copia_cartacea_caricamento_num_iscr_sito_identificativo_delete) | **DELETE** /copia-cartacea/caricamento/{num_iscr_sito}/{identificativo} | Cancella copia FIR cartaceo
[**copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get**](CopiaFIRCartaceoApi.md#copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get) | **GET** /copia-cartacea/caricamento/{num_iscr_sito}/{identificativo}/documento | Documento copia FIR cartaceo
[**copia_cartacea_caricamento_num_iscr_sito_identificativo_get**](CopiaFIRCartaceoApi.md#copia_cartacea_caricamento_num_iscr_sito_identificativo_get) | **GET** /copia-cartacea/caricamento/{num_iscr_sito}/{identificativo} | Dettaglio copia FIR cartaceo
[**copia_cartacea_caricamento_num_iscr_sito_post**](CopiaFIRCartaceoApi.md#copia_cartacea_caricamento_num_iscr_sito_post) | **POST** /copia-cartacea/caricamento/{num_iscr_sito} | 🔁[ASYNC] Carica copia FIR cartaceo
[**copia_cartacea_conferma_identificativo_soggetto_get**](CopiaFIRCartaceoApi.md#copia_cartacea_conferma_identificativo_soggetto_get) | **GET** /copia-cartacea/conferma/{identificativo_soggetto} | Copie FIR cartacei disponibili
[**copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get**](CopiaFIRCartaceoApi.md#copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get) | **GET** /copia-cartacea/conferma/{identificativo_soggetto}/{identificativo}/documento | Documento copia FIR cartaceo disponibile
[**copia_cartacea_conferma_identificativo_soggetto_identificativo_get**](CopiaFIRCartaceoApi.md#copia_cartacea_conferma_identificativo_soggetto_identificativo_get) | **GET** /copia-cartacea/conferma/{identificativo_soggetto}/{identificativo} | Dettaglio copia FIR cartaceo disponibile
[**copia_cartacea_conferma_identificativo_soggetto_put**](CopiaFIRCartaceoApi.md#copia_cartacea_conferma_identificativo_soggetto_put) | **PUT** /copia-cartacea/conferma/{identificativo_soggetto} | Conferma copia FIR cartaceo disponibile
[**copia_cartacea_transazione_id_result_get**](CopiaFIRCartaceoApi.md#copia_cartacea_transazione_id_result_get) | **GET** /copia-cartacea/{transazione_id}/result | ⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione
[**copia_cartacea_transazione_id_status_get**](CopiaFIRCartaceoApi.md#copia_cartacea_transazione_id_status_get) | **GET** /copia-cartacea/{transazione_id}/status | ⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione


# **copia_cartacea_caricamento_num_iscr_sito_get**
> List[CopiaCartaceaResult] copia_cartacea_caricamento_num_iscr_sito_get(num_iscr_sito, paging_page=paging_page, paging_page_size=paging_page_size, numero_fir=numero_fir, confermate=confermate)

Elenco copie FIR cartaceo caricate

Ottiene la lista delle copie dei FIR cartacei caricate dall'unità locale del trasportatore.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_result import CopiaCartaceaResult
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del trasportatore che ha caricato le copie dei FIR cartacei             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)
    numero_fir = 'numero_fir_example' # str | Pattern per filtrare i numeri delle copie dei FIR cartacei da restituire (optional)
    confermate = True # bool | Opzione per filtrare solo le copie dei FIR cartacei confermate o solo quelle non confermate, non specificare il valore per averle tutte (optional)

    try:
        # Elenco copie FIR cartaceo caricate
        api_response = api_instance.copia_cartacea_caricamento_num_iscr_sito_get(num_iscr_sito, paging_page=paging_page, paging_page_size=paging_page_size, numero_fir=numero_fir, confermate=confermate)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del trasportatore che ha caricato le copie dei FIR cartacei             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize | [optional] [default to 100]
 **numero_fir** | **str**| Pattern per filtrare i numeri delle copie dei FIR cartacei da restituire | [optional] 
 **confermate** | **bool**| Opzione per filtrare solo le copie dei FIR cartacei confermate o solo quelle non confermate, non specificare il valore per averle tutte | [optional] 

### Return type

[**List[CopiaCartaceaResult]**](CopiaCartaceaResult.md)

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_caricamento_num_iscr_sito_identificativo_delete**
> copia_cartacea_caricamento_num_iscr_sito_identificativo_delete(num_iscr_sito, identificativo)

Cancella copia FIR cartaceo

Elimina il caricamento della copia del FIR cartaceo. L'operazione è possibile solo se nessuno dei soggetti a cui è stata resa disponibile la copia del FIR cartaceo l'ha già presa in carico con l'operazione di conferma.

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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR cartaceo da cancellare

    try:
        # Cancella copia FIR cartaceo
        api_instance.copia_cartacea_caricamento_num_iscr_sito_identificativo_delete(num_iscr_sito, identificativo)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_identificativo_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR cartaceo da cancellare | 

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
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get**
> DownloadableBaseResponse copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get(num_iscr_sito, identificativo)

Documento copia FIR cartaceo

Restituisce il file contenente la copia del FIR cartaceo caricata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.downloadable_base_response import DownloadableBaseResponse
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR cartaceo della quale restituire il documento caricato

    try:
        # Documento copia FIR cartaceo
        api_response = api_instance.copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get(num_iscr_sito, identificativo)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_identificativo_documento_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR cartaceo della quale restituire il documento caricato | 

### Return type

[**DownloadableBaseResponse**](DownloadableBaseResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_caricamento_num_iscr_sito_identificativo_get**
> CopiaCartaceaResult copia_cartacea_caricamento_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)

Dettaglio copia FIR cartaceo

Recupera le informazioni di dettaglio del caricamento della copia del FIR cartaceo specificata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_result import CopiaCartaceaResult
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR cartaceo

    try:
        # Dettaglio copia FIR cartaceo
        api_response = api_instance.copia_cartacea_caricamento_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del trasportatore che ha caricato la copia del FIR cartaceo             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR cartaceo | 

### Return type

[**CopiaCartaceaResult**](CopiaCartaceaResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_caricamento_num_iscr_sito_post**
> TransazioneModel copia_cartacea_caricamento_num_iscr_sito_post(num_iscr_sito, copia_cartacea_model, x_reply_to=x_reply_to)

🔁[ASYNC] Carica copia FIR cartaceo

Acquisisce la richiesta di restituzione della copia del FIR cartaceo che consente al Trasportatore di renderla disponibile ai soggetti specificati.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.   Il file caricato deve essere in uno dei seguenti formati: PDF, JPG, PNG.  Il file non deve superare la dimensione di 5 MB. <br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_model import CopiaCartaceaModel
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del trasportatore che carica la copia del FIR cartaceo. Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    copia_cartacea_model = rentri_formulari.CopiaCartaceaModel() # CopiaCartaceaModel | Dati relativi alla copia del FIR cartaceo e ai soggetti a cui la si rende disponibile
    x_reply_to = 'x_reply_to_example' # str | URL di callback opzionale alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Carica copia FIR cartaceo
        api_response = api_instance.copia_cartacea_caricamento_num_iscr_sito_post(num_iscr_sito, copia_cartacea_model, x_reply_to=x_reply_to)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_caricamento_num_iscr_sito_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del trasportatore che carica la copia del FIR cartaceo. Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **copia_cartacea_model** | [**CopiaCartaceaModel**](CopiaCartaceaModel.md)| Dati relativi alla copia del FIR cartaceo e ai soggetti a cui la si rende disponibile | 
 **x_reply_to** | **str**| URL di callback opzionale alla quale verrà inviata la notifica di fine elaborazione | [optional] 

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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_conferma_identificativo_soggetto_get**
> List[CopiaCartaceaResult] copia_cartacea_conferma_identificativo_soggetto_get(identificativo_soggetto, numero_fir=numero_fir, confermate=confermate, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, num_iscr_sito=num_iscr_sito, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)

Copie FIR cartacei disponibili

Ottiene la lista delle copie dei FIR cartacei, disponibili per la conferma o già confermati, per il soggetto specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_result import CopiaCartaceaResult
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per cui richiedere l'elenco delle copie dei FIR cartacei disponibili
    numero_fir = 'numero_fir_example' # str | Numero FIR della copia del FIR cartaceo (optional)
    confermate = True # bool | Filtra le copie dei FIR digitali confermate o non confermate. (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    num_iscr_sito = 'num_iscr_sito_example' # str | Eventuale numero di iscrizione dell'unità locale per la quale si richiedeono le copie cartacee dei FIR. Se non indicato ma si richiedono le sole copie cartacee confermate, verranno restituite solo le copie cartacee che sono state confermate senza essere associate ad alcuna unità locale (optional)
    ruolo = rentri_formulari.RuoloConfermaCopiaCartacea() # RuoloConfermaCopiaCartacea | Specifica il ruolo per cui si richiedono le copie cartacee dei FIR.  Se non indicato ma si indica una unità locale, vengono considerati tutti i ruoli associati all'unità locale specificata. (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)

    try:
        # Copie FIR cartacei disponibili
        api_response = api_instance.copia_cartacea_conferma_identificativo_soggetto_get(identificativo_soggetto, numero_fir=numero_fir, confermate=confermate, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, num_iscr_sito=num_iscr_sito, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per cui richiedere l&#39;elenco delle copie dei FIR cartacei disponibili | 
 **numero_fir** | **str**| Numero FIR della copia del FIR cartaceo | [optional] 
 **confermate** | **bool**| Filtra le copie dei FIR digitali confermate o non confermate. | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **num_iscr_sito** | **str**| Eventuale numero di iscrizione dell&#39;unità locale per la quale si richiedeono le copie cartacee dei FIR. Se non indicato ma si richiedono le sole copie cartacee confermate, verranno restituite solo le copie cartacee che sono state confermate senza essere associate ad alcuna unità locale | [optional] 
 **ruolo** | [**RuoloConfermaCopiaCartacea**](.md)| Specifica il ruolo per cui si richiedono le copie cartacee dei FIR.  Se non indicato ma si indica una unità locale, vengono considerati tutti i ruoli associati all&#39;unità locale specificata. | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize | [optional] [default to 100]

### Return type

[**List[CopiaCartaceaResult]**](CopiaCartaceaResult.md)

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get**
> DownloadableBaseResponse copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get(identificativo_soggetto, identificativo)

Documento copia FIR cartaceo disponibile

Restituisce il documento della copia del FIR cartaceo specificata caricata dal trasportatore.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.downloadable_base_response import DownloadableBaseResponse
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per il quale si richiede il documento della copia del FIR cartaceo
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR cartaceo caricata dal trasportatore

    try:
        # Documento copia FIR cartaceo disponibile
        api_response = api_instance.copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get(identificativo_soggetto, identificativo)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_identificativo_documento_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per il quale si richiede il documento della copia del FIR cartaceo | 
 **identificativo** | **str**| Identificativo della copia del FIR cartaceo caricata dal trasportatore | 

### Return type

[**DownloadableBaseResponse**](DownloadableBaseResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**204** | No Content |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_conferma_identificativo_soggetto_identificativo_get**
> CopiaCartaceaResult copia_cartacea_conferma_identificativo_soggetto_identificativo_get(identificativo_soggetto, identificativo)

Dettaglio copia FIR cartaceo disponibile

Restituisce il dettaglio dei dati di caricamento della copia del FIR cartaceo caricata dal trasportatore.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_result import CopiaCartaceaResult
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto a cui è resa disponibile la copia del FIR cartaceo
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR cartaceo per cui vengono richieste le informazioni di dettaglio

    try:
        # Dettaglio copia FIR cartaceo disponibile
        api_response = api_instance.copia_cartacea_conferma_identificativo_soggetto_identificativo_get(identificativo_soggetto, identificativo)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto a cui è resa disponibile la copia del FIR cartaceo | 
 **identificativo** | **str**| Identificativo della copia del FIR cartaceo per cui vengono richieste le informazioni di dettaglio | 

### Return type

[**CopiaCartaceaResult**](CopiaCartaceaResult.md)

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_conferma_identificativo_soggetto_put**
> copia_cartacea_conferma_identificativo_soggetto_put(identificativo_soggetto, copia_cartacea_conferma_model)

Conferma copia FIR cartaceo disponibile

Pone in stato \"confermata\" la copia del FIR cartaceo specificata associandola all'unità locale specificata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_cartacea_conferma_model import CopiaCartaceaConfermaModel
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per il quale si conferma la copia del FIR cartaceo
    copia_cartacea_conferma_model = rentri_formulari.CopiaCartaceaConfermaModel() # CopiaCartaceaConfermaModel | Struttura dati contenente l'identificativo della copia del FIR cartaceo e l'eventuale identificativo dell'unità locale a cui associare la conferma

    try:
        # Conferma copia FIR cartaceo disponibile
        api_instance.copia_cartacea_conferma_identificativo_soggetto_put(identificativo_soggetto, copia_cartacea_conferma_model)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_conferma_identificativo_soggetto_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per il quale si conferma la copia del FIR cartaceo | 
 **copia_cartacea_conferma_model** | [**CopiaCartaceaConfermaModel**](CopiaCartaceaConfermaModel.md)| Struttura dati contenente l&#39;identificativo della copia del FIR cartaceo e l&#39;eventuale identificativo dell&#39;unità locale a cui associare la conferma | 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | No Content |  -  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_transazione_id_result_get**
> EsitoCopiaCartaceaModel copia_cartacea_transazione_id_result_get(transazione_id)

⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione

Ottiene l'esito dell'elaborazione di una richiesta asincrona.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.esito_copia_cartacea_model import EsitoCopiaCartaceaModel
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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta

    try:
        # ⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione
        api_response = api_instance.copia_cartacea_transazione_id_result_get(transazione_id)
        print("The response of CopiaFIRCartaceoApi->copia_cartacea_transazione_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_transazione_id_result_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transazione_id** | **str**| Id della richiesta | 

### Return type

[**EsitoCopiaCartaceaModel**](EsitoCopiaCartaceaModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esito dell&#39;elaborazione con eventuali errori. |  -  |
**400** | Richiesta non ancora elaborata. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Richiesta non trovata. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_cartacea_transazione_id_status_get**
> copia_cartacea_transazione_id_status_get(transazione_id)

⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione

Ottiene lo stato di elaborazione di una richiesta di vidimazione FIR.

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
    api_instance = rentri_formulari.CopiaFIRCartaceoApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta

    try:
        # ⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione
        api_instance.copia_cartacea_transazione_id_status_get(transazione_id)
    except Exception as e:
        print("Exception when calling CopiaFIRCartaceoApi->copia_cartacea_transazione_id_status_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transazione_id** | **str**| Id della richiesta | 

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
**200** | Richiesta non ancora elaborata. |  -  |
**303** | La richiesta è stata elaborata e l&#39;URL per il recupero dell&#39;esito si trova nell&#39;header Location. |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Bad Request |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Richiesta non trovata. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

