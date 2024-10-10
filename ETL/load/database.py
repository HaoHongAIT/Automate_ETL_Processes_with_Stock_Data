import sqlite3


def create_connection():
    # config = {"host": "localhost", "database": "stock_market",
    #           "user": "root", "password": "root"}
    return sqlite3.connect('stock_market.db')

def create_database():
    conn = None
    try:
        conn = create_connection()
        cursor = conn.cursor()
        path = './ETL/load/database.sql'
        with open(path, "r") as queryFile:
            create_tables_script = queryFile.read()

        cursor.executescript(create_tables_script)
        conn.commit()
        print("Database and tables created successfully.")

    except sqlite3.Error as e:
        print(e)

    finally:
        if conn:
            conn.close()
