import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from student.q4 import generate_squares

class TestGenerateSquares(unittest.TestCase):

    @weight(5)
    @number("4.1")
    def test_squares_length(self):
        """Test Case 1: Validate the length of the squares list."""
        result = generate_squares()
        self.assertEqual(len(result), 30)

    @weight(5)
    @number("4.2")
    def test_squares_values(self):
        """Test Case 2: Validate the contents of the squares list."""
        result = generate_squares()
        expected = [x**2 for x in range(1, 31)]
        self.assertEqual(result, expected)

    @weight(5)
    @number("4.3")
    def test_first_and_last_values(self):
        """Test Case 3: Check the first and last values in the list."""
        result = generate_squares()
        self.assertEqual(result[0], 1)       # First square
        self.assertEqual(result[-1], 900)   # Last square

    @weight(5)
    @number("4.4")
    def test_middle_values(self):
        """Test Case 4: Validate specific middle values."""
        result = generate_squares()
        self.assertEqual(result[14], 225)   # Square of 15
        self.assertEqual(result[19], 400)   # Square of 20
