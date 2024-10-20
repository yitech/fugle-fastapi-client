# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.k_lines import KLines

class TestKLines(unittest.TestCase):
    """KLines unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> KLines:
        """Test KLines
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `KLines`
        """
        model = KLines()
        if include_optional:
            return KLines(
                symbol = '',
                type = '',
                exchange = '',
                market = '',
                timeframe = '',
                data = [
                    openapi_client.models.k_line.KLine(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        open = 1.337, 
                        high = 1.337, 
                        low = 1.337, 
                        close = 1.337, 
                        volume = 56, )
                    ]
            )
        else:
            return KLines(
                symbol = '',
                type = '',
                exchange = '',
                market = '',
                timeframe = '',
                data = [
                    openapi_client.models.k_line.KLine(
                        date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(), 
                        open = 1.337, 
                        high = 1.337, 
                        low = 1.337, 
                        close = 1.337, 
                        volume = 56, )
                    ],
        )
        """

    def testKLines(self):
        """Test KLines"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
