from unittest import TestCase
from unittest.mock import patch, MagicMock
import unittest
from External_module import *

class Test_mock_get_price(TestCase):
    @patch('External_module.get_price')
    def test_calc_total_price(self, mock_get_price):
        # Using Mock to set the return value of get_price
        mock_get_price.return_value = 1.29
        # Test calc_total_price function
        total = calc_total_price(1000)
        self.assertEqual(total, 1000 * 1.29)
        mock_get_price.assert_called_once_with("GBP/USD")

    @patch('External_module.return_tuple')
    def test_calc_return_tuple(self, mock_return_tuple):
        # using MagicMock doesn't work
        mock_return_tuple.return_value = {(1, 2): 1, (2, 3): 2}
        myList = calc_return_tuple()
        self.assertEqual(myList, {(1, 2): 1, (2, 3): 2})


if __name__ == '__main__':
    unittest.main()