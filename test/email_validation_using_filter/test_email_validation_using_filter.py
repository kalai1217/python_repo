import unittest

from src.email_validation_using_filter.utils import *


class test_email_validation_using_filter(unittest.TestCase):
    def test_one(self):
        expected_output = ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
        self.assertEqual(email_validation_using_filter(),expected_output)
        '''3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com'''