from src.simple_library_01.functions import get_month_days
import unittest


class Test(unittest.TestCase):

    def test_get_month_days(self):
        self.assertRaises(AttributeError, get_month_days, 1999, -1)
        assert 30 == get_month_days(1930, 8)
        assert 29 == get_month_days(2012, 2)
        assert 28 == get_month_days(2011, 2)
        assert 30 == get_month_days(2001, 4)
        assert 31 == get_month_days(2001, 1)
