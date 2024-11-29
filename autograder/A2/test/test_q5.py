import unittest
from unittest.mock import patch
from io import StringIO
from student.q5 import find_min_max

class TestFindMinMax(unittest.TestCase):

    @patch('builtins.input', side_effect=["5", "3", "9", "0"])  # Mock user inputs
    def test_find_min_max_valid_input(self, mock_input):
        """Test find_min_max with a valid sequence of inputs."""
        min_num, max_num = find_min_max()

        # Validate return values
        self.assertEqual(min_num, 3)
        self.assertEqual(max_num, 9)

    @patch('builtins.input', side_effect=["0"])  # Mock user inputs with no numbers
    def test_find_min_max_no_input(self, mock_input):
        """Test find_min_max when no numbers are entered."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            min_num, max_num = find_min_max()
            console_output = mock_stdout.getvalue()

        # Validate printed message
        self.assertIn("No numbers were entered.", console_output)

        # Validate return values
        self.assertIsNone(min_num)
        self.assertIsNone(max_num)

    @patch('builtins.input', side_effect=["10", "20", "30", "0"])  # Mock increasing sequence
    def test_find_min_max_increasing(self, mock_input):
        """Test find_min_max with an increasing sequence of inputs."""
        min_num, max_num = find_min_max()

        # Validate return values
        self.assertEqual(min_num, 10)
        self.assertEqual(max_num, 30)

    @patch('builtins.input', side_effect=["-5", "-3", "-9", "0"])  # Mock negative inputs
    def test_find_min_max_negative_numbers(self, mock_input):
        """Test find_min_max with negative numbers."""
        min_num, max_num = find_min_max()

        # Validate return values
        self.assertEqual(min_num, -9)
        self.assertEqual(max_num, -3)

if __name__ == "__main__":
    unittest.main()
