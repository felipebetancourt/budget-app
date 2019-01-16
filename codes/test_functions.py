from unittest.mock import patch
import unittest

from input_dialog import *
from common_input import *
from menu_dialog import *

from time import gmtime, strftime


class TestFuntions(unittest.TestCase):

    def test_leap_year(self):

        self.assertFalse(leap_year(2018))
        self.assertTrue(leap_year(2020))

    def test_check_date(self):

        self.assertTrue(check_date('01/01/2019'))
        self.assertFalse(check_date('02/02/19'))
        self.assertFalse(check_date('01/01/2017'))
        self.assertTrue(check_date('29/02/2020'))
        self.assertFalse(check_date('30/02/2020'))
        self.assertFalse(check_date('30/02/2019'))
        self.assertFalse(check_date('31/04/2019'))
        self.assertTrue(check_date('31/01/2019'))

    def test_check_quantity(self):

        self.assertEqual(check_quantity(12.6589), 12.66)

    def test_transaction_type(self):

        with patch('builtins.input', side_effect='1'):
            self.assertEqual(transaction_type(), 'CASH_OUT')

        with patch('builtins.input', side_effect='2'):
            self.assertEqual(transaction_type(), 'CASH_IN')

        with patch('builtins.input', side_effect='3'):
            self.assertEqual(transaction_type(), 'SAVING')

    def test_generate_id(self):

        year = strftime("%y", gmtime())
        month = strftime("%m", gmtime())

        self.assertEqual(generate_id(year + month + '03'), year + month + '04')
        self.assertEqual(generate_id(year + month + '99'), year + month + '00')


if __name__ == '__main__':
    unittest.main()
