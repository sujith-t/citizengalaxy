import unittest

from webapp.service.search import GalaxyLocatorServiceImpl


class GalaxyLocatorTestCase(unittest.TestCase):

    def test_instance(self):
        locator = GalaxyLocatorServiceImpl()
        self.assertTrue(isinstance(locator, GalaxyLocatorServiceImpl))  # add assertion here

    def test_paginated_results(self):
        locator = GalaxyLocatorServiceImpl()
        # checking whether the page size is 25
        default_page_size = 25
        no_of_pages, objects = locator.get_page_result(3)
        self.assertEqual(default_page_size, objects.count())

        # when page number goes beyond the total pages no objects will be returned
        no_of_pages, objects = locator.get_page_result(no_of_pages + 1)
        self.assertEqual(0, len(objects))

    def test_search_by_object_id(self):
        self.assertEqual(True, True)  # add assertion here

    def test_search_by_iauname(self):
        self.assertEqual(True, True)  # add assertion here

    def test_search_by_ra_dec(self):
        self.assertEqual(True, True)

    def test_get_details(self):
        self.assertEqual(True, True)
