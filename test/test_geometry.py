# coding: utf-8

"""
    DUPR Backend APIs

    Internal RESTful APIs to access DUPR ratings, users and provide matches.

    The version of the OpenAPI document: v1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.geometry import Geometry

class TestGeometry(unittest.TestCase):
    """Geometry unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Geometry:
        """Test Geometry
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Geometry`
        """
        model = Geometry()
        if include_optional:
            return Geometry(
                bounds = dupr_backend.models.bounds.Bounds(
                    northeast = dupr_backend.models.lat_lng.LatLng(
                        lat = 1.337, 
                        lng = 1.337, ), 
                    southwest = dupr_backend.models.lat_lng.LatLng(
                        lat = 1.337, 
                        lng = 1.337, ), ),
                location = dupr_backend.models.lat_lng.LatLng(
                    lat = 1.337, 
                    lng = 1.337, ),
                location_type = 'ROOFTOP',
                viewport = dupr_backend.models.bounds.Bounds(
                    northeast = dupr_backend.models.lat_lng.LatLng(
                        lat = 1.337, 
                        lng = 1.337, ), 
                    southwest = dupr_backend.models.lat_lng.LatLng(
                        lat = 1.337, 
                        lng = 1.337, ), )
            )
        else:
            return Geometry(
        )
        """

    def testGeometry(self):
        """Test Geometry"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
