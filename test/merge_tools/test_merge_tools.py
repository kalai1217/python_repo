import unittest
from src.merge_tools.utils import *
class test_merge_tools(unittest.TestCase):
    def test_merge_tools1(self):
        actual_input=merge_the_tools()
        expected_output="AB\nCA\nAD"
        self.assertEqual(actual_input,expected_output)
if __name__ == '__main__':
    unittest.main()