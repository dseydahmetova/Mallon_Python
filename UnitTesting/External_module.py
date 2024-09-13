from my_mock import *
def calc_total_price(amount):
    price = get_price("GBP/USD")
    return price * amount


def calc_return_tuple(*args):
    return return_tuple(args)
