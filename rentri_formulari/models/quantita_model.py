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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from rentri_formulari.models.unita_misura import UnitaMisura
from typing import Optional, Set
from typing_extensions import Self

class QuantitaModel(BaseModel):
    """
    QuantitaModel
    """ # noqa: E501
    valore: Union[StrictFloat, StrictInt] = Field(description="Quantità (parte intera: 10, parte decimale: 4) compresa tra 0.0000 e 9999999999.9999.")
    unita_misura: UnitaMisura = Field(description="Unità di misura della quantità  Vedi API di codifica: <i>GET /codifiche/v1.0/unita-misura</i><p>Valori ammessi:<ul style=\"margin:0\"><li><i>kg</i> - Chilogrammi</li><li><i>l</i> - Litri</li></ul></p>")
    __properties: ClassVar[List[str]] = ["valore", "unita_misura"]

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
        """Create an instance of QuantitaModel from a JSON string"""
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
        """Create an instance of QuantitaModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "valore": obj.get("valore"),
            "unita_misura": obj.get("unita_misura")
        })
        return _obj


