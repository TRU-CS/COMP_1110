import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from q1 import find_missing_number

class TestFindMissingNumber(unittest.TestCase):

    @weight(5)
    @number("1.1")
    def test_missing_number_in_middle(self):
        """Test Case 1: Missing number in the middle of the list."""

        result = find_missing_number([0, 1, 2, 4, 5])
        self.assertEqual(result, 3)

    @weight(5)
    @number("1.2")
    def test_missing_number_at_start(self):
        """Test Case 2: Missing number is the first number."""
        result = find_missing_number([1, 2, 3, 4])
        self.assertEqual(result, 0)

    @weight(5)
    @number("1.3")
    def test_no_missing_number(self):
        """Test Case 3: No numbers are missing."""
        result = find_missing_number([0, 1, 2, 3, 4])
        self.assertIsNone(result)

    @weight(5)
    @number("1.4")
    def test_large_missing_number(self):
        """Test Case 4: Missing the largest number."""
        result = find_missing_number([0, 1, 2, 3])
        self.assertEqual(result, 4)

    @weight(5)
    @number("1.5")
    def test_empty_list(self):
        """Test Case 5: The list is empty."""
        result = find_missing_number([])
        self.assertEqual(result, 0)

    @weight(5)
    @number("1.6")
    def test_single_element_list(self):
        """Test Case 6: Single element list."""
        result = find_missing_number([1])
        self.assertEqual(result, 0)
