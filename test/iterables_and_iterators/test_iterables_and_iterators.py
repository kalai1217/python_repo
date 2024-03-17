import unittest
from src.iterables_and_iterators.utils import *
class test_iai1(unittest.TestCase):
    def test_min1(self):
        '''4
a a c d
'''
        actual_input=iterables_and_iterators()
        expected_output=0.833333333333
        self.assertEqual(actual_input,expected_output)
if __name__ == '__main__':
    unittest.main()