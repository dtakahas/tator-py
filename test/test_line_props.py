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
from tator.models.line_props import LineProps  # noqa: E501
from tator.rest import ApiException

class TestLineProps(unittest.TestCase):
    """LineProps unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test LineProps
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = tator.models.line_props.LineProps()  # noqa: E501
        if include_optional :
            return LineProps(
                x0 = 0.0, 
                x1 = 0.0, 
                y0 = 0.0, 
                y1 = 0.0
            )
        else :
            return LineProps(
                x0 = 0.0,
                x1 = 0.0,
                y0 = 0.0,
                y1 = 0.0,
        )

    def testLineProps(self):
        """Test LineProps"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == '__main__':
    unittest.main()
