# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.settlement_response import SettlementResponse

class TestSettlementResponse(unittest.TestCase):
    """SettlementResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SettlementResponse:
        """Test SettlementResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SettlementResponse`
        """
        model = SettlementResponse()
        if include_optional:
            return SettlementResponse(
                c_date = '',
                var_date = '',
                price = ''
            )
        else:
            return SettlementResponse(
                c_date = '',
                var_date = '',
                price = '',
        )
        """

    def testSettlementResponse(self):
        """Test SettlementResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
