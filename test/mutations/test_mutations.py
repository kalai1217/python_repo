import unittest
from src.mutations.utils import *
class string_mutations(unittest.TestCase):
    def test_mutations1(self):
        """
                abracadabra
                5 k
        """
        actual_input=mutate_string()
        expected_output="abrackdabra"
        self.assertEqual(actual_input,expected_output)
    def test_mutations2(self):
        """
                appte
                3 l
        """
        actual_input=mutate_string()
        expected_output="apple"
        self.assertEqual(actual_input,expected_output)
    def test_mutations3(self):
        """
                hello vorld
                6 w
        """
        actual_input=mutate_string()
        expected_output="hello world"
        self.assertEqual(actual_input,expected_output)

if __name__ == '__main__':
    unittest.main()

