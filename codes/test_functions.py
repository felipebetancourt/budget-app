import unittest
from input_dialog import *
from common_input import *
from menu_dialog import *


class TestFuntions(unittest.TestCase):

    def test_leap_year(self):

        self.assertFalse(leap_year(2018))
        self.assertTrue(leap_year(2020))


if __name__ == '__main__':
    unittest.main()
