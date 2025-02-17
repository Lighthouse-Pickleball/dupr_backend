# coding: utf-8

"""
    DUPR Middleware

    Application REST APIs

    The version of the OpenAPI document: v1.0 alpha
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from dupr_backend.models.post_request import PostRequest

class TestPostRequest(unittest.TestCase):
    """PostRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PostRequest:
        """Test PostRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PostRequest`
        """
        model = PostRequest()
        if include_optional:
            return PostRequest(
                actor = 5333652862,
                checkin = dupr_backend.models.check_in_location.CheckInLocation(
                    address = dupr_backend.models.address_request.AddressRequest(
                        address_line = '402, B wing', 
                        geocode = dupr_backend.models.geocoding_result.GeocodingResult(
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
                                ], ), 
                        place_id = 'ChIJW37e6g4AwTsRfjFKn0_XRiU', ), 
                    id = 5333652862, 
                    type = 'RAW/CLUB/EVENT/NONE', ),
                content = 'Welcome to my Feed',
                feed = dupr_backend.models.feed.Feed(
                    feed_id = 1, 
                    slug = 'USER/CLUB/EVENT/DUPR', ),
                hashtags = [Welcome, Feeds],
                images = [/path/to/image],
                matches = [7578951408],
                tags = [5333652862],
                verb = 'POST'
            )
        else:
            return PostRequest(
        )
        """

    def testPostRequest(self):
        """Test PostRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
