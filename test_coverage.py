import os
import unittest


def add_and_multiply(x, y):
    addition = add(x , y)
    multiple = multiply(x, y)
    return (addition, multiple)

def add(x, y):
    return x + y 

def multiply(x, y):
    return x * y 
   
class TestCoverage(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(11, 2), 13)

    def test_multiply(self):
        self.assertEqual(multiply(-11, -1), 11)

if __name__ == '__main__':
    unittest.main()

