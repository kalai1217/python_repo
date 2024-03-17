import unittest
from src.piling_up.utils import *
class test_pu1(unittest.TestCase):
    def test_min1(self):
        '''2
6
4 3 2 1 3 4
3
1 3 2'''
        actual_input=piling_up()
        expected_output='''Yes
No'''
        self.assertEqual(actual_input,expected_output)
if __name__ == '__main__':
    unittest.main()