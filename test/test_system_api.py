# coding: utf-8

"""
    FastAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from fugle_fastapi_client.api.system_api import SystemApi


class TestSystemApi(unittest.TestCase):
    """SystemApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemApi()

    def tearDown(self) -> None:
        pass

    def test_ping_api_v1_ping_get(self) -> None:
        """Test case for ping_api_v1_ping_get

        Ping
        """
        pass


if __name__ == '__main__':
    unittest.main()
