from pathlib import Path, PosixPath

from employee import Employee
from employee_database import EmployeeDatabase

if __name__ == '__main__':
    db_name: str = 'test_employees'
    db_folder: PosixPath = Path(__file__).parent.parent
    db_file_path: PosixPath = db_folder.joinpath(f"db/{db_name}.db")
    
    #db = EmployeeDatabase(db_name=db_file_path)
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
    db.create_table('employees')

    print("\n----------- insert_employee -----------")
    for emp in employees:
        db.insert_employee(emp)

    print("\n----------- select_all -----------")
    db.select_all()

    print("\n----------- select_last_name -----------")
    karatsioris_employees = db.select_last_name('Karatsioris')
    print(karatsioris_employees)

    print("\n----------- update_salary -----------")
    db.update_salary(employees[2], 1000)
    print(db.select_last_name('Karatsioris'))

    print("\n----------- delete_employee -----------")
    db.delete_employee(employees[0])
    print(db.select_last_name('Doe'))

    db.close_connection()