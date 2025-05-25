
from dataclasses import dataclass

@dataclass
class Employee:
    """
    Represents an employee with a first name, last name, and salary.
    """
    first_name: str
    last_name: str
    salary: int

    def __post_init__(self):
        """
        Normalize names (capitalize first letter, lowercase the rest) after initialization.
        """
        self.first_name = self.first_name.lower().capitalize()
        self.last_name = self.last_name.lower().capitalize()

    @property
    def email(self) -> str:
        """
        Generate a fake email address based on the employee's name.
        """
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"

    @property
    def full_name(self) -> str:
        """
        Returns the employee's full name.
        """
        return f"{self.first_name} {self.last_name}"

"""

class Employee:
    def __init__(self, first_name: str, last_name: str, salary: int) -> None:
        self.first_name: str = first_name.lower().capitalize()
        self.last_name: str = last_name.lower().capitalize()
        self.salary: int = salary
    
    @property
    def email(self) -> str:
        return f"{self.first_name.lower()}.{self.last_name.lower()}@email.com"
    
    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def __repr__(self) -> str:
        return f"Employee(first_name={self.first_name}, last_name={self.last_name}, salary={self.salary})"

"""