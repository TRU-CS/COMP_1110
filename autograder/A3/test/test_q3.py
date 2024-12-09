import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from student.q3 import remove_duplicates

class TestRemoveDuplicates(unittest.TestCase):

    @weight(5)
    @number("3.1")
    def test_with_duplicates(self):
        """Test Case 1: List with duplicates."""
        result = remove_duplicates([1, 2, 2, 3, 4, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    @weight(5)
    @number("3.2")
    def test_all_duplicates(self):
        """Test Case 2: List where all elements are duplicates."""
        result = remove_duplicates([10, 10, 10])
        self.assertEqual(result, [10])

    @weight(5)
    @number("3.3")
    def test_no_duplicates(self):
        """Test Case 3: List with no duplicates."""
        result = remove_duplicates([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])

    @weight(5)
    @number("3.4")
    def test_empty_list(self):
        """Test Case 4: Empty list."""
        result = remove_duplicates([])
        self.assertEqual(result, [])

    @weight(5)
    @number("3.5")
    def test_large_list_with_duplicates(self):
        """Test Case 5: Large list with duplicates."""
        result = remove_duplicates([1] * 100 + [2] * 100 + [3] * 100)
        self.assertEqual(result, [1, 2, 3])

    @weight(5)
    @number("3.6")
    def test_list_with_mixed_data(self):
        """Test Case 6: Mixed list with duplicates."""
        result = remove_duplicates([1, 2, 'a', 'b', 'a', 3, 2, 'c'])
        self.assertEqual(result, [1, 2, 'a', 'b', 3, 'c'])
