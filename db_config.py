import os
import mysql.connector
from mysql.connector import Error
import configparser


def load_db_config(filename='config.properties'):
    # Read configuration properties using configparser
    config = configparser.ConfigParser()

    # Get the exact folder where this script lives (\aniket)
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Create the absolute path to the config file
    file_path = os.path.join(script_dir, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file not found: {file_path}")

    config.read(file_path, encoding='utf-8')

    # Fix: verify the [mysql] section actually exists before returning it.
    if 'mysql' not in config:
        raise KeyError(f"Section [mysql] missing in {file_path}")

    return config['mysql']


def get_connection():
    # Establish mysql connection and return connection status
    try:
        db_props = load_db_config()
    except Exception as e:
        # Fix: config errors were previously uncaught and crashed the caller.
        print(f"Error reading config: {e}")
        return None

    try:
        connection = mysql.connector.connect(
            host=db_props['host'],
            user=db_props['user'],
            password=db_props['password'],
            database=db_props['database']
        )
        return connection
    except Error as e:
        print(f"Error connecting to MYSQL : {e}")
        return None


# testing ::
# Fix: guarded the test block so importing db_config from db_operation.py
# does not open (and immediately close) an extra connection every time.
if __name__ == "__main__":
    conn = get_connection()
    if conn and conn.is_connected():
        print(" Connection tested successfully! ")
        conn.close()
    else:
        print(" Connection failed. ")
