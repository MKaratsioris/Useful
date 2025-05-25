from sqlite3 import connect
from pathlib import Path, PosixPath

db_name: str = 'test_stores'
db_folder: PosixPath = Path(__file__).parent.parent
db_file_path: PosixPath = db_folder.joinpath(f"db/{db_name}.db")
#connection = connect(db_file_path)
connection = connect(':memory:')
cursor = connection.cursor()

# Create Stores Table
create_stores_table_query = """CREATE TABLE IF NOT EXISTS stores_table(store_id INTEGER PRIMARY KEY, location TEXT)"""
cursor.execute(create_stores_table_query)

# Add data to stores_table
cursor.execute("INSERT INTO stores_table VALUES (21, 'Minneapolis, MN')")
cursor.execute("INSERT INTO stores_table VALUES (95, 'Chicago, IL')")
cursor.execute("INSERT INTO stores_table VALUES (64, 'Iowa City, IA')")

# Create Purchases Table
create_purchases_table_query = """CREATE TABLE IF NOT EXISTS 
purchases_table(purchase_id INTEGER PRIMARY KEY, store_id INTEGER, total_cost FLOAT, FOREIGN KEY(store_id) REFERENCES stores(store_id))"""
cursor.execute(create_purchases_table_query)

# Add data to purchases_table
cursor.execute("INSERT INTO purchases_table VALUES (54, 21, 15.49)")
cursor.execute("INSERT INTO purchases_table VALUES (23, 64, 21.12)")

# Get all purchases
cursor.execute("SELECT * FROM purchases_table")
select_all_purchases = cursor.fetchall()
print(f"{select_all_purchases=}")

# Get all stores
cursor.execute("SELECT * FROM stores_table")
select_all_stores = cursor.fetchall()
print(f"{select_all_stores=}")