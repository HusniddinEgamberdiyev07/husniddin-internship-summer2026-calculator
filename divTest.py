import unittest
from div import *

class TestSub(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(divide(10, 5), 2)

    def test_negative_numbers(self):
        self.assertEqual(divide(-1, -1), 1)

    def test_zeroDivision(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)    

    def test_str(self):
        with self.assertRaises(TypeError):
            divide(10, "10")
            
if __name__ == "__main__":
    unittest.main()