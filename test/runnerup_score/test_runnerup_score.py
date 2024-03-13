import unittest
from src.runnerup_score.utils import *
class test_runnerup_score(unittest.TestCase):
    def test_score1(self):
        """
        5
        2 3 6 6 5
        """
        actual_input = runnerup_score()
        expected_output = 5
        self.assertEqual(actual_input, expected_output)
    def test_score2(self):
        """6
        7 8 8 8 8 8
        """
        actual_input = runnerup_score()
        expected_output = 7
        self.assertEqual(actual_input, expected_output)
    def test_score3(self):
        """
        4
        57 -57 57 -57
        """
        actual_input = runnerup_score()
        expected_output =-57
        self.assertEqual(actual_input, expected_output)
if __name__ == "__main__":
    unittest.main()
