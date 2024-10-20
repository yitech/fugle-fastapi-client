# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.inventory_detail import InventoryDetail
from typing import Optional, Set
from typing_extensions import Self

class InventoryResponse(BaseModel):
    """
    InventoryResponse
    """ # noqa: E501
    ap_code: Optional[StrictStr] = None
    cost_qty: Union[StrictFloat, StrictInt]
    cost_sum: Union[StrictFloat, StrictInt]
    make_a_per: Union[StrictFloat, StrictInt]
    make_a_sum: Union[StrictFloat, StrictInt]
    price_avg: Union[StrictFloat, StrictInt]
    price_evn: Union[StrictFloat, StrictInt]
    price_mkt: Union[StrictFloat, StrictInt]
    price_now: Union[StrictFloat, StrictInt]
    price_qty_sum: Union[StrictFloat, StrictInt]
    qty_b: StrictInt
    qty_bm: StrictInt
    qty_c: StrictInt
    qty_l: StrictInt
    qty_s: StrictInt
    qty_sm: StrictInt
    rec_va_sum: Union[StrictFloat, StrictInt]
    s_type: StrictStr
    stk_dats: List[InventoryDetail]
    stk_na: StrictStr
    stk_no: StrictStr
    trade: Optional[StrictInt] = None
    value_mkt: Union[StrictFloat, StrictInt]
    value_now: Union[StrictFloat, StrictInt]
    __properties: ClassVar[List[str]] = ["ap_code", "cost_qty", "cost_sum", "make_a_per", "make_a_sum", "price_avg", "price_evn", "price_mkt", "price_now", "price_qty_sum", "qty_b", "qty_bm", "qty_c", "qty_l", "qty_s", "qty_sm", "rec_va_sum", "s_type", "stk_dats", "stk_na", "stk_no", "trade", "value_mkt", "value_now"]

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
        """Create an instance of InventoryResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in stk_dats (list)
        _items = []
        if self.stk_dats:
            for _item_stk_dats in self.stk_dats:
                if _item_stk_dats:
                    _items.append(_item_stk_dats.to_dict())
            _dict['stk_dats'] = _items
        # set to None if ap_code (nullable) is None
        # and model_fields_set contains the field
        if self.ap_code is None and "ap_code" in self.model_fields_set:
            _dict['ap_code'] = None

        # set to None if trade (nullable) is None
        # and model_fields_set contains the field
        if self.trade is None and "trade" in self.model_fields_set:
            _dict['trade'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InventoryResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ap_code": obj.get("ap_code"),
            "cost_qty": obj.get("cost_qty"),
            "cost_sum": obj.get("cost_sum"),
            "make_a_per": obj.get("make_a_per"),
            "make_a_sum": obj.get("make_a_sum"),
            "price_avg": obj.get("price_avg"),
            "price_evn": obj.get("price_evn"),
            "price_mkt": obj.get("price_mkt"),
            "price_now": obj.get("price_now"),
            "price_qty_sum": obj.get("price_qty_sum"),
            "qty_b": obj.get("qty_b"),
            "qty_bm": obj.get("qty_bm"),
            "qty_c": obj.get("qty_c"),
            "qty_l": obj.get("qty_l"),
            "qty_s": obj.get("qty_s"),
            "qty_sm": obj.get("qty_sm"),
            "rec_va_sum": obj.get("rec_va_sum"),
            "s_type": obj.get("s_type"),
            "stk_dats": [InventoryDetail.from_dict(_item) for _item in obj["stk_dats"]] if obj.get("stk_dats") is not None else None,
            "stk_na": obj.get("stk_na"),
            "stk_no": obj.get("stk_no"),
            "trade": obj.get("trade"),
            "value_mkt": obj.get("value_mkt"),
            "value_now": obj.get("value_now")
        })
        return _obj

