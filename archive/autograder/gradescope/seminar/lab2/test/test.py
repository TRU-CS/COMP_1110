import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number

from lab2 import (
    calculate_distance,
    calculate_mpg,
    convert_seconds,
    book_club_points,
    day_of_week,
)

class TestLabActivity2(unittest.TestCase):

    # 1. Calculate Distance Traveled
    @weight(5)
    @number("1.1")
    def test_distance_traveled(self):
        """Test calculate_distance returns correct values."""
        distance_6_hours, distance_10_hours = calculate_distance()

        # Validate return values
        self.assertEqual(distance_6_hours, 420)
        self.assertEqual(distance_10_hours, 700)

    # 2. Calculate Miles-Per-Gallon (MPG)
    @weight(5)
    @number("1.2")
    @patch('builtins.input', side_effect=["100", "10"])  # Mock input for miles and gallons
    def test_valid_mpg(self, mock_input):
        """Test calculate_mpg with valid input."""
        mpg = calculate_mpg()

        # Validate return values
        self.assertEqual(mpg, 10.0)

    # 3. Convert Seconds to Minutes and Seconds
    @weight(5)
    @number("1.3")
    @patch('builtins.input', return_value="125")  # Mock input for seconds
    def test_valid_seconds(self, mock_input):
        """Test convert_seconds with seconds >= 60."""
        minutes, remaining_seconds = convert_seconds()

        # Validate return values
        self.assertEqual(minutes, 2)
        self.assertEqual(remaining_seconds, 5)

    @weight(5)
    @number("1.4")
    @patch('builtins.input', return_value="45")  # Mock input for seconds < 60
    def test_less_than_one_minute(self, mock_input):
        """Test convert_seconds with seconds < 60."""
        minutes, remaining_seconds = convert_seconds()

        # Validate return values
        self.assertEqual(minutes, 45)
        self.assertEqual(remaining_seconds, 0)

    # 4. Book Club Points System
    @weight(5)
    @number("1.5")
    @patch('builtins.input', return_value="0")  # Mock input for books purchased
    def test_zero_books(self, mock_input):
        """Test book_club_points for zero books."""
        points = book_club_points()

        # Validate return value
        self.assertEqual(points, 0)

    @weight(5)
    @number("1.6")
    @patch('builtins.input', return_value="4")  # Mock input for 4 books purchased
    def test_multiple_books(self, mock_input):
        """Test book_club_points for 4 books."""
        points = book_club_points()

        # Validate return value
        self.assertEqual(points, 15)

    # 5. Day of the Week
    @weight(5)
    @number("1.7")
    @patch('builtins.input', return_value="3")  # Mock input for day number
    def test_valid_day(self, mock_input):
        """Test day_of_week with a valid day number."""
        day = day_of_week()

        # Validate return value
        self.assertEqual(day, "wednesday")

    @weight(5)
    @number("1.8")
    @patch('builtins.input', return_value="8")  # Mock input for invalid day number
    def test_invalid_day(self, mock_input):
        """Test day_of_week with an invalid day number."""
        day = day_of_week()

        # Validate return value
        self.assertIsNone(day)


if __name__ == "__main__":
    unittest.main()
