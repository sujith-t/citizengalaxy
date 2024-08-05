import unittest

from webapp.model.dto import GalaxyDetail
from webapp.service.search import GalaxyLocatorServiceImpl


# @author Sujith T
# Deus et Scientia Erit Pactum Meum 2024
class GalaxyLocatorTestCase(unittest.TestCase):

    # test the instance
    def test_instance(self):
        locator = GalaxyLocatorServiceImpl()
        self.assertTrue(isinstance(locator, GalaxyLocatorServiceImpl))  # add assertion here

    # test the paginated results
    def test_paginated_results(self):
        locator = GalaxyLocatorServiceImpl()
        # checking whether the page size is 25
        default_page_size = 25
        no_of_pages, objects = locator.get_page_result(3)
        self.assertEqual(default_page_size, objects.count())

        # when page number goes beyond the total pages no objects will be returned
        no_of_pages, objects = locator.get_page_result(no_of_pages + 1)
        self.assertEqual(0, len(objects))

    # test whether search by object id works
    def test_search_by_object_id(self):
        locator = GalaxyLocatorServiceImpl()

        param = {'search_option': "obj_id", 'search_value': "587722981742018657"}
        result = locator.search(param)
        self.assertEqual(1, len(result))  # check whether a single record is returned

        param["search_value"] = "001"
        result = locator.search(param)
        self.assertEqual(0, len(result))  # check whether a single record is returned

    # test search by iauname
    def test_search_by_iauname(self):
        locator = GalaxyLocatorServiceImpl()

        param = {'search_option': "iauname", 'search_value': "J121808.55-010350.8"}
        result = locator.search(param)
        self.assertEqual(1, len(result))  # check whether a single record is returned

        param["search_value"] = "J0001"
        result = locator.search(param)
        self.assertEqual(0, len(result))  # check whether a single record is returned

    # search by RA and DEC parameters
    def test_search_by_ra_dec(self):
        locator = GalaxyLocatorServiceImpl()

        param = {'search_option': "ra_dec", 'ra': 184.53, 'dec': -1.0641}
        result = locator.search(param)
        self.assertTrue(len(result) > 0)

    # search by RA and DEC parameters
    def test_search_by_ra_dec_no_output(self):
        locator = GalaxyLocatorServiceImpl()

        param = {'search_option': "ra_dec", 'ra': 270, 'dec': 3.664}
        result = locator.search(param)
        self.assertEquals(0, len(result))

    # find complete galaxy details by id
    def test_get_details_by_id(self):
        locator = GalaxyLocatorServiceImpl()
        search_param = {"search_value": "587722981742018657", "search_option": "obj_id"}
        galaxy = locator.get_details(search_param)
        self.assertTrue(isinstance(galaxy, GalaxyDetail))

        search_param["search_value"] = "58x"
        galaxy = locator.get_details(search_param)
        self.assertEquals(galaxy, None)
