# Part 1: Modelling Trades
import decimal
from abc import ABCMeta, abstractmethod
from sideTypes import Side
class Trade(metaclass=ABCMeta):
    count = 0
    @classmethod
    def incr(cls):
        cls.count += 1
        return cls.count
    def __init__(self, exchange, symbol, price, quantity, side):
        try:
            price_decimal = round(decimal.Decimal(price),2)
            quantity_int = int(quantity)
        except Exception:
            raise ValueError("Invalid type.")
        if price_decimal <= 0 or quantity_int <= 0:
            raise ValueError ("Value must be greater than zero")
        self.trade_ID = f"id{self.incr()}"
        self.exchange = exchange
        self.symbol = symbol
        self.price = price_decimal
        self.quantity = quantity_int
        self.side = side

    #getters
    @property
    def get_trade_ID(self):
        return self.trade_ID

    @property
    def get_symbol(self):
        return self.symbol

    @property
    def get_price(self):
        return self.price

    @property
    def get_quantity(self):
        return self.quantity

    @property
    def get_trade_ID(self):
        return self.trade_ID

    @property
    def get_exchange(self):
        return self.exchange

    @property
    def get_side(self):
        return self.side

    #setters
    @get_side.setter
    def set_price(self, newPrice):
        # if not (price >= 0) :
        #     raise ValueError("Value must be greater than zero")
        self.price = newPrice

    @get_quantity.setter
    def set_quantity(self, newValue):
        self.quantity = newValue

    @abstractmethod
    def calc_value(self):
        pass

    def __lt__(self, other):
        return self.calc_value() < other.calc_value()

    def __gt__(self, other):
        return self.calc_value() > other.calc_value()

    def __str__(self):
        return (f"Trade_ID: {self.trade_ID}, Excahnge: {self.exchange}, Symbol: {self.symbol}, "
                f"Price: {self.price}, Quantity: {self.quantity}, Side: {self.side}")
