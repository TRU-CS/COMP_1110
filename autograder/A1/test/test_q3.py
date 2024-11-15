import unittest
from unittest.mock import patch
from gradescope_utils.autograder_utils.decorators import weight, number
from questions.q3 import python_quiz_application

class TestPythonQuizApplication(unittest.TestCase):
    
    @weight(5)
    @number("4.1")
    def test_easy_level_mixed_answers(self):
        """Test Case 1: Easy level with a mix of correct and incorrect answers."""
        inputs = [
            "Alice",  # User name
            "1",  # Easy level
            "a", "b", "d", "b", "a"  # Answers: 3 correct, 2 incorrect
        ]
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mocked_print:
            python_quiz_application()
            
            # Verify player greeting and level choice
            mocked_print.assert_any_call("Welcome to the Python Quiz, Alice!")
            mocked_print.assert_any_call("Choose a difficulty level:")
            
            # Check for correct and incorrect responses
            mocked_print.assert_any_call("Correct!")
            mocked_print.assert_any_call("Invalid choice. The correct answer was: a")  # for incorrect question
            
            # Final score expectation: 3/5
            mocked_print.assert_any_call("\nQuiz completed! Alice, your final score is: 3/5")
    
    @weight(5)
    @number("4.2")
    def test_average_level_all_correct(self):
        """Test Case 2: Average level with all correct answers."""
        inputs = [
            "Bob",  # User name
            "2",  # Average level
            "c", "b", "a", "c", "a"  # All answers correct
        ]
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mocked_print:
            python_quiz_application()
            
            # Verify player greeting and level choice
            mocked_print.assert_any_call("Welcome to the Python Quiz, Bob!")
            mocked_print.assert_any_call("Choose a difficulty level:")
            
            # Check for correct response without "Invalid choice" messages
            mocked_print.assert_any_call("Correct!")
            mocked_print.assert_any_call("\nQuiz completed! Bob, your final score is: 5/5")

    @weight(5)
    @number("4.3")
    def test_hard_level_all_incorrect(self):
        """Test Case 3: Hard level with all incorrect answers."""
        inputs = [
            "Charlie",  # User name
            "3",  # Hard level
            "b", "b", "a", "a", "d"  # All answers incorrect
        ]
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mocked_print:
            python_quiz_application()
            
            # Verify player greeting and level choice
            mocked_print.assert_any_call("Welcome to the Python Quiz, Charlie!")
            mocked_print.assert_any_call("Choose a difficulty level:")
            
            # Expect "Invalid choice" for each incorrect answer
            mocked_print.assert_any_call("Invalid choice. The correct answer was: a")
            
            # Final score expectation: 0/5
            mocked_print.assert_any_call("\nQuiz completed! Charlie, your final score is: 0/5")

    @weight(5)
    @number("4.4")
    def test_invalid_level_choice(self):
        """Test Case 4: Invalid level choice."""
        inputs = ["Dave", "4"]  # Invalid level
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mocked_print:
            python_quiz_application()
            mocked_print.assert_any_call("Invalid choice. Exiting the quiz.")
            
    @weight(5)
    @number("4.5")
    def test_no_questions_answered(self):
        """Test Case 5: No questions answered due to exiting on invalid level."""
        inputs = ["Eve", "0"]  # Exiting with invalid level input
        with patch('builtins.input', side_effect=inputs), patch('builtins.print') as mocked_print:
            python_quiz_application()
            mocked_print.assert_any_call("Invalid choice. Exiting the quiz.")
