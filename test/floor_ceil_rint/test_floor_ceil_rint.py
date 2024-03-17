import unittest
from src.floor_ceil_rint.utils import *
class test_floor_ceil_rint(unittest.TestCase):
    def test_floor1(self):
        """
        1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
        """
        actual_input = floor_ceil_rint()
        expected_output ='''[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]'''
        self.assertEqual(actual_input, expected_output)
    def test_floor2(self):
        """
        1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8
        """
        actual_input = floor_ceil_rint()
        expected_output ='''[ 1.  2.  3.  4.  5.  6.  7.  8.]
[ 2.  3.  4.  5.  6.  7.  8.  9.]
[ 1.  2.  3.  4.  6.  7.  8.  9.]'''
        self.assertEqual(actual_input, expected_output)
    def test_floor3(self):
        """
        2.2 3.3 4.4 5.5 6.6 7.7 8.8
        """
        actual_input = floor_ceil_rint()
        expected_output ='''[ 2.  3.  4.  5.  6.  7.  8.]
[ 3.  4.  5.  6.  7.  8.  9.]
[ 2.  3.  4.  6.  7.  8.  9.]'''
        self.assertEqual(actual_input, expected_output)
if __name__ == "__main__":
    unittest.main()
