import unittest
from src.string_formatting.utils import *
class test_string_formatting1(unittest.TestCase):
    def test_string1(self):
        """
        17
        """
        actual_input = string_formatted()
        expected_output = '''    1     1     1     1
    2     2     2    10
    3     3     3    11
    4     4     4   100
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8    10     8  1000
    9    11     9  1001
   10    12     A  1010
   11    13     B  1011
   12    14     C  1100
   13    15     D  1101
   14    16     E  1110
   15    17     F  1111
   16    20    10 10000
   17    21    11 10001
'''
        self.assertEqual(actual_input, expected_output)
if __name__ == "__main__":
    unittest.main()
