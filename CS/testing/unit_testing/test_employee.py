import unittest
from unittest.mock import patch
from main_unittest import Employee

class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Use this if you want to create something that costs too much to create before every single test
        ...
    
    @classmethod
    def tearDownClass(cls):
        # Use this if you want to create something that costs too much to create before every single test
        ...
    
    def setUp(self):
        self.employee_1 = Employee('Corey', 'Schafer', 50_000)
        self.employee_2 = Employee('Sue', 'Smith', 60_000)
    
    def tearDown(self):
        ...
    
    def test_email(self):
        self.assertEqual(self.employee_1.email, 'Corey.Schafer@email.com')
        self.assertEqual(self.employee_2.email, 'Sue.Smith@email.com')
        
        self.employee_1.first_name = 'John'
        self.employee_2.first_name = 'Jane'
        
        self.assertEqual(self.employee_1.email, 'John.Schafer@email.com')
        self.assertEqual(self.employee_2.email, 'Jane.Smith@email.com')
    
    def test_full_name(self):
        self.assertEqual(self.employee_1.full_name, 'Corey Schafer')
        self.assertEqual(self.employee_2.full_name, 'Sue Smith')
        
        self.employee_1.first_name = 'John'
        self.employee_2.first_name = 'Jane'
        
        self.assertEqual(self.employee_1.full_name, 'John Schafer')
        self.assertEqual(self.employee_2.full_name, 'Jane Smith')
    
    def test_apply_raise(self):        
        self.employee_1.apply_raise()
        self.employee_2.apply_raise()
        
        self.assertEqual(self.employee_1.salary, 52_500)
        self.assertEqual(self.employee_2.salary, 63_000)
    
    def test_monthly_schedule(self):
        with patch('main_unittest.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success'
            schedule = self.employee_1.monthly_schedule('May')
            mocked_get.assert_called_with('https://company.com/Schafer/May')
            self.assertEqual(schedule, 'Success')
            
            mocked_get.return_value.ok = False
            schedule = self.employee_2.monthly_schedule('June')
            mocked_get.assert_called_with('https://company.com/Smith/June')
            self.assertEqual(schedule, 'Bad response!')
            


if __name__ == '__main__':
    unittest.main()