import unittest
from src.no_idea.utils import *
class test_no_idea(unittest.TestCase):
    def test_na1(self):
        '''3 2
1 5 3
3 1
5 7'''
        actual_input=no_idea()
        expected_output=1
        self.assertEqual(actual_input,expected_output)
    def test_na2(self):
        '''5 5
1 2 3 4 5
1 3 5 7 9
2 4 6 8 10'''
        actual_input = no_idea()
        expected_output = 1
        self.assertEqual(actual_input, expected_output)
    def test_na3(self):
        '''5 5
999999991 999999992 999999993 999999994 999999999
999999991 999999993 999999995 999999999 999999997
999999990 999999992 999999996 999999998 999999994'''
        actual_input = no_idea()
        expected_output = 1
        self.assertEqual(actual_input, expected_output)
if __name__ == '__main__':
    unittest.main()