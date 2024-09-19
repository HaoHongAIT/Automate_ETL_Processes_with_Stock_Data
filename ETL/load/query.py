import mysql.connector
import pandas as pd


def insert(cursor, cols: list, table_name: str, dataframe: pd.DataFrame):
    # create a sub string in insert query (Ex: "col_1, col_2, col_3, col_4")
    cols_str = ",".join(cols)
    # create a sub string in insert query (Ex: "?, ?, ?, ?")
    param_str = ["?" for _ in cols] # ["?" ,?" , "?" , "?"]
    param_str = ",".join(param_str)
    # create a insert query (Ex: INSERT INTO table_name (col_1, col_2, col_3, col_4))
    #                            VALUES (?, ?, ? , ?)
    insert_query = f"INSERT INTO {table_name} ("+ cols_str + f") VALUES ({param_str})"
    try:
        for row in range(len(dataframe)):
            cursor.execute(insert_query, dataframe.iloc[row].values.tolist())

    except mysql.connector.Error as e:
        raise e


# def show(cursor, table):
#     query = f"SELECT * FROM {table}"
#     cursor.execute(query)
#     for row in cursor:
#         print(row)
