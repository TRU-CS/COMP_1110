import unittest
from unittest.mock import patch
from io import StringIO
from q3 import python_quiz_application  
from gradescope_utils.autograder_utils.decorators import weight, number

class TestPythonQuizApplication(unittest.TestCase):

    @weight(5)
    @number("3.1")
    def test_easy_level_mixed_answers(self):
        """Test Case 1: Easy level with a mix of correct and incorrect answers."""
        inputs = [
            "Alice",  # User name
            "1",      # Easy level
            "a", "b", "d", "b", "d"  # Answers: 3 correct, 2 incorrect
        ]
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculate_result=python_quiz_application()
            self.assertEqual(calculate_result, 3)

    @weight(5)
    @number("3.2")
    def test_average_level_all_correct(self):
        """Test Case 2: Average level with all correct answers."""
        inputs = [
            "Bob",  # User name
            "2",  # Average level
            "c", "b", "a", "c", "a"  # All answers correct
        ]
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculate_result= python_quiz_application()
            self.assertEqual(calculate_result, 5)

    @weight(5)
    @number("3.3")
    def test_hard_level_all_incorrect(self):
        """Test Case 3: Hard level with all incorrect answers."""
        inputs = [
            "Charlie",  # User name
            "3",  # Hard level
            "b", "b", "a", "a", "d"  # All answers incorrect
        ]
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculate_result=python_quiz_application()
            self.assertEqual(calculate_result, 0)

    @weight(5)
    @number("3.4")
    def test_invalid_level_choice(self):
        """Test Case 4: Invalid level choice."""
        inputs = ["Dave", "4"]  # Invalid level
        with patch('builtins.input', side_effect=inputs), patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            calculate_result = python_quiz_application()
            output = mock_stdout.getvalue()

            # Check if the word "invalid" appears in the output
            self.assertIn("invalid", output.lower())

