import unittest
from unittest.mock import patch
from io import StringIO
from q3 import who_am_i

class TestWhoAmI(unittest.TestCase):

    @patch('builtins.input', side_effect=["yes", "yes", "yes"])  # Mock responses for all "yes"
    def test_adventurous_outgoing(self, mock_input):
        """Test if function identifies 'adventurous and outgoing'."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            who_am_i()
            console_output = mock_stdout.getvalue()

        # Validate printed output
        self.assertIn("You are adventurous and outgoing!", console_output)

    @patch('builtins.input', side_effect=["no", "no", "no"])  # Mock responses for all "no"
    def test_thoughtful_reserved(self, mock_input):
        """Test if function identifies 'thoughtful and reserved'."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            who_am_i()
            console_output = mock_stdout.getvalue()

        # Validate printed output
        self.assertIn("You are thoughtful and reserved.", console_output)

    @patch('builtins.input', side_effect=["yes", "no", "yes"])  # Mixed responses
    def test_balanced_personality(self, mock_input):
        """Test if function identifies 'balanced personality'."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            who_am_i()
            console_output = mock_stdout.getvalue()

        # Validate printed output
        self.assertIn("You have a balanced personality.", console_output)

if __name__ == "__main__":
    unittest.main()
