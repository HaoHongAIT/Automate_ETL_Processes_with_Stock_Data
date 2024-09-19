import mysql.connector

CONFIG = {"host": "localhost", "database": "stock_market",
          "user": "root", "password": "root"}

def create_connection():
    try:
        return mysql.connector.connect(**CONFIG)

    except mysql.connector.Error as err:
        print(err)

def create_database():
    conn = None
    try:
        # Connect to SQLite database (or create it if it doesn't exist)
        conn = create_connection()
        # Create a cursor object to interact with the database
        cursor = conn.cursor()

        # Read the SQL script to create tables
        path_to_file = './ETL/load/database.sql'
        with open(path_to_file, "r") as queryFile:
            create_tables_script = queryFile.read()

        cursor.execute(create_tables_script)
        conn.commit()
        print("Database and tables created successfully.")

    except mysql.connector.Error as err:
        print(err)

    finally:
        if conn:
            conn.close()
