from app.models.employee import Employee
from app.db.employee_database import EmployeeDatabase

def test_insert_and_get():
    db = EmployeeDatabase()
    employee = Employee('Test', 'User', 12345)
    db.insert_employee(employee)
    results = db.select_last_name('User')
    assert len(results) == 1
    assert results[0].salary == 12345
    db.close()
