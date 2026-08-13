import unittest
from io import StringIO
from unittest.mock import patch
from q4 import fizz_buzz

class TestFizzBuzz(unittest.TestCase):

    def test_fizz_buzz_output(self):
        """Test fizz_buzz function output for correctness."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            fizz_buzz()
            console_output = mock_stdout.getvalue().strip().split('\n')

        # Expected output for numbers 1 to 20
        expected_output = [
            "1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz",
            "11", "Fizz", "13", "14", "FizzBuzz", "16", "17", "Fizz", "19", "Buzz"
        ]

        # Validate output
        self.assertEqual(console_output, expected_output)

if __name__ == "__main__":
    unittest.main()
