# Fix 1: Cleaned up duplicate create_table import
from db_operation import create_table, insert_record, fetch_record, close_connection


def main():
    table_name = "sales"

    # Table schema setup
    schema = {
        "sales_id": "INT PRIMARY KEY",
        "sales_name": "VARCHAR(100)"
    }

    # Called the imported function directly without module prefix
    create_table(table_name, schema)

    # Fix 2: Aligned columns indentation perfectly to match the other blocks
    columns = ["sales_id", "sales_name"]
    records = [
        (101, "Amit"),
        (102, "Aniket"),
        (103, "sohan")
    ]

    # Kept argument formats consistent to avoid positional mixing errors
    insert_record(table_name, columns, records)

    # Fetch records
    data = fetch_record(table_name)

    print("\n--- Fetched Data Results ---")
    for row in data:
        print(row)

    # Fix 3: release the cursor/connection before the program exits
    close_connection()


if __name__ == "__main__":
    main()
