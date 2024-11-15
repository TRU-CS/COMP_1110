from questions.q2 import check_three_digit

import unittest
from gradescope_utils.autograder_utils.decorators import weight, number

class TestBasic(unittest.TestCase):
    @weight(5)
    @number("3.1")
    def test_three_digit_positive(self):
        """Test Case 1: Checks if a positive three-digit number is identified correctly."""
        with unittest.mock.patch('builtins.input', return_value='123'):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_three_digit()
                mocked_print.assert_called_once_with("The number is a three-digit number.")

    @weight(5)
    @number("3.2")
    def test_two_digit_number(self):
        """Test Case 2: Checks if a two-digit number is identified correctly."""
        with unittest.mock.patch('builtins.input', return_value='45'):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_three_digit()
                mocked_print.assert_called_once_with("The number is not a three-digit number.")

    @weight(5)
    @number("3.3")
    def test_four_digit_number(self):
        """Test Case 3: Checks if a four-digit number is identified correctly."""
        with unittest.mock.patch('builtins.input', return_value='1000'):
            with unittest.mock.patch('builtins.print') as mocked_print:
                check_three_digit()
                mocked_print.assert_called_once_with("The number is not a three-digit number.")


