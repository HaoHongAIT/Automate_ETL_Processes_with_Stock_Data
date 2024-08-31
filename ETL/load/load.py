import sqlite3
import csv

conn = sqlite3.connect('stock_market.db')
cursor = conn.cursor()


def load_data_from_csv(csv_file, table_name, cursor):
    with open(csv_file, 'r') as file:
        # Use the csv reader to read the CSV file
        reader = csv.reader(file)
        print(next(reader))
        # Skip the header row
        next(reader)

        if table_name == 'prices_history':
            query = '''INSERT INTO prices_history (date, open_price, close_price, high_price, low_price, volume, stock_symbol)
                       VALUES (?, ?, ?, ?, ?, ?, ?)'''
        elif table_name == 'stock_trades':
            query = '''INSERT INTO stock_trades (date, buy_volume, sell_volume, net_volume, stock_symbol, stock_price_id)
                       VALUES (?, ?, ?, ?, ?, ?)'''
        elif table_name == 'stock_transactions':
            query = '''INSERT INTO stock_transactions (date, buy_volume, buy_value, sell_volume, sell_value, net_volume, net_value, stock_symbol)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        elif table_name == 'detailed_stock_trades':
            query = '''INSERT INTO detailed_stock_trades (stock_symbol, date, buy_volume, buy_value, sell_volume, sell_value, net_volume, net_value)
                       VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''

        # Execute the insertion for each row
        for row in reader:
            cursor.execute(query, row)


# Load data into each table

load_data_from_csv('transformed_fpt_1.csv', 'prices_history', cursor)
load_data_from_csv('transformed_fpt_2.csv', 'stock_trades', cursor)
load_data_from_csv('transformed_fpt_3.csv', 'stock_transactions', cursor)
load_data_from_csv('transformed_fpt_4.csv', 'detailed_stock_trades', cursor)

# Commit the transactions
conn.commit()

# Close the connection
conn.close()

print("CSV data loaded successfully into the database.")
