import decimal

class Trade_Dividend:
    def calc_trade_dividend(self, num_share):
        div_per_share = 0.68
        return decimal.Decimal(num_share * div_per_share)
