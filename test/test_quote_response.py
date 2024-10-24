# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fugle_fastapi_client.models.quote_response import QuoteResponse

class TestQuoteResponse(unittest.TestCase):
    """QuoteResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> QuoteResponse:
        """Test QuoteResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `QuoteResponse`
        """
        model = QuoteResponse()
        if include_optional:
            return QuoteResponse(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                type = '',
                exchange = '',
                market = '',
                symbol = '',
                name = '',
                reference_price = 1.337,
                previous_close = 1.337,
                open_price = 1.337,
                open_time = 56,
                high_price = 1.337,
                high_time = 56,
                low_price = 1.337,
                low_time = 56,
                close_price = 1.337,
                close_time = 56,
                avg_price = 1.337,
                change = 1.337,
                change_percent = 1.337,
                amplitude = 1.337,
                last_price = 1.337,
                last_size = 56,
                bids = [
                    fugle_fastapi_client.models.bid_ask.BidAsk(
                        price = 1.337, 
                        size = 56, )
                    ],
                asks = [
                    fugle_fastapi_client.models.bid_ask.BidAsk(
                        price = 1.337, 
                        size = 56, )
                    ],
                total = fugle_fastapi_client.models.total.Total(
                    trade_value = 56, 
                    trade_volume = 56, 
                    trade_volume_at_bid = 56, 
                    trade_volume_at_ask = 56, 
                    transaction = 56, 
                    time = 56, ),
                last_trade = fugle_fastapi_client.models.last_trade.LastTrade(
                    bid = 1.337, 
                    ask = 1.337, 
                    price = 1.337, 
                    size = 56, 
                    time = 56, 
                    serial = 56, ),
                last_trial = fugle_fastapi_client.models.last_trial.LastTrial(
                    bid = 1.337, 
                    ask = 1.337, 
                    price = 1.337, 
                    size = 56, 
                    time = 56, 
                    serial = 56, ),
                is_trial = True,
                is_delayed_open = True,
                is_delayed_close = True,
                is_open = True,
                is_close = True,
                last_updated = 56,
                serial = 56
            )
        else:
            return QuoteResponse(
                var_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                type = '',
                exchange = '',
                market = '',
                symbol = '',
                name = '',
                reference_price = 1.337,
                previous_close = 1.337,
                open_price = 1.337,
                open_time = 56,
                high_price = 1.337,
                high_time = 56,
                low_price = 1.337,
                low_time = 56,
                close_price = 1.337,
                close_time = 56,
                avg_price = 1.337,
                change = 1.337,
                change_percent = 1.337,
                amplitude = 1.337,
                last_price = 1.337,
                last_size = 56,
                bids = [
                    fugle_fastapi_client.models.bid_ask.BidAsk(
                        price = 1.337, 
                        size = 56, )
                    ],
                asks = [
                    fugle_fastapi_client.models.bid_ask.BidAsk(
                        price = 1.337, 
                        size = 56, )
                    ],
                total = fugle_fastapi_client.models.total.Total(
                    trade_value = 56, 
                    trade_volume = 56, 
                    trade_volume_at_bid = 56, 
                    trade_volume_at_ask = 56, 
                    transaction = 56, 
                    time = 56, ),
                last_trade = fugle_fastapi_client.models.last_trade.LastTrade(
                    bid = 1.337, 
                    ask = 1.337, 
                    price = 1.337, 
                    size = 56, 
                    time = 56, 
                    serial = 56, ),
                last_trial = fugle_fastapi_client.models.last_trial.LastTrial(
                    bid = 1.337, 
                    ask = 1.337, 
                    price = 1.337, 
                    size = 56, 
                    time = 56, 
                    serial = 56, ),
                last_updated = 56,
                serial = 56,
        )
        """

    def testQuoteResponse(self):
        """Test QuoteResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
