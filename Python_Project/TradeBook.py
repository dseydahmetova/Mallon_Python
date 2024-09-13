import decimal

from Stock import *
from TradeDividend import *
class Tradebook:
    def __init__(self):
        self.reference_list = []
        self.big_trades_list = []
        self.small_trades_list = []

    def get_reference_list(self):
        return self.reference_list

    def get_big_trades_list(self):
        return self.big_trades_list

    def get_small_trades_list(self):
        return self.small_trades_list

    def get_avg_values_from_list(self, trade_list):
        sum = 0
        for trade in trade_list:
            sum += trade.calc_value()
        length = len(trade_list)
        if length == 0:
            average = 0
        else:
            average = round(sum / length, 2)
        return average

    def add(self, new_trade):
        if len(self.reference_list) == 0:
            self.reference_list.append(new_trade)
        elif new_trade > self.reference_list[0]:
            self.big_trades_list.append(new_trade)
        elif new_trade < self.reference_list[0]:
            self.small_trades_list.append(new_trade)
        else:
            reference_list.add(new_trade)

    def print_reference_trades_statistics(self):
        length = len(self.reference_list)
        average = self.get_avg_values_from_list(self.reference_list)
        print(f"reference_list has {length} items and Average Value is: {average}")

    def print_small_trades_statistics(self):
        length = len(self.small_trades_list)
        average = self.get_avg_values_from_list(self.small_trades_list)
        print(f"small_trades has {length} items and Average Value is: {average}")

    def print_large_trades_statistics(self):
        length = len(self.big_trades_list)
        average = self.get_avg_values_from_list(self.big_trades_list)
        print(f"big_trades_list has {length} items and Average Value is: {average}")

    def calc_trade_return(self, trade, prev_price):
        trade_dividend = Trade_Dividend()
        dividend = trade_dividend.calc_trade_dividend(trade.get_quantity)
        return_on_stock = round((trade.get_price + decimal.Decimal(dividend))/ decimal.Decimal(prev_price) - 1, 2)
        return return_on_stock


    def __str__(self):
        return (f"TradeBook: \nreference_list = {self.reference_list}, \nbig_trades_list = {self.big_trades_list}, \nsmall_trades_list = {self.small_trades_list}")

    __repr__ = __str__