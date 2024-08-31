import sqlite3
import pandas as pd
import csv

conn = sqlite3.connect('stock_market.db')
cursor = conn.cursor()

def create_string(name_lst):
    cols_str = ",".join(name_lst)
    param_str = ["?" for i in name_lst]
    param_str = ",".join(param_str)
    return param_str, cols_str

def load_to_database(dataframe, table_name, cols_name, cursor):
    param_str, cols_str = create_string(name_lst=cols_name)
    query = f"INSERT INTO {table_name} ("+cols_str + f") VALUES ({param_str})"
    for row in range(len(dataframe)):
        cursor.execute(query, dataframe.iloc[row].values.tolist())

table_names = ['prices_history', 'order_flow_stat', 'foreign_investors', 'proprietary_trading']
for i in range(len(table_names)):
    df = pd.read_csv(f"./data/transformed/fpt/transformed_fpt_{i+1}.csv")
    load_to_database(df, table_names[i], df.columns.tolist(), cursor)


ticker_table = pd.read_excel(f".\data\document\code_stock.xlsx")
load_to_database(ticker_table, 'stock_ticker', ticker_table.columns.tolist(), cursor)

conn.commit()
conn.close()

print("CSV data loaded successfully into the database.")

