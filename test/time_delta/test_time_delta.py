import unittest
from src.time_delta.utils import *
class test_time1(unittest.TestCase):
    def test_time1(self):
        '''2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000'''
        actual_input = time_delta()
        expected_output ='''25200
88200'''
        self.assertEqual(actual_input, expected_output)
    def test_time2(self):
        """6
        7 8 8 8 8 8
        """
        actual_input = runnerup_score()
        expected_output = 7
        self.assertEqual(actual_input, expected_output)
    def test_time3(self):
        """
        4
        57 -57 57 -57
        """
        actual_input = runnerup_score()
        expected_output =-57
        self.assertEqual(actual_input, expected_output)
if __name__ == "__main__":
    unittest.main()
