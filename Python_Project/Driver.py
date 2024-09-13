import decimal
import os
from Stock import *
from TradeBook import *
import random
import csv


def main():
    stockList = []
    # Call the Tradebook constructor
    tradebook = Tradebook()

    # ---------------------FR4: Writing a driver program-----------------
    # stock1 = Stock("CHX", "FB", 100.00, 120, "sell")
    # print(stock1)
    # stock2 = Stock( "NASDAQ", "AAPL", 150.50, 75, "buy")
    # print(stock2)
    # stock3 = Stock("CHX", "ORCL", 70.22, 160, "sell")
    # print(stock3)
    # stock4 = Stock("NYSE", "F", 50.34, 200, "buy")
    # print(stock4)
    # stock5 = Stock("NASDAQ", "AAPL", 155.99, 65, "buy")
    # print(stock5)
    # stock6 = Stock("NASDAQ", "F", 55.12, 200, "buy")
    # print(stock6)
    # stock7 = Stock("NYSE", "FB", 100.34, 120, "sell")
    # print(stock7)
    # stock8 = Stock("CHX", "AAPL", 150.44, 75, "buy")
    # print(stock8)
    # stock9 = Stock("NYSE", "AAPL", 150.73, 80, "sell")
    # print(stock9)
    # stock10 = Stock("CHX", "ORCL", 75.89, 170, "sell")
    # print(stock10)

    # -------------- FR6: Indentifying the firm's end of day positons--------
    def total_value():
        sum = 0
        for stock in stockList:
            sum += stock.calc_value()
        return sum

    def total_value_by_attribute(attribute, value):
        sumSell = 0
        sumBuy = 0
        for stock in stockList:
            stock_value = getattr(stock, f"get_{attribute}")
            if stock_value == value:
                if stock.get_side == "buy":
                    sumBuy += stock.calc_value()
                else:
                    sumSell += stock.calc_value()
        return sumBuy, sumSell


# ------------FR5: Reading and processing the trading log file---------------------
    Path = r"C:\Users\DanaSeidakhmetova\PycharmProjects\pythonProject\.venv\Python_Project\trades.csv"
    print("\n------------------Welcome to Trading Activity Log--------------------")
    # file_path = str(input("Enter the path to the transaction file: "))

    try:
        with open(Path, 'r') as f:
            print('\n--------------------Reading file-----------------')
            reader = csv.reader(f, delimiter=";")
            if os.stat(Path).st_size == 0:
                print("File is empty")
                exit()
            try:
                for line in reader:
                    (time, exchange, symbol, quantity, price, side) = line
                    price = decimal.Decimal(price)
                    quantity = int(quantity)
                    stock = Stock(exchange, symbol, price, quantity, side)
                    # Add the stocks to the stockList
                    stockList.append(stock)
                    # Add the trades to the Tradebook
                    tradebook.add(stock)
            except ValueError as e:
                print(f"Error processing line: {line}. Error: {e}")
    except FileNotFoundError as e:
        print(f"Could not open/read file: {type(e)}: {e}")
    finally:
        f.close()

    while True:
        print("\n1. Total value for given day")
        print("2. Total value by symbol")
        print("3. Total value by exchange")
        print("4. Generate and print the statistics")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            print(f"\nTotal value for given day: {total_value()}")
        if choice == "2":
            symbol = str(input("Enter the symbol to summarise the total values: ")).upper()
            print(f"\nTotal value for {symbol}: {total_value_by_attribute("symbol", symbol)[0]} for Buy")
            print(f"Total value for {symbol}: {total_value_by_attribute("symbol", symbol)[1]} for Sell")
        if choice == "3":
            exchange = str(input("Enter the exchange to summarise the total values: ")).upper()
            print(f"\nTotal value for {exchange}: {total_value_by_attribute("exchange", exchange)[0]} for Buy")
            print(f"Total value for {exchange}: {total_value_by_attribute("exchange", exchange)[1]} for Sell")
        if choice == "4":
            # Generate and print the statistics
            tradebook.print_reference_trades_statistics()
            tradebook.print_small_trades_statistics()
            tradebook.print_large_trades_statistics()
        if choice == "5":
            exit()

    # ---------------------FR7: Monitor how traders are performing---------

    # # Add the trades to the Tradebook
    # tradebook.add(stock1)
    # tradebook.add(stock2)
    # tradebook.add(stock3)
    # tradebook.add(stock4)
    # tradebook.add(stock5)
    # tradebook.add(stock6)
    # tradebook.add(stock7)
    # tradebook.add(stock8)
    # tradebook.add(stock9)
    # tradebook.add(stock10)

    reference_list = tradebook.get_reference_list()
    big_trades_list = tradebook.get_big_trades_list()
    small_trades_list = tradebook.get_small_trades_list()

    # print(f"reference_list: {reference_list}\n")
    # print(f"big_trades_list: {big_trades_list}\n")
    # print(f"small_trades_list: {small_trades_list}\n")


if __name__ == '__main__':
    main()