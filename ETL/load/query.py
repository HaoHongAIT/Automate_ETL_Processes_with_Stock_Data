import mysql.connector
import pandas as pd
import numpy as np


def insert(cursor, header: list, table_name: str, stock_codes: list):
    # create a sub string in insert query (Ex: "col_1, col_2, col_3, col_4")
    cols_str = ",".join(header)
    # create a sub string in insert query (Ex: "?, ?, ?, ?")
    param_str = ["?" for _ in header] # ["?" ,?" , "?" , "?"]
    param_str = ",".join(param_str)
    # create a insert query (Ex: INSERT INTO table_name (col_1, col_2, col_3, col_4))
    #                            VALUES (?, ?, ? , ?)
    insert_query = f"INSERT INTO {table_name} ("+ cols_str + f") VALUES ({param_str})"
    try:
        for row in stock_codes:
            cursor.execute(insert_query, row)

    except mysql.connector.Error as e:
        raise e


# def show(cursor, table):
#     query = f"SELECT * FROM {table}"
#     cursor.execute(query)
#     for row in cursor:
#         print(row)
