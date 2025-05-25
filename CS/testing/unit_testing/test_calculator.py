import unittest
import unit_testing.main_unittest as main_unittest

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(main_unittest.add(10, 5), 15)
        self.assertEqual(main_unittest.add(-1, 1), 0)
        self.assertEqual(main_unittest.add(-10, -5), -15)
    
    def test_subtract(self):
        self.assertEqual(main_unittest.subtract(10, 5), 5)
        self.assertEqual(main_unittest.subtract(-1, 1), -2)
        self.assertEqual(main_unittest.subtract(-10, -5), -5)
    
    def test_multiply(self):
        self.assertEqual(main_unittest.multiply(10, 5), 50)
        self.assertEqual(main_unittest.multiply(-1, 1), -1)
        self.assertEqual(main_unittest.multiply(-10, -5), 50)
    
    def test_divide(self):
        self.assertEqual(main_unittest.divide(10, 5), 2)
        self.assertEqual(main_unittest.divide(-1, 1), -1)
        self.assertEqual(main_unittest.divide(-10, -5), 2)
        self.assertEqual(main_unittest.divide(5, 2), 2.5)
        #self.assertRaises(ValueError, calculator.divide, 10, 0)
        with self.assertRaises(ValueError):
            main_unittest.divide(10, 0)


if __name__ == '__main__':
    unittest.main()