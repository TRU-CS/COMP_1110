# test_check_three_digit.py
import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from unittest.mock import patch
from q2 import check_three_digit

class TestCheckThreeDigit(unittest.TestCase):
    def init(self):
        self.maxDiff = None


    @weight(5)
    @number("1.1")
    def test_three_digit_number(self):
        """Test Case 1: Input is a three-digit number."""
        with patch('builtins.input', side_effect=['123']):
            with patch('builtins.print') as mocked_print:
                check_three_digit()
                # Check if "is a" is present in the output
                output = [call[0][0] for call in mocked_print.call_args_list]
                self.assertTrue(any("is a" in line for line in output))

    @weight(5)
    @number("1.2")
    def test_not_three_digit_number(self):
        """Test Case 2: Input is not a three-digit number."""
        with patch('builtins.input', side_effect=['45']):
            with patch('builtins.print') as mocked_print:
                check_three_digit()
                # Check if "not " is present in the output
                output = [call[0][0] for call in mocked_print.call_args_list]
                self.assertTrue(any("not " in line for line in output))

    @weight(5)
    @number("1.3")
    def test_negative_three_digit_number(self):
        """Test Case 3: Input is a negative three-digit number."""
        with patch('builtins.input', side_effect=['-456']):
            with patch('builtins.print') as mocked_print:
                check_three_digit()
                # Check if "is a" is present in the output
                output = [call[0][0] for call in mocked_print.call_args_list]
                self.assertTrue(any("is a" in line for line in output))

    @weight(5)
    @number("1.4")
    def test_not_three_digit_negative_number(self):
        """Test Case 4: Input is not a three-digit number (negative)."""
        with patch('builtins.input', side_effect=['-23']):
            with patch('builtins.print') as mocked_print:
                check_three_digit()
                # Check if "not " is present in the output
                output = [call[0][0] for call in mocked_print.call_args_list]
                self.assertTrue(any("not " in line for line in output))

    @weight(5)
    @number("1.5")
    def test_invalid_input(self):
        """Test Case 5: Input is not a valid integer."""
        with patch('builtins.input', side_effect=['abc']):
            with patch('builtins.print') as mocked_print:
                check_three_digit()
                # Check if the error message for invalid input is present
                output = [call[0][0] for call in mocked_print.call_args_list]
                self.assertTrue(any("Invalid input" in line for line in output))
