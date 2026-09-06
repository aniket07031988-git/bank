import db_config
from mysql.connector import Error
import mysql.connector

# Initialize global connection and cursor
connection = db_config.get_connection()
cursor = connection.cursor() if connection else None

if connection:
    print(" Program ready for next process ")
else:
    print(" Some issue ")


def fetch_record(table_name):
    # Fix: cursor is None when the connection failed -> AttributeError.
    if cursor is None:
        print("No active database connection.")
        return []

    try:
        query = f"SELECT * FROM {table_name}"
        cursor.execute(query)
        return cursor.fetchall()

    except Exception as e:
        print(f"Error fetching data: {e}")
        return []


def insert_record(table_name, columns, records):
    if cursor is None:
        print("No active database connection.")
        return

    try:
        col_str = ",".join(columns)
        placeholders = ",".join(["%s"] * len(columns))

        query = f"INSERT INTO {table_name} ({col_str}) VALUES ({placeholders})"

        cursor.executemany(query, records)
        connection.commit()
        print(f"{cursor.rowcount} records inserted successfully into {table_name}")

    except Exception as e:
        # Fix: roll back so a partial batch does not stay open in the transaction.
        connection.rollback()
        print(f"Error inserting data: {e}")


def create_table(table_name, schema):
    if cursor is None:
        print("No active database connection.")
        return

    try:
        columns_dfs = ",".join([f"{col} {dtype}" for col, dtype in schema.items()])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_dfs})"

        # Fix 1: Corrected typo 'quer' to 'query'
        cursor.execute(query)
        connection.commit()
        print(f"Table '{table_name}' checked/created successfully.")

    except Exception as e:
        print(f"Error creating table: {e}")


def close_connection():
    # Fix: nothing ever closed the cursor/connection, leaving it open at exit.
    try:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()
            print("Connection closed.")
    except Exception as e:
        print(f"Error closing connection: {e}")
