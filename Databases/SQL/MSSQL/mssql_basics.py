import pyodbc
# source : https://www.youtube.com/watch?v=YwjlHvzSl_c&list=PLMi6KgK4_mk0yXrfyLJfxcSoyXHxQJq8K

#print(pyodbc.drivers())
#drivers = [item for item in pyodbc.drivers()]
driver = "ODBC Driver 18 for SQL Server"
server = "."
database = "new"
uid = "sa"
pwd = "mkar1984!"

mssql_connection = pyodbc.connect(driver=driver, host=server, database=database, user=uid, password=pwd, TrustServerCertificate="yes")
mssql_connection.autocommit = True
#mssql_connection.execute(f"CREATE DATABASE iWillDropYou")
#mssql_connection.execute("DROP DATABASE iWillDropYou")

print("OK")
