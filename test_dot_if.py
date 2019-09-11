import os
import dot_if
import numpy as np
import unittest

class TestDot(unittest.TestCase):
    def test_normal(self):  
        m1 = np.arange(0,6).reshape(2,3)
        m2 = np.arange(0,6).reshape(3,2)
        m = dot_if.dot(m1, m2)
        
        self.assertEqual(m.ndim, 2)
        self.assertEqual(m.shape, (2,2))
        self.assertEqual(m[0][0], 10)
        self.assertEqual(m[0][1], 13)
        self.assertEqual(m[1][0], 28)
        self.assertEqual(m[1][1], 40)

    def test_empty_input(self):  
        m1 = np.arange(0,0).reshape(0,0)
        m2 = np.arange(0,0).reshape(0,0)
        m = dot_if.dot(m1, m2)
        self.assertEqual(m.shape[0], 0)
        self.assertEqual(m.shape[1], 0)
        

    def test_error_input1(self):
        m1 = np.arange(1,5).reshape(2,2)
        m2 = np.arange(0,9).reshape(3,3)
        self.assertRaises(dot_if.ParameterError, dot_if.dot, m1, m2)

    def test_error_input2(self):
        m1 = np.arange(0,9).reshape(3,3)
        m2 = np.arange(0,5).reshape(1,5)
        self.assertRaises(dot_if.ParameterError, dot_if.dot, m1, m2)

    def test_error_input3(self):  #这个测试用例发现一个问题
        m1 = np.arange(0,9).reshape(9)
        m2 = np.arange(0,5).reshape(1,5)
        self.assertRaises(dot_if.ParameterError, dot_if.dot, m1, m2)

    def test_error_input4(self):  
        m1 = [[]]
        m2 = np.arange(0,5).reshape(1,5)
        self.assertRaises(dot_if.ParameterError, dot_if.dot, m1, m2)


if __name__ == '__main__':
    unittest.main()
