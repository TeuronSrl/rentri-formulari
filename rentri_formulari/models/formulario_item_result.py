# coding: utf-8

"""
    formulari

    Servizio Formulari RENTRI

    The version of the OpenAPI document: 1.0.20250114-507
    Contact: techref@rentri.it
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from rentri_formulari.models.intermediario_item_result import IntermediarioItemResult
from rentri_formulari.models.stati_fisici import StatiFisici
from rentri_formulari.models.stato_formulario import StatoFormulario
from rentri_formulari.models.trasbordo_parziale_origine_result import TrasbordoParzialeOrigineResult
from rentri_formulari.models.trasportatore_item_result import TrasportatoreItemResult
from rentri_formulari.models.unita_locale_item_result import UnitaLocaleItemResult
from rentri_formulari.models.unita_misura import UnitaMisura
from typing import Optional, Set
from typing_extensions import Self

class FormularioItemResult(BaseModel):
    """
    FormularioItemResult
    """ # noqa: E501
    numero_fir: Optional[StrictStr] = None
    data_emissione: Optional[datetime] = None
    num_iscr_sito: Optional[StrictStr] = None
    identificativo_soggetto: Optional[StrictStr] = None
    data_creazione: Optional[StrictStr] = None
    codice_eer: Optional[StrictStr] = None
    quantita: Optional[Union[StrictFloat, StrictInt]] = None
    unita_misura: Optional[UnitaMisura] = Field(default=None, description="<p>Valori ammessi:<ul style=\"margin:0\"><li><i>kg</i> - Chilogrammi</li><li><i>l</i> - Litri</li></ul></p>")
    stato_fisico: Optional[StatiFisici] = Field(default=None, description="<p>Valori ammessi:<ul style=\"margin:0\"><li><i>SP</i> - In polvere o pulverulento</li><li><i>S</i> - Solido</li><li><i>FP</i> - Fangoso</li><li><i>L</i> - Liquido</li><li><i>VS</i> - Vischioso sciropposo</li></ul></p>")
    caratteristiche_pericolo: Optional[StrictStr] = None
    destinazione_rifiuto: Optional[StrictStr] = None
    produttore: Optional[UnitaLocaleItemResult] = None
    trasbordo_parziale_origine: Optional[TrasbordoParzialeOrigineResult] = None
    destinatari: Optional[List[UnitaLocaleItemResult]] = None
    trasportatori: Optional[List[TrasportatoreItemResult]] = None
    intermediari: Optional[List[IntermediarioItemResult]] = None
    stato: Optional[StatoFormulario] = Field(default=None, description="<p>Valori ammessi:<ul style=\"margin:0\"><li><i>InserimentoQuantita</i> - Il formulario necessita dei dati sulla quantità del rifiuto</li><li><i>InserimentoQuantitaTrasportoIniziale</i> - Il formulario necessita dei dati sulla quantità del rifiuto e dei dati del trasporto iniziale</li><li><i>InserimentoTrasportoIniziale</i> - Il formulario necessita dei dati del trasporto iniziale</li><li><i>FirmaProduttoreTrasportatoreIniziale</i> - Il formulario necessita della firma del produttore e del trasportatore iniziale</li><li><i>FirmaTrasportatoreIniziale</i> - Il formulario necessita della firma del trasportatore iniziale</li><li><i>FirmaProduttore</i> - Il formulario necessita della firma del produttore</li><li><i>InserimentoTrasportoSuccessivo</i> - Il formulario è in carico ad un traportatore e necessita dell'inserimento dei dati del trasporto successivo;             il trasportatore che ha in carico il rifiuto può inserire informazioni aggiuntive (annotazioni, trasbordo parziale, sosta tecnica, trasbordo totale, allegati)             che dovranno essere successivamente firmate</li><li><i>FirmaTrasportatoreSuccessivo</i> - Il formulario necessita della firma del trasportatore successivo al primo che ha in carico il rifiuto</li><li><i>FirmaAnnotazione</i> - Il formulario necessita della firma dell'annotazione da parte del soggetto che l'ha inserita</li><li><i>FirmaTrasbordoParziale</i> - Il formulario necessita della firma del trasportatore che effettua il trasbordo parziale del rifiuto</li><li><i>FirmaTrasbordoTotale</i> - Il formulario necessita della firma del trasportatore che prende in carico il rifiuto con l'operazione di trasbordo totale del rifiuto</li><li><i>FirmaSostaTecnica</i> - Il formulario necessita della firma del trasportatore che ha in carico il rifiuto e ha inserito i dati della sosta tecnica</li><li><i>FirmaAllegato</i> - Il formulario necessita della firma del soggetto che ha aggiunto i dati relativi all'allegato al formulario digitale</li><li><i>InserimentoAccettazione</i> - Il formulario è in carico all'ultimo trasportatore ed è in attesa dell'inserimento dei dati di accettazione da parte del destinatario verso cui è destinato il rifiuto             (a meno di ulteriori informazioni aggiuntive che l'ultimo trasportatore può inserire prima della consegna al destinatario)</li><li><i>FirmaAccettazione</i> - Il formulario necessita della firma del destinatario indicato nei dati di partenza</li><li><i>Accettato</i> - Il formulario è stato accettato dal destinatario ed ha concluso il suo ciclo di vita</li><li><i>RespintoParzialmenteRespinto</i> - Il formulario è stato respinto o parzialmente respinto, il trasportatore che ha in carico il rifiuto può inserire (in accordo con il produttore) i dati              di un nuovo destinatario</li><li><i>FirmaDestinatarioSuccessivo</i> - Il formulario è in attesa della firma dei dati del nuovo destinatario inseriti da parte del trasportatore che ha in carico il rifiuto</li><li><i>FirmaAccettazioneSuccessiva</i> - Il formulario necessita della firma del destinatario successivo a quello indicato nei dati di partenza che ha rifiutato totalmente o parzialmente il rifiuto</li><li><i>FirmaAnnullamento</i> - Il formulario necessita della firma dei dati di annullamento inseriti dal soggetto titolare della vidimazione del numero FIR</li><li><i>Annullato</i> - Il formulario risulta essere stato annullato</li><li><i>Indeterminato</i> - Il formulario è in uno stato non determinato per incoerenza dei dati contenuti</li></ul></p>")
    __properties: ClassVar[List[str]] = ["numero_fir", "data_emissione", "num_iscr_sito", "identificativo_soggetto", "data_creazione", "codice_eer", "quantita", "unita_misura", "stato_fisico", "caratteristiche_pericolo", "destinazione_rifiuto", "produttore", "trasbordo_parziale_origine", "destinatari", "trasportatori", "intermediari", "stato"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of FormularioItemResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of produttore
        if self.produttore:
            _dict['produttore'] = self.produttore.to_dict()
        # override the default output from pydantic by calling `to_dict()` of trasbordo_parziale_origine
        if self.trasbordo_parziale_origine:
            _dict['trasbordo_parziale_origine'] = self.trasbordo_parziale_origine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in destinatari (list)
        _items = []
        if self.destinatari:
            for _item_destinatari in self.destinatari:
                if _item_destinatari:
                    _items.append(_item_destinatari.to_dict())
            _dict['destinatari'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trasportatori (list)
        _items = []
        if self.trasportatori:
            for _item_trasportatori in self.trasportatori:
                if _item_trasportatori:
                    _items.append(_item_trasportatori.to_dict())
            _dict['trasportatori'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in intermediari (list)
        _items = []
        if self.intermediari:
            for _item_intermediari in self.intermediari:
                if _item_intermediari:
                    _items.append(_item_intermediari.to_dict())
            _dict['intermediari'] = _items
        # set to None if numero_fir (nullable) is None
        # and model_fields_set contains the field
        if self.numero_fir is None and "numero_fir" in self.model_fields_set:
            _dict['numero_fir'] = None

        # set to None if data_emissione (nullable) is None
        # and model_fields_set contains the field
        if self.data_emissione is None and "data_emissione" in self.model_fields_set:
            _dict['data_emissione'] = None

        # set to None if num_iscr_sito (nullable) is None
        # and model_fields_set contains the field
        if self.num_iscr_sito is None and "num_iscr_sito" in self.model_fields_set:
            _dict['num_iscr_sito'] = None

        # set to None if identificativo_soggetto (nullable) is None
        # and model_fields_set contains the field
        if self.identificativo_soggetto is None and "identificativo_soggetto" in self.model_fields_set:
            _dict['identificativo_soggetto'] = None

        # set to None if data_creazione (nullable) is None
        # and model_fields_set contains the field
        if self.data_creazione is None and "data_creazione" in self.model_fields_set:
            _dict['data_creazione'] = None

        # set to None if codice_eer (nullable) is None
        # and model_fields_set contains the field
        if self.codice_eer is None and "codice_eer" in self.model_fields_set:
            _dict['codice_eer'] = None

        # set to None if quantita (nullable) is None
        # and model_fields_set contains the field
        if self.quantita is None and "quantita" in self.model_fields_set:
            _dict['quantita'] = None

        # set to None if unita_misura (nullable) is None
        # and model_fields_set contains the field
        if self.unita_misura is None and "unita_misura" in self.model_fields_set:
            _dict['unita_misura'] = None

        # set to None if stato_fisico (nullable) is None
        # and model_fields_set contains the field
        if self.stato_fisico is None and "stato_fisico" in self.model_fields_set:
            _dict['stato_fisico'] = None

        # set to None if caratteristiche_pericolo (nullable) is None
        # and model_fields_set contains the field
        if self.caratteristiche_pericolo is None and "caratteristiche_pericolo" in self.model_fields_set:
            _dict['caratteristiche_pericolo'] = None

        # set to None if destinazione_rifiuto (nullable) is None
        # and model_fields_set contains the field
        if self.destinazione_rifiuto is None and "destinazione_rifiuto" in self.model_fields_set:
            _dict['destinazione_rifiuto'] = None

        # set to None if produttore (nullable) is None
        # and model_fields_set contains the field
        if self.produttore is None and "produttore" in self.model_fields_set:
            _dict['produttore'] = None

        # set to None if trasbordo_parziale_origine (nullable) is None
        # and model_fields_set contains the field
        if self.trasbordo_parziale_origine is None and "trasbordo_parziale_origine" in self.model_fields_set:
            _dict['trasbordo_parziale_origine'] = None

        # set to None if destinatari (nullable) is None
        # and model_fields_set contains the field
        if self.destinatari is None and "destinatari" in self.model_fields_set:
            _dict['destinatari'] = None

        # set to None if trasportatori (nullable) is None
        # and model_fields_set contains the field
        if self.trasportatori is None and "trasportatori" in self.model_fields_set:
            _dict['trasportatori'] = None

        # set to None if intermediari (nullable) is None
        # and model_fields_set contains the field
        if self.intermediari is None and "intermediari" in self.model_fields_set:
            _dict['intermediari'] = None

        # set to None if stato (nullable) is None
        # and model_fields_set contains the field
        if self.stato is None and "stato" in self.model_fields_set:
            _dict['stato'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FormularioItemResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numero_fir": obj.get("numero_fir"),
            "data_emissione": obj.get("data_emissione"),
            "num_iscr_sito": obj.get("num_iscr_sito"),
            "identificativo_soggetto": obj.get("identificativo_soggetto"),
            "data_creazione": obj.get("data_creazione"),
            "codice_eer": obj.get("codice_eer"),
            "quantita": obj.get("quantita"),
            "unita_misura": obj.get("unita_misura"),
            "stato_fisico": obj.get("stato_fisico"),
            "caratteristiche_pericolo": obj.get("caratteristiche_pericolo"),
            "destinazione_rifiuto": obj.get("destinazione_rifiuto"),
            "produttore": UnitaLocaleItemResult.from_dict(obj["produttore"]) if obj.get("produttore") is not None else None,
            "trasbordo_parziale_origine": TrasbordoParzialeOrigineResult.from_dict(obj["trasbordo_parziale_origine"]) if obj.get("trasbordo_parziale_origine") is not None else None,
            "destinatari": [UnitaLocaleItemResult.from_dict(_item) for _item in obj["destinatari"]] if obj.get("destinatari") is not None else None,
            "trasportatori": [TrasportatoreItemResult.from_dict(_item) for _item in obj["trasportatori"]] if obj.get("trasportatori") is not None else None,
            "intermediari": [IntermediarioItemResult.from_dict(_item) for _item in obj["intermediari"]] if obj.get("intermediari") is not None else None,
            "stato": obj.get("stato")
        })
        return _obj


