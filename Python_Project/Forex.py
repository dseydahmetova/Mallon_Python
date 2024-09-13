# FR1: Modelling Stock Trades
from Trade import *
from sideTypes import Side

class Forex(Trade):
    def __init__(self, exchange, symbol, price, quantity, side, base_currency, quote_currency):
        Trade.__init__(exchange, symbol, price, quantity, side)
        self.base_currency = base_currency
        self.quote_currency = quote_currency

    def calc_value(self):
        # Forex value is typically price * quantity (assumed to be in base currency units)
        return self.price * self.quantity

    def __str__(self):
        return (f"Forex_ID: {self.trade_ID}, Exchange: {self.exchange}, Symbol: {self.symbol}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Side: {self.side}, "
                f"Base Currency: {self.base_currency}, Quote Currency: {self.quote_currency}")

    __repr__ = __str__