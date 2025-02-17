# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.array_wrapper_of_geocoding_result import ArrayWrapperOfGeocodingResult

class TestArrayWrapperOfGeocodingResult(unittest.TestCase):
    """ArrayWrapperOfGeocodingResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ArrayWrapperOfGeocodingResult:
        """Test ArrayWrapperOfGeocodingResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ArrayWrapperOfGeocodingResult`
        """
        model = ArrayWrapperOfGeocodingResult()
        if include_optional:
            return ArrayWrapperOfGeocodingResult(
                message = 'Show this message to user.',
                results = [
                    dupr_backend.models.geocoding_result.GeocodingResult(
                        address_components = [
                            dupr_backend.models.address_component.AddressComponent(
                                long_name = '', 
                                short_name = '', 
                                types = [
                                    'ADMINISTRATIVE_AREA_LEVEL_1'
                                    ], )
                            ], 
                        formatted_address = '', 
                        geometry = dupr_backend.models.geometry.Geometry(
                            bounds = dupr_backend.models.bounds.Bounds(
                                northeast = dupr_backend.models.lat_lng.LatLng(
                                    lat = 1.337, 
                                    lng = 1.337, ), 
                                southwest = dupr_backend.models.lat_lng.LatLng(
                                    lat = 1.337, 
                                    lng = 1.337, ), ), 
                            location = , 
                            location_type = 'APPROXIMATE', 
                            viewport = dupr_backend.models.bounds.Bounds(), ), 
                        partial_match = True, 
                        place_id = '', 
                        plus_code = dupr_backend.models.plus_code.PlusCode(
                            compound_code = '', 
                            global_code = '', ), 
                        postcode_localities = [
                            ''
                            ], 
                        types = [
                            'ACCOUNTING'
                            ], )
                    ],
                status = 'FAILURE'
            )
        else:
            return ArrayWrapperOfGeocodingResult(
        )
        """

    def testArrayWrapperOfGeocodingResult(self):
        """Test ArrayWrapperOfGeocodingResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
