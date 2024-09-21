import pandas as pd
from .database import create_database, create_connection
from .query import insert
import mysql.connector
import csv

def iter_excel_pandas(file):
    yield from pd.read_excel(file).to_dict('records')


def read_file(path, type="csv"):
    data = []
    if type == "csv":
        with open(path, "r") as csv_file:
            csvreader = csv.reader(csv_file)
            header = next(csvreader)
            for row in csvreader:
                data.append(row)

    elif type == "xlsx":
        with open('file.xlsx', 'rb') as xlsx_file:
            xlsx_file = iter_excel_pandas(xlsx_file)
            header = next(xlsx_file)
    return header, data

class Load:
    def __init__(self):
        self.table_names = ['prices_history', 'order_flow_stat', 'foreign_investors', 'proprietary_trading']
        self.conn = None

    def create_connection(self):
        config = {"host" : "localhost", "database": "stock_market",
                  "user" : "root", "password" : "root"}
        try:
            self.conn = mysql.connector.connect(**config)

        except mysql.connector.Error as err:
            print(err)

    def run(self, init=False):
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
            header, ticker_table = read_file(path= f".\\data\\document\\code_stock.xlsx", type="xlsx")
            insert(cursor=cursor, header=header,
                   table_name='stock_ticker', stock_codes=ticker_table)
            self.conn.commit()


        except mysql.connector.Error as err:
            print(err)

        finally:
            if self.conn: self.conn.close()
