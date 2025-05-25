
from dataclasses import dataclass

@dataclass
class Employee:
    """
    TODO    Implement   logging
    TODO    Implement   testing
    Represents an employee with a first name, last name, and salary.
    
    Attributes
    ----------
    first_name: str
    last_name: str
    salary: int
    email: str
    full_name: str
    """
    first_name: str
    last_name: str
    salary: int

    def __post_init__(self):
        """Normalize names (capitalize first letter, lowercase the rest) after initialization."""
        self.first_name = self.first_name.lower().capitalize()
        self.last_name = self.last_name.lower().capitalize()

    @property
    def email(self) -> str:
        """Generate a fake email address based on the employee's name."""
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"

    @property
    def full_name(self) -> str:
        """Returns the employee's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self) -> str:
        return f"First name\t{self.first_name}\nLast name:\t{self.last_name}\nSalary:\t\t{self.salary}€"
    
    def __repr__(self) -> str:
        return f"Employee(first_name={self.first_name}, last_name={self.last_name}, salary={self.salary})"

if __name__ == '__main__':
    employee_1: Employee = Employee(first_name='Michalis', last_name='Karatsioris', salary=1_000)
    print(employee_1)
    print(str(employee_1))
    print(repr(employee_1))
    print(f"{employee_1.full_name=}")
    print(f"{employee_1.email=}")