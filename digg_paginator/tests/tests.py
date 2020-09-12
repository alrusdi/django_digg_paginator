import unittest

from django.core.paginator import InvalidPage

from paginators import ExPaginator


class DiggPaginatorTests(unittest.TestCase):

    def test_supports_softlimit(self):
        items = range(1, 1000)
        paginator = ExPaginator(items, 10)
        page = paginator.page(1000, softlimit=True)

        self.assertEqual(str(page), "<Page 100 of 100>")

    def test_graceful_handles_non_int_page(self):
        items = range(1, 1000)
        paginator = ExPaginator(items, 10)

        try:
            page = paginator.page("str")
            self.assertEqual(False, "Must raise an exception")
        except InvalidPage:
            return True

        self.assertEqual(False, "Wrong exception raised")

