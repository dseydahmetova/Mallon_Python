# FR1: Modelling Stock Trades
from Trade import *
from sideTypes import Side

class Bond(Trade):
    def __init__(self, exchange, symbol, price, quantity, side, maturity, coupon):
        Trade.__init__(exchange, symbol, price, quantity, side)
        self.maturity = maturity
        self.coupon = coupon

    def calc_value(self):
        # For simplicity, assume the value of a bond is its price multiplied by quantity
        return self.price * self.quantity

    def __str__(self):
        return (f"Bond_ID: {self.trade_ID}, Exchange: {self.exchange}, Symbol: {self.symbol}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Side: {self.side}, "
                f"Maturity: {self.maturity}, Coupon: {self.coupon}")

    __repr__ = __str__