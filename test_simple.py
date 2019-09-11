import os
import unittest

#没有考虑负数
def max_number(a):
    max_value = 0
    for i in range(len(a)):
        if a[i] > max_value:
            max_value = a[i]
    return max_value
    
class TestMaxNumber(unittest.TestCase):
    def test1(self):
        self.assertEqual(max_number((11, 0)), 11)

    def test2(self):
        self.assertEqual(max_number((-11, -1)), -1)

if __name__ == "__main__":
    unittest.main()
