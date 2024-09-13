# FR2: Using tests to undertake a TDD approach to developing trade classess

from Stock import *
import unittest

class TestTrades(unittest.TestCase):
    def setUp(self):
        #              trade_ID, exchange, symbol, price, quantity, side):
        self.stock = Stock("CHX", "FB", 100.00, 120, "sell")
        self.stock2 = Stock("NYSE", "AAPL", 150.73, 80, "buy")


    def test_create_a_stock(self):
        self.assertEqual(self.stock.get_symbol, "FB", 'stock was created successfully')
        self.assertEqual(self.stock.get_price, 100.00, 'stock\t''s price is $ 12.0' )
        self.assertEqual(self.stock.get_trade_ID, "id3", 'stock ID is "id1"')
        self.assertEqual(self.stock.get_exchange, "CHX", 'stock\t''s exchange is CHX')
        self.assertEqual(self.stock.get_quantity, 120, 'stock\ts quantity is 120')
        self.assertEqual(self.stock.get_side, "sell", 'stock\t''s side is "SELL"')

    def test_set_value(self):
        self.stock.price = 21.25
        self.assertEqual(self.stock.get_price, 21.25, 'stock new price is $21.25')
        self.stock.set_quantity = 210
        self.assertEqual(self.stock.get_quantity, 210, 'stock new quantity is $210')

    def test_calc_stock_value(self):
        self.assertEqual(self.stock.calc_value(), 12000.00, 'stock value is 12000.00')

    def test_create_a_stock_with_wrong_price_value(self):
        with self.assertRaises(ValueError, msg = "Value must be greater than zero"):
            self.stock1 = Stock("CHX", "FB", -100.0, 120, "sell")
        with self.assertRaises(ValueError, msg="Value must be greater than zero"):
            self.stock1 = Stock("CHX", "FB", 0, 120, "sell")

    def test_create_a_stock_with_wrong_quantity_value(self):
        with self.assertRaises(ValueError, msg="Value must be greater than zero"):
            self.stock1 = Stock("CHX", "FB", 100.0, -120, "sell")
        with self.assertRaises(ValueError, msg="Value must be greater than zero"):
            self.stock1 = Stock("CHX", "FB", 100, 0, "sell")

    def test_create_a_stock_with_wrong_price_type(self):
        with self.assertRaises(ValueError, msg = "Value must be decimal"):
            self.stock1 = Stock("CHX", "FB", "Random String", 120, "sell")

    def test_create_a_stock_with_wrong_quantity_type(self):
        with self.assertRaises(ValueError, msg="Value must be decimal"):
            self.stock1 = Stock("CHX", "FB", 120, "Random String", "sell")

    def test_greater_than_func(self):
        self.assertFalse(self.stock > self.stock2, "Stock's value is NOT greater than stock2")
        self.assertTrue(self.stock2 > self.stock, "Stock2's value is greater than stock")

    def test_less_than_func(self):
        self.assertFalse(self.stock2 < self.stock, "Stock2's value is NOT less than stock")
        self.assertTrue(self.stock < self.stock2, "Stock's value is less than stock2")


if __name__ == '__main__':
    unittest.main()