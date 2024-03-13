import unittest
from src.finding_the_percentage.utils import *


class test_finding_the_perecentage(unittest.TestCase):
    def test_percentage1(self):
        """
        3
        Krishna 67 68 69
        Arjun 70 98 63
        Malika 52 56 60
        Malika
        """
        actual_input = finding_the_percentage()
        expected_output = 56.00
        self.assertEqual(actual_input, expected_output)
    def test_percentage2(self):
        """2
        Harsh 25 26.5 28
        Anurag 26 28 30
        Harsh"""
        actual_input = finding_the_percentage()
        expected_output = 26.50
        self.assertEqual(actual_input, expected_output)
    def test_percentage3(self):
        """
        4
        Kalai 78 32 83
        Sriram 67 23 44.2
        Vijay 58 29 92
        Raji 78 23 64.3 21
        Sriram
        """
        actual_input = finding_the_percentage()
        expected_output = 33.55
        self.assertEqual(actual_input, expected_output)
if __name__ == "__main__":
    unittest.main()
