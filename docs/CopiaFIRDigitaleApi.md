# rentri_formulari.CopiaFIRDigitaleApi

All URIs are relative to *https://api.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**copia_digitale_caricamento_num_iscr_sito_get**](CopiaFIRDigitaleApi.md#copia_digitale_caricamento_num_iscr_sito_get) | **GET** /copia-digitale/caricamento/{num_iscr_sito} | Copie FIR digitali caricate
[**copia_digitale_caricamento_num_iscr_sito_identificativo_delete**](CopiaFIRDigitaleApi.md#copia_digitale_caricamento_num_iscr_sito_identificativo_delete) | **DELETE** /copia-digitale/caricamento/{num_iscr_sito}/{identificativo} | Cancella copia FIR digitale
[**copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get**](CopiaFIRDigitaleApi.md#copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get) | **GET** /copia-digitale/caricamento/{num_iscr_sito}/{identificativo}/documento | Documento copia FIR digitale
[**copia_digitale_caricamento_num_iscr_sito_identificativo_get**](CopiaFIRDigitaleApi.md#copia_digitale_caricamento_num_iscr_sito_identificativo_get) | **GET** /copia-digitale/caricamento/{num_iscr_sito}/{identificativo} | Dettaglio copia FIR digitale
[**copia_digitale_caricamento_numero_fir_post**](CopiaFIRDigitaleApi.md#copia_digitale_caricamento_numero_fir_post) | **POST** /copia-digitale/caricamento/{numero_fir} | 🔁[ASYNC] Carica copia FIR digitale
[**copia_digitale_conferma_identificativo_soggetto_get**](CopiaFIRDigitaleApi.md#copia_digitale_conferma_identificativo_soggetto_get) | **GET** /copia-digitale/conferma/{identificativo_soggetto} | Copie FIR digitali disponibili
[**copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get**](CopiaFIRDigitaleApi.md#copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get) | **GET** /copia-digitale/conferma/{identificativo_soggetto}/{identificativo}/documento | Documento copia FIR digitale disponibile
[**copia_digitale_conferma_identificativo_soggetto_identificativo_get**](CopiaFIRDigitaleApi.md#copia_digitale_conferma_identificativo_soggetto_identificativo_get) | **GET** /copia-digitale/conferma/{identificativo_soggetto}/{identificativo} | Dettaglio copia digitale FIR disponibile
[**copia_digitale_conferma_num_iscr_sito_identificativo_put**](CopiaFIRDigitaleApi.md#copia_digitale_conferma_num_iscr_sito_identificativo_put) | **PUT** /copia-digitale/conferma/{num_iscr_sito}/{identificativo} | Conferma copia FIR digitale disponibile
[**copia_digitale_transazione_id_result_get**](CopiaFIRDigitaleApi.md#copia_digitale_transazione_id_result_get) | **GET** /copia-digitale/{transazione_id}/result | ⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione
[**copia_digitale_transazione_id_status_get**](CopiaFIRDigitaleApi.md#copia_digitale_transazione_id_status_get) | **GET** /copia-digitale/{transazione_id}/status | ⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione


# **copia_digitale_caricamento_num_iscr_sito_get**
> List[CopiaDigitaleItemResult] copia_digitale_caricamento_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, tipo_accettazione=tipo_accettazione, confermate=confermate, comune_id=comune_id, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)

Copie FIR digitali caricate

Ottiene la lista delle copie dei FIR digitali caricate dal destinatario e rese disponibili agli altri soggetti del FIR.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_digitale_item_result import CopiaDigitaleItemResult
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del destinatario che ha caricato le copie dei FIR digitali
    numero_fir = 'numero_fir_example' # str | Numero FIR della copia del FIR digitale (optional)
    tipo_accettazione = rentri_formulari.TipiAccettazione() # TipiAccettazione | Filtra le copia dei FIR digitali per tipo di accettazione del destinatario (optional)
    confermate = True # bool | Filtra le copie dei FIR digitali confermate o non confermate. (optional)
    comune_id = 'comune_id_example' # str | Filtra le copie dei FIR digitali per il comune. Il valore viene considerato solo per il ruolo di produttore (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Filta le copie digiitali dei FIR per il codice EER del rifiuto (optional)
    ruolo = rentri_formulari.RuoloConfermaCopiaDigitale() # RuoloConfermaCopiaDigitale | Ruolo per il quale si richiedono le copie dei FIR digitali da confermare (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)

    try:
        # Copie FIR digitali caricate
        api_response = api_instance.copia_digitale_caricamento_num_iscr_sito_get(num_iscr_sito, numero_fir=numero_fir, tipo_accettazione=tipo_accettazione, confermate=confermate, comune_id=comune_id, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del destinatario che ha caricato le copie dei FIR digitali | 
 **numero_fir** | **str**| Numero FIR della copia del FIR digitale | [optional] 
 **tipo_accettazione** | [**TipiAccettazione**](.md)| Filtra le copia dei FIR digitali per tipo di accettazione del destinatario | [optional] 
 **confermate** | **bool**| Filtra le copie dei FIR digitali confermate o non confermate. | [optional] 
 **comune_id** | **str**| Filtra le copie dei FIR digitali per il comune. Il valore viene considerato solo per il ruolo di produttore | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Filta le copie digiitali dei FIR per il codice EER del rifiuto | [optional] 
 **ruolo** | [**RuoloConfermaCopiaDigitale**](.md)| Ruolo per il quale si richiedono le copie dei FIR digitali da confermare | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize | [optional] [default to 100]

### Return type

[**List[CopiaDigitaleItemResult]**](CopiaDigitaleItemResult.md)

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

# **copia_digitale_caricamento_num_iscr_sito_identificativo_delete**
> copia_digitale_caricamento_num_iscr_sito_identificativo_delete(num_iscr_sito, identificativo)

Cancella copia FIR digitale

Elimina il caricamento della copia del FIR digitale. L'operazione è possibile solo se nessuno dei soggetti a cui è stata resa disponibile la copia del FIR digitale ne ha già preso visione con l'operazione di conferma.

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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale da cancellare

    try:
        # Cancella copia FIR digitale
        api_instance.copia_digitale_caricamento_num_iscr_sito_identificativo_delete(num_iscr_sito, identificativo)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_identificativo_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale da cancellare | 

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

# **copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get**
> DownloadableBaseResponse copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get(num_iscr_sito, identificativo)

Documento copia FIR digitale

Restituisce il file xFIR precedentemente caricato dal destinatario stesso.

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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale della quale restituire il documento caricato

    try:
        # Documento copia FIR digitale
        api_response = api_instance.copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get(num_iscr_sito, identificativo)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_identificativo_documento_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale della quale restituire il documento caricato | 

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

# **copia_digitale_caricamento_num_iscr_sito_identificativo_get**
> CopiaDigitaleResult copia_digitale_caricamento_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)

Dettaglio copia FIR digitale

Recupera le informazioni di dettaglio del caricamento della copia del FIR digitale.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_digitale_result import CopiaDigitaleResult
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale

    try:
        # Dettaglio copia FIR digitale
        api_response = api_instance.copia_digitale_caricamento_num_iscr_sito_identificativo_get(num_iscr_sito, identificativo)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_caricamento_num_iscr_sito_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del destinatario che ha caricato la copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale | 

### Return type

[**CopiaDigitaleResult**](CopiaDigitaleResult.md)

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

# **copia_digitale_caricamento_numero_fir_post**
> TransazioneModel copia_digitale_caricamento_numero_fir_post(numero_fir, copia_digitale_model, x_reply_to=x_reply_to)

🔁[ASYNC] Carica copia FIR digitale

Acquisisce la richiesta di chiusura del ciclo di vita del FIR mediante invio, da parte del destinatario del formulario, del file xFIR che ne contiene le informazioni.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto operatore a cui afferisce il numero di iscrizione dell'unità locale indicato nel parametro <b>num_iscr_sito</b>.  L'unità locale specificata nel parametro <b>num_iscr_sito</b> deve essere iscritta con attività di <i>Recupero</i> o <i>Smaltimento</i> o <i>Centro di raccolta</i> e deve risultare come il soggetto destinatario del formulario.  Il formulario caricato deve essere nello stato <i>Accettato</i> o <i>RespintoAccettatoParzialmente</i>.  Il file xFIR inviato deve essere valido secondo le regole definite nella <i>Guida tecnica alla compilazione del FIR digitale</i>  e verificabile dalla specifica funzione di validazione definita dall'endpoint <i>Validazione xFIR</i> delle API \"Formulario digitale\".  La dimensione massima accettata del file xFIR è 3 MB.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito. <br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_digitale_model import CopiaDigitaleModel
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero del FIR incluso nel file xFIR
    copia_digitale_model = rentri_formulari.CopiaDigitaleModel() # CopiaDigitaleModel | Oggetto contenente il contenuto del file xFIR
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Carica copia FIR digitale
        api_response = api_instance.copia_digitale_caricamento_numero_fir_post(numero_fir, copia_digitale_model, x_reply_to=x_reply_to)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_caricamento_numero_fir_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_caricamento_numero_fir_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero del FIR incluso nel file xFIR | 
 **copia_digitale_model** | [**CopiaDigitaleModel**](CopiaDigitaleModel.md)| Oggetto contenente il contenuto del file xFIR | 
 **x_reply_to** | **str**| URL di callback alla quale verrà inviata la notifica di fine elaborazione | [optional] 

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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_digitale_conferma_identificativo_soggetto_get**
> List[CopiaDigitaleItemResult] copia_digitale_conferma_identificativo_soggetto_get(identificativo_soggetto, num_iscr_sito=num_iscr_sito, numero_fir=numero_fir, tipo_accettazione=tipo_accettazione, confermate=confermate, comune_id=comune_id, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)

Copie FIR digitali disponibili

Ottiene la lista delle copie dei FIR digitali, disponibili per la conferma o già confermati, per il soggetto specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_digitale_item_result import CopiaDigitaleItemResult
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per cui richiedere l'elenco delle copie dei FIR digitali disponibili
    num_iscr_sito = 'num_iscr_sito_example' # str | Eventuale numero di iscrizione dell'unità locale per la quale si richiedono le copie dei FIR digitali (optional)
    numero_fir = 'numero_fir_example' # str | Numero FIR della copia del FIR digitale (optional)
    tipo_accettazione = rentri_formulari.TipiAccettazione() # TipiAccettazione | Filtra le copia dei FIR digitali per tipo di accettazione del destinatario (optional)
    confermate = True # bool | Filtra le copie dei FIR digitali confermate o non confermate. (optional)
    comune_id = 'comune_id_example' # str | Filtra le copie dei FIR digitali per il comune. Il valore viene considerato solo per il ruolo di produttore (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Filta le copie digiitali dei FIR per il codice EER del rifiuto (optional)
    ruolo = rentri_formulari.RuoloConfermaCopiaDigitale() # RuoloConfermaCopiaDigitale | Ruolo per il quale si richiedono le copie dei FIR digitali da confermare (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize (optional) (default to 100)

    try:
        # Copie FIR digitali disponibili
        api_response = api_instance.copia_digitale_conferma_identificativo_soggetto_get(identificativo_soggetto, num_iscr_sito=num_iscr_sito, numero_fir=numero_fir, tipo_accettazione=tipo_accettazione, confermate=confermate, comune_id=comune_id, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, ruolo=ruolo, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per cui richiedere l&#39;elenco delle copie dei FIR digitali disponibili | 
 **num_iscr_sito** | **str**| Eventuale numero di iscrizione dell&#39;unità locale per la quale si richiedono le copie dei FIR digitali | [optional] 
 **numero_fir** | **str**| Numero FIR della copia del FIR digitale | [optional] 
 **tipo_accettazione** | [**TipiAccettazione**](.md)| Filtra le copia dei FIR digitali per tipo di accettazione del destinatario | [optional] 
 **confermate** | **bool**| Filtra le copie dei FIR digitali confermate o non confermate. | [optional] 
 **comune_id** | **str**| Filtra le copie dei FIR digitali per il comune. Il valore viene considerato solo per il ruolo di produttore | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono le copie dei FIR digitali (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Filta le copie digiitali dei FIR per il codice EER del rifiuto | [optional] 
 **ruolo** | [**RuoloConfermaCopiaDigitale**](.md)| Ruolo per il quale si richiedono le copie dei FIR digitali da confermare | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize | [optional] [default to 100]

### Return type

[**List[CopiaDigitaleItemResult]**](CopiaDigitaleItemResult.md)

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

# **copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get**
> DownloadableBaseResponse copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get(identificativo_soggetto, identificativo)

Documento copia FIR digitale disponibile

Restituisce il file xFIR che rappresenta la copia del FIR digitale caricata dal destinatario.

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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per il quale si richiede il documento della copia del FIR digitale
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale caricata dal destinatario

    try:
        # Documento copia FIR digitale disponibile
        api_response = api_instance.copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get(identificativo_soggetto, identificativo)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_identificativo_documento_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per il quale si richiede il documento della copia del FIR digitale | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale caricata dal destinatario | 

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

# **copia_digitale_conferma_identificativo_soggetto_identificativo_get**
> CopiaDigitaleResult copia_digitale_conferma_identificativo_soggetto_identificativo_get(identificativo_soggetto, identificativo)

Dettaglio copia digitale FIR disponibile

Restituisce il dettaglio dei dati di caricamento della copia digitale del FIR caricata.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.copia_digitale_result import CopiaDigitaleResult
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto a cui è resa disponibile la copia del FIR digitale
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale per cui vengono richieste le informazioni di dettaglio

    try:
        # Dettaglio copia digitale FIR disponibile
        api_response = api_instance.copia_digitale_conferma_identificativo_soggetto_identificativo_get(identificativo_soggetto, identificativo)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_identificativo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_conferma_identificativo_soggetto_identificativo_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto a cui è resa disponibile la copia del FIR digitale | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale per cui vengono richieste le informazioni di dettaglio | 

### Return type

[**CopiaDigitaleResult**](CopiaDigitaleResult.md)

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

# **copia_digitale_conferma_num_iscr_sito_identificativo_put**
> copia_digitale_conferma_num_iscr_sito_identificativo_put(num_iscr_sito, identificativo, ruolo=ruolo, respingi=respingi)

Conferma copia FIR digitale disponibile

Permette al soggetto a cui è stata resa disponibile la copia del FIR digitale di impostarne la stato di presa visione.

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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale del soggetto che conferma la presa visione della copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti.
    identificativo = 'identificativo_example' # str | Identificativo della copia del FIR digitale della quale restituire il file xFIR caricato
    ruolo = rentri_formulari.RuoloConfermaCopiaDigitale() # RuoloConfermaCopiaDigitale | Ruolo all'interno del FIR del soggetto per cui si effettua l'operazione di conferma di presa visione.              In caso di ambiguità (lo stesso soggetto a cui si riferisce l'unità locale \"numIscrSito\" appare con più ruoli all'interno del FIR) il parametro è obbligatorio (optional)
    respingi = True # bool | Se valorizzato a true annulla una eventuale precedente operazione di presa visione per i parametri specificati (optional)

    try:
        # Conferma copia FIR digitale disponibile
        api_instance.copia_digitale_conferma_num_iscr_sito_identificativo_put(num_iscr_sito, identificativo, ruolo=ruolo, respingi=respingi)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_conferma_num_iscr_sito_identificativo_put: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale del soggetto che conferma la presa visione della copia del FIR digitale.             Per recuperare i numeri di iscrizione attribuiti alle unità locali è possibile utilizzare /anagrafiche/v1.0/operatore/{num_iscr}/siti. | 
 **identificativo** | **str**| Identificativo della copia del FIR digitale della quale restituire il file xFIR caricato | 
 **ruolo** | [**RuoloConfermaCopiaDigitale**](.md)| Ruolo all&#39;interno del FIR del soggetto per cui si effettua l&#39;operazione di conferma di presa visione.              In caso di ambiguità (lo stesso soggetto a cui si riferisce l&#39;unità locale \&quot;numIscrSito\&quot; appare con più ruoli all&#39;interno del FIR) il parametro è obbligatorio | [optional] 
 **respingi** | **bool**| Se valorizzato a true annulla una eventuale precedente operazione di presa visione per i parametri specificati | [optional] 

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
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **copia_digitale_transazione_id_result_get**
> EsitoCopiaDigitaleModel copia_digitale_transazione_id_result_get(transazione_id)

⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione

Ottiene l'esito dell'elaborazione di una richiesta asincrona.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.esito_copia_digitale_model import EsitoCopiaDigitaleModel
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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta

    try:
        # ⚠️[DEPRECATO] - utilizzare /{transazioneId}/result - Esito transazione
        api_response = api_instance.copia_digitale_transazione_id_result_get(transazione_id)
        print("The response of CopiaFIRDigitaleApi->copia_digitale_transazione_id_result_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_transazione_id_result_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **transazione_id** | **str**| Id della richiesta | 

### Return type

[**EsitoCopiaDigitaleModel**](EsitoCopiaDigitaleModel.md)

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

# **copia_digitale_transazione_id_status_get**
> copia_digitale_transazione_id_status_get(transazione_id)

⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione

Ottiene lo stato di elaborazione di una richiesta di caricamento di una copia di un FIR digitale.

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
    api_instance = rentri_formulari.CopiaFIRDigitaleApi(api_client)
    transazione_id = 'transazione_id_example' # str | Id della richiesta

    try:
        # ⚠️[DEPRECATO] - utilizzare /{transazioneId}/status - Stato transazione
        api_instance.copia_digitale_transazione_id_status_get(transazione_id)
    except Exception as e:
        print("Exception when calling CopiaFIRDigitaleApi->copia_digitale_transazione_id_status_get: %s\n" % e)
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

