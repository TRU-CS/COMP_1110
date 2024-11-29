import unittest
from gradescope_utils.autograder_utils.decorators import weight, number
from student.q1 import convert_to_miles

class TestConvertToMiles(unittest.TestCase):

    @weight(1)
    @number("1.1")
    def test_small_distance(self):
        """Test conversion with a small distance."""
        result = convert_to_miles(1)  # 1 km = 0.6214 miles
        self.assertAlmostEqual(result, 0.62, places=2)

    @weight(1)
    @number("1.2")
    def test_large_distance(self):
        """Test conversion with a large distance."""
        result = convert_to_miles(1000)  # 1000 km = 621.4 miles
        self.assertAlmostEqual(result, 621.4, places=2)

    @weight(1)
    @number("1.3")
    def test_zero_distance(self):
        """Test conversion with zero distance."""
        result = convert_to_miles(0)  # 0 km = 0 miles
        self.assertAlmostEqual(result, 0, places=2)

    @weight(1)
    @number("1.4")
    def test_fractional_distance(self):
        """Test conversion with a fractional distance."""
        result = convert_to_miles(0.5)  # 0.5 km = 0.3107 miles
        self.assertAlmostEqual(result, 0.31, places=2)

    @weight(1)
    @number("1.5")
    def test_negative_distance(self):
        """Test conversion with a negative distance."""
        result = convert_to_miles(-5)  # -5 km = -3.107 miles
        self.assertAlmostEqual(result, -3.10, places=2)

if __name__ == "__main__":
    unittest.main()
