# FR3: Implementing classesfrom Trade import *

from sideTypes import Side
import itertools
from Trade import *

class Stock(Trade):
    def __init__(self, exchange, symbol, price, quantity, side):
        Trade.__init__(self, exchange, symbol, price, quantity, side)

    def calc_value(self):
        value = self.price * self.quantity
        return value

    def __str__(self):
        return (f"Stock_ID: {self.trade_ID}, Excahnge: {self.exchange}, Symbol: {self.symbol}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Side: {self.side}, Value: {self.calc_value()}")

    __repr__ =__str__
