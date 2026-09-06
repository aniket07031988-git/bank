import mysql.connector 
from mysql.connector import Error 

try:
    # step1 - Database connection establish 
    connection = mysql.connector.connect(host="localhost", user="root", password="mysql7388", database="test")
   
    # step2 : check connection
    if connection.is_connected():
        print("Successfully connected to MYSQL database test!")
    
    # step3 : Create Cursor
    cursor = connection.cursor()
    print(".............Cursor Created ...............")

    # 1. task : create table employee  
    print("\n[1] Table Creation in Progress...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        role VARCHAR(100)
    )
    """)
    print("Table ready!")
	
    # 2. insert 10 records 
    print("\n[2] Inserting 10 records...")
    insert_query = "INSERT INTO employee (name, role) VALUES (%s, %s)"
    
    # List containing exactly 10 records
    records_to_insert = [
        ("Aniket", "IT"),
        ("Amit", "HR"),
        ("Rahul", "Developer"),
        ("Priya", "QA Analyst"),
        ("Sneha", "Manager"),
        ("Vikram", "DevOps"),
        ("Rohan", "Data Scientist"),
        ("Neha", "UI Designer"),
        ("Aakash", "Support"),
        ("Siddharth", "Security Engineer")
    ]
    
    # CRITICAL FIX: Use executemany for bulk lists/tuples
    cursor.executemany(insert_query, records_to_insert)
    connection.commit() 
    print(f"Successfully inserted {cursor.rowcount} records!")

    # 3. read data from table
    print("\n[3] Reading data...")
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID : {row[0]} | Name : {row[1]} | Role : {row[2]}")
    
    # 4. update record
    print("\n[4] Updating data...")
    update_query = "UPDATE employee SET role = %s WHERE name = %s"
    update_data = ("Architect", "Aniket")
    cursor.execute(update_query, update_data)
    connection.commit()
    print(f"Rows updated: {cursor.rowcount}")

    # 5. read and validate data after update
    print("\n[5] Validating data after update...")
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(f"ID : {row[0]} | Name : {row[1]} | Role : {row[2]}")

      # 6. delete records based on role
    print("\n[6] Deleting data for HR role...")
    delete_query = "DELETE FROM employee WHERE role = %s"  # Changed 'id' to 'role'
    cursor.execute(delete_query, ("HR",))  
    connection.commit()
    print(f"Rows deleted: {cursor.rowcount}")


except Error as e:
    print(f"Database error occurred: {e}")
   
finally:
    if 'connection' in locals() and connection.is_connected():
        if 'cursor' in locals() and cursor is not None:
            cursor.close()
        connection.close()
        print("\nMysql Connection closed safely")
