from src.simple_library_01.functions import is_leap
import unittest


class Test(unittest.TestCase):

    def test_leap(self):
        assert is_leap(400)
        assert not (is_leap(200))
        assert is_leap(16)
        assert not (is_leap(1))
        self.assertRaises(AttributeError, is_leap, 0)

