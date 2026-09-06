import mysql.connector 
from mysql.connector import Error 

# step1 - Database connection establish 
try:
    connection = mysql.connector.connect(host="localhost", user="root", password="mysql7388", database="test")
   
    # step2 : check - either connection is done or not 
    if connection.is_connected():
        print("Successfully connected to MYSQL database AniketDB!")
    
    # ANY SQL TASK Perform : with Cursor ( Acts as pointer on table )
    # step3 : Create Cursor to use for SQL query 
    cursor = connection.cursor()
    print(".............Cursor Created ...............")

# The except block must align perfectly with the try block
except Error as e:
    print(f"Database error occurred: {e}")
   
finally:
    if 'connection' in locals() and connection.is_connected():
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        connection.close()
        print("\nMysql Connection closed safely")
