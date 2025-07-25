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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class UnitaLocaleItemResult(BaseModel):
    """
    UnitaLocaleItemResult
    """ # noqa: E501
    num_iscr_sito: Optional[StrictStr] = None
    denominazione: Optional[StrictStr] = None
    codice_fiscale: Optional[StrictStr] = None
    indirizzo: Optional[StrictStr] = None
    civico: Optional[StrictStr] = None
    comune_id: Optional[StrictStr] = None
    nazione_id: Optional[StrictStr] = None
    citta_estera: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["num_iscr_sito", "denominazione", "codice_fiscale", "indirizzo", "civico", "comune_id", "nazione_id", "citta_estera"]

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
        """Create an instance of UnitaLocaleItemResult from a JSON string"""
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
        # set to None if num_iscr_sito (nullable) is None
        # and model_fields_set contains the field
        if self.num_iscr_sito is None and "num_iscr_sito" in self.model_fields_set:
            _dict['num_iscr_sito'] = None

        # set to None if denominazione (nullable) is None
        # and model_fields_set contains the field
        if self.denominazione is None and "denominazione" in self.model_fields_set:
            _dict['denominazione'] = None

        # set to None if codice_fiscale (nullable) is None
        # and model_fields_set contains the field
        if self.codice_fiscale is None and "codice_fiscale" in self.model_fields_set:
            _dict['codice_fiscale'] = None

        # set to None if indirizzo (nullable) is None
        # and model_fields_set contains the field
        if self.indirizzo is None and "indirizzo" in self.model_fields_set:
            _dict['indirizzo'] = None

        # set to None if civico (nullable) is None
        # and model_fields_set contains the field
        if self.civico is None and "civico" in self.model_fields_set:
            _dict['civico'] = None

        # set to None if comune_id (nullable) is None
        # and model_fields_set contains the field
        if self.comune_id is None and "comune_id" in self.model_fields_set:
            _dict['comune_id'] = None

        # set to None if nazione_id (nullable) is None
        # and model_fields_set contains the field
        if self.nazione_id is None and "nazione_id" in self.model_fields_set:
            _dict['nazione_id'] = None

        # set to None if citta_estera (nullable) is None
        # and model_fields_set contains the field
        if self.citta_estera is None and "citta_estera" in self.model_fields_set:
            _dict['citta_estera'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UnitaLocaleItemResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "num_iscr_sito": obj.get("num_iscr_sito"),
            "denominazione": obj.get("denominazione"),
            "codice_fiscale": obj.get("codice_fiscale"),
            "indirizzo": obj.get("indirizzo"),
            "civico": obj.get("civico"),
            "comune_id": obj.get("comune_id"),
            "nazione_id": obj.get("nazione_id"),
            "citta_estera": obj.get("citta_estera")
        })
        return _obj


