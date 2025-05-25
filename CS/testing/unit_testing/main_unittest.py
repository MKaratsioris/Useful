
import requests

def add(x, y):
    """Add function."""
    return x + y

def subtract(x, y):
    """Subtract function."""
    return x - y

def multiply(x, y):
    """Multiply function."""
    return x * y

def divide(x, y):
    """Divide function."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

class Employee:
    """A sample Employee class"""
    
    raise_amt = 1.05
    
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@email.com"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    def apply_raise(self):
        self.salary = int(self.salary * self.raise_amt)
    
    def monthly_schedule(self, month):
        response = requests.get(f"https://company.com/{self.last_name}/{month}")
        if response.ok:
            return response.text
        return 'Bad response!'