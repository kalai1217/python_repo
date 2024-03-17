import unittest
from src.linear_algebra.utils import *
class test_linear_algebra(unittest.TestCase):
    def test_la1(self):
        '''2
1.1 1.1
1.1 1.1'''
        actual_input=linear_algebra()
        expected_output=0.0
        self.assertEqual(actual_input,expected_output)
    def test_la2(self):
        '''2
1.1 1.1
1.1 1.2'''
        actual_input=linear_algebra()
        expected_output=0.11
        self.assertEqual(actual_input,expected_output)
    def test_la3(self):
        '''3
1 2 3
4 5 6
1 2 1'''
        actual_input=linear_algebra()
        expected_output=6.0
        self.assertEqual(actual_input,expected_output)
if __name__ == '__main__':
    unittest.main()