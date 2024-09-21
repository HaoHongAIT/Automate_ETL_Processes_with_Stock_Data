import mysql.connector



def create_connection():
    config = {"host": "localhost", "database": "stock_market",
              "user": "root", "password": "root"}
    return mysql.connector.connect(**config)

def create_database():
    conn = None
    try:
        conn = create_connection()
        cursor = conn.cursor()
        path_to_file = './ETL/load/database.sql'
        with open(path_to_file, "r") as queryFile:
            create_database_script = queryFile.read()

        cursor.execute(create_database_script)
        conn.commit()
        print("Database and tables created successfully.")

    except mysql.connector.Error as err:
        print(err)

    finally:
        if conn:
            conn.close()
