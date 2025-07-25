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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class NormativaADRModel(BaseModel):
    """
    Normativa ADR
    """ # noqa: E501
    numero_onu: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="Numero ONU")
    classe: Optional[Annotated[str, Field(strict=True, max_length=20)]] = None
    note: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, description="Note ADR")
    __properties: ClassVar[List[str]] = ["numero_onu", "classe", "note"]

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
        """Create an instance of NormativaADRModel from a JSON string"""
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
        # set to None if numero_onu (nullable) is None
        # and model_fields_set contains the field
        if self.numero_onu is None and "numero_onu" in self.model_fields_set:
            _dict['numero_onu'] = None

        # set to None if classe (nullable) is None
        # and model_fields_set contains the field
        if self.classe is None and "classe" in self.model_fields_set:
            _dict['classe'] = None

        # set to None if note (nullable) is None
        # and model_fields_set contains the field
        if self.note is None and "note" in self.model_fields_set:
            _dict['note'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of NormativaADRModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numero_onu": obj.get("numero_onu"),
            "classe": obj.get("classe"),
            "note": obj.get("note")
        })
        return _obj


