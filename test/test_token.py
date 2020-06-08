# coding: utf-8

"""
    Tator REST API

    Interface to the Tator backend.  # noqa: E501

    The version of the OpenAPI document: v1
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import tator
from tator.models.token import Token  # noqa: E501
from tator.rest import ApiException

class TestToken(unittest.TestCase):
    """Token unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test Token
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.token.Token()  # noqa: E501
        if include_optional :
            return Token(
                token = '0'
            )
        else :
            return Token(
        )

    def testToken(self):
        """Test Token"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
