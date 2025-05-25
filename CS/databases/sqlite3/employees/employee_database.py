from pathlib import Path
from sqlite3 import Connection, connect, Cursor
from typing import List

from employee import Employee

class EmployeeDatabase:
    """
    TODO    Implement   logging
    TODO    Implement   testing
    Handles SQLite database operations for managing Employee records.
    
    Attributes
    ----------
    db_name: str
        Database name
    connection: sqlite3.Connection
        Connection to database
    cursor: Cursor
        Utilizes the connection to execute queries and fetch data
    
    Methods
    -------
    create_table(self, table_name: str = 'db_table') -> None
        Create a table if it doesn't already exist.
    insert_employee(self, employee: Employee) -> None
        Insert a new employee into the database.
    select_last_name(self, last_name: str) -> List[Employee]
        Retrieve all employees with a given last name.
    update_salary(self, employee: Employee, new_salary: int) -> None
        Update an employee's salary.
    delete_employee(self, employee: Employee) -> None
        Delete an employee from the table.
    select_all(self) -> None
        Print all employee records currently in the database.
    close_connection(self) -> None
        Close the database connection.
    """
    def __init__(self, db_name: str = ':memory:') -> None:
        """
        Initialize the database and connects.
        
        Parameters
        ----------
        db_name : str, optional
            Database name, by default ':memory:'
        """
        self.db_name: str = 'in memory' if db_name == ':memory:' else db_name.name.split('.')[0]
        self.connection: Connection = connect(db_name)
        print(f"Database {self.db_name} created successfully!")
        self.cursor: Cursor = self.connection.cursor()
        print(f"You are now connected to database {db_name}.")

    def create_table(self, table_name: str = 'db_table') -> None:
        """
        TODO    Add as parameters the table columns.
        Create a table if it doesn't already exist.
        
        Parameters
        ----------
        table_name : str, optional
            Table name, by default 'db_table'
        """
        self.table_name: str = table_name
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {table_name} (
                first_name TEXT,
                last_name TEXT,
                salary INTEGER
            )
        ''')
        self.connection.commit()
        print(f"Table {table_name} created successfully!")

    def insert_employee(self, employee: Employee) -> None:
        """
        Insert a new employee into the database.
        
        Parameters
        ----------
        employee : Employee
            The Employee object to insert.
        """
        with self.connection:
            self.cursor.execute(
                f"INSERT INTO {self.table_name} VALUES (:first_name, :last_name, :salary)",
                vars(employee)
            )

    def select_last_name(self, last_name: str) -> List[Employee]:
        """
        Retrieve all employees with a given last name.
        
        Parameters
        ----------
        last_name : str
            The last name to search for.
        
        Returns
            List of matching Employee objects.
        """
        self.cursor.execute(
            f"SELECT * FROM {self.table_name} WHERE last_name = :last_name",
            {'last_name': last_name.capitalize()}
        )
        return [Employee(*row) for row in self.cursor.fetchall()]

    def update_salary(self, employee: Employee, new_salary: int) -> None:
        """
        Update an employee's salary.
        
        Parameters
        ----------
        employee : Employee
            The Employee whose salary should be updated.
        new_salary : int
            The new salary amount.
        """
        with self.connection:
            self.cursor.execute(
                f'''UPDATE {self.table_name} SET salary = :salary
                   WHERE first_name = :first_name AND last_name = :last_name''',
                {
                    'first_name': employee.first_name,
                    'last_name': employee.last_name,
                    'salary': new_salary
                }
            )

    def delete_employee(self, employee: Employee) -> None:
        """
        Delete an employee from the table.
        
        Parameters
        ----------
        employee : Employee
            The Employee to delete.
        """
        with self.connection:
            self.cursor.execute(
                f"DELETE FROM {self.table_name} WHERE first_name = :first_name AND last_name = :last_name",
                {
                    'first_name': employee.first_name,
                    'last_name': employee.last_name
                }
            )

    def select_all(self) -> None:
        """Print all employee records currently in the database."""
        self.cursor.execute(f"SELECT * FROM {self.table_name}")
        for row in self.cursor.fetchall():
            print(row)

    def close_connection(self) -> None:
        """Close the database connection."""
        self.connection.close()
        print("Database connection closed successfully!")
