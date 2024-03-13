import unittest
from src.calendar_module.utils import *
class test_calendar_module(unittest.TestCase):
    def test_calendar_module1(self):
        #02 12 2002
        actual_output=calendar_module()
        expected_output="TUESDAY"
        self.assertEqual(actual_output,expected_output)
    def test_calendar_module2(self):
        #08 05 2015
        actual_output=calendar_module()
        expected_output="WEDNESDAY"
        self.assertEqual(actual_output,expected_output)
    def test_calendar_module3(self):
        #12 07 2008
        actual_output=calendar_module()
        expected_output="SUNDAY"
        self.assertEqual(actual_output,expected_output)
if __name__ == '__main__':
    unittest.main
