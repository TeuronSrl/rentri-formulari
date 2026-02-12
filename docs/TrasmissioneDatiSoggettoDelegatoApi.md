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
> List[TrasmissioneDatiItemResult] trasmissioni_soggetto_delegato_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, data_trasmissione_da=data_trasmissione_da, data_trasmissione_a=data_trasmissione_a, codice_eer=codice_eer, tipo=tipo, stato=stato, includi_trasportatore_per_conto_produttore=includi_trasportatore_per_conto_produttore, paging_page=paging_page, paging_page_size=paging_page_size)

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
    numero_fir = 'numero_fir_example' # str | Numero del FIR oggetto della trasmissione (optional)
    data_trasmissione_da = '2013-10-20T19:20:30+01:00' # datetime | Formato ISO 8601 UTC (optional)
    data_trasmissione_a = '2013-10-20T19:20:30+01:00' # datetime | Formato ISO 8601 UTC (optional)
    codice_eer = 'codice_eer_example' # str | Codice EER del rifiuto indicati nei formulari oggetto della trasmissione FIR da elencare (optional)
    tipo = rentri_formulari.TipoTrasmissione() # TipoTrasmissione | Tipo di trasmissione (optional)
    stato = rentri_formulari.StatiTrasmissioneDati() # StatiTrasmissioneDati | Stato della trasmissione (optional)
    includi_trasportatore_per_conto_produttore = True # bool | Indica se includere nella ricerca anche le eventuali trasmissioni effettuate dall'operatore indicato nel parametro di rottta <i>numIscrSito</i> in qualità di primo trasportatore per conto del produttore del rifiuto (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)

    try:
        # Trasmissioni effettuate
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, data_trasmissione_da=data_trasmissione_da, data_trasmissione_a=data_trasmissione_a, codice_eer=codice_eer, tipo=tipo, stato=stato, includi_trasportatore_per_conto_produttore=includi_trasportatore_per_conto_produttore, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione dell&#39;unità locale per cui si vogliono recuperare le trasmissioni | 
 **numero_fir** | **str**| Numero del FIR oggetto della trasmissione | [optional] 
 **data_trasmissione_da** | **datetime**| Formato ISO 8601 UTC | [optional] 
 **data_trasmissione_a** | **datetime**| Formato ISO 8601 UTC | [optional] 
 **codice_eer** | **str**| Codice EER del rifiuto indicati nei formulari oggetto della trasmissione FIR da elencare | [optional] 
 **tipo** | [**TipoTrasmissione**](.md)| Tipo di trasmissione | [optional] 
 **stato** | [**StatiTrasmissioneDati**](.md)| Stato della trasmissione | [optional] 
 **includi_trasportatore_per_conto_produttore** | **bool**| Indica se includere nella ricerca anche le eventuali trasmissioni effettuate dall&#39;operatore indicato nel parametro di rottta &lt;i&gt;numIscrSito&lt;/i&gt; in qualità di primo trasportatore per conto del produttore del rifiuto | [optional] 
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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post**
> TransazioneModel trasmissioni_soggetto_delegato_num_iscr_sito_numero_fir_estrai_post(num_iscr_sito, numero_fir, estrai_dati_xfir_model, x_reply_to=x_reply_to)

🔁[ASYNC] Estrazione dati per FIR digitale

Effettua l'estrazione dei dati che devono essere trasmessi dal file del FIR digitale che viene specificato tra i dati della richiesta.     L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto operatore a cui afferisce il numero di iscrizione dell'unità locale indicato nel parametro <b>num_iscr_sito</b>.            Il file xFIR inviato deve essere valido secondo le regole definite nella <i>Guida tecnica alla compilazione del FIR digitale</i>   e verificabile dalla specifica funzione di validazione definita dall'endpoint <i>Validazione xFIR</i> delle API \"Formulario digitale\".    Il file xFIR non deve contenere dati pertinenti al formulario non firmati digitalmente.     La dimensione massima accettata del file xFIR da cui estrarre i dati è 3 MB.    Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **trasmissioni_soggetto_delegato_num_iscr_sito_post**
> TrasmissioneFormularioResponse trasmissioni_soggetto_delegato_num_iscr_sito_post(num_iscr_sito, dati_trasmissione_formulario_model, num_iscr_sito_trasportatore=num_iscr_sito_trasportatore)

Trasmette i dati del FIR digitale

Effettua la trasmissione dei dati estratti da un FIR digitale riferibile all'unità locale specificata in <b>num_iscr_sito</b>.   Se non viene specificato il parametro <b>num_iscr_sito_trasportatore</b>, l'operazione può essere richiesta solo da un'utenza che abbia incarichi per (o coincida con)  il soggetto operatore a cui afferisce il numero di iscrizione dell'unità locale indicato nel parametro <b>num_iscr_sito</b>.  Tale soggetto deve essere uno dei soggetti coinvolti nel formulario che viene trasmesso.  Se viene specificato il parametro <b>num_iscr_sito_trasportatore</b>, l'operazione di trasmissione è intesa come effettuata dal trasportatore per conto del produttore,  e può essere richiesta solo da un'utenza che abbia incarichi per (o coincida con) il soggetto trasportatore a cui afferisce il numero di iscrizione dell'unità locale indicato in questo parametro.  Questo soggetto deve essere quello indicato come primo trasportatore nei dati del formulario che viene trasmesso, mentre il valore di <b>num_iscr_sito</b> deve riferirsi al soggetto produttore. La trasmissione dei dati del FIR digitale effettuata dal trasportatore per conto del produttore è possibile solo se il numero FIR è stato vidimato al trasportatore.  È possibile trasmettere più volte i dati dello stesso formulario relativamente ad una stessa unità locale.  In caso di trasmissioni ripetute per numero FIR e unità locale, l'ultima trasmissione dati effettuata in ordine temporale annulla e sostituisce le precedenti.

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
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero di iscrizione dell'unità locale alla quale è riferita la trasmissione dei dati del FIR digitale
    dati_trasmissione_formulario_model = rentri_formulari.DatiTrasmissioneFormularioModel() # DatiTrasmissioneFormularioModel | Dati del FIR digitale trasmessi
    num_iscr_sito_trasportatore = 'num_iscr_sito_trasportatore_example' # str | Eventuale numero di iscrizione dell'unità locale del trasportatore che effettua la trasmissione per conto del produttore (optional)

    try:
        # Trasmette i dati del FIR digitale
        api_response = api_instance.trasmissioni_soggetto_delegato_num_iscr_sito_post(num_iscr_sito, dati_trasmissione_formulario_model, num_iscr_sito_trasportatore=num_iscr_sito_trasportatore)
        print("The response of TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TrasmissioneDatiSoggettoDelegatoApi->trasmissioni_soggetto_delegato_num_iscr_sito_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero di iscrizione dell&#39;unità locale alla quale è riferita la trasmissione dei dati del FIR digitale | 
 **dati_trasmissione_formulario_model** | [**DatiTrasmissioneFormularioModel**](DatiTrasmissioneFormularioModel.md)| Dati del FIR digitale trasmessi | 
 **num_iscr_sito_trasportatore** | **str**| Eventuale numero di iscrizione dell&#39;unità locale del trasportatore che effettua la trasmissione per conto del produttore | [optional] 

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
**201** | Created |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

