# FR2: Using tests to undertake a TDD approach to developing trade classess

from Stock import *
from TradeBook import *
import unittest
from unittest.mock import patch, MagicMock, ANY, call

class TestTradeBook(unittest.TestCase):
    def setUp(self):
        self.tradeBook = Tradebook()
        self.stock1 = Stock("CHX", "FB", 100.00, 120, "sell")
        self.stock2 = Stock("NASDAQ", "AAPL", 150.50, 75, "buy")
        self.stock3 = Stock("CHX", "ORCL", 70.22, 160, "sell")
        self.stock4 = Stock("NYSE", "F", 50.34, 200, "buy")
        self.stock5 = Stock("NASDAQ", "AAPL", 155.99, 65, "buy")

        self.tradeBook.add(self.stock1)
        self.tradeBook.add(self.stock2)
        self.tradeBook.add(self.stock3)
        self.tradeBook.add(self.stock4)
        self.tradeBook.add(self.stock5)

        self.reference_list = self.tradeBook.get_reference_list()
        self.big_trades_list = self.tradeBook.get_big_trades_list()
        self.small_trades_list = self.tradeBook.get_small_trades_list()

    def test_add_stock_to_tardebook(self):
        total_length = len(self.reference_list) + len(self.big_trades_list) + len(self.small_trades_list)
        self.assertEqual(self.reference_list[0], self.stock1,'stock was added successfully')
        self.assertEqual(total_length, 5, 'Tradebook has 5 items in total' )

    def test_get_avg_values_from_list(self):
        self.assertEqual(self.tradeBook.get_avg_values_from_list(self.reference_list), 12000, 'reference_list avg value: 1200')

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        # self.stock1 = Stock("CHX", "FB", 100.00, 120, "sell")
        # return_on_stock = (trade.get_price + dividend )/ prev_price - 1
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        self.assertEqual( float(return_on_stock), 0.74, "(100 + 69)/97 - = 1.74 - 1 = 0.74")

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return_call_with(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        # mock object was called but also that it was called exactly once
        # and with specific arguments
        mock_calc_trade_dividend.assert_called_once_with(self.stock1.get_quantity)

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return_has_calls(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        return_on_stock = self.tradeBook.calc_trade_return(self.stock2, 90)
        # for asserting the order in which methods were called on a mock object.
        mock_calc_trade_dividend.assert_has_calls([call.calc_trade_dividend(self.stock1.get_quantity), call.calc_trade_dividend(self.stock2.get_quantity)])

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return_call_multiple_times(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 90)
        # if you don’t care how many times a specific method is called,
        # but you want to ensure that every time the method is called,
        # it is called with some fixed arguments.
        mock_calc_trade_dividend.assert_called_with(self.stock1.get_quantity)

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return_called(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        # Use assert_called to check if the method was called
        # No matter how many times it’s called, it should have been atleast called once.
        mock_calc_trade_dividend.assert_called()
        # you might just want to call a specific function on a mock object only once.
        mock_calc_trade_dividend.assert_called_once()

    @patch('TradeDividend.Trade_Dividend.calc_trade_dividend')
    def test_calc_trade_return_assert_any_call(self, mock_calc_trade_dividend):
        mock_calc_trade_dividend.return_value = 69.00
        return_on_stock = self.tradeBook.calc_trade_return(self.stock1, 97)
        return_on_stock = self.tradeBook.calc_trade_return(self.stock2, 40)
        return_on_stock = self.tradeBook.calc_trade_return(self.stock3, 55)
        # Use it to verify that a specific method on a mock object has been called
        # at least once during a test with the correct arguments.
        mock_calc_trade_dividend.assert_any_call(self.stock1.get_quantity) # This will pass
        # mock_calc_trade_dividend.assert_any_call(self.stock5.get_quantity) # This will fail

if __name__ == '__main__':
    unittest.main()