import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
from lab3 import categorize_age, sum_of_squares, sum_of_cubes, print_even_numbers, sum_of_digits_while, sum_of_digits_for

class TestFunctions(unittest.TestCase):

    @weight(5)
    @number("1.1")
    def test_categorize_age_minor(self):
        """Test Case 1: Age category - Minor (age < 18)."""
        with patch('builtins.input', return_value='10'):
            with patch('builtins.print') as mocked_print:
                result = categorize_age()
                self.assertEqual(result, (1, 0, 0))

    @weight(5)
    @number("1.2")
    def test_categorize_age_adult(self):
        """Test Case 2: Age category - Adult (18 ≤ age ≤ 64)."""
        with patch('builtins.input', return_value='30'):
            with patch('builtins.print') as mocked_print:
                result = categorize_age()
                self.assertEqual(result, (0, 1, 0))

    @weight(5)
    @number("1.3")
    def test_categorize_age_senior(self):
        """Test Case 3: Age category - Senior (age > 64)."""
        with patch('builtins.input', return_value='70'):
            with patch('builtins.print') as mocked_print:
                result = categorize_age()
                self.assertEqual(result, (0, 0, 1))

    @weight(5)
    @number("2.1")
    def test_sum_of_squares(self):
        """Test Case 4: Sum of squares of first 50 numbers."""
        result = sum_of_squares()
        self.assertEqual(result, 42925)

    @weight(5)
    @number("3.1")
    def test_sum_of_cubes(self):
        """Test Case 5: Sum of cubes of first n numbers (n=5)."""
        with patch('builtins.input', return_value='5'):
            with patch('builtins.print') as mocked_print:
                result = sum_of_cubes()
                self.assertEqual(result, 225)

    @weight(5)
    @number("4.1")
    def test_print_even_numbers(self):
        """Test Case 6: Print even numbers between 1 and 10."""
        with patch('builtins.input', side_effect=['1', '10']):
            with patch('builtins.print') as mocked_print:
                result = print_even_numbers()
                self.assertEqual(result, [2, 4, 6, 8, 10])

    @weight(5)
    @number("5.1")
    def test_sum_of_digits_while(self):
        """Test Case 7: Sum of digits using while loop (num=1234)."""
        with patch('builtins.input', return_value='1234'):
            with patch('builtins.print') as mocked_print:
                result = sum_of_digits_while()
                self.assertEqual(result, 10)

    @weight(5)
    @number("6.1")
    def test_sum_of_digits_for(self):
        """Test Case 8: Sum of digits using for loop (num=567)."""
        with patch('builtins.input', return_value='567'):
            with patch('builtins.print') as mocked_print:
                result = sum_of_digits_for()
                self.assertEqual(result, 18)

if __name__ == '__main__':
    unittest.main()
