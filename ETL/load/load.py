import pandas as pd
from .query import insert
import mysql.connector



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

    def run(self):
        try:
            cursor = self.conn.cursor()
            # load transformed data to 4 tables
            for i in range(len(self.table_names)):
                df = pd.read_csv(f".\\data\\transformed\\2024-09-14\\{self.table_names[i]}.csv")
                insert(cursor=cursor, cols=df.columns.tolist(), table_name=self.table_names[i], dataframe=df)
            # load information code stock to ticker table
            ticker_table = pd.read_excel(f".\\data\\document\\code_stock.xlsx")
            insert(cursor=cursor, cols=ticker_table.columns.tolist(),
                   table_name='stock_ticker', dataframe=ticker_table)
            self.conn.commit()

        except:
            pass

        finally:
            if self.conn:
                self.conn.close()
