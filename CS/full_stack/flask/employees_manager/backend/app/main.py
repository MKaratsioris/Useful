from app.models.employee import Employee
from app.db.employee_database import EmployeeDatabase

def run():
    """
    Populate and demonstrate basic employee operations in the database.
    """
    db = EmployeeDatabase()

    employees = [
        Employee('John', 'Doe', 80000),
        Employee('Jane', 'Doe', 90000),
        Employee('Michalis', 'Karatsioris', 10000),
        Employee('Vasiliki', 'Agou', 40000),
        Employee('Charalampos', 'Dimos', 50000),
        Employee('Sarantis', 'Kyritsis', 100000),
        Employee('Alejandra', 'Mantinan', 200000),
        Employee('Tina', 'Karatsioris', 1000)
    ]

    for emp in employees:
        db.insert(emp)

    print("\nAll Employees:")
    db.show_all()

    print("\nKaratsioris:")
    print(db.get_by_last_name("Karatsioris"))

    db.close()
