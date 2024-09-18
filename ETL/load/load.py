import sqlite3
import pandas as pd


def create_string(name_lst):
    # create a sub string in insert query (Ex: "col_1, col_2, col_3, col_4")
    cols_str = ",".join(name_lst)
    # create a sub string in insert query (Ex: "?, ?, ?, ?")
    param_str = ["?" for i in name_lst]
    param_str = ",".join(param_str)
    return param_str, cols_str

def load_to_database(dataframe, table_name, cols_name, cursor):
    param_str, cols_str = create_string(name_lst=cols_name)
    # create a insert query (Ex: INSERT INTO table_name (col_1, col_2, col_3, col_4))
    #                            VALUES (?, ?, ? , ?)
    query = f"INSERT INTO {table_name} ("+cols_str + f") VALUES ({param_str})"

    for row in range(len(dataframe)):
        cursor.execute(query, dataframe.iloc[row].values.tolist())

class Load:
    def __init__(self):
        self.table_names = ['prices_history', 'order_flow_stat', 'foreign_investors', 'proprietary_trading']
        self.conn = None

    def run(self):
        try:
            self.conn = sqlite3.connect('stock_market.db')
            cursor = self.conn.cursor()
            # query = "SELECT * FROM prices_history"
            # cursor.execute(query)
            # for row in cursor:
            #     print(row)

            # load transformed data to 4 tables
            for i in range(len(self.table_names)):
                df = pd.read_csv(f".\\data\\transformed\\2024-09-14\\{self.table_names[i]}.csv")
                load_to_database(df, self.table_names[i], df.columns.tolist(), cursor)
            # load information code stock to ticker table
            ticker_table = pd.read_excel(f".\\data\\document\\code_stock.xlsx")
            load_to_database(ticker_table, 'stock_ticker', ticker_table.columns.tolist(), cursor)
            self.conn.commit()

        except sqlite3.Error as e:
            print(e)

        finally:
            if self.conn:
                self.conn.close()
