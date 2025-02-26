import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
from lab4 import *

class TestFunctions(unittest.TestCase):

    @weight(5)
    @number("1.1")
    def test_max_of_three(self):
        with patch('builtins.input', side_effect=[1, 12, 34]):
                result = max_of_three()
                self.assertEqual(result, 34)

if __name__ == '__main__':
    unittest.main()
