import sqlite3
import pandas as pd
from query import insert



class Load:
    def __init__(self):
        self.table_names = ['prices_history', 'order_flow_stat', 'foreign_investors', 'proprietary_trading']
        self.conn = None

    def run(self):
        try:
            self.conn = sqlite3.connect('stock_market.db')
            cursor = self.conn.cursor()

            # load transformed data to 4 tables
            for i in range(len(self.table_names)):
                df = pd.read_csv(f".\\data\\transformed\\2024-09-14\\{self.table_names[i]}.csv")
                insert(cursor=cursor, cols=df.columns.tolist(), table_name=table_names[i] cursor)
            # load information code stock to ticker table
            ticker_table = pd.read_excel(f".\\data\\document\\code_stock.xlsx")
            load_to_database(ticker_table, 'stock_ticker', ticker_table.columns.tolist(), cursor)
            self.conn.commit()

        except sqlite3.Error as e:
            print(e)

        finally:
            if self.conn:
                self.conn.close()
