from .database import create_database, create_connection
from .query import insert
import csv
import sqlite3

def read_file(path):
    with open(path, "r", encoding="utf-8-sig") as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader)
        data=  list(csvreader)

    return header, data


class Load:
    def __init__(self):
        self.table_names = ['prices_history', 'order_flow_stat', 'foreign_investors', 'proprietary_trading']
        self.conn = None

    def run(self, init=True):
        if init:
            create_database()

        try:
            self.conn = create_connection()
            cursor = self.conn.cursor()
            # load transformed data to 4 tables
            for i in range(len(self.table_names)):
                header, stock_codes = read_file(f".\\data\\transformed\\2024-09-14\\{self.table_names[i]}.csv")
                insert(cursor=cursor, header=header, table_name=self.table_names[i], stock_codes=stock_codes)
            # load information code stock to ticker table
            header, ticker_table = read_file(path= f".\\data\\document\\code_stock.csv")
            insert(cursor=cursor, header=header,
                   table_name='stock_ticker', stock_codes=ticker_table)
            self.conn.commit()

        except sqlite3.Error as err:
            print(err)

        finally:
            if self.conn: self.conn.close()
