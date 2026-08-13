import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
import io
from contextlib import redirect_stdout
from lab4 import *

class TestFunctions(unittest.TestCase):

    @weight(4)
    @number("1.1")
    def test_max_of_three(self):
        with patch('builtins.input', side_effect=[1, 12, 34]):
            result = max_of_three()
            self.assertEqual(result, 34)

    @weight(4)
    @number("1.2")
    def test_is_palindrome(self):
        with patch('builtins.input', side_effect=[121]):
            result = isPalindrome()
            self.assertEqual(result, True)

        with patch('builtins.input', side_effect=[123]):
            result = isPalindrome()
            self.assertEqual(result, False)
            
            
    @weight(6)
    @number("1.3")   
    def test_guessing_game(self):
        # Mock input and random.randint within a single 'with' block
        with patch('builtins.input', side_effect=[50, 70, 60]) as mock_input, \
             patch('random.randint', return_value=60) as mock_random:

            # Capture the printed output using StringIO and redirect_stdout
            f = io.StringIO()
            with redirect_stdout(f):
                guessing_game()

            result = f.getvalue()

              # Split the result into lines
            result_lines = result.splitlines()

            # Check specific line (e.g., line 1, which is index 1)
            self.assertIn("Too low, try again.", result_lines[0])  # This checks the second line
            self.assertIn("Too high, try again.", result_lines[1])  # This checks the third line
            self.assertIn("Congratulations! You guessed it!", result_lines[2])  # This checks the fourth line




    @weight(2.5)
    @number("1.4.1")
    def test_calculate_square_root(self):
         # Simulate the user input for positive and negative numbers
        with patch('builtins.input', side_effect=[25]):
            result = calculate_square_root()
            self.assertEqual(result, 5.0)

    @weight(2.5)
    @number("1.4.2")
    def test_calculate_square_root_negative(self):
            with patch('builtins.input', side_effect=[-9]):
                with self.assertRaises(ValueError):
                    calculate_square_root()

    @weight(6)
    @number("1.5")
    def test_create_matrix(self):
           # Simulate user input for rows, columns, and matrix values
        with patch('builtins.input', side_effect=[2, 3, 1, 2, 3, 4, 5, 6]):
            result = create_matrix()
               # Check if the matrix is correctly created and printed
            self.assertEqual(result, [[1, 2, 3], [4, 5, 6]])



if __name__ == '__main__':
    unittest.main()