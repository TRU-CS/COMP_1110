import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
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
         # Simulate a guessing game with predefined inputs and check the logic.
        with patch('builtins.input', side_effect=[50, 30, 70, 60, 55, 60]):  # Simulate the user guesses
            with patch('random.randint', return_value=60):  # Simulate the random number being 60
                result = guessing_game()
                self.assertEqual(result, "Congratulations! You guessed it!")       



    @weight(5)
    @number("1.4")
    def test_calculate_square_root(self):
         # Simulate the user input for positive and negative numbers
        with patch('builtins.input', side_effect=[25]):
            result = calculate_square_root()
            self.assertEqual(result, 5.0)
    
        with patch('builtins.input', side_effect=[-9]):
            result = calculate_square_root()
            self.assertEqual(result, "Error: Cannot calculate the square root of a negative number.")


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