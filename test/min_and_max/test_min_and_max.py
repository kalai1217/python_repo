import unittest
from src.min_and_max.utils import *
class test_min1(unittest.TestCase):
    def test_min1(self):
        '''4 2
2 5
3 7
1 3
4 0'''
        actual_input=min_and_max()
        expected_output=3
        self.assertEqual(actual_input,expected_output)
    def test_min2(self):
        '''4 2
2 5
8 7
1 4
4 0'''
        actual_input=min_and_max()
        expected_output=7
        self.assertEqual(actual_input,expected_output)
    def test_min3(self):
        '''3 2
2 5
1 4
4 0'''
        actual_input=min_and_max()
        expected_output=2
        self.assertEqual(actual_input,expected_output)

if __name__ == '__main__':
    unittest.main()