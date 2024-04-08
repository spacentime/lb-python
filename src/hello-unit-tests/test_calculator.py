import unittest
from calculator import add, subtract, multiply, divide
class TestCalculatorFx(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(3, 2), 1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(0, 5), 0)    

class MoreTests(unittest.TestCase):
    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(10, 0)
    
    def test_add_large_number(self):
        self.assertEqual(add(500000, 3000000), 3500000)        

if __name__ == '__main__':
    unittest.main()
