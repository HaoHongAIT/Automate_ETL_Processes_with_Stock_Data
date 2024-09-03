import sqlite3


conn = None
try:
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('stock_market.db')

    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # Read the SQL script to create tables
    PATH_TO_FILE = './ETL/load/database.sql'
    with open(PATH_TO_FILE, "r") as queryFile:
        create_tables_script = queryFile.read()

    cursor.executescript(create_tables_script)
    conn.commit()
    print("Database and tables created successfully.")
except sqlite3.Error as e:
    print(e)
finally:
    if conn:
        conn.close()
