# rentri_formulari.FormularioDigitaleApi

All URIs are relative to *https://api.rentri.gov.it/formulari/v1.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**count_get**](FormularioDigitaleApi.md#count_get) | **GET** /count | Conteggio formulari
[**numero_fir_accettazione_post**](FormularioDigitaleApi.md#numero_fir_accettazione_post) | **POST** /{numero_fir}/accettazione | 🔁[ASYNC] Accettazione FIR
[**numero_fir_acquisizione_firma_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_firma_post) | **POST** /{numero_fir}/acquisizione-firma | 🔁[ASYNC] Imposta dati firma
[**numero_fir_acquisizione_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_num_iscr_sito_post) | **POST** /{numero_fir}/acquisizione/{num_iscr_sito} | ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/acquisizione-visibilita/{numIscrSito} - Acquisizione visibilità FIR
[**numero_fir_acquisizione_visibilita_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_acquisizione_visibilita_num_iscr_sito_post) | **POST** /{numero_fir}/acquisizione-visibilita/{num_iscr_sito} | Acquisizione visibilità FIR
[**numero_fir_allegato_allegato_id_delete**](FormularioDigitaleApi.md#numero_fir_allegato_allegato_id_delete) | **DELETE** /{numero_fir}/allegato/{allegato_id} | 🔁[ASYNC] Rimuove un allegato
[**numero_fir_allegato_allegato_id_get**](FormularioDigitaleApi.md#numero_fir_allegato_allegato_id_get) | **GET** /{numero_fir}/allegato/{allegato_id} | Download un allegato
[**numero_fir_allegato_post**](FormularioDigitaleApi.md#numero_fir_allegato_post) | **POST** /{numero_fir}/allegato | 🔁[ASYNC] Aggiunge un allegato
[**numero_fir_annotazione_post**](FormularioDigitaleApi.md#numero_fir_annotazione_post) | **POST** /{numero_fir}/annotazione | 🔁[ASYNC] Aggiunge annotazione
[**numero_fir_annulla_fir_post**](FormularioDigitaleApi.md#numero_fir_annulla_fir_post) | **POST** /{numero_fir}/annulla-fir | 🔁[ASYNC] Annullamento FIR
[**numero_fir_annulla_post**](FormularioDigitaleApi.md#numero_fir_annulla_post) | **POST** /{numero_fir}/annulla | 🔁[ASYNC] ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/annulla-fir - Annullamento FIR
[**numero_fir_azioni_get**](FormularioDigitaleApi.md#numero_fir_azioni_get) | **GET** /{numero_fir}/azioni | Operazioni disponibili
[**numero_fir_destinatario_post**](FormularioDigitaleApi.md#numero_fir_destinatario_post) | **POST** /{numero_fir}/destinatario | 🔁[ASYNC] Aggiunge nuovo destinatario
[**numero_fir_get**](FormularioDigitaleApi.md#numero_fir_get) | **GET** /{numero_fir} | Dettaglio FIR
[**numero_fir_hash_post**](FormularioDigitaleApi.md#numero_fir_hash_post) | **POST** /{numero_fir}/hash | 🔁[ASYNC] Calcolo del codice hash da firmare
[**numero_fir_invia_a_dispositivo_post**](FormularioDigitaleApi.md#numero_fir_invia_a_dispositivo_post) | **POST** /{numero_fir}/invia-a-dispositivo | Invia il FIR ad un dispositivo
[**numero_fir_note_annullamento_post**](FormularioDigitaleApi.md#numero_fir_note_annullamento_post) | **POST** /{numero_fir}/note-annullamento | 🔁[ASYNC] Imposta le note di annullamento del FIR
[**numero_fir_pdf_get**](FormularioDigitaleApi.md#numero_fir_pdf_get) | **GET** /{numero_fir}/pdf | Stampa PDF del FIR
[**numero_fir_put**](FormularioDigitaleApi.md#numero_fir_put) | **PUT** /{numero_fir} | 🔁[ASYNC] Modifica FIR
[**numero_fir_quantita_post**](FormularioDigitaleApi.md#numero_fir_quantita_post) | **POST** /{numero_fir}/quantita | 🔁[ASYNC] Imposta quantità
[**numero_fir_reset_post**](FormularioDigitaleApi.md#numero_fir_reset_post) | **POST** /{numero_fir}/reset | 🔁[ASYNC] Reset stato
[**numero_fir_respingi_post**](FormularioDigitaleApi.md#numero_fir_respingi_post) | **POST** /{numero_fir}/respingi | ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/rilascio-visibilita/{numIscrSito} - Rilascio visibilità FIR
[**numero_fir_rilascio_visibilita_num_iscr_sito_post**](FormularioDigitaleApi.md#numero_fir_rilascio_visibilita_num_iscr_sito_post) | **POST** /{numero_fir}/rilascio-visibilita/{num_iscr_sito} | Rilascio visibilità FIR
[**numero_fir_rollback_firma_post**](FormularioDigitaleApi.md#numero_fir_rollback_firma_post) | **POST** /{numero_fir}/rollback-firma | 🔁[ASYNC] Rollback dell&#39;ultima firma
[**numero_fir_sosta_tecnica_post**](FormularioDigitaleApi.md#numero_fir_sosta_tecnica_post) | **POST** /{numero_fir}/sosta-tecnica | 🔁[ASYNC] Aggiunge sosta tecnica
[**numero_fir_stato_get**](FormularioDigitaleApi.md#numero_fir_stato_get) | **GET** /{numero_fir}/stato | Stato FIR
[**numero_fir_trasbordo_parziale_post**](FormularioDigitaleApi.md#numero_fir_trasbordo_parziale_post) | **POST** /{numero_fir}/trasbordo-parziale | 🔁[ASYNC] Aggiunge trasbordo parziale
[**numero_fir_trasbordo_totale_post**](FormularioDigitaleApi.md#numero_fir_trasbordo_totale_post) | **POST** /{numero_fir}/trasbordo-totale | 🔁[ASYNC] Aggiunge trasbordo totale
[**numero_fir_trasporto_post**](FormularioDigitaleApi.md#numero_fir_trasporto_post) | **POST** /{numero_fir}/trasporto | 🔁[ASYNC] Aggiunge dati trasporto
[**numero_fir_xfir_get**](FormularioDigitaleApi.md#numero_fir_xfir_get) | **GET** /{numero_fir}/xfir | Download xFIR
[**numero_fir_xfir_post**](FormularioDigitaleApi.md#numero_fir_xfir_post) | **POST** /{numero_fir}/xfir | 🔁[ASYNC] Upload xFIR
[**root_get**](FormularioDigitaleApi.md#root_get) | **GET** / | Elenco formulari
[**root_post**](FormularioDigitaleApi.md#root_post) | **POST** / | 🔁[ASYNC] Crea FIR
[**xfir_valida_post**](FormularioDigitaleApi.md#xfir_valida_post) | **POST** /xfir/valida | 🔁[ASYNC] Validazione xFIR


# **count_get**
> int count_get(num_iscr_sito=num_iscr_sito, identificativo_soggetto=identificativo_soggetto, solo_senza_visibilita_siti=solo_senza_visibilita_siti, numero_fir=numero_fir, codice_blocco=codice_blocco, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, stati=stati)

Conteggio formulari

Ottiene il conteggio dei formulari digitali con visibilità per l'unità locale indicata e con i filtri specificati.

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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione per il quale si richiedono i formulari. Il dato deve essere valorizzato in assenza di un valore per la proprietà \"identificativo_soggetto\". (optional)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Identificativo del soggetto. Quando viene specificato vengono restituiti tutti i FIR digitali nei quali il valore specificato  coincide con il codice fiscale di uno dei soggetti indicati, indipendentemente dallo specifico ruolo  e indipendentemente dall'aver acquisito la visibilità del FIR digitale in una specifica Unità Locale. Il dato deve essere valorizzato in assenza di un valore per la proprietà \"num_iscr_sito\". (optional)
    solo_senza_visibilita_siti = True # bool | Se valorizzata a true, quando viene valorizzata la proprietà \"identificativo_soggetto\" esclude dalla lista restituita  i FIR per cui esiste già visibilità per almeno un'unità locale riconducibile al soggetto stesso. (optional)
    numero_fir = 'numero_fir_example' # str | Numero del FIR (optional)
    codice_blocco = 'codice_blocco_example' # str | Codice blocco del FIR (optional)
    data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Codice EER (optional)
    stati = ['stati_example'] # List[str] |  (optional)

    try:
        # Conteggio formulari
        api_response = api_instance.count_get(num_iscr_sito=num_iscr_sito, identificativo_soggetto=identificativo_soggetto, solo_senza_visibilita_siti=solo_senza_visibilita_siti, numero_fir=numero_fir, codice_blocco=codice_blocco, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, stati=stati)
        print("The response of FormularioDigitaleApi->count_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->count_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione per il quale si richiedono i formulari. Il dato deve essere valorizzato in assenza di un valore per la proprietà \&quot;identificativo_soggetto\&quot;. | [optional] 
 **identificativo_soggetto** | **str**| Identificativo del soggetto. Quando viene specificato vengono restituiti tutti i FIR digitali nei quali il valore specificato  coincide con il codice fiscale di uno dei soggetti indicati, indipendentemente dallo specifico ruolo  e indipendentemente dall&#39;aver acquisito la visibilità del FIR digitale in una specifica Unità Locale. Il dato deve essere valorizzato in assenza di un valore per la proprietà \&quot;num_iscr_sito\&quot;. | [optional] 
 **solo_senza_visibilita_siti** | **bool**| Se valorizzata a true, quando viene valorizzata la proprietà \&quot;identificativo_soggetto\&quot; esclude dalla lista restituita  i FIR per cui esiste già visibilità per almeno un&#39;unità locale riconducibile al soggetto stesso. | [optional] 
 **numero_fir** | **str**| Numero del FIR | [optional] 
 **codice_blocco** | **str**| Codice blocco del FIR | [optional] 
 **data_creazione_da** | **datetime**| Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_creazione_a** | **datetime**| Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Codice EER | [optional] 
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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita sul Registro. |  -  |
**404** | Not Found |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_accettazione_post**
> TransazioneModel numero_fir_accettazione_post(numero_fir, dati_accettazione_model, x_reply_to=x_reply_to)

🔁[ASYNC] Accettazione FIR

Acquisisce la richiesta di aggiunta dei dati di accettazione del rifiuto da parte del destinatario per il FIR specificato.  L'aggiunta dei dati di accettazione è consentita solo ad un'utenza che abbia visibilità per (o coincida con) il soggetto destinatario che è in attesa del rifiuto.   Stati del formulario ammessi: <ul><li>InserimentoAccettazione</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_accettazione_model import DatiAccettazioneModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_firma_post**
> TransazioneModel numero_fir_acquisizione_firma_post(numero_fir, firma_model, x_reply_to=x_reply_to)

🔁[ASYNC] Imposta dati firma

Acquisisce la richiesta di aggiunta dei dati per completare la creazione del file di firma digitale XAdES nel file xFIR.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto, tra quelli indicati nel formulario, coinvolto nell'operazione di aggiunta delle informazioni da firmare.  Il formulario deve essere in uno stato di attesa di firma, conseguente all'aggiunta di nuove informazioni.  Stati del formulario ammessi: <ul><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaProduttore</li><li>FirmaTrasportatoreIniziale</li><li>FirmaTrasportatoreSuccessivo</li><li>FirmaAccettazione</li><li>FirmaAnnotazione</li><li>FirmaAnnullamento</li><li>FirmaTrasbordoParziale</li><li>FirmaTrasbordoTotale</li><li>FirmaSostaTecnica</li><li>FirmaDestinatarioSuccessivo</li><li>FirmaAccettazioneSuccessiva</li></ul> Il valore della proprietà <i>firma</i> deve corrispondere alla firma crittografica calcolata con la chiave privata  associata al certificato X509 indicato nella proprietà <i>certificato</i>.  Il valore della proprietà <i>token</i> deve coincidere con il valore restituito dalla precedente invocazione all'endpoint <i>POST /{numero_fir}/hash</i>, utilizzata per richiedere il codice hash da firmare.  In ambiente di <b>PRODUZIONE</b> l'operazione asincrona, con l'identificativo della transazione restituito dall'endpoint, avrà esito positivo solo se  il codice hash firmato è stato calcolato sulla base di una data dichiarata di firma successiva alle ore 00:00 del giorno 13/02/2026.  L'art. 7 c.3 del D.M. 59/2023 prevede che il FIR sia sottoscritto da parte degli operatori coinvolti nelle diverse fasi del trasporto,  per cui se il certificato di firma è intestato ad una persona giuridica deve riferirsi al soggetto firmatario. Esclusivamente in ambiente <b>DEMO</b>, se il certificato firmatario non viene riconosciuto come valido secondo la regola qui descritta, il sistema produrrà un avviso non bloccante. In ambiente di <b>PRODUZIONE</b> il controllo sarà bloccante.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.firma_model import FirmaModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_num_iscr_sito_post**
> numero_fir_acquisizione_num_iscr_sito_post(numero_fir, num_iscr_sito)

⚠️[DEPRECATO] - utilizzare /{numeroFIR}/acquisizione-visibilita/{numIscrSito} - Acquisizione visibilità FIR

Acquisisce la visibilità in ricerca sull'unità locale specificata di un FIR digitale creato da terzi.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario,  e a cui deve essere riferibile il numero di iscrizione dell'unità locale specificata nel parametro <b>num_iscr_sito</b> . L'operazione consente di rendere visibile il FIR digitale in ricerca per una specifica unità locale.

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_acquisizione_visibilita_num_iscr_sito_post**
> numero_fir_acquisizione_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)

Acquisizione visibilità FIR

Acquisisce la visibilità in ricerca sull'unità locale specificata di un FIR digitale creato da terzi.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario,  e a cui deve essere riferibile il numero di iscrizione dell'unità locale specificata nel parametro <b>num_iscr_sito</b> . L'operazione consente di rendere visibile il FIR digitale in ricerca per una specifica unità locale.

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_allegato_allegato_id_delete**
> TransazioneModel numero_fir_allegato_allegato_id_delete(numero_fir, allegato_id, x_reply_to=x_reply_to)

🔁[ASYNC] Rimuove un allegato

Acquisisce la richiesta di eliminazione di un allegato dal formulario digitale specificato.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto a cui è stato riferito l'allegato specificato in fase di inserimento.  L'operazione può essere eseguita in tutti gli stati, salvo gli stati Annullato e FirmaAnnullamento.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    allegato_id = 56 # int | Identificativo dell'allegato all'interno del FIR digitale
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Rimuove un allegato
        api_response = api_instance.numero_fir_allegato_allegato_id_delete(numero_fir, allegato_id, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_allegato_allegato_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_allegato_allegato_id_delete: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **allegato_id** | **int**| Identificativo dell&#39;allegato all&#39;interno del FIR digitale | 
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_allegato_allegato_id_get**
> DownloadableBaseResponse numero_fir_allegato_allegato_id_get(numero_fir, allegato_id)

Download un allegato

Restituisce il file allegato al formulario digitale specificato.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto a cui è stato riferito l'allegato specificato in fase di inserimento.

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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    allegato_id = 56 # int | Identificativo dell'allegato all'interno del FIR digitale

    try:
        # Download un allegato
        api_response = api_instance.numero_fir_allegato_allegato_id_get(numero_fir, allegato_id)
        print("The response of FormularioDigitaleApi->numero_fir_allegato_allegato_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_allegato_allegato_id_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **allegato_id** | **int**| Identificativo dell&#39;allegato all&#39;interno del FIR digitale | 

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
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_allegato_post**
> TransazioneModel numero_fir_allegato_post(numero_fir, dati_allegato_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge un allegato

Acquisisce la richiesta di aggiunta di un allegato al formulario digitale specificato.  L'operazione può essere eseguita in tutti gli stati, salvo gli stati Annullato e FirmaAnnullamento.  Il file aggiunto all'xFIR viene inserito all'interno del contenitore ZIP e non ncessita di essere firmato.  Il file da allegare non deve superare 1 MB di dimensione, e la dimensione massima del file xFIR risultante non deve superare i 3 MB. I file accettati come allegati da questo endpoint devono necessariamente essere dei file PDF.  Per il recupero dell'allegato è necessario scaricare il file xFIR.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_allegato_model import DatiAllegatoModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_allegato_model = rentri_formulari.DatiAllegatoModel() # DatiAllegatoModel | Insieme delle informazioni riguardanti l'allegato da aggiungere al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge un allegato
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_annotazione_post**
> TransazioneModel numero_fir_annotazione_post(numero_fir, dati_annotazione_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge annotazione

Acquisisce la richiesta di aggiunta di un'annotazione da allegare al formulario digitale specificato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto del formulario, trasportatore o destinatario, che risulta avere in carico il rifiuto successivamente alle firme di partenza.  Stati del formulario ammessi: <ul><li>InserimentoAccettazione</li><li>InserimentoTrasportoSuccessivo</li><li>Accettato</li><li>RespintoAccettatoParzialmente</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_annotazione_model import DatiAnnotazioneModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_annulla_fir_post**
> TransazioneModel numero_fir_annulla_fir_post(numero_fir, x_reply_to=x_reply_to)

🔁[ASYNC] Annullamento FIR

Acquisisce la richiesta di annullamento del FIR specificato.  L'operazione può essere richiesta solo da un utenza che abbia incarichi per (o coincida con) il soggetto che, tra produttore e trasportatore iniziale, ha vidimato il numero FIR.  L'annullamento può essere richiesto solo se il formulario non risulta già essere firmato sia dal produttore che dal trasportatore.  Stati del formulario ammessi: <ul><li>InserimentoQuantita</li><li>InserimentoQuantitaTrasportoIniziale</li><li>InserimentoTrasportoIniziale</li><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaProduttore</li><li>FirmaTrasportatoreIniziale</li></ul> Ulteriori condizioni affinché l'annullamento sia eseguito sono: <ul><li>Non deve risultare una copia digitale del FIR con lo stesso numero già consegnata dal destinatario</li><li>Non deve risultare (per rifiuti pericolosi) alcuna trasmissione di dati del FIR digitale con lo stesso numero avvenuta da parte di alcun soggetto coinvolto nel FIR.</li></ul> L'operazione di annullamento provvede ad annullare il FIR e la relativa vidimazione.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Annullamento FIR
        api_response = api_instance.numero_fir_annulla_fir_post(numero_fir, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_annulla_fir_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_annulla_fir_post: %s\n" % e)
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_annulla_post**
> TransazioneModel numero_fir_annulla_post(numero_fir, dati_annullamento_model, x_reply_to=x_reply_to)

🔁[ASYNC] ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/annulla-fir - Annullamento FIR

Acquisisce la richiesta di annullamento del FIR specificato.  L'annullamento può essere richiesto solo se il formulario non risulta già essere firmato sia dal produttore che dal trasportatore.  L'operazione di annullamento provvede ad annullare il FIR e la relativa vidimazione. Questa operazione può essere richiesta solo dal soggetto che ha vidimato il numero FIR. Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_annullamento_model import DatiAnnullamentoModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    dati_annullamento_model = rentri_formulari.DatiAnnullamentoModel() # DatiAnnullamentoModel | Insieme delle informazioni riguardanti l'allegato da aggiungere al formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] ⚠️[DEPRECATO] - utilizzare /{numeroFIR}/annulla-fir - Annullamento FIR
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_azioni_get**
> AzioniResult numero_fir_azioni_get(numero_fir, identificativo_soggetto, num_iscr_sito=num_iscr_sito)

Operazioni disponibili

Restituisce l'elenco delle azioni che è possibile eseguire sul formulario indicato, in funzione dello stato in cui si trova, dal soggetto specificato nel parametro <b>identificativo_soggetto</b>.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto specificato nel parametro <b>identificativo_soggetto</b> ed almeno uno dei soggetti coinvolti nel formulario.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.azioni_result import AzioniResult
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Codice fiscale del soggetto per il quale si richiedono le azioni possibili
    num_iscr_sito = 'num_iscr_sito_example' # str | Se valorizzato con il numero di iscrizione di una unità locale del soggetto specificato con il parametro <b>identificativo_soggetto</b>, l'unità locale acquisisce automaticamente la visibilità per il FIR digitale (optional)

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
 **num_iscr_sito** | **str**| Se valorizzato con il numero di iscrizione di una unità locale del soggetto specificato con il parametro &lt;b&gt;identificativo_soggetto&lt;/b&gt;, l&#39;unità locale acquisisce automaticamente la visibilità per il FIR digitale | [optional] 

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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_destinatario_post**
> TransazioneModel numero_fir_destinatario_post(numero_fir, numero_fir_destinatario_post_request, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge nuovo destinatario

Acquisisce la richiesta di aggiunta dei dati del nuovo destinatario per il rifiuto indicato nel formulario specificato, a seguito del respingimento o della parziale accettazione del rifiuto da parte del destinatario precedente.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto produttore o il soggetto trasportatore che risulta avere  in carico il rifiuto al momento del respingimento.  Stati del formulario ammessi: <ul><li>RespintoAccettatoParzialmente</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.numero_fir_destinatario_post_request import NumeroFirDestinatarioPostRequest
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_get**
> DettaglioFormulario numero_fir_get(numero_fir)

Dettaglio FIR

Restituisce i dati completi del formulario indicato.   L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dettaglio_formulario import DettaglioFormulario
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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_hash_post**
> TransazioneModel numero_fir_hash_post(numero_fir, dati_per_firma_model, x_reply_to=x_reply_to)

🔁[ASYNC] Calcolo del codice hash da firmare

Acquisisce la richiesta per il calcolo del codice hash di tipo SHA256 da firmare per poter apporre la firma digitale sul formulario.    L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto tra quelli indicati nel formulario   coinvolto nell'operazione di aggiunta delle informazioni da firmare.    Il formulario deve essere in uno stato di attesa di firma, conseguente all'aggiunta di nuove informazioni.    Stati del formulario ammessi:  <ul><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaProduttore</li><li>FirmaTrasportatoreIniziale</li><li>FirmaTrasportatoreSuccessivo</li><li>FirmaAccettazione</li><li>FirmaAnnotazione</li><li>FirmaAnnullamento</li><li>FirmaTrasbordoParziale</li><li>FirmaTrasbordoTotale</li><li>FirmaSostaTecnica</li><li>FirmaDestinatarioSuccessivo</li><li>FirmaAccettazioneSuccessiva</li></ul>  Questa operazione non muta lo stato del formulario.    Il codice hash SHA256 prodotto da questo endpoint è calcolato sull'elemento della struttura dati XAdES <i>ds:SignedInfo</i>,  che contiene un riferimento ad una data dichiarata di firma impostata con l'ora corrente al momento dell'invocazione.     Il codice hash dovrà essere firmato con la chiave privata associata al certificato X509 indicato nella proprietà <i>certificato</i> del modello di input.    Per completare l'apposizione della firma al formulario digitale dovrà essere successivamente invocato l'endpoint <i>POST /{numero_fir}/acquisizione-firma</i>   specificando nel modello di input:   <ul><li>lo stesso certificato X509 incluso nell'invocazione di questo endpoint</li><li>lo stesso token ricevuto nell'esito di questa invocazione</li><li>la firma crittografica calcolata con la chiave privata associata al certificato X509</li></ul>  L'art. 7 c.3 del D.M. 59/2023 prevede che il FIR sia sottoscritto da parte degli operatori coinvolti nelle diverse fasi del trasporto,   per cui se il certificato di firma è intestato ad una persona giuridica deve riferirsi al soggetto firmatario.  Esclusivamente in ambiente <b>DEMO</b>, se il certificato firmatario non viene riconosciuto come valido secondo la regola qui descritta, il sistema produrrà un avviso non bloccante.  In ambiente di <b>PRODUZIONE</b> il controllo sarà bloccante.    Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_per_firma_model import DatiPerFirmaModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_invia_a_dispositivo_post**
> numero_fir_invia_a_dispositivo_post(numero_fir, credentials_id)

Invia il FIR ad un dispositivo

Effettua l'invio delle informazioni di un formulario al dispositivo associato all'identificativo delle credenziali.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.  Le credenziali indicate nel parametro <b>credentials_id</b> devono essere state create attraverso le API \"Firma remota RENTRI\",  e devono essere associate o all'unità locale che ha creato il FIR digitale, oppure ad una delle unità locali che abbiano già acquisito la visibilità del FIR digitale.

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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    credentials_id = 'credentials_id_example' # str | Identificativo delle credenziali

    try:
        # Invia il FIR ad un dispositivo
        api_instance.numero_fir_invia_a_dispositivo_post(numero_fir, credentials_id)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_invia_a_dispositivo_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **credentials_id** | **str**| Identificativo delle credenziali | 

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
**200** | L&#39;invio del FIR è avvenuto con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_note_annullamento_post**
> TransazioneModel numero_fir_note_annullamento_post(numero_fir, note_annullamento_model, x_reply_to=x_reply_to)

🔁[ASYNC] Imposta le note di annullamento del FIR

Acquisisce la richiesta di aggiunta delle note di annullamento per il FIR specificato.  L'operazione può essere richiesta solo da un utenza che abbia incarichi per (o coincida con) il soggetto che, tra produttore e trasportatore iniziale, ha vidimato il numero FIR.  Stati del formulario ammessi: <ul><li>Annullato (il formulario deve essere privo di note)</li></ul> Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.note_annullamento_model import NoteAnnullamentoModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    note_annullamento_model = rentri_formulari.NoteAnnullamentoModel() # NoteAnnullamentoModel | Dati di annullamento
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Imposta le note di annullamento del FIR
        api_response = api_instance.numero_fir_note_annullamento_post(numero_fir, note_annullamento_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_note_annullamento_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_note_annullamento_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario | 
 **note_annullamento_model** | [**NoteAnnullamentoModel**](NoteAnnullamentoModel.md)| Dati di annullamento | 
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
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_pdf_get**
> DownloadableBaseResponse numero_fir_pdf_get(numero_fir)

Stampa PDF del FIR

Ottiene una stampa in PDF del FIR.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

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
**200** | Formulario in formato PDF restituito in payload |  -  |
**204** | No Content |  -  |
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita |  -  |
**404** | Formulario non trovato |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_put**
> TransazioneModel numero_fir_put(numero_fir, nuovo_formulario_model, x_reply_to=x_reply_to)

🔁[ASYNC] Modifica FIR

Acquisisce la richiesta di modifica dei dati di un FIR esistente.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto produttore o il soggetto del primo trasportatore indicati nel formulario originale.  Stati del formulario ammessi: <ul><li>InserimentoQuantita</li><li>InserimentoQuantitaTrasportoIniziale</li><li>InserimentoTrasportoIniziale</li><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaTrasportatoreIniziale (per formulario da trasbordo parziale)</li></ul> Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.nuovo_formulario_model import NuovoFormularioModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
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
 **numero_fir** | **str**| Numero FIR del formulario | 
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_quantita_post**
> TransazioneModel numero_fir_quantita_post(numero_fir, quantita_rifiuto_model, x_reply_to=x_reply_to)

🔁[ASYNC] Imposta quantità

Acquisice la richiesta di aggiunta o modifica del dato della quantità sul formulario indicato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il produttore o il primo trasportatore.  Stati del formulario ammessi: <ul><li>InserimentoQuantita</li><li>InserimentoQuantitaTrasportoIniziale</li><li>InserimentoTrasportoIniziale</li><li>FirmaProduttoreTrasportatoreIniziale</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.quantita_rifiuto_model import QuantitaRifiutoModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_reset_post**
> TransazioneModel numero_fir_reset_post(numero_fir, x_reply_to=x_reply_to)

🔁[ASYNC] Reset stato

Acquisisce la richiesta di cancellazione degli ultimi dati inseriti nel formulario in attesa di firma, riportando lo stato del formulario a quello precedente.  La cancellazione degli ultimi dati inseriti (e non ancora firmati) è consentita solo alle utenze con visibilità per (o che coincidono con)  gli stessi soggetti coinvolti nel formulario a cui è consentito l'inserimento del tipo di informazione che si sta eliminando. Stati del formulario ammessi: <ul><li>FirmaTrasportatoreIniziale (per formulario da trasbordo parziale)</li><li>FirmaTrasportatoreSuccessivo</li><li>FirmaDestinatarioSuccessivo</li><li>FirmaAccettazione</li><li>FirmaAccettazioneSuccessiva</li><li>FirmaAnnotazione</li><li>FirmaAnnullamento</li><li>FirmaTrasbordoParziale</li><li>FirmaTrasbordoTotale</li><li>FirmaSostaTecnica</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_respingi_post**
> numero_fir_respingi_post(numero_fir, num_iscr_sito=num_iscr_sito)

⚠️[DEPRECATO] - utilizzare /{numeroFIR}/rilascio-visibilita/{numIscrSito} - Rilascio visibilità FIR

Abbandona la visibilità in ricerca sull'unità locale specificata, ottenuta con l'operazione di \"acquisizione di visibilità\", relativamente al FIR digitale specificato creato da terzi.

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
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_rilascio_visibilita_num_iscr_sito_post**
> numero_fir_rilascio_visibilita_num_iscr_sito_post(numero_fir, num_iscr_sito)

Rilascio visibilità FIR

Abbandona la visibilità in ricerca sull'unità locale specificata, ottenuta con l'operazione di \"acquisizione\", relativamente al FIR digitale specificato creato da terzi.

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
**200** | Il rilascio della visibilità è avvenuto con successo |  -  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_rollback_firma_post**
> TransazioneModel numero_fir_rollback_firma_post(numero_fir, x_reply_to=x_reply_to)

🔁[ASYNC] Rollback dell'ultima firma

Acquisisce la richiesta di rollback dell'ultima firma apposta (tranne la firma di annullamento) riportando lo stato del formulario a quello di attesa firma precedente alla sua apposizione.  L'operazione di apposizione delle firme digitali in un FIR attraverso gli endpoint di queste API è reversibile solo a determinate condizioni: <ul><li>la firma è l'ultima apposta al FIR digitale in ordine temporale</li><li>la firma è stata apposta con le API RENTRI senza che il file sia stato ricaricato con un'operazione di upload dopo la sua apposizione</li><li>la firma è stata apposta su dati riferiti ad un soggetto che coincide con l'identità di chi invoca l'endpoint (o per cui l'utente che invoca l'endpoint ha visibilità)</li><li>la firma è stata apposta entro i 15 minuti precedenti al momento in cui si richiede l'operazione (calcolati dalla data firma presente nella struttura dati XAdES del file di firma)</li><li>non è stata effettuata, dopo l'acquisizione della firma, alcuna operazione di download (via API, portale Operatori iscritti, App RENTRI) del file xFIR attraverso <i>GET /{numero_fir}/xfir</i>; da parte di alcun soggetto che abbia visibilità del FIR</li><li>non è presente a sistema una copia cartacea con lo stesso numero FIR restituita dal trasportatore agli altri soggetti coinvolti nel FIR</li><li>non è presente a sistema una copia digitale con lo stesso numero FIR restituita dal destinatario agli altri soggetti coinvolti nel FIR</li></ul> Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Rollback dell'ultima firma
        api_response = api_instance.numero_fir_rollback_firma_post(numero_fir, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_rollback_firma_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_rollback_firma_post: %s\n" % e)
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_sosta_tecnica_post**
> TransazioneModel numero_fir_sosta_tecnica_post(numero_fir, dati_sosta_tecnica_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge sosta tecnica

Acquisisce la richiesta per l'aggiunta dei dati di sosta tecnica per il formulario indicato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto trasportatore che risulta avere  in carico il rifiuto.  Stati del formulario ammessi: <ul><li>InserimentoAccettazione</li><li>InserimentoTrasportoSuccessivo</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_sosta_tecnica_model import DatiSostaTecnicaModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_stato_get**
> InfoFormulario numero_fir_stato_get(numero_fir)

Stato FIR

Restituisce lo stato del formulario

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.info_formulario import InfoFormulario
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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasbordo_parziale_post**
> TransazioneModel numero_fir_trasbordo_parziale_post(numero_fir, dati_trasbordo_parziale_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge trasbordo parziale

Acquisisce la richiesta per l'aggiunta dei dati di un trasbordo parziale per il formulario indicato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto trasportatore che risulta avere  in carico il rifiuto.  Stati del formulario ammessi: <ul><li>InserimentoAccettazione</li><li>InserimentoTrasportoSuccessivo</li></ul> In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_trasbordo_parziale_model import DatiTrasbordoParzialeModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiungono i dati del trasbordo
    dati_trasbordo_parziale_model = rentri_formulari.DatiTrasbordoParzialeModel() # DatiTrasbordoParzialeModel | Dati con il dettaglio del trasbordo parziale
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Aggiunge trasbordo parziale
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
 **dati_trasbordo_parziale_model** | [**DatiTrasbordoParzialeModel**](DatiTrasbordoParzialeModel.md)| Dati con il dettaglio del trasbordo parziale | 
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
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasbordo_totale_post**
> TransazioneModel numero_fir_trasbordo_totale_post(numero_fir, dati_trasbordo_totale_model, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge trasbordo totale

Acquisisce la richiesta per l'aggiunta dei dati di un trasbordo totale per il formulario indicato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto trasportatore che risulta avere  in carico il rifiuto.  Stati del formulario ammessi: <ul><li>InserimentoAccettazione</li><li>InserimentoTrasportoSuccessivo</li></ul> Il tipo del trasporto deve essere <b>\"Terrestre\"</b>.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.dati_trasbordo_totale_model import DatiTrasbordoTotaleModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario a cui si aggiungono i dati del trasbordo totale
    dati_trasbordo_totale_model = rentri_formulari.DatiTrasbordoTotaleModel() # DatiTrasbordoTotaleModel | Dati con il dettaglio del trasbordo totale
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
 **dati_trasbordo_totale_model** | [**DatiTrasbordoTotaleModel**](DatiTrasbordoTotaleModel.md)| Dati con il dettaglio del trasbordo totale | 
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
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_trasporto_post**
> TransazioneModel numero_fir_trasporto_post(numero_fir, numero_fir_trasporto_post_request, x_reply_to=x_reply_to)

🔁[ASYNC] Aggiunge dati trasporto

Acquisisce la richiesta di aggiunta dei dati di trasporto del rifiuto da parte del trasportatore che ha in carico il FIR specificato.  L'operazione può essere eseguita da un'utenza che abbia visibilità su (o coincida con) il soggetto produttore o il soggetto trasportatore iniziale, nel caso il formulario non sia ancora stato firmato, oppure il trasportatore che effettua la presa in carico del rifiuto dal trasportatore precedente.  Stati del formulario ammessi: <ul><li>InserimentoQuantita</li><li>InserimentoQuantitaTrasportoIniziale</li><li>InserimentoTrasportoIniziale</li><li>InserimentoTrasportoSuccessivo</li><li>FirmaProduttoreTrasportatoreIniziale</li><li>FirmaTrasportatoreIniziale (per formulario da trasbordo parziale)</li><li>FirmaTrasportatoreSuccessivo</li><li>FirmaTrasbordoTotale</li></ul> Il tipo di modello passato come contenuto del POST determina la modalità del trasporto.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.numero_fir_trasporto_post_request import NumeroFirTrasportoPostRequest
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_xfir_get**
> DownloadableBaseResponse numero_fir_xfir_get(numero_fir)

Download xFIR

Restituisce il file in formato xFIR che rappresenta il formulario specificato con il numero FIR.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.

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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita. |  -  |
**404** | Formulario non trovato. |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza). |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **numero_fir_xfir_post**
> TransazioneModel numero_fir_xfir_post(numero_fir, upload_xfir_model, x_reply_to=x_reply_to)

🔁[ASYNC] Upload xFIR

Carica un file xFIR esterno nell'area virtuale di interscambio per permetterne l'aggiunta di informazioni e relative firme attraverso le API formulari.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) almeno uno dei soggetti coinvolti nel formulario.  Se non esiste alcun FIR digitale in compilazione con lo stesso numero, l'endpoint lo aggiunge all'area virtuale di interscambio permettendone l'interazione con queste API.  Se il file xFIR è già presente nell'area virtuale di interscambio, e le informazioni contenute nel file caricato sono compatibili con quelle del file xFIR già presente, l'endpoint aggiorna il file xFIR con quello caricato.   La compatibilità delle nuove informazioni rispetto a quelle eventualmente già presenti in area virtuale di interscambio è determinata dalla presenza degli stessi dati firmati e degli stessi valori per le relative firme crittografiche.  Il file xFIR inviato deve essere valido secondo le regole definite nella <i>Guida tecnica alla compilazione del FIR digitale</i>  e verificabile dalla specifica funzione di validazione definita dall'endpoint <i>Validazione xFIR</i>. Relativamente alle date dichiarate nell'apposizione delle firme presenti nel file xFIR, l'esito della validazione deve essere <i>Ok</i> per tutti i controlli con codice <i>firmaDataDichiarata</i>.  In ambiente di <b>PRODUZIONE</b>, la validazione dei controlli con codice <i>firmaDataDichiarata</i> sulle date dichiarate di firma presenti nei file XAdES dell'xFIR  avrà esito positivo solo con date successive alle ore 00:00 del giorno 13/02/2026.  In caso esista una copia del FIR digitale già restituita con accettazione totale del rifiuto, l'operazione non è consentita.  La dimensione massima accettata del file xFIR è 3 MB.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.models.upload_xfir_model import UploadXfirModel
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    numero_fir = 'numero_fir_example' # str | Numero FIR del formulario, deve coincidere con quello deducibile dalle informazioni presenti nel file xFIR
    upload_xfir_model = rentri_formulari.UploadXfirModel() # UploadXfirModel | Oggetto contenente il contenuto del file xFIR da caricare
    x_reply_to = 'x_reply_to_example' # str | URL di callback alla quale verrà inviata la notifica di fine elaborazione (optional)

    try:
        # 🔁[ASYNC] Upload xFIR
        api_response = api_instance.numero_fir_xfir_post(numero_fir, upload_xfir_model, x_reply_to=x_reply_to)
        print("The response of FormularioDigitaleApi->numero_fir_xfir_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->numero_fir_xfir_post: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **numero_fir** | **str**| Numero FIR del formulario, deve coincidere con quello deducibile dalle informazioni presenti nel file xFIR | 
 **upload_xfir_model** | [**UploadXfirModel**](UploadXfirModel.md)| Oggetto contenente il contenuto del file xFIR da caricare | 
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
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_get**
> List[FormularioItemResult] root_get(num_iscr_sito=num_iscr_sito, identificativo_soggetto=identificativo_soggetto, solo_senza_visibilita_siti=solo_senza_visibilita_siti, numero_fir=numero_fir, codice_blocco=codice_blocco, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, stati=stati, paging_page=paging_page, paging_page_size=paging_page_size)

Elenco formulari

Ottiene l'elenco dei formulari richiesti con visibilità per l'unità locale indicata e con i filtri specificati.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.formulario_item_result import FormularioItemResult
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
    api_instance = rentri_formulari.FormularioDigitaleApi(api_client)
    num_iscr_sito = 'num_iscr_sito_example' # str | Numero iscrizione unità locale rilasciato all'iscrizione per il quale si richiedono i formulari. Il dato deve essere valorizzato in assenza di un valore per la proprietà \"identificativo_soggetto\". (optional)
    identificativo_soggetto = 'identificativo_soggetto_example' # str | Identificativo del soggetto. Quando viene specificato vengono restituiti tutti i FIR digitali nei quali il valore specificato  coincide con il codice fiscale di uno dei soggetti indicati, indipendentemente dallo specifico ruolo  e indipendentemente dall'aver acquisito la visibilità del FIR digitale in una specifica Unità Locale. Il dato deve essere valorizzato in assenza di un valore per la proprietà \"num_iscr_sito\". (optional)
    solo_senza_visibilita_siti = True # bool | Se valorizzata a true, quando viene valorizzata la proprietà \"identificativo_soggetto\" esclude dalla lista restituita  i FIR per cui esiste già visibilità per almeno un'unità locale riconducibile al soggetto stesso. (optional)
    numero_fir = 'numero_fir_example' # str | Numero del FIR (optional)
    codice_blocco = 'codice_blocco_example' # str | Codice blocco del FIR (optional)
    data_creazione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_creazione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_da = '2013-10-20T19:20:30+01:00' # datetime | Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    data_emissione_a = '2013-10-20T19:20:30+01:00' # datetime | Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) (optional)
    codice_eer = 'codice_eer_example' # str | Codice EER (optional)
    stati = ['stati_example'] # List[str] |  (optional)
    paging_page = 1 # int | Valore per l'header Paging-Page. (optional) (default to 1)
    paging_page_size = 100 # int | Valore per l'header Paging-PageSize. (optional) (default to 100)

    try:
        # Elenco formulari
        api_response = api_instance.root_get(num_iscr_sito=num_iscr_sito, identificativo_soggetto=identificativo_soggetto, solo_senza_visibilita_siti=solo_senza_visibilita_siti, numero_fir=numero_fir, codice_blocco=codice_blocco, data_creazione_da=data_creazione_da, data_creazione_a=data_creazione_a, data_emissione_da=data_emissione_da, data_emissione_a=data_emissione_a, codice_eer=codice_eer, stati=stati, paging_page=paging_page, paging_page_size=paging_page_size)
        print("The response of FormularioDigitaleApi->root_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FormularioDigitaleApi->root_get: %s\n" % e)
```



### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **num_iscr_sito** | **str**| Numero iscrizione unità locale rilasciato all&#39;iscrizione per il quale si richiedono i formulari. Il dato deve essere valorizzato in assenza di un valore per la proprietà \&quot;identificativo_soggetto\&quot;. | [optional] 
 **identificativo_soggetto** | **str**| Identificativo del soggetto. Quando viene specificato vengono restituiti tutti i FIR digitali nei quali il valore specificato  coincide con il codice fiscale di uno dei soggetti indicati, indipendentemente dallo specifico ruolo  e indipendentemente dall&#39;aver acquisito la visibilità del FIR digitale in una specifica Unità Locale. Il dato deve essere valorizzato in assenza di un valore per la proprietà \&quot;num_iscr_sito\&quot;. | [optional] 
 **solo_senza_visibilita_siti** | **bool**| Se valorizzata a true, quando viene valorizzata la proprietà \&quot;identificativo_soggetto\&quot; esclude dalla lista restituita  i FIR per cui esiste già visibilità per almeno un&#39;unità locale riconducibile al soggetto stesso. | [optional] 
 **numero_fir** | **str**| Numero del FIR | [optional] 
 **codice_blocco** | **str**| Codice blocco del FIR | [optional] 
 **data_creazione_da** | **datetime**| Data di creazione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_creazione_a** | **datetime**| Data massima di creazione per la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_da** | **datetime**| Data di emissione a partire dalla quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **data_emissione_a** | **datetime**| Data massima di emissione entro la quale si richiedono i formulari (formato ISO 8601 UTC) | [optional] 
 **codice_eer** | **str**| Codice EER | [optional] 
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
**400** | Dettaglio degli errori di validazione in caso di parametri richiesti non specificati |  -  |
**403** | Operazione non consentita |  -  |
**404** | Entità non trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **root_post**
> TransazioneModel root_post(nuovo_formulario_model, codice_blocco=codice_blocco, x_reply_to=x_reply_to)

🔁[ASYNC] Crea FIR

Acquisisce la richiesta di creazione di un nuovo FIR.  L'operazione può essere eseguita da un'utenza che abbia incarichi per (o coincida con) il soggetto produttore o il soggetto del primo trasportatore indicati nei dati del formulario usati come modello.  Il numero del nuovo FIR può essere specificato nell'apposita proprietà del modello, altrimenti verrà generato automaticamente dal sistema dal blocco indicato nel parametro <b>codice_blocco</b>.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.nuovo_formulario_model import NuovoFormularioModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**403** | Operazione non consentita |  -  |
**404** | Almeno una delle entità specificate nel modello o tra i parametri non è stata trovata |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **xfir_valida_post**
> TransazioneModel xfir_valida_post(valida_xfir_model, x_reply_to=x_reply_to)

🔁[ASYNC] Validazione xFIR

Acquisisce la richiesta di controllo di validità dei dati contenuti nel file xFIR secondo le specifiche del formato definite nella <i>Guida tecnica alla struttura del FIR digitale</i>.  L'operazione può essere eseguita da qualsiasi utenza o soggetto, non necessariamente coinvolta nel formulario.  La dimensione massima accettata del file xFIR è 3 MB.  Con l'identificativo della transazione restituito è possibile consultare lo stato di avanzamento dell'elaborazione e richiederne l'esito.<br/>Se viene specificato un URL nell'header <i>X-ReplyTo</i>, al termine dell'elaborazione dei dati, il fruitore riceverà una notifica con l'esito dell'elaborazione all'URL specificato.

### Example

* Bearer (JWT) Authentication (Bearer):
```python
import time
import os
import rentri_formulari
from rentri_formulari.models.transazione_model import TransazioneModel
from rentri_formulari.models.valida_xfir_model import ValidaXfirModel
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
**202** | Richiesta accettata |  * Location - URL per verificare lo stato dell&#39;elaborazione. Restituito solo se non viene specificata una URL di callback nell&#39;header &lt;i&gt;X-ReplyTo&lt;/i&gt;. <br>  |
**400** | Dettaglio degli errori di validazione in caso di modello dati non valido |  -  |
**423** | Sono state eseguite troppe richieste non valide.        Questa risposta viene restituita quando viene rilevato un numero eccessivo di richieste concorrenti, autenticate ma non valide.        In questo caso, le eventuali richieste valide continueranno ad essere accettate, mentre solo le richieste non valide verranno bloccate applicando un meccanismo di \&quot;ban\&quot; a livello di chiamante (Issuer).        Il servizio di assistenza per l&#39;interoperabilità RENTRI potrà essere contattato dal fruitore del servizio per i chiarimenti relativi alle richieste non valide, al fine di apportare le correzioni necessarie ai client. |  -  |
**429** | Troppe richieste. Questa risposta viene restituita quando vengono rilevate più di 100 richieste in 5 secondi. |  * Retry-After - Indica quanto tempo il fruitore deve attendere prima di effettuare una nuova richiesta. <br>  |
**500** | Errore non gestito (contattare l&#39;assistenza) |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

