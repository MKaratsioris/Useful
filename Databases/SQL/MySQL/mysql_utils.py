import logging
import time
#import mysql.connector
from mysql.connector import (connection)
from mysql.connector import errorcode
from mysql.connector.errors import Error
from mysql.connector.cursor_cext import MySQLCursorAbstract
from mysql.connector.connection_cext import MySQLConnectionAbstract

# TODO: Add logs in the functionality

# Set up logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# Log to console
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

file_handler = logging.FileHandler("mysql-errors.log")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def query_error(
    err, 
    db_name: str
    ) -> None:
    """Customize errors."""
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print(f"Something is wrong with your user name or password.")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print(f"Database {db_name} does not exist.")
    else:
      print(f"Could not connect to {db_name}.")
    print(err)


def connect_to_mysql(
    config: dict, 
    attempts: int = 3, 
    delay: int = 2
    ) -> connection.MySQLConnection:
    """Create connection to MySQL."""
    attempt = 1
    while attempt < attempts + 1:  # Reconnection routine
        try:
            #return mysql.connector.connect(**config)
            return connection.MySQLConnection(**config)
        except (Error, IOError) as err:
            if (attempts is attempt):
                logger.info(f"Failed to connect, exiting without a connection: {err}")
                return MySQLConnectionAbstract.close()  # Return this option so i do not have typing errors
            logger.info(f"Connection failed: {err}. Retrying ({attempt}/{attempts-1})...")
            time.sleep(delay ** attempt)  # progressive reconnect delay
            attempt += 1
    return MySQLConnectionAbstract.close()  # Return this option so i do not have typing errors


def create_mysql_database(
    cursor: MySQLCursorAbstract, 
    db_name: str
    ) -> None:
    """Create a database."""
    cursor.execute(f"CREATE DATABASE {db_name}")
    cursor.execute(f"USE {db_name}")


def create_mysql_tables(
    cursor: MySQLCursorAbstract, 
    tables: dict
    ) -> None:
    """Create list of tables."""
    for table_name in tables:
        table_description = tables[table_name]
        cursor.execute(table_description)


def print_mysql_table(
    cursor: MySQLCursorAbstract, 
    db_name: str, 
    table_name: str, 
    first_row: int = 0, 
    last_row: int = 10
    ) -> None:
    """Print from a specific table, the requested rows."""
    cursor.execute(f"USE {db_name}")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows[first_row:last_row + 1]:
        print(row)


def add_data(
    connection: connection.MySQLConnection, 
    cursor: MySQLCursorAbstract, 
    db_name: str, 
    query: str, 
    data: list
    ) -> None:
    cursor.execute(f"USE {db_name}")
    for element in data:
        cursor.execute(query, element)
    connection.commit()