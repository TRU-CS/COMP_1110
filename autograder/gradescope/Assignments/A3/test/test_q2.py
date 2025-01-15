import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from student.q2 import split_list

class TestSplitList(unittest.TestCase):

    @weight(5)
    @number("2.1")
    def test_valid_split(self):
        """Test Case 1: Valid split within the bounds of the list."""
        result = split_list([1, 2, 3, 4, 5], 3)
        self.assertEqual(result, ([1, 2, 3], [4, 5]))

    @weight(5)
    @number("2.2")
    def test_split_at_zero(self):
        """Test Case 2: Split length is zero."""
        result = split_list([1, 2, 3, 4, 5], 0)
        self.assertEqual(result, ([], [1, 2, 3, 4, 5]))

    @weight(5)
    @number("2.3")
    def test_split_at_length(self):
        """Test Case 3: Split length is equal to the length of the list."""
        result = split_list([1, 2, 3, 4, 5], 5)
        self.assertEqual(result, ([1, 2, 3, 4, 5], []))

    @weight(5)
    @number("2.4")
    def test_split_exceeds_length(self):
        """Test Case 4: Split length exceeds the length of the list."""
        result = split_list([1, 2, 3, 4, 5], 6)
        self.assertEqual(result, "Invalid input. The split length exceeds the length of the list.")

    @weight(5)
    @number("2.5")
    def test_negative_split_length(self):
        """Test Case 5: Split length is negative."""
        result = split_list([1, 2, 3, 4, 5], -1)
        self.assertEqual(result, "Invalid input. The split length cannot be negative.")

    @weight(5)
    @number("2.6")
    def test_empty_list(self):
        """Test Case 6: Input list is empty."""
        result = split_list([], 0)
        self.assertEqual(result, ([], []))

    @weight(5)
    @number("2.7")
    def test_split_with_large_input(self):
        """Test Case 7: Large list and valid split."""
        input_list = list(range(1000))
        split_length = 500
        result = split_list(input_list, split_length)
        self.assertEqual(result, (list(range(500)), list(range(500, 1000))))
