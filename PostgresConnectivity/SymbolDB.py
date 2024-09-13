import psycopg
from psycopg.errors import UniqueViolation
from decimal import Decimal, InvalidOperation
import os
import csv


conn = None
try:
    with psycopg.connect("dbname='postgres' user='postgres' host='localhost' password='postgres'") as conn:
        # Open a cursor to perform database operations
        with conn.cursor() as cur:
            # Create a new schema
            cur.execute(f"CREATE SCHEMA IF NOT EXISTS trade_data")

            # Drop the tables if they already exist
            cur.execute(f"DROP TABLE IF EXISTS trade_data.stock")
            cur.execute(f"DROP TABLE IF EXISTS trade_data.symbols")

            # Create the symbols table
            cur.execute(f"""
            CREATE TABLE trade_data.symbols (
                symbol VARCHAR(10) PRIMARY KEY,
                name VARCHAR(100),
                industry VARCHAR(100)
            )
            """)

            symbols_data = [
                ('WMT', 'Walmart Inc.', 'Discount Stores'),
                ('TSLA', 'Tesla, Inc.', 'Auto Manufacturers'),
                ('GE', 'General Electric Company', 'Specialty Industrial Machinery'),
                ('F', 'Ford Motor Company', 'Auto Manufacturers'),
                ('CNP', 'CenterPoint Energy, Inc.', 'Utilities-Regulated Electric')
            ]
            for symbol, name, industry in symbols_data:
                try:
                    cur.execute(f"INSERT INTO trade_data.symbols (symbol, name, industry) VALUES (%s, %s, %s)",
                                (symbol, name, industry))
                except UniqueViolation:
                    print(f"Symbol {symbol} already exists in the table.")

            # Create the daily stock information table
            cur.execute(f"""
            CREATE TABLE trade_data.stock (
                date DATE,
                symbol VARCHAR(10),
                high DECIMAL(10, 3),
                low DECIMAL(10, 3),
                close DECIMAL(10, 3),
                volume INTEGER,
                PRIMARY KEY (date, symbol),
                FOREIGN KEY (symbol) REFERENCES trade_data.symbols(symbol)
            )
            """)

            # Path to the CSV file
            file_path = r"C:\Users\DanaSeidakhmetova\PycharmProjects\pythonProject\.venv\PostgresConnectivity\daily-symbols.csv"

            # Populate the daily stock table by processing the CSV file
            try:
                with open(file_path, 'r') as f:
                    reader = csv.reader(f)
                    next(reader)  # Skip header row
                    for line in reader:
                        try:
                            date, symbol, high, low, close, volume = line
                            high = Decimal(high)
                            low = Decimal(low)
                            close = Decimal(close)
                            volume = int(volume)

                            # Insert data into the daily stock table
                            cur.execute(f"""
                            INSERT INTO trade_data.stock (date, symbol, high, low, close, volume)
                            VALUES (%s, %s, %s, %s, %s, %s)
                            """, (date, symbol, high, low, close, volume))
                        except (InvalidOperation, ValueError) as e:
                            print(f"Error processing line: {line}. Error: {e}")

                    # Commit the transaction
                    conn.commit()

            except FileNotFoundError as e:
                print(f"Could not open/read file: {type(e)}: {e}")

except Exception as error:
    print(error)

finally:
    if conn is not None:
        conn.close()
