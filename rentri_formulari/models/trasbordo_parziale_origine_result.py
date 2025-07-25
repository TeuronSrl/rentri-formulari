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
from rentri_formulari.models.soggetto_item_result import SoggettoItemResult
from typing import Optional, Set
from typing_extensions import Self

class TrasbordoParzialeOrigineResult(BaseModel):
    """
    TrasbordoParzialeOrigineResult
    """ # noqa: E501
    numero_fir_origine: Optional[StrictStr] = None
    produttore_origine: Optional[SoggettoItemResult] = None
    __properties: ClassVar[List[str]] = ["numero_fir_origine", "produttore_origine"]

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
        """Create an instance of TrasbordoParzialeOrigineResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of produttore_origine
        if self.produttore_origine:
            _dict['produttore_origine'] = self.produttore_origine.to_dict()
        # set to None if numero_fir_origine (nullable) is None
        # and model_fields_set contains the field
        if self.numero_fir_origine is None and "numero_fir_origine" in self.model_fields_set:
            _dict['numero_fir_origine'] = None

        # set to None if produttore_origine (nullable) is None
        # and model_fields_set contains the field
        if self.produttore_origine is None and "produttore_origine" in self.model_fields_set:
            _dict['produttore_origine'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TrasbordoParzialeOrigineResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "numero_fir_origine": obj.get("numero_fir_origine"),
            "produttore_origine": SoggettoItemResult.from_dict(obj["produttore_origine"]) if obj.get("produttore_origine") is not None else None
        })
        return _obj


