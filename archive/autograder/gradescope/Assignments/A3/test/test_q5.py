import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from q5 import calculate_adjusted_average

class TestCalculateAdjustedAverage(unittest.TestCase):

    @weight(5)
    @number("5.1")
    def test_typical_case(self):
        """Test Case 1: Typical case with multiple scores."""
        result = calculate_adjusted_average([78, 85, 62, 90])
        self.assertEqual(result, 84.33)

    @weight(5)
    @number("5.2")
    def test_all_scores_identical(self):
        """Test Case 2: All scores are identical."""
        result = calculate_adjusted_average([70, 70, 70, 70])
        self.assertEqual(result, 70.0)

    @weight(5)
    @number("5.3")
    def test_lowest_score_dropped(self):
        """Test Case 3: Lowest score is dropped correctly."""
        result = calculate_adjusted_average([100, 95, 80, 85])
        self.assertEqual(result, 95.0)

    @weight(5)
    @number("5.4")
    def test_minimum_input_size(self):
        """Test Case 4: Minimum input size (two scores)."""
        result = calculate_adjusted_average([60, 90])
        self.assertEqual(result, 90.0)


    @weight(5)
    @number("5.6")
    def test_large_input(self):
        """Test Case 6: Large input with multiple scores."""
        scores = [i for i in range(50, 101)]  # Scores from 50 to 100
        result = calculate_adjusted_average(scores)
        expected_total = sum(scores) - 50
        expected_average = expected_total / (len(scores) - 1)
        self.assertEqual(result, round(expected_average, 2))
