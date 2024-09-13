# FR1: Modelling Stock Trades
from Trade import *
from sideTypes import Side

class Future(Trade):
    def __init__(self, exchange, symbol, price, quantity, side, contract_size):
        Trade.__init__(exchange, symbol, price, quantity, side)
        self.contract_size = contract_size

    def calc_value(self):
        # Futures value is typically price * quantity * contract_size
        return self.price * self.quantity * self.contract_size

    def __str__(self):
        return (f"Futures_ID: {self.trade_ID}, Exchange: {self.exchange}, Symbol: {self.symbol}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Side: {self.side}, "
                f"Contract Size: {self.contract_size}")

    __repr__ = __str__
