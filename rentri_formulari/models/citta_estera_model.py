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

from pydantic import BaseModel, ConfigDict, Field, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class CittaEsteraModel(BaseModel):
    """
    Città estera
    """ # noqa: E501
    nazione_id: Annotated[str, Field(min_length=1, strict=True, max_length=2)] = Field(description="Codice ISO 3166-1 alpha-2 della nazione, in caso di \"IT\" è possibile omettere.  Vengono accettati solo codici previsti dallo standard ISO 3166-1 alpha-2.  Vedi API di codifica: <i>GET /codifiche/v1.0/nazioni</i>")
    nome_citta: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(description="Città estera")
    __properties: ClassVar[List[str]] = []

    @field_validator('nazione_id')
    def nazione_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(?!.*(?i)it).*$", value):
            raise ValueError(r"must validate the regular expression /^(?!.*(?i)it).*$/")
        return value

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
        """Create an instance of CittaEsteraModel from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CittaEsteraModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
        })
        return _obj


