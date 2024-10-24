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

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from fugle_fastapi_client.models.bid_ask import BidAsk
from fugle_fastapi_client.models.last_trade import LastTrade
from fugle_fastapi_client.models.last_trial import LastTrial
from fugle_fastapi_client.models.total import Total
from typing import Optional, Set
from typing_extensions import Self

class QuoteResponse(BaseModel):
    """
    QuoteResponse
    """ # noqa: E501
    var_date: date = Field(alias="date")
    type: StrictStr
    exchange: StrictStr
    market: StrictStr
    symbol: StrictStr
    name: StrictStr
    reference_price: Union[StrictFloat, StrictInt] = Field(alias="referencePrice")
    previous_close: Union[StrictFloat, StrictInt] = Field(alias="previousClose")
    open_price: Union[StrictFloat, StrictInt] = Field(alias="openPrice")
    open_time: StrictInt = Field(alias="openTime")
    high_price: Union[StrictFloat, StrictInt] = Field(alias="highPrice")
    high_time: StrictInt = Field(alias="highTime")
    low_price: Union[StrictFloat, StrictInt] = Field(alias="lowPrice")
    low_time: StrictInt = Field(alias="lowTime")
    close_price: Union[StrictFloat, StrictInt] = Field(alias="closePrice")
    close_time: StrictInt = Field(alias="closeTime")
    avg_price: Union[StrictFloat, StrictInt] = Field(alias="avgPrice")
    change: Union[StrictFloat, StrictInt]
    change_percent: Union[StrictFloat, StrictInt] = Field(alias="changePercent")
    amplitude: Union[StrictFloat, StrictInt]
    last_price: Union[StrictFloat, StrictInt] = Field(alias="lastPrice")
    last_size: StrictInt = Field(alias="lastSize")
    bids: List[BidAsk]
    asks: List[BidAsk]
    total: Total
    last_trade: LastTrade = Field(alias="lastTrade")
    last_trial: LastTrial = Field(alias="lastTrial")
    is_trial: Optional[StrictBool] = Field(default=None, alias="isTrial")
    is_delayed_open: Optional[StrictBool] = Field(default=None, alias="isDelayedOpen")
    is_delayed_close: Optional[StrictBool] = Field(default=None, alias="isDelayedClose")
    is_open: Optional[StrictBool] = Field(default=None, alias="isOpen")
    is_close: Optional[StrictBool] = Field(default=None, alias="isClose")
    last_updated: StrictInt = Field(alias="lastUpdated")
    serial: StrictInt
    __properties: ClassVar[List[str]] = ["date", "type", "exchange", "market", "symbol", "name", "referencePrice", "previousClose", "openPrice", "openTime", "highPrice", "highTime", "lowPrice", "lowTime", "closePrice", "closeTime", "avgPrice", "change", "changePercent", "amplitude", "lastPrice", "lastSize", "bids", "asks", "total", "lastTrade", "lastTrial", "isTrial", "isDelayedOpen", "isDelayedClose", "isOpen", "isClose", "lastUpdated", "serial"]

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
        """Create an instance of QuoteResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in bids (list)
        _items = []
        if self.bids:
            for _item_bids in self.bids:
                if _item_bids:
                    _items.append(_item_bids.to_dict())
            _dict['bids'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in asks (list)
        _items = []
        if self.asks:
            for _item_asks in self.asks:
                if _item_asks:
                    _items.append(_item_asks.to_dict())
            _dict['asks'] = _items
        # override the default output from pydantic by calling `to_dict()` of total
        if self.total:
            _dict['total'] = self.total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_trade
        if self.last_trade:
            _dict['lastTrade'] = self.last_trade.to_dict()
        # override the default output from pydantic by calling `to_dict()` of last_trial
        if self.last_trial:
            _dict['lastTrial'] = self.last_trial.to_dict()
        # set to None if is_trial (nullable) is None
        # and model_fields_set contains the field
        if self.is_trial is None and "is_trial" in self.model_fields_set:
            _dict['isTrial'] = None

        # set to None if is_delayed_open (nullable) is None
        # and model_fields_set contains the field
        if self.is_delayed_open is None and "is_delayed_open" in self.model_fields_set:
            _dict['isDelayedOpen'] = None

        # set to None if is_delayed_close (nullable) is None
        # and model_fields_set contains the field
        if self.is_delayed_close is None and "is_delayed_close" in self.model_fields_set:
            _dict['isDelayedClose'] = None

        # set to None if is_open (nullable) is None
        # and model_fields_set contains the field
        if self.is_open is None and "is_open" in self.model_fields_set:
            _dict['isOpen'] = None

        # set to None if is_close (nullable) is None
        # and model_fields_set contains the field
        if self.is_close is None and "is_close" in self.model_fields_set:
            _dict['isClose'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of QuoteResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "date": obj.get("date"),
            "type": obj.get("type"),
            "exchange": obj.get("exchange"),
            "market": obj.get("market"),
            "symbol": obj.get("symbol"),
            "name": obj.get("name"),
            "referencePrice": obj.get("referencePrice"),
            "previousClose": obj.get("previousClose"),
            "openPrice": obj.get("openPrice"),
            "openTime": obj.get("openTime"),
            "highPrice": obj.get("highPrice"),
            "highTime": obj.get("highTime"),
            "lowPrice": obj.get("lowPrice"),
            "lowTime": obj.get("lowTime"),
            "closePrice": obj.get("closePrice"),
            "closeTime": obj.get("closeTime"),
            "avgPrice": obj.get("avgPrice"),
            "change": obj.get("change"),
            "changePercent": obj.get("changePercent"),
            "amplitude": obj.get("amplitude"),
            "lastPrice": obj.get("lastPrice"),
            "lastSize": obj.get("lastSize"),
            "bids": [BidAsk.from_dict(_item) for _item in obj["bids"]] if obj.get("bids") is not None else None,
            "asks": [BidAsk.from_dict(_item) for _item in obj["asks"]] if obj.get("asks") is not None else None,
            "total": Total.from_dict(obj["total"]) if obj.get("total") is not None else None,
            "lastTrade": LastTrade.from_dict(obj["lastTrade"]) if obj.get("lastTrade") is not None else None,
            "lastTrial": LastTrial.from_dict(obj["lastTrial"]) if obj.get("lastTrial") is not None else None,
            "isTrial": obj.get("isTrial"),
            "isDelayedOpen": obj.get("isDelayedOpen"),
            "isDelayedClose": obj.get("isDelayedClose"),
            "isOpen": obj.get("isOpen"),
            "isClose": obj.get("isClose"),
            "lastUpdated": obj.get("lastUpdated"),
            "serial": obj.get("serial")
        })
        return _obj


