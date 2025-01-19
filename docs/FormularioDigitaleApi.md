# rentri_formulari.FormularioDigitaleApi

All URIs are relative to *https://demoapi.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](FormularioDigitaleApi.md#count_get) | **GET** /count | Conteggio formulari
[**numero_fir_accettazione_post**](FormularioDigitaleApi.md#numero_fir_accettazione_post) | **POST** /{numero_fir}/accettazione | 🔁[ASYNC] Accettazione FIR
[**numero_fir_acquisizione_firma_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_firma_post) | **POST** /{numero_fir}/acquisizione-firma | 🔁[ASYNC] Imposta dati firma
[**numero_fir_acquisizione_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_num_iscr_sito_post) | **POST** /{numero_fir}/acquisizione/{num_iscr_sito} | ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/acquisizione-visibilita/{numIscrSito} - Acquisizione visibilità FIR
[**numero_fir_acquisizione_visibilita_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_visibilita_num_iscr_sito_post) | **POST** /{numero_fir}/acquisizione-visibilita/{num_iscr_sito} | Acquisizione visibilità FIR
[**numero_fir_allegato_post**](FormularioDigitaleApi.md#numero_fir_allegato_post) | **POST** /{numero_fir}/allegato | 🔁[ASYNC] Aggiunge allegato
[**numero_fir_annotazione_post**](FormularioDigitaleApi.md#numero_fir_annotazione_post) | **POST** /{numero_fir}/annotazione | 🔁[ASYNC] Aggiunge annotazione
[**numero_fir_annulla_post**](FormularioDigitaleApi.md#numero_fir_annulla_post) | **POST** /{numero_fir}/annulla | 🔁[ASYNC] Annullamento FIR
[**numero_fir_azioni_get**](FormularioDigitaleApi.md#numero_fir_azioni_get) | **GET** /{numero_fir}/azioni | Operazioni disponibili
[**numero_fir_destinatario_post**](FormularioDigitaleApi.md#numero_fir_destinatario_post) | **POST** /{numero_fir}/destinatario | 🔁[ASYNC] Aggiunge nuovo destinatario
[**numero_fir_get**](FormularioDigitaleApi.md#numero_fir_get) | **GET** /{numero_fir} | Dettaglio FIR
[**numero_fir_hash_post**](FormularioDigitaleApi.md#numero_fir_hash_post) | **POST** /{numero_fir}/hash | 🔁[ASYNC] Calcolo del codice hash da firmare
[**numero_fir_pdf_get**](FormularioDigitaleApi.md#numero_fir_pdf_get) | **GET** /{numero_fir}/pdf | Stampa PDF del FIR
[**numero_fir_put**](FormularioDigitaleApi.md#numero_fir_put) | **PUT** /{numero_fir} | 🔁[ASYNC] Modifica FIR
[**numero_fir_quantita_post**](FormularioDigitaleApi.md#numero_fir_quantita_post) | **POST** /{numero_fir}/quantita | 🔁[ASYNC] Imposta quantità
[**numero_fir_reset_post**](FormularioDigitaleApi.md#numero_fir_reset_post) | **POST** /{numero_fir}/reset | 🔁[ASYNC] Reset stato
[**numero_fir_respingi_post**](FormularioDigitaleApi.md#numero_fir_respingi_post) | **POST** /{numero_fir}/respingi | ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/rilascio-visibilita/{numIscrSito} - Rilascio visibilità FIR
[**numero_fir_rilascio_visibilita_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_rilascio_visibilita_num_iscr_sito_post) | **POST** /{numero_fir}/rilascio-visibilita/{num_iscr_sito} | Rilascio visibilità FIR
[**numero_fir_sosta_tecnica_post**](FormularioDigitaleApi.md#numero_fir_sosta_tecnica_post) | **POST** /{numero_fir}/sosta-tecnica | 🔁[ASYNC] Aggiunge sosta tecnica
[**numero_fir_stato_get**](FormularioDigitaleApi.md#numero_fir_stato_get) | **GET** /{numero_fir}/stato | Stato FIR
[**numero_fir_tipo_trasporto_get**](FormularioDigitaleApi.md#numero_fir_tipo_trasporto_get) | **GET** /{numero_fir}/tipo-trasporto | Tipo trasporto FIR
[**numero_fir_trasbordo_parziale_post**](FormularioDigitaleApi.md#numero_fir_trasbordo_parziale_post) | **POST** /{numero_fir}/trasbordo-parziale | 🔁[ASYNC] Aggiunge trasbordo praziale
[**numero_fir_trasbordo_totale_post**](FormularioDigitaleApi.md#numero_fir_trasbordo_totale_post) | **POST** /{numero_fir}/trasbordo-totale | 🔁[ASYNC] Aggiunge trasbordo totale
[**numero_fir_trasporto_post**](FormularioDigitaleApi.md#numero_fir_trasporto_post) | **POST** /{numero_fir}/trasporto | 🔁[ASYNC] Aggiunge dati trasporto
[**numero_fir_xfir_get**](FormularioDigitaleApi.md#numero_fir_xfir_get) | **GET** /{numero_fir}/xfir | Download xFIR
[**root_get**](FormularioDigitaleApi.md#root_get) | **GET** / | Elenco formulari
[**root_post**](FormularioDigitaleApi.md#root_post) | **POST** / | 🔁[ASYNC] Crea FIR
[**xfir_valida_post**](FormularioDigitaleApi.md#xfir_valida_post) | **POST** /xfir/valida | 🔁[ASYNC] Validazione xFIR


# **count_get**
> int count_get(num_iscr_sito, numero_fir=numero_fir, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, tipo_ricerca=tipo_ricerca, stati=stati)

Conteggio formulari

Ottiene il conteggio dei formulari digitali con visibilità per l'unità locale indicata e con i filtri specificati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione per il quale si richiedono i formulari
    numero_fir = 'numero_fir_example' # str | Numero del FIR (optional)
    data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Codice EER (optional)
    tipo_ricerca = rentri_formulari.TipoRicerca() # TipoRicerca |  (optional)
    stati = ['stati_example'] # List[str] |  (optional)

    try:
        # Conteggio formulari
        api_response = api_instance.count_get(num_iscr_sito, numero_fir=numero_fir, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, tipo_ricerca=tipo_ricerca, stati=stati)
        print("The response of FormularioDigitaleApi->count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->count_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione per il quale si richiedono i formulari | 
 **numero_fir** | **str**| Numero del FIR | [optional] 
 **data_creazione_da** | **datetime**| Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_creazione_a** | **datetime**| Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Codice EER | [optional] 
 **tipo_ricerca** | [**TipoRicerca**](.md)|  | [optional] 
 **stati** | [**List[str]**](str.md)|  | [optional] 

### Return type

**int**

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Conteggio dei formulari corrispondenti ai criteri di ricerca specificati. |  -  |
**403** | Operazione non consentita sul Registro. |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_accettazione_post**
> TransazioneModel numero_fir_accettazione_post(numero_fir, dati_accettazione_model, x_reply_to=x_reply_to)

🔁[ASYNC] Accettazione FIR

Acquisisce la richiesta di aggiunta dei dati di accettazione del rifiuto da parte del destinatario per il FIR specificato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_accettazione_model import DatiAccettazioneModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_accettazione_model = rentri_formulari.DatiAccettazioneModel() # DatiAccettazioneModel | Dati di accettazione del rifiuto
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Accettazione FIR
        api_response = api_instance.numero_fir_accettazione_post(numero_fir, dati_accettazione_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_accettazione_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_accettazione_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **dati_accettazione_model** | [**DatiAccettazioneModel**](DatiAccettazioneModel.md)| Dati di accettazione del rifiuto | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_firma_post**
> TransazioneModel numero_fir_acquisizione_firma_post(numero_fir, firma_model, x_reply_to=x_reply_to)

🔁[ASYNC] Imposta dati firma

Acquisisce la richiesta di aggiunta dei dati per completare l'apposizione della firma digitale del soggetto indicato nel file xFIR.  Stati del formulario ammessi: <ul><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaProduttore</li><li>FirmaTrasportatoreIniziale</li><li>FirmaTrasportatoreSuccessivo</li><li>FirmaAccettazione</li><li>FirmaAnnotazione</li><li>FirmaAllegato</li><li>FirmaAnnullamento</li><li>FirmaTrasbordoParziale</li><li>FirmaTrasbordoTotale</li><li>FirmaSostaTecnica</li><li>FirmaDestinatarioSuccessivo</li><li>FirmaAccettazioneSuccessiva</li></ul> Il valore della proprietà <i>Token</i> deve coincidere con il valore restituito dalla precedente invocazione all'endpoint <i>POST /{numero_fir}/hash</i> che ha determinato il passaggio allo stato corrente del formulario. L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto tra quelli indicati nel formulario coinvolto nell'operazione di firma.  L'art. 7 c.3 del D.M. 59/2023 prevede che il FIR sia sottoscritto da parte degli operatori coinvolti nelle diverse fasi del trasporto,  per cui se il certificato di firma è intestato ad una persona giuridica (cioè è un \"sigillo\") deve riferirsi al soggetto firmatario,  mentre se il certificato di firma è intestato ad una persona fisica, deve coincidere con il codice fiscale di un utente incaricato per il soggetto firmatario. Esclusivamente in ambiente DEMO, se il certificato firmatario non viene riconosciuto come valido secondo la regola qui descritta, il sistema produrrà un avviso non bloccante. In ambiente di produzione il controllo sarà bloccante.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.firma_model import FirmaModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiunge la firma
    firma_model = rentri_formulari.FirmaModel() # FirmaModel | Dati necessari per aggiungere la firma al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Imposta dati firma
        api_response = api_instance.numero_fir_acquisizione_firma_post(numero_fir, firma_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_acquisizione_firma_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_acquisizione_firma_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiunge la firma | 
 **firma_model** | [**FirmaModel**](FirmaModel.md)| Dati necessari per aggiungere la firma al formulario | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_num_iscr_sito_post**
> numero_fir_acquisizione_num_iscr_sito_post(numero_fir, num_iscr_sito)

⚠️[DEPRECATO] - utilizzare /{numeroFIR}/acquisizione-visibilita/{numIscrSito} - Acquisizione visibilità FIR

Acquisisce la visibilità in ricerca sull'unità locale specificata di un FIR digitale creato da terzi. L'operazione consente di rendere visibile il FIR digitale in ricerca per una specifica unità locale. Il numero iscrizione unità locale indicata deve essere riconducibile ad uno dei soggetti presenti nel FIR.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 
    num_iscr_sito = 'num_iscr_sito_example' # str | 

    try:
        # ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/acquisizione-visibilita/{numIscrSito} - Acquisizione visibilità FIR
        api_instance.numero_fir_acquisizione_num_iscr_sito_post(numero_fir, num_iscr_sito)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_acquisizione_num_iscr_sito_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 
 **num_iscr_sito** | **str**|  | 

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
**200** | L&#39;acquisizione di visibilità è avvenuta con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_visibilita_num_iscr_sito_post**
> numero_fir_acquisizione_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)

Acquisizione visibilità FIR

Acquisisce la visibilità in ricerca sull'unità locale specificata di un FIR digitale creato da terzi. L'operazione consente di rendere visibile il FIR digitale in ricerca per una specifica unità locale. Il numero iscrizione unità locale indicata deve essere riconducibile ad uno dei soggetti presenti nel FIR.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 
    num_iscr_sito = 'num_iscr_sito_example' # str | 

    try:
        # Acquisizione visibilità FIR
        api_instance.numero_fir_acquisizione_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_acquisizione_visibilita_num_iscr_sito_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 
 **num_iscr_sito** | **str**|  | 

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
**200** | L&#39;acquisizione di visibilità è avvenuta con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_allegato_post**
> TransazioneModel numero_fir_allegato_post(numero_fir, dati_allegato_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge allegato

Acquisisce la richiesta di aggiunta di un allegato al formulario digitale specificato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_allegato_model import DatiAllegatoModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_allegato_model = rentri_formulari.DatiAllegatoModel() # DatiAllegatoModel | Insieme delle informazioni riguardanti l'allegato da aggiungere al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge allegato
        api_response = api_instance.numero_fir_allegato_post(numero_fir, dati_allegato_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_allegato_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_allegato_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **dati_allegato_model** | [**DatiAllegatoModel**](DatiAllegatoModel.md)| Insieme delle informazioni riguardanti l&#39;allegato da aggiungere al formulario | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_annotazione_post**
> TransazioneModel numero_fir_annotazione_post(numero_fir, dati_annotazione_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge annotazione

Acquisisce la richiesta di aggiunta di un'annotazione da allegare al formulario digitale specificato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_annotazione_model import DatiAnnotazioneModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_annotazione_model = rentri_formulari.DatiAnnotazioneModel() # DatiAnnotazioneModel | Insieme delle informazioni riguardanti l'allegato da aggiungere al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge annotazione
        api_response = api_instance.numero_fir_annotazione_post(numero_fir, dati_annotazione_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_annotazione_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_annotazione_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **dati_annotazione_model** | [**DatiAnnotazioneModel**](DatiAnnotazioneModel.md)| Insieme delle informazioni riguardanti l&#39;allegato da aggiungere al formulario | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_annulla_post**
> TransazioneModel numero_fir_annulla_post(numero_fir, dati_annullamento_model, x_reply_to=x_reply_to)

🔁[ASYNC] Annullamento FIR

Acquisisce la richiesta di annullamento del FIR specificato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito. L'annullamento può essere richiesto solo se il formulario non risulta già essere firmato sia dal produttore che dal trasportatore.  L'operazione di annullamento provvede ad annullare anche la vidimazione del numero FIR corrispondente, e pertanto può essere richiesta solo dal soggetto a cui è stato vidimato il numero FIR. <br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_annullamento_model import DatiAnnullamentoModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_annullamento_model = rentri_formulari.DatiAnnullamentoModel() # DatiAnnullamentoModel | Insieme delle informazioni riguardanti l'allegato da aggiungere al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Annullamento FIR
        api_response = api_instance.numero_fir_annulla_post(numero_fir, dati_annullamento_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_annulla_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_annulla_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **dati_annullamento_model** | [**DatiAnnullamentoModel**](DatiAnnullamentoModel.md)| Insieme delle informazioni riguardanti l&#39;allegato da aggiungere al formulario | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_azioni_get**
> AzioniResult numero_fir_azioni_get(numero_fir, identificativo_soggetto, num_iscr_sito=num_iscr_sito)

Operazioni disponibili

Restituisce l'elenco delle azioni che è possibile eseguire sul formulario indicato, in funzione dello stato in cui si trova. Per ogni azione che è possibile eseguire viene restituito l'elenco degli identificatvi dei soggetti che possono invocarla. L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.azioni_result import AzioniResult
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per il quale si richiedono le azioni possibili
    num_iscr_sito = 'num_iscr_sito_example' # str |  (optional)

    try:
        # Operazioni disponibili
        api_response = api_instance.numero_fir_azioni_get(numero_fir, identificativo_soggetto, num_iscr_sito=num_iscr_sito)
        print("The response of FormularioDigitaleApi->numero_fir_azioni_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_azioni_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **identificativo_soggetto** | **str**| Codice fiscale del soggetto per il quale si richiedono le azioni possibili | 
 **num_iscr_sito** | **str**|  | [optional] 

### Return type

[**AzioniResult**](AzioniResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operazione eseguita con successo. |  -  |
**400** | Bad Request |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_destinatario_post**
> TransazioneModel numero_fir_destinatario_post(numero_fir, numero_fir_destinatario_post_request, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge nuovo destinatario

Acquisisce la richiesta di aggiungta dei dati del nuovo destinatario per il rifiuto indicato nel formulario specificato, a seguito del respingimento o della parziale accettazione del rifiuto da parte del destinatrio precedente.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.numero_fir_destinatario_post_request import NumeroFirDestinatarioPostRequest
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiunge il nuovo destinatario
    numero_fir_destinatario_post_request = rentri_formulari.NumeroFirDestinatarioPostRequest() # NumeroFirDestinatarioPostRequest | Informazioni sul nuovo destinatario da aggiungere
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge nuovo destinatario
        api_response = api_instance.numero_fir_destinatario_post(numero_fir, numero_fir_destinatario_post_request, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_destinatario_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_destinatario_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiunge il nuovo destinatario | 
 **numero_fir_destinatario_post_request** | [**NumeroFirDestinatarioPostRequest**](NumeroFirDestinatarioPostRequest.md)| Informazioni sul nuovo destinatario da aggiungere | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_get**
> DettaglioFormulario numero_fir_get(numero_fir)

Dettaglio FIR

Restituisce i dati completi del formulario indicato.   L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dettaglio_formulario import DettaglioFormulario
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero del FIR per il quale si richiede il dettaglio

    try:
        # Dettaglio FIR
        api_response = api_instance.numero_fir_get(numero_fir)
        print("The response of FormularioDigitaleApi->numero_fir_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero del FIR per il quale si richiede il dettaglio | 

### Return type

[**DettaglioFormulario**](DettaglioFormulario.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operazione eseguita con successo. |  -  |
**400** | Bad Request |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_hash_post**
> TransazioneModel numero_fir_hash_post(numero_fir, dati_per_firma_model, x_reply_to=x_reply_to)

🔁[ASYNC] Calcolo del codice hash da firmare

Acquisisce la richiesta per il calcolo dell'impronta SHA256 da firmare per poter apporre la firma digitale sul formulario.  Il codice hash SHA256 prodotto da questa procedura dovrà essere firmato con la chiave privata associata al certificato indicato nel modello di input.  Per completare l'apposizione della firma al formulario digitale dovrà essere quindi successivamente invocato l'endpoint <i>POST /{numero_fir}/acquisizione-firma</i>  specificando nel modello di input:  <ul><li>lo stesso certificato incluso nell'invocazione di questo endpoint</li><li>la firma digitale calcolata con la chiave privata associata al certificato</li><li>il token ricevuto nell'esito di questa invocazione</li></ul> Il formulario deve essere in uno stato di attesa di firma, conseguente all'aggiunta di nuove informazioni.  L'art. 7 c.3 del D.M. 59/2023 prevede che il FIR sia sottoscritto da parte degli operatori coinvolti nelle diverse fasi del trasporto,  per cui se il certificato di firma è intestato ad una persona giuridica (cioè è un \"sigillo\") deve riferirsi al soggetto firmatario,  mentre se il certificato di firma è intestato ad una persona fisica, deve coincidere con il codice fiscale di un utente incaricato per il soggetto firmatario. Esclusivamente in ambiente DEMO, se il certificato firmatario non viene riconosciuto come valido secondo la regola qui descritta, il sistema produrrà un avviso non bloccante. In ambiente di produzione il controllo sarà bloccante.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_per_firma_model import DatiPerFirmaModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiunge la firma
    dati_per_firma_model = rentri_formulari.DatiPerFirmaModel() # DatiPerFirmaModel | Informazioni necessarie per il calcolo del codice hash da firmare
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Calcolo del codice hash da firmare
        api_response = api_instance.numero_fir_hash_post(numero_fir, dati_per_firma_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_hash_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_hash_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiunge la firma | 
 **dati_per_firma_model** | [**DatiPerFirmaModel**](DatiPerFirmaModel.md)| Informazioni necessarie per il calcolo del codice hash da firmare | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_pdf_get**
> DownloadableBaseResponse numero_fir_pdf_get(numero_fir)

Stampa PDF del FIR

Ottiene una stampa in PDF del FIR

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.downloadable_base_response import DownloadableBaseResponse
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario

    try:
        # Stampa PDF del FIR
        api_response = api_instance.numero_fir_pdf_get(numero_fir)
        print("The response of FormularioDigitaleApi->numero_fir_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 

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
**200** | Formulario in formato PDF. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_put**
> TransazioneModel numero_fir_put(numero_fir, nuovo_formulario_model, x_reply_to=x_reply_to)

🔁[ASYNC] Modifica FIR

Acquisisce la richiesta di modifica dei dati di un FIR esistente. Lo stato del formulario deve essere compatibile con l'operazione richiesta, ovvero non devono essere presenti firme.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.nuovo_formulario_model import NuovoFormularioModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 
    nuovo_formulario_model = rentri_formulari.NuovoFormularioModel() # NuovoFormularioModel | Dati del formulario da sostituire a quelli presenti
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Modifica FIR
        api_response = api_instance.numero_fir_put(numero_fir, nuovo_formulario_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 
 **nuovo_formulario_model** | [**NuovoFormularioModel**](NuovoFormularioModel.md)| Dati del formulario da sostituire a quelli presenti | 
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_quantita_post**
> TransazioneModel numero_fir_quantita_post(numero_fir, quantita_rifiuto_model, x_reply_to=x_reply_to)

🔁[ASYNC] Imposta quantità

Acquisice la richiesta di aggiunta o modifica del dato della quantità sul formulario indicato.  Stati del formulario ammessi: <ul><li>InserimentoQuantitaTrasportoIniziale</li><li>InserimentoTrasportoIniziale</li><li>InserimentoQuantita</li><li>FirmaProduttoreTrasportatoreIniziale</li></ul> L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il <i>produttore</i> o il <i>primo trasportatore</i>.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.quantita_rifiuto_model import QuantitaRifiutoModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    quantita_rifiuto_model = rentri_formulari.QuantitaRifiutoModel() # QuantitaRifiutoModel | 
    x_reply_to = 'x_reply_to_example' # str |  (optional)

    try:
        # 🔁[ASYNC] Imposta quantità
        api_response = api_instance.numero_fir_quantita_post(numero_fir, quantita_rifiuto_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_quantita_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_quantita_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **quantita_rifiuto_model** | [**QuantitaRifiutoModel**](QuantitaRifiutoModel.md)|  | 
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

# **numero_fir_reset_post**
> TransazioneModel numero_fir_reset_post(numero_fir, x_reply_to=x_reply_to)

🔁[ASYNC] Reset stato

Acquisisce la richiesta di cancellazione degli ultimi dati inseriti nel formulario in attesa di firma, riportando lo stato del formulario a quello precedente.  Stati del formulario ammessi:  <ul><li>FirmaTrasportatoreSuccessivo</li><li>FirmaDestinatarioSuccessivo</li><li>FirmaAccettazione</li><li>FirmaAccettazioneSuccessiva</li><li>FirmaAnnotazione</li><li>FirmaAllegato</li><li>FirmaAnnullamento</li><li>FirmaTrasbordoParziale</li><li>FirmaTrasbordoTotale</li><li>FirmaSostaTecnica</li></ul> Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Reset stato
        api_response = api_instance.numero_fir_reset_post(numero_fir, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_reset_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_reset_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **x_reply_to** | **str**| URL di callback alla quale verrà inviata la notifica di fine elaborazione | [optional] 

### Return type

[**TransazioneModel**](TransazioneModel.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **numero_fir_respingi_post**
> numero_fir_respingi_post(numero_fir, num_iscr_sito=num_iscr_sito)

⚠️[DEPRECATO] - utilizzare /{numeroFIR}/rilascio-visibilita/{numIscrSito} - Rilascio visibilità FIR

Abbandona la visibilità in ricerca sull'unità locale specificata, ottenuta con l'operazione di \"acquisizione\", relativamente al FIR digitale specificato creato da terzi.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 
    num_iscr_sito = 'num_iscr_sito_example' # str |  (optional)

    try:
        # ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/rilascio-visibilita/{numIscrSito} - Rilascio visibilità FIR
        api_instance.numero_fir_respingi_post(numero_fir, num_iscr_sito=num_iscr_sito)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_respingi_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 
 **num_iscr_sito** | **str**|  | [optional] 

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
**200** | Il respingimento è avvenuto con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_rilascio_visibilita_num_iscr_sito_post**
> numero_fir_rilascio_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)

Rilascio visibilità FIR

Abbandona la visibilità in ricerca sull'unità locale specificata, ottenuta con l'operazione di \"acquisizione\", relativamente al FIR digitale specificato creato da terzi.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 
    num_iscr_sito = 'num_iscr_sito_example' # str | 

    try:
        # Rilascio visibilità FIR
        api_instance.numero_fir_rilascio_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_rilascio_visibilita_num_iscr_sito_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 
 **num_iscr_sito** | **str**|  | 

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
**200** | Il respingimento è avvenuto con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_sosta_tecnica_post**
> TransazioneModel numero_fir_sosta_tecnica_post(numero_fir, dati_sosta_tecnica_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge sosta tecnica

Acquisisce la richiesta per l'aggiunta dei dati di sosta tecnica per il formulario indicato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_sosta_tecnica_model import DatiSostaTecnicaModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiungono i dati di sosta tecnica
    dati_sosta_tecnica_model = rentri_formulari.DatiSostaTecnicaModel() # DatiSostaTecnicaModel | Dati con il dettaglio della sosta
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge sosta tecnica
        api_response = api_instance.numero_fir_sosta_tecnica_post(numero_fir, dati_sosta_tecnica_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_sosta_tecnica_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_sosta_tecnica_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiungono i dati di sosta tecnica | 
 **dati_sosta_tecnica_model** | [**DatiSostaTecnicaModel**](DatiSostaTecnicaModel.md)| Dati con il dettaglio della sosta | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_stato_get**
> InfoFormulario numero_fir_stato_get(numero_fir)

Stato FIR

Restituisce lo stato del formulario

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.info_formulario import InfoFormulario
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero del FIR per il quale si richiede lo stato

    try:
        # Stato FIR
        api_response = api_instance.numero_fir_stato_get(numero_fir)
        print("The response of FormularioDigitaleApi->numero_fir_stato_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_stato_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero del FIR per il quale si richiede lo stato | 

### Return type

[**InfoFormulario**](InfoFormulario.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operazione eseguita con successo. |  -  |
**400** | Bad Request |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_tipo_trasporto_get**
> TipoTrasportoResult numero_fir_tipo_trasporto_get(numero_fir)

Tipo trasporto FIR

Restituisce il tipo di trasporto del FIR

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.tipo_trasporto_result import TipoTrasportoResult
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | 

    try:
        # Tipo trasporto FIR
        api_response = api_instance.numero_fir_tipo_trasporto_get(numero_fir)
        print("The response of FormularioDigitaleApi->numero_fir_tipo_trasporto_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_tipo_trasporto_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**|  | 

### Return type

[**TipoTrasportoResult**](TipoTrasportoResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Operazione avvenuta con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasbordo_parziale_post**
> TransazioneModel numero_fir_trasbordo_parziale_post(numero_fir, dati_trasbordo_parziale_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge trasbordo praziale

Acquisisce la richiesta per l'aggiunta dei dati di un trasbordo parziale per il formulario indicato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_trasbordo_parziale_model import DatiTrasbordoParzialeModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiungono i dati del trasbordo
    dati_trasbordo_parziale_model = rentri_formulari.DatiTrasbordoParzialeModel() # DatiTrasbordoParzialeModel | Dati con il dettaglio della sosta
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge trasbordo praziale
        api_response = api_instance.numero_fir_trasbordo_parziale_post(numero_fir, dati_trasbordo_parziale_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_trasbordo_parziale_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_trasbordo_parziale_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiungono i dati del trasbordo | 
 **dati_trasbordo_parziale_model** | [**DatiTrasbordoParzialeModel**](DatiTrasbordoParzialeModel.md)| Dati con il dettaglio della sosta | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasbordo_totale_post**
> TransazioneModel numero_fir_trasbordo_totale_post(numero_fir, dati_trasbordo_totale_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge trasbordo totale

Acquisisce la richiesta per l'aggiunta dei dati di un trasbordo totale per il formulario indicato. Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.dati_trasbordo_totale_model import DatiTrasbordoTotaleModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiungono i dati del trasbordo totale
    dati_trasbordo_totale_model = rentri_formulari.DatiTrasbordoTotaleModel() # DatiTrasbordoTotaleModel | Dati con il dettaglio della sosta
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge trasbordo totale
        api_response = api_instance.numero_fir_trasbordo_totale_post(numero_fir, dati_trasbordo_totale_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_trasbordo_totale_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_trasbordo_totale_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario a cui si aggiungono i dati del trasbordo totale | 
 **dati_trasbordo_totale_model** | [**DatiTrasbordoTotaleModel**](DatiTrasbordoTotaleModel.md)| Dati con il dettaglio della sosta | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasporto_post**
> TransazioneModel numero_fir_trasporto_post(numero_fir, numero_fir_trasporto_post_request, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge dati trasporto

Acquisisce la richiesta di aggiunta dei dati di trasporto del rifiuto da parte del trasportatore che ha in carico il FIR specificato.  Il tipo di modello passato come contenuto del POST determina la modalità del trasporto.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.numero_fir_trasporto_post_request import NumeroFirTrasportoPostRequest
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    numero_fir_trasporto_post_request = rentri_formulari.NumeroFirTrasportoPostRequest() # NumeroFirTrasportoPostRequest | Dati di trasporto del rifiuto
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge dati trasporto
        api_response = api_instance.numero_fir_trasporto_post(numero_fir, numero_fir_trasporto_post_request, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_trasporto_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_trasporto_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **numero_fir_trasporto_post_request** | [**NumeroFirTrasportoPostRequest**](NumeroFirTrasportoPostRequest.md)| Dati di trasporto del rifiuto | 
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
**202** | Accepted |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Bad Request |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Internal Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_xfir_get**
> DownloadableBaseResponse numero_fir_xfir_get(numero_fir)

Download xFIR

Restituisce il file in formato xFIR che rappresenta il formulario specificato con il numero FIR. L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.downloadable_base_response import DownloadableBaseResponse
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario

    try:
        # Download xFIR
        api_response = api_instance.numero_fir_xfir_get(numero_fir)
        print("The response of FormularioDigitaleApi->numero_fir_xfir_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_xfir_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 

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
**200** | Operazione eseguita con successo. |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> List[FormularioItemResult] root_get(num_iscr_sito, numero_fir=numero_fir, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, tipo_ricerca=tipo_ricerca, stati=stati, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco formulari

Ottiene l'elenco dei formulari richiesti con visibilità per l'unità locale indicata e con i filtri specificati.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.formulario_item_result import FormularioItemResult
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione per il quale si richiedono i formulari
    numero_fir = 'numero_fir_example' # str | Numero del FIR (optional)
    data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Codice EER (optional)
    tipo_ricerca = rentri_formulari.TipoRicerca() # TipoRicerca |  (optional)
    stati = ['stati_example'] # List[str] |  (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize. (optional) (default to 100)

    try:
        # Elenco formulari
        api_response = api_instance.root_get(num_iscr_sito, numero_fir=numero_fir, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, tipo_ricerca=tipo_ricerca, stati=stati, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of FormularioDigitaleApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->root_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione per il quale si richiedono i formulari | 
 **numero_fir** | **str**| Numero del FIR | [optional] 
 **data_creazione_da** | **datetime**| Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_creazione_a** | **datetime**| Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Codice EER | [optional] 
 **tipo_ricerca** | [**TipoRicerca**](.md)|  | [optional] 
 **stati** | [**List[str]**](str.md)|  | [optional] 
 **paging_page** | **int**| Valore per l&#39;header Paging-Page. | [optional] [default to 1]
 **paging_page_size** | **int**| Valore per l&#39;header Paging-PageSize. | [optional] [default to 100]

### Return type

[**List[FormularioItemResult]**](FormularioItemResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Esito della richiesta |  * Paging-PageCount - Numero totale di pagine. <br>  * Paging-Page - Numero di pagina. <br>  * Paging-PageSize - Dimensione della pagina. <br>  * Paging-TotalRecordCount - Numero totale di record. <br>  |
**400** | Entità non trovata |  -  |
**403** | Operazione non consentita |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> TransazioneModel root_post(nuovo_formulario_model, codice_blocco=codice_blocco, x_reply_to=x_reply_to)

🔁[ASYNC] Crea FIR

Acquisisce la richiesta di creazione di un nuovo FIR.  Il numero del nuovo FIR può essere specificato nell'apposita proprietà del modello, altrimenti verrà generato automaticamente dal sistema dal blocco indicato nel parametro codiceBlocco.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.nuovo_formulario_model import NuovoFormularioModel
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    nuovo_formulario_model = rentri_formulari.NuovoFormularioModel() # NuovoFormularioModel | Dati del formulario da creare
    codice_blocco = 'codice_blocco_example' # str | Codice blocco dal nuovo dal quale verrà vidimato in automatico il nuovo numero FIR da associare al formulario (optional)
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Crea FIR
        api_response = api_instance.root_post(nuovo_formulario_model, codice_blocco=codice_blocco, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->root_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->root_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nuovo_formulario_model** | [**NuovoFormularioModel**](NuovoFormularioModel.md)| Dati del formulario da creare | 
 **codice_blocco** | **str**| Codice blocco dal nuovo dal quale verrà vidimato in automatico il nuovo numero FIR da associare al formulario | [optional] 
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xfir_valida_post**
> TransazioneModel xfir_valida_post(valida_xfir_model, x_reply_to=x_reply_to)

🔁[ASYNC] Validazione xFIR

Acquisisce la richiesta di controllo di validità dei dati contenuti nel file xFIR secondo le specifiche dal formato.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header X-ReplyTo, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import rentri_formulari
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.models.valida_xfir_model import ValidaXfirModel
from rentri_formulari.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://demoapi.rentri.gov.it/formulari/v1.0
# See configuration.py for a list of all supported configuration parameters.
configuration = rentri_formulari.Configuration(
    host = "https://demoapi.rentri.gov.it/formulari/v1.0"
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    valida_xfir_model = rentri_formulari.ValidaXfirModel() # ValidaXfirModel | Oggetto contenente il contenuto del file xFIR
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Validazione xFIR
        api_response = api_instance.xfir_valida_post(valida_xfir_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->xfir_valida_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->xfir_valida_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **valida_xfir_model** | [**ValidaXfirModel**](ValidaXfirModel.md)| Oggetto contenente il contenuto del file xFIR | 
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header X-ReplyTo. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5s, in caso occorre attendere 10s per effettuare una nuova richiesta. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

