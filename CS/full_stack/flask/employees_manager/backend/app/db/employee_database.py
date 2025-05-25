from sqlite3 import Connection
from typing import List

from app.models.employee import Employee

class EmployeeDatabase:
    """
    Handles SQLite database operations for managing Employee records.
    """
    def __init__(self, connection: Connection):
        """
        Initialize the database connection and create the employees table.
        """
        self.connection = connection
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self) -> None:
        """
        Create the employees table if it doesn't already exist.
        """
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                first_name TEXT,
                last_name TEXT,
                salary INTEGER
            )
        ''')
        self.connection.commit()

    def insert(self, employee: Employee) -> None:
        """
        Insert a new employee into the database.
        
        :param employee: The Employee object to insert.
        """
        with self.connection:
            self.cursor.execute(
                "INSERT INTO employees VALUES (:first_name, :last_name, :salary)",
                vars(employee)
            )

    def get_by_last_name(self, last_name: str) -> List[Employee]:
        """
        Retrieve all employees with a given last name.
        
        :param last_name: The last name to search for.
        :return: List of matching Employee objects.
        """
        self.cursor.execute(
            "SELECT * FROM employees WHERE last_name = :last_name",
            {'last_name': last_name.capitalize()}
        )
        return [Employee(*row) for row in self.cursor.fetchall()]

    def update_salary(self, employee: Employee, new_salary: int) -> None:
        """
        Update an employee's salary.
        
        :param employee: The Employee whose salary should be updated.
        :param new_salary: The new salary amount.
        """
        with self.connection:
            self.cursor.execute(
                '''UPDATE employees SET salary = :salary
                   WHERE first_name = :first_name AND last_name = :last_name''',
                {
                    'first_name': employee.first_name,
                    'last_name': employee.last_name,
                    'salary': new_salary
                }
            )

    def delete(self, employee: Employee) -> None:
        """
        Delete an employee from the database.
        
        :param employee: The Employee to delete.
        """
        with self.connection:
            self.cursor.execute(
                "DELETE FROM employees WHERE first_name = :first_name AND last_name = :last_name",
                {
                    'first_name': employee.first_name,
                    'last_name': employee.last_name
                }
            )

    def show_all(self) -> None:
        """
        Print all employee records currently in the database.
        """
        self.cursor.execute("SELECT * FROM employees")
        for row in self.cursor.fetchall():
            print(row)

    def close(self) -> None:
        """
        Close the database connection.
        """
        self.connection.close()
