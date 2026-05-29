import unittest
from sub import *

class TestSub(unittest.TestCase):

    def test_positive_numbers(self):
        self.assertEqual(substract(10, 3), 7)

    def test_negative_numbers(self):
        self.assertEqual(substract(-1, -1), 0)

    def test_zero(self):
        self.assertEqual(substract(10, 0), 10)    

    def test_str(self):
        self.assertEqual        

if __name__ == "__main__":
    unittest.main()